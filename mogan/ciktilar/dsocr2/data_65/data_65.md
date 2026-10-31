0,185
0,18
0,175
0,17
0,165
0,16
0,155
0,15
200 Epok Sonunda

Transfer Öğrenmeli
Transfer Öğrenmesiz

Şekil 3. Faster R-CNN transfer öğrenmenin uygulanmadığı/transfer öğrenmeli 200 epokluk eğitim sonucundaki yitim değeri

0,16
0,14
0,12
0,1
0,08
0,06
0,04
0,02
0
200 Epok Sonunda

Şekil 4. YOLO V4 transfer öğrenmenin uygulanmadığı/transfer öğrenmeli 200 epokluk eğitim sonucundaki yitim değeri

0,14
0,12
0,1
0,08
0,06
0,04
0,02
0
200 Epok Sonunda

Şekil 5. YOLO V5 transfer öğrenmenin uygulanmadığı/transfer öğrenmeli 200 epokluk eğitim sonucundaki yitim değeri

0,185
0,18
0,175
0,17
0,165
0,16
0,155
0,15
200 Epok Sonunda

Transfer Öğrenmeli
Transfer Öğrenmesiz

Şekil 6. Transfer öğrenmeli YOLO V5 modelinden birkaç başarılı örnek

Tablo 1’den görüleceği üzere transfer öğrenmenin uygulandığı modeller, 3.500 adet eğitim ve validasyon görüntüsü üzerindeki 200 epokluk eğitimlerinde, süre açısından bir avantaj sağlamamış aynı zamanda kayda değer bir zaman kaybına sebep de açmamıştır. Tüm modellerin en başarı eğitimleri, transfer öğrenmenin uygulandığı modellere göre az da olsa daha kısa sürede tamamlanmıştır.

Transfer öğrenmenin uygulanmadığı modellerin doğru tespit oranları transfer öğrenme uygulananlara göre daha az çıkmıştır. Transfer öğrenme modellerin yüksek başarım çıkmasındaki sebep yanlış tespit oranlarının daha az olmasıdır.

6 modelin 750 test görüntüsündeki 3.564 adet nesneyi tespit başarım karşılaştırmasını sunan karışıklık matrisleri Şekil 7’de gösterildiği gibidir.

---

### Tablo 1. Modellerin eğitim süresi karşılaştırması

| Eğitim modelleri (200 Epok) | Eğitim süreleri (saat) |
|---|---|
| Transfer öğrenmesiz faster R-CNN | 64.53 |
| Transfer öğrenmeli faster R-CNN | 65.58 |
| Transfer öğrenmesiz YOLO V4 | 15.13 |
| Transfer öğrenmeli YOLO V4 | 15.30 |
| Transfer öğrenmesiz YOLO V5 | 4.65 |
| Transfer öğrenmeli YOLO V5 | 4.84 |