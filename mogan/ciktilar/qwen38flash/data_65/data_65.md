```markdown
<!-- Image (105, 22, 450, 183) -->

Şekil 3. Faster R-CNN transfer öğrenmenin uygulanmadığı/transfer öğrenmeli 200 epokluk eğitim sonucundaki yitim değeri

<!-- Image (105, 259, 449, 418) -->

Şekil 4. YOLO V4 transfer öğrenmenin uygulanmadığı/transfer öğrenmeli 200 epokluk eğitim sonucundaki yitim değeri

<!-- Image (108, 488, 447, 645) -->

Şekil 5. YOLO V5 transfer öğrenmenin uygulanmadığı/transfer öğrenmeli 200 epokluk eğitim sonucundaki yitim değeri

Tablo 1.Modellerin eğitim süresi karşılaştırması
<!-- Table (108, 733, 886, 957) -->
\begin{tabular}{|l|l|}
\hline
\textbf{Eğitim modelleri} & \textbf{Eğitim süreleri (saat)} \\
\textbf{(200 Epok)} & \\
\hline
Transfer öğrenmesiz faster R-CNN & 64.53 \\
Transfer öğrenmeli faster R-CNN & 65.58 \\
Transfer öğrenmesiz YOLO V4 & 15.13 \\
Transfer öğrenmeli YOLO V4 & 15.30 \\
Transfer öğrenmesiz YOLO V5 & 4.65 \\
Transfer öğrenmeli YOLO V5 & 4.84 \\
\hline
\end{tabular}

Kayıp değeri, bizim problemimiz için kask tespit hatasını göstermektedir. Yani ne kadar büyük bir yitim değeri çıkarsa o kadar yanlış tespit yapılmış demektir. 200 epok sonucunda, 6 model arasında 0.1 ile en düşük (başarılı) yitim değerine ulaşan model, transfer öğrenmeli YOLO V5'tir. Transfer öğrenmeli YOLO V5 modeli \%98 f1 skor ile en yüksek başarıma ulaşmıştır.

<!-- Image (580, 146, 868, 396) -->

Şekil 6.Transfer öğrenmeli YOLO V5 modelinden birkaç başarılı örnek

Tabo 1'den görüleceği üzere transfer öğrenmenin uygulandığı modeller, 3.500 adet eğitim ve validasyon görüntüsü üzerindeki 200 epokluk eğitimlerinde, süre açısından bir avantaj sağlamamış aynı zamanda kayda değer bir zaman kaybına sebep de açmamıştır. Tüm modellerin en baştan eğitimleri, transfer öğrenmenin uygulandığı modellere göre az da olsa daha kısa sürede tamamlanmıştır.
Transfer öğrenmenin uygulanmadığı modellerin doğru tespit oranları transfer öğrenme uygulananlara göre daha az çıkmıştır. Transfer öğrenme modellerin yüksek başarıım çıkmasındaki sebep yanlış tespit oranlarının daha az olmasıdır.
6 modelin 750 test görüntüsündeki 3.564 adet nesneyi tespit başarım karşılaştırmasını sunan karışıklık matrisleri Şekil 7'de gösterildiği gibidir.
```