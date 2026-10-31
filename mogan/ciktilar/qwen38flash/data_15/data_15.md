```markdown
<!-- Image (156, 32, 471, 245) -->

Şekil 12. Maksimum Tensile Stress Theory'ye göre emniyet katsayısı (S) (Safety coefficient (S) according to Maximum Tensile Stress Theory)

## Yapay Sinir Ağları (YSA) Sonuçları

Gerçek YSA modelinin belirlenmesi için farklı algoritmalarla denemeler yapılmış, hem eğitim (training) hem de test performansı en yüksek değere sahip olan YSA modeli belirlenmiştir. Çizelge 2'de çeşitli öğrenme fonksiyonu, gizli katman sayıları ve nöron sayılarına sahip YSA modelleri ve model performansları verilmiştir.

10 Girdi+Gizli Katman 1 Tansig (13)+Gizli Katman 2 Tansig (15)+Gizli Katman 3 Logsig (27)+Gizli Katman 4 Purelin (9) ve 9 Çıktılı modelde elde edilen sonuçlar aşağıda sırası ile verilmiştir. Şekil 13'de YSA modelinin Best Traning performans değeri verilmiştir. Şekle göre modelin en iyi öğrenme performansı $4.0111.E^{-10}$ olarak 929. Epoch'da elde edildiği görülmektedir. Modelin öğrenme performansı R~1 olarak hesaplanmıştır (Şekil 14).

Çizelge 2. Farklı YSA modelleri ve performans değerleri
(Different ANN models and performance values)

<!-- Image (542, 31, 882, 303) -->

Şekil 13. En iyi öğrenme performansı (Best Training performance)

<!-- Image (551, 360, 874, 634) -->

Şekil 14. Öğrenme Performansı (Learning Performance)

<!-- Table (116, 671, 914, 922) -->
\begin{tabular}{|l|l|l|l|l|l|l|l|l|l|}
\hline
\textbf{Test} & \textbf{Net Adı} & \textbf{Eğitim} & \textbf{Test} & \textbf{Eğitim} & \textbf{Test} & \textbf{Eğitim} & \textbf{Hata} & \textbf{Gizli} & \textbf{Çıktı} \\
\textbf{No} & & \textbf{performans} & \textbf{performans} & \textbf{Hatasi} & \textbf{Hatasi} & \textbf{Algoritması} & \textbf{Fonk.} & \textbf{katman} & \textbf{katman} \\
& & & & & & & & \textbf{Aktivasyon} & \textbf{Aktivasyon} \\
& & & & & & & & \textbf{Fonk.} & \textbf{Fonk.} \\
\hline
1 & RBF 6-35-1 & -0.173001 & 0.47628 & 1.53E+12 & 1.23E+11 & RBFT & SOS & Gaussian & Identity \\
\hline
2 & MLP 6-35-1 & 0.950973 & 0.970745 & 3.30E-03 & 4.80E-03 & BFGS 9 & SOS & Identity & Identity \\
\hline
3 & MLP 6-35-1 & 0.93528 & 0.961201 & 4.40E-03 & 4.44E-03 & BFGS 7 & SOS & Identity & Tanh \\
\hline
4 & MLP 6-35-1 & 0.977747 & 0.991454 & 1.58E-03 & 9.54E-04 & BFGS 9 & SOS & Identity & Logistic \\
\hline
5 & MLP 6-35-1 & 0.950781 & 0.971731 & 3.32E-03 & 4.18E-03 & BFGS 9 & SOS & Identity & Sine \\
\hline
6 & MLP 6-35-1 & 0.950871 & 0.969959 & 3.31E-03 & 4.95E-03 & BFGS 35 & SOS & Sine & Identity \\
\hline
7 & MLP 6-35-1 & 0.934904 & 0.959152 & 4.42E-03 & 4.77E-03 & BFGS 7 & SOS & Sine & Tanh \\
\hline
8 & MLP 6-35-1 & 0.972084 & 0.990051 & 2.82E-03 & 9.37E-04 & BFGS 5 & SOS & Sine & Logistic \\
\hline
9 & MLP 6-35-1 & 0.993797 & 0.998625 & 4.54E-04 & 2.84E-04 & BFGS 8 & SOS & Sine & Exponential \\
\hline
10 & MLP 6-35-1 & 0.95013 & 0.969395 & 3.35E-03 & 4.73E-03 & BFGS 22 & SOS & Sine & Sine \\
\hline
\end{tabular}
```