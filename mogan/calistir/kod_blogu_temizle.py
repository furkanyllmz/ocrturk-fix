"""Model ciktisindaki kod blogu isaretlerini (```markdown, ```html, ```) satir olarak siler, icerige dokunmaz.
eval.py ``` ... ``` arasini tamamen sildigi icin, ciktisini kod bloguna saran modeller icin ayri olcum.
Kullanim: python kod_blogu_temizle.py <girdi_klasoru> <cikti_klasoru>"""
import pathlib
import re
import sys

CIT = re.compile(r"^[ \t]*```[\w-]*[ \t]*$", re.M)

girdi, cikti = map(pathlib.Path, sys.argv[1:3])
n = degisen = 0
for md in girdi.glob("data_*/data_*.md"):
    metin = md.read_text(encoding="utf-8", errors="ignore")
    yeni = CIT.sub("", metin)
    hedef = cikti / md.relative_to(girdi)
    hedef.parent.mkdir(parents=True, exist_ok=True)
    hedef.write_text(yeni, encoding="utf-8")
    n += 1
    degisen += yeni != metin
print(f"{girdi}: {n} sayfa, {degisen} sayfada kod blogu isareti silindi")
