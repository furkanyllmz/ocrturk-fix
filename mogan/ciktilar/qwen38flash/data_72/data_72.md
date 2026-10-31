```markdown
### 2.6. Evrişimsel Sinir Ağları

Evrişimsel sinir ağları, çok boyutlu girdiler için ve özellikle iki boyutlu görsel veriler için önerilmiş bir derin öğrenme yöntemidir (LeCun vd., 1998). Evrişimsel sinir ağları diğer sinir ağlarına göre daha az sayıda nöron bağlantısına sahiptir ve birçok farklı sürümü literatürde mevcuttur. Bu sinir ağları öğrenme aşamasında oldukça büyük boyutta işaretli veriye ihtiyaç duymaktadır (Ravi vd., 2017). Bu derin öğrenme yöntemi doğal dil işleme alanındaki çeşitli problemler üzerinde uygulanmış ve başarılı sonuçlar elde edilmiştir.

## 3. DOĞAL DİL İŞLEME ALANINDAKİ DERİN ÖĞRENME ÇALIŞMALARI

Derin öğrenmenin bir önceki bölümde anlatılan farklı yöntemlerinden özellikle yinelenen sinir ağları ve evrişimsel sinir ağlarının doğal dil işleme problemlerini çözmede de başarılı sonuçlar verdiği görülmüştür. Örneğin; evrişimsel sinir ağlarının doğal dil işlemenin çok farklı problemlerini çözmede kullanılabileceği, çok görevli öğrenme için birleşik bir mimarinin tanıtıldığı bir çalışmada gösterilmiştir (Collobert ve Weston, 2008). Bahsi geçen bu iki yöntemle birlikte; diğer derin öğrenme yöntemlerinin de doğal dil işlemenin çeşitli problemlerinde kullanılabileceği ve bu yöntemlere dayalı başarılı sistemlerin geliştirilebileceği, literatürdeki farklı çalışmalarda ifade edilmiştir (Socher vd., 2012).

Bu bölümün aşağıdaki alt bölümlerinde de doğal dil işleme alanındaki örnek problemler ve bu problemler için derin öğrenme yaklaşımlarının tanıtıldığı çalışmalara yer verilmiştir. Ayrıca, Tablo 2'de bu alt bölümlerde açıklanan problemler ve çözümünde kullanılan derin öğrenme yöntemleri özet şeklinde sunulmuştur.

Tablo 2. Tanıtılan Doğal Dil İşleme Problemleri ve Kullanılan Derin Öğrenme Yöntemleri

<!-- Table (80, 560, 787, 928) -->
\begin{tabular}{|l|l|}
\hline
\textbf{Doğal Dil İşleme Problemi} & \textbf{Kullanılan Derin Öğrenme Yöntemleri} \\
\hline
\textbf{Metin Sınıflandırma} & \textbullet{} Evrişimsel Sinir Ağları \\
& \textbullet{} Yinelenmeli Evrişimsel Sinir Ağları \\
& \textbullet{} LSTM ve Evrişimsel Sinir Ağları \\
\hline
\textbf{Metin Ayırıştırma} & \textbullet{} Evrişimsel Sinir Ağları \\
\hline
\textbf{Duygu Analizi} & \textbullet{} Derin Oto-Kodlayıcılar \\
& \textbullet{} Evrişimsel Sinir Ağları \\
\hline
\textbf{Bilgi Çıkarımı} & \textbullet{} Derin Sinir Ağları \\
\hline
\textbf{Varlık İsmi Tanıma} & \textbullet{} LSTM ve Evrişimsel Sinir Ağları \\
\hline
\textbf{Zamansal İlişki Çıkarımı} & \textbullet{} Evrişimsel Sinir Ağları \\
\hline
\textbf{Olay Çıkarımı} & \textbullet{} Evrişimsel Sinir Ağları \\
\hline
\textbf{Sözcük Türü Etiketleme} & \textbullet{} Derin Sinir Ağları \\
& \textbullet{} LSTM \\
\hline
\textbf{Metin Sıralama} & \textbullet{} Evrişimsel Sinir Ağları \\
\hline
\textbf{Otomatik Harf Çevirisi} & \textbullet{} Derin İnanaç Ağları \\
\hline
\textbf{Otomatik Soru Cevaplama} & \textbullet{} Evrişimsel Sinir Ağları \\
& \textbullet{} LSTM \\
\hline
\end{tabular}
```