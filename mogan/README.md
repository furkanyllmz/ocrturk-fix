# Düzeltilmiş OCRTurk değerlendirmesi (Mogan-OCR)

Bu klasör, OCRTurk'ün orijinal dosyalarına (`data/`, `eval.py`) dokunmadan şunları ekler:
- düzeltilmiş bir değerlendirme betiği,
- yerelde model çalıştırma betiği,
- 7 modelin ham çıktıları ve skorları.

## Neden

Depodaki `eval.py` makaledeki ([arXiv 2602.03693](https://arxiv.org/abs/2602.03693)) yöntemi uygulamıyor ve birkaç hata içeriyor:

1. **TEDS'te maliyet ters.** `sub_cost = 1 - _ned_similarity(...)` yazıyor, ama `_ned_similarity` benzerlik değil uzaklık döndürüyor. Doğru tablo kendisiyle karşılaştırılınca 1,0 yerine **0,59** alıyor.
2. **TEDS ağaç üzerinde değil.** Makale ağaç düzenleme mesafesi tanımlıyor; kod satır dizisi üzerinde hesaplıyor.
3. **Tablo ve formül skorları bütün sayfalarda ortalanıyor.** Öğesi olmayan sayfa tam puan alıyor: 180 sayfanın 138'i tablosuz ve hepsi TEDS 1,0 alıyor.
4. **Metin küçük harfe çevriliyor.** Bu yüzden İ/I hataları TCS'de hiç sayılmıyor: 5 İ→I hatası olan sayfa TCS 1,000 alıyor.
5. **TCS hizalaması hatalı sayıyor.** `difflib` (autojunk açık) uzun sayfalarda hata sayısını şişiriyor: 52 ı→i hatası 0,687 yerine 0,639 veriyor.
6. **Makaledeki temizlik kodda yok.** Makale ˘g→ğ, ¸s→ş düzeltmesini ve `#`, `**` silmeyi tarif ediyor, kod yapmıyor.
7. **Kod blokları metinden tamamen siliniyor.** Çıktısını ```` ``` ```` içine yazan modeller metin skorunda çöküyor.
8. **Tablo içerikleri ve blok formüller metin skoruna da giriyor.** Aynı hata iki kez cezalandırılıyor.
9. **Formüller sırayla eşleştiriliyor.** Tek bir kayma bütün eşleşmeleri bozuyor.

`ocrturk_duzgun.py` bunları şöyle düzeltir:
- Gerçek TEDS (APTED ile HTML ağacı) ve harfe duyarlı TCS.
- TCS'nin yanında yalnız ı/i, İ/I, ş/s, ğ/g, ç/c, ö/o, ü/u karışmalarını sayan bir "aksan karışıklığı" ölçütü.
- Formül ve tablolarda en iyi eşleşme (Macar algoritması). LaTeX `tabular` tablolar da HTML'e çevrilir.
- Tablo ve formül skorları yalnız o öğeyi içeren sayfalarda ortalanır.
- Sayfa ortalamasının yanında toplam NED.
- %95 bootstrap güven aralığı.

Ayrıntı betiğin başındaki açıklamada.

**Doğrulama:** Doğru etiket kendisiyle karşılaştırılınca 180 sayfanın hepsinde kusursuz skor alıyor. Kontrollü hatalar beklenen değeri veriyor: 5 İ→I hatası 0,971, 52 ı→i hatası 0,696.

**Şekiller:** Şekil ölçümleri (MSE, DreamSim) bu betikte yok. Şekilleri ayrı dosya olarak çıkaran modeller için orijinal `eval.py --images` kullanılabilir.

## Dosyalar

| Yol | İçerik |
|---|---|
| `ocrturk_duzgun.py` | Düzeltilmiş değerlendirme |
| `calistir/ocrturk_kos.py` | Yerelde MLX ile okutma (Qwen3.5-2B bf16) |
| `calistir/kod_blogu_temizle.py` | Yalnız kod bloğu satırlarını siler; orijinal `eval.py` ile karşılaştırma için |
| `ciktilar/<model>/data_N/data_N.md` | Modellerin ham çıktıları; `kayit.jsonl` süre ve token |
| `sonuclar/duzgun_ozet*.csv` | Düzeltilmiş değerlendirmenin özeti ve sayfa düzeyindeki skorlar |
| `sonuclar/orijinal_eval/<model>/` | Orijinal `eval.py` çıktıları; `_temiz` = kod bloğu temizlenmiş |

## Çalıştırma

Depo kökünden:

```bash
pip install -r mogan/requirements.txt
mkdir -p png && for d in data/data_*/; do n=$(basename $d); pdftoppm -r 150 -png -singlefile "$d/$n.pdf" "png/$n"; done

# yerelde model çalıştırma (MLX); kalan sayfadan devam eder
python mogan/calistir/ocrturk_kos.py --png png --cikti mogan/ciktilar/qwen35_2b

# düzeltilmiş değerlendirme
python mogan/ocrturk_duzgun.py data mogan/sonuclar/duzgun_ozet.csv \
  gemma4=mogan/ciktilar/gemma4 qwen3vl30b=mogan/ciktilar/qwen3vl30b \
  qwen38flash=mogan/ciktilar/qwen38flash dsocr2=mogan/ciktilar/dsocr2 qwen35_2b=mogan/ciktilar/qwen35_2b
```

Bütün modellere aynı istem verildi (`calistir/ocrturk_kos.py` içinde `ISTEM`): Markdown, tablolar HTML, formüller LaTeX, üst ve alt bilgi atlanır.

## Sonuçlar (düzeltilmiş ölçüm)

| Model | Metin NED, toplam ↓ | Metin NED, sayfa ort. ↓ | TCS ↑ | Aksan karışıklığı ↓ | Tablo TEDS ↑ (42 sayfa) | Formül CDM ↑ (27 sayfa) |
|---|---:|---:|---:|---:|---:|---:|
| Qwen3.8-flash-next | **0,042** | **0,059** | **0,941** | **0,002** | 0,745 | 0,898 |
| Qwen3-VL-30B (178 sayfa) | 0,071 | 0,126 | 0,871 | 0,010 | 0,849 | 0,843 |
| Gemma-4-31B | 0,075 | 0,100 | 0,928 | 0,003 | **0,905** | **0,920** |
| DeepSeek-OCR-2 | 0,178 | 0,175 | 0,840 | 0,007 | 0,732 | 0,830 |
| Qwen3.5-2B (yerel) | 0,275 | 0,144 | 0,856 | 0,010 | 0,721 | 0,776 |

- **Güven aralıkları:** `sonuclar/duzgun_ozet.csv` içinde. İlk üç modelin aralıkları örtüşüyor.
- **Qwen3.5-2B:** 13 sayfada tekrar döngüsüne girip 6.000 token sınırına dayanıyor; toplam NED'i bu yüzden yüksek.
- **Yarım koşular:** DeepSeek-v4.1-flash (`dsflash`) ve MiMo-v2.6-pro (`mimo`) henüz tamamlanmadı.
