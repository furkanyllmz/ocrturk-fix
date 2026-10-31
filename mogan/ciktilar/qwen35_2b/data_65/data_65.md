```markdown
# Şekil 3. Faster R-CNN transfer öğrenmenin uygulanmadığı/transfer öğrenmeli 200 epokluk eğitim sonucundaki yitim değeri

Kayıp değeri, bizim problemimiz için kask tespit hatası göstermektedir. Yani ne kadar büyük bir yitim değeri çıkarsa o kadar yanlış tespit yapılmış demektir. 200 epok sonunda, 6 model arasında 0.1 ile en düşük (başarılı) yitim değrine ulaşan model, transfer öğrenmeli YOLO V5'tir. Transfer öğrenmeli YOLO V5 modeli %98 fl skor ile en yüksek başarima ulaşmıştır.

Şekil 4. YOLO V4 transfer öğrenmenin uygulanmadığı/transfer öğrenmeli 200 epokluk eğitim sonucundaki yitim değeri

Şekil 5. YOLO V5 transfer öğrenmenin uygulanmadığı/transfer öğrenmeli 200 epokluk eğitim sonucundaki yitim değeri

Tablo 1'den görüleceği üzere transfer öğrenmenin uygulandığı modeller, 3.500 adet eğitim ve validasyon görüntüsü üzerinde 200 epokluk eğitimlerinde, sürede bir avantaj sağlamış aynı zamanda kayda değer bir zaman kaybına sebep de oynamamıştır. Tüm modellerin en başta eğitimleri, transfer öğrenmenin uygulandığı modellere göre az da olsa daha kısa sürede tamamlanmıştır.

Transfer öğrenmenin uygulandığı modellerin doğru tespit oranları transfer öğrenme uygulanananlara göre daha az çıkmıştır. Transfer öğrenme modellerin yüksek başarım çıkmasındaki sebep yanlış tespit oranlarının daha az olmasıdır.

6 modelin 750 test görüntüsündeki 3.564 adet nesneyi tespit başarım karşılaştırmasını sunan karışıklık matrisleri Şekil 7'de gösterildiği gibidir.

Şekil 6. Transfer öğrenmeli YOLO V5 modelinden birkaç başarılı örnek

## Tablo 1. Modellerin eğitim süresi karşılaştırması

| Eğitim modelleri (200 Epok) | Eğitim süreleri (saat) |
| :--- | :--- |
| Transfer öğrenmez faster R-CNN | 64.53 |
| Transfer öğrenmeli faster R-CNN | 65.58 |
| Transfer öğrenmez YOLO V4 | 15.13 |
| Transfer öğrenmeli YOLO V4 | 15.30 |
| Transfer öğrenmez YOLO V5 | 4.65 |
| Transfer öğrenmeli YOLO V5 | 4.84 |
```