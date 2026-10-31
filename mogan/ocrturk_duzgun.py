"""OCRTurk icin duzeltilmis degerlendirme (makaledeki tanimlara gore, eval.py'nin hatalari olmadan).

Farklar (eval.py'ye gore):
- On isleme (GT ve model ciktisina ayni): kod blogu isaretleri, makaledeki temizlik (˘g->ğ, ¸s->ş; #, ** silinir),
  Unicode NFC, satir basi madde isaretleri (-, *, •) silinir (GT'de bu isaretler karisik).
- Metin: tablolar ve blok formuller metinden cikarilir (makale: "ogeleri cikarip ham metinle kaliriz"),
  kucuk harfe CEVRILMEZ (TCS tanimi buyuk harfleri de sayar).
- TCS: makaledeki E/N tanimi, ama hizalama Levenshtein'in en iyi hizalamasiyla (difflib autojunk yok), harfe duyarli.
- Aksan karisikligi: hizali yer degistirmelerde yalniz ı/i, İ/I, ş/s, ğ/g, ç/c, ö/o, ü/u karismalari (/ N).
- Tablo: gercek TEDS (PubTabNet/OmniDocBench gibi, APTED ile HTML agaci); yalniz GT'de tablo olan sayfalarda ortalanir.
  LaTeX tabular ve markdown boru tablolari da HTML'e cevrilir; tablolar en iyi eslesmeyle (Macar) eslenir.
- Formul: GT'de makaledeki gibi $$..$$, \\[..\\], \\(..\\); modelde bunlar + cumle ici $..$ aday olur
  (GT bazen cumle ici formulu ayri satira almis). En iyi eslesmeyle eslenir; yalniz GT'de formul olan sayfalarda ortalanir.
- %95 bootstrap guven araligi. Metin NED sayfa ortalamasinin yaninda toplam NED (toplam mesafe / toplam uzunluk) de verilir.

Kullanim: python ocrturk_duzgun.py <gt_kok> <cikti_csv> ad=klasor [ad=klasor ...]
"""
import re
import sys
import unicodedata
from pathlib import Path

import Levenshtein
import numpy as np
import pandas as pd
from apted import APTED, Config
from bs4 import BeautifulSoup

TURKCE = set("çğıöşüÇĞİÖŞÜ")
IKIZ = {frozenset(p) for p in ["ıi", "İI", "şs", "ŞS", "ğg", "ĞG", "çc", "ÇC", "öo", "ÖO", "üu", "ÜU"]}
CIT = re.compile(r"^[ \t]*```[\w-]*[ \t]*$", re.M)
DUZELT = {"˘g": "ğ", "˘G": "Ğ", "¸s": "ş", "¸S": "Ş", "¸c": "ç", "¸C": "Ç", "¨o": "ö", "¨O": "Ö", "¨u": "ü", "¨U": "Ü"}
BLOK_FORMUL = [re.compile(r"\$\$(.*?)\$\$", re.S), re.compile(r"\\\[(.*?)\\\]", re.S), re.compile(r"\\\((.*?)\\\)", re.S)]
SATIR_ICI = re.compile(r"(?<!\$)\$([^$\n]+)\$(?!\$)")
HTML_TABLO = re.compile(r"<table.*?</table>", re.S | re.I)
TABULAR = re.compile(r"\\begin\{tabular\}(?:\{[^}]*\})?(.*?)\\end\{tabular\}", re.S)


def tabular_html(govde):
    """LaTeX tabular -> basit HTML tablo (\\hline, \\textbf vb. atilir)."""
    govde = re.sub(r"\\(hline|toprule|midrule|bottomrule|cline\{[^}]*\})", "", govde)
    govde = re.sub(r"\\multicolumn\{\d+\}\{[^}]*\}\{([^}]*)\}", r"\1", govde)
    govde = re.sub(r"\\text(bf|it|rm)\{([^}]*)\}", r"\2", govde)
    satirlar = [s for s in re.split(r"\\\\", govde) if s.strip()]
    return "<table>" + "".join("<tr>" + "".join(f"<td>{c.strip()}</td>" for c in s.split("&")) + "</tr>"
                               for s in satirlar) + "</table>"


def eslestir(gt, hyp, maliyet):
    """En iyi bire bir eslesme (Macar algoritmasi): [(gt_i, hyp_j)]."""
    from scipy.optimize import linear_sum_assignment
    if not gt or not hyp:
        return []
    m = np.array([[maliyet(g, h) for h in hyp] for g in gt])
    return list(zip(*linear_sum_assignment(m)))


def on_isle(s):
    s = CIT.sub("", s)
    for k, v in DUZELT.items():
        s = s.replace(k, v)
    s = unicodedata.normalize("NFC", s)
    s = re.sub(r"^[ \t]*#{1,6}[ \t]*", "", s, flags=re.M)
    s = s.replace("**", "").replace("__", "")
    s = re.sub(r"^[ \t]*[-*•+][ \t]+", "", s, flags=re.M)
    return s


def md_tablolari(s):
    """Boru (|) tablolarini bul: [(baslangic, bitis, satirlar)]."""
    satirlar, out, i = s.split("\n"), [], 0
    konum = np.cumsum([0] + [len(l) + 1 for l in satirlar])
    while i < len(satirlar) - 1:
        if "|" in satirlar[i] and re.match(r"^\s*\|?[\s:\-|]+\|?\s*$", satirlar[i + 1]) and "-" in satirlar[i + 1]:
            j = i + 2
            while j < len(satirlar) and "|" in satirlar[j] and satirlar[j].strip():
                j += 1
            hucreler = [[c.strip() for c in l.strip().strip("|").split("|")] for l in [satirlar[i]] + satirlar[i + 2:j]]
            out.append((konum[i], konum[j], hucreler))
            i = j
        else:
            i += 1
    return out


def ayristir(s):
    s = on_isle(s)
    tablolar, parcalar = [], []
    for m in HTML_TABLO.finditer(s):
        tablolar.append((m.start(), m.group(0)))
    for m in TABULAR.finditer(s):
        tablolar.append((m.start(), tabular_html(m.group(1))))
    s = TABULAR.sub(" ", s)
    for a, b, hucreler in md_tablolari(s):
        html = "<table>" + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in hucreler) + "</table>"
        tablolar.append((a, html))
    tablolar = [h for _, h in sorted(tablolar)]
    metin = HTML_TABLO.sub(" ", s)
    for a, b, _ in reversed(md_tablolari(metin)):
        metin = metin[:a] + " " + metin[b:]
    formuller = []
    for p in BLOK_FORMUL:
        formuller += [m.group(1).strip() for m in p.finditer(metin)]
        metin = p.sub(" ", metin)
    satir_ici = [m.group(1).strip() for m in SATIR_ICI.finditer(metin)]  # metinde kalir, yalniz formul eslemede aday
    metin = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", metin)
    metin = re.sub(r"<[^>]+>", " ", metin)
    metin = re.sub(r"\s+", " ", metin).strip()
    return metin, tablolar, formuller, satir_ici


def ned(a, b):
    return Levenshtein.distance(a, b) / max(len(a), len(b)) if (a or b) else 0.0


def tcs_ve_karisiklik(ref, hyp):
    n = sum(c in TURKCE for c in ref)
    if n == 0:
        return np.nan, np.nan
    e = 0
    for tag, i1, i2, j1, j2 in Levenshtein.opcodes(ref, hyp):
        if tag in ("delete", "replace"):
            e += sum(c in TURKCE for c in ref[i1:i2])
        if tag in ("insert", "replace"):
            e += sum(c in TURKCE for c in hyp[j1:j2])
    kar = sum(1 for op, i, j in Levenshtein.editops(ref, hyp) if op == "replace" and frozenset((ref[i], hyp[j])) in IKIZ)
    return max(0.0, 1 - e / n), kar / n


# --- TEDS (PubTabNet tanimi: dugum = etiket + colspan/rowspan + hucre icerigi) ---
class Dugum:
    def __init__(self, etiket, colspan=1, rowspan=1, icerik=""):
        self.etiket, self.colspan, self.rowspan, self.icerik, self.children = etiket, colspan, rowspan, icerik, []


class TedsAyar(Config):
    def rename(self, a, b):
        if a.etiket != b.etiket or a.colspan != b.colspan or a.rowspan != b.rowspan:
            return 1.0
        if a.etiket == "td":
            return ned(a.icerik, b.icerik)
        return 0.0

    def children(self, d):
        return d.children


def agac(html):
    t = BeautifulSoup(html, "lxml").find("table")
    kok, n = Dugum("table"), 1
    for tr in t.find_all("tr"):
        satir = Dugum("tr")
        n += 1
        for td in tr.find_all(["td", "th"]):
            icerik = re.sub(r"\s+", " ", td.get_text(" ")).strip()
            satir.children.append(Dugum("td", int(td.get("colspan", 1) or 1), int(td.get("rowspan", 1) or 1), icerik))
            n += 1
        kok.children.append(satir)
    return kok, n


def teds(gt_html, hyp_html):
    (a, na), (b, nb) = agac(gt_html), agac(hyp_html)
    return 1 - APTED(a, b, TedsAyar()).compute_edit_distance() / max(na, nb)


def tablo_metni(htmls):
    return re.sub(r"\s+", " ", " ".join(BeautifulSoup(h, "lxml").get_text(" ") for h in htmls)).strip()


def cdm(ref, hyp):
    ops = Levenshtein.opcodes(ref, hyp)
    tp = sum(i2 - i1 for t, i1, i2, _, _ in ops if t == "equal")
    return 2 * tp / (len(ref) + len(hyp)) if (ref or hyp) else 1.0


def sayfa(gt_md, hyp_md):
    gm, gt_tab, gt_for, _ = ayristir(gt_md)
    hm, hy_tab, hy_for, hy_satir_ici = ayristir(hyp_md)
    hy_for = hy_for + hy_satir_ici  # GT'de blok olan formulu model cumle icinde yazmis olabilir
    tcs, kar = tcs_ve_karisiklik(gm, hm)
    r = {"metin_ned": ned(gm, hm), "metin_mesafe": Levenshtein.distance(gm, hm), "metin_payda": max(len(gm), len(hm)),
         "tcs": tcs, "aksan_karisiklik": kar,
         "gt_tablo": len(gt_tab), "model_tablo": len(hy_tab), "gt_formul": len(gt_for)}
    if gt_tab:
        # en iyi eslesme; eslesmeyen GT ya da fazla model tablosu 0 sayilir
        t = {(i, j): teds(gt_tab[i], hy_tab[j]) for i in range(len(gt_tab)) for j in range(len(hy_tab))}
        es = eslestir(list(range(len(gt_tab))), list(range(len(hy_tab))), lambda i, j: 1 - t[i, j])
        r["tablo_teds"] = sum(t[i, j] for i, j in es) / max(len(gt_tab), len(hy_tab))
        r["tablo_ned"] = ned(tablo_metni(gt_tab), tablo_metni(hy_tab))
    else:
        r["tablo_uydurma"] = float(bool(hy_tab))
    if gt_for:
        # GT formulu basina en iyi eslesen model formulu; eslesmeyen GT: NED 1, CDM 0
        sade = lambda x: re.sub(r"\s+", "", x)
        g, h = [sade(x) for x in gt_for], [sade(x) for x in hy_for]
        es = eslestir(g, h, ned)
        r["formul_ned"] = (sum(ned(g[i], h[j]) for i, j in es) + len(g) - len(es)) / len(g)
        r["formul_cdm"] = sum(cdm(g[i], h[j]) for i, j in es) / len(g)
    return r


def guven(x, rng):
    x = np.asarray([v for v in x if not np.isnan(v)])
    if len(x) == 0:
        return np.nan, np.nan, np.nan, 0
    b = rng.choice(x, (5000, len(x))).mean(1)
    return x.mean(), np.percentile(b, 2.5), np.percentile(b, 97.5), len(x)


def main():
    gt_kok, cikti = Path(sys.argv[1]), Path(sys.argv[2])
    modeller = dict(a.split("=", 1) for a in sys.argv[3:])
    gt = {p.parent.name: p.read_text(encoding="utf-8", errors="ignore") for p in gt_kok.glob("data_*/data_*.md")}
    satirlar, ozet, rng = [], [], np.random.default_rng(0)
    for ad, klasor in modeller.items():
        for d, gmd in gt.items():
            p = Path(klasor) / d / f"{d}.md"
            if not p.exists():
                continue
            r = sayfa(gmd, p.read_text(encoding="utf-8", errors="ignore"))
            r.update(model=ad, sayfa=d)
            satirlar.append(r)
        df = pd.DataFrame([s for s in satirlar if s["model"] == ad])
        # toplam NED: her karakter esit agirlikli (kisa sayfalar ortalamayi domine etmez)
        o = {"model": ad, "sayfa": len(df), "metin_ned_toplam": round(df.metin_mesafe.sum() / df.metin_payda.sum(), 3)}
        for c in ["metin_ned", "tcs", "aksan_karisiklik", "tablo_teds", "tablo_ned", "formul_ned", "formul_cdm", "tablo_uydurma"]:
            if c in df:
                m, lo, hi, n = guven(df[c].values, rng)
                o[c] = round(m, 3)
                if c in ("metin_ned", "tcs", "tablo_teds"):
                    o[c + "_ga"] = f"{lo:.3f}-{hi:.3f}"
                if c in ("tablo_teds", "formul_ned"):
                    o[c + "_n"] = n
        ozet.append(o)
    pd.DataFrame(satirlar).to_csv(cikti.with_name(cikti.stem + "_sayfa.csv"), index=False)
    oz = pd.DataFrame(ozet)
    oz.to_csv(cikti, index=False)
    with pd.option_context("display.width", 250, "display.max_columns", 30):
        print(oz.to_string(index=False))


if __name__ == "__main__":
    main()
