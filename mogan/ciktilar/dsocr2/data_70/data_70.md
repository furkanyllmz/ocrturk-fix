**Tablo 4.** Farklı Boyut Küçültme Algoritmalarının Performansı (Performance of Different Feature Selection Algorithms)

| Algoritma/ Doğruluk Ölçüleri | Toplam Doğruluk (%) | F-değerlendirme (Anormal sınıf)(%) |
|---|---|---|
| CFS    | 58.39    | 58.0    |
| İkinci Öznitelik Değerlendirme (Correlation Attribute Evaluation) | 56.20 | 55.2    |
| Kazanım Oranı (Gain Ratio)    | 58.02    | 57.3    |
| Bilgi Kazanımı (Info Gain)    | 60.94    | 60.2    |
| PCA    | 61.31    | 60.1    |
| Relief Ranking    | 56.56    | 55.5    |
| Simetrik Belirsizlik (Symmetrical Uncertainty) | 58.75 | 58.2    |
| Tek Kural Öznitelik (One Rule Attribute) | 60.58 | 60.6    |

Bir başka deneyde literatürde görüntü sınıflandırma görevlerinde daha fazla tercih edilen çok katmanlı algılayıcı (MLP) VS2 üzerinde uygulanmıştır. Kullanılan MLP’nin girdi katmanı, bir adet gizli katmanı ve çıktı katmanı bulunmaktadır. Gizli katmanın 25 adet gizli birimi (\(M\)) bulunmaktadır. Gizli katman ve çıktı katmanın aktivasyon fonksiyonu hiperbolik tanjant ve maliyet fonksiyonu çarpan etki arzını ön plana getirmiştir. Ağırlıklar [-1,1] aralığında düzgün dağılım kullanarak stratejik başlatılmıştır. Başlangıçta sabit bir öğrenme oranı olan \(\eta = 0.1\) kullanılmıştır. Optimum eşdeğerlik ve yineleme sayısını bulmak için erken durdurmak kriterli kullanılmıştır. Bu kriterin çalışma prensibi takip eden adımlardan oluşmaktadır; veri setinin %80’i eğitim seti, %10’u doğrulama ve gerisi test seti olarak kullanılmıştır. En fazla 20 eşdeğerlik seçeneklerinin toplam sayısı eşdeğerlik seçenekleri ve yineleme, doğrulama veri seti kullanılarak bulunmuştur. Optimum sayıda yineleme ve eşdeğerlik seçeneklerinin toplam sayısının toplam eşdeğerlik seçenekleri ile eşdeğerlik seçimi sınıflandırma için sınıflandırma için sınıflandırma için sınıflandırma için sınıflandırma için sınırlarını seçmiştir.

**Tablo 5.** MLP ile 10-Katı Çapraz Doğrulama Sonuçları (MLP Results for 10 Fold CV)

| Görüntü/Doğruluk Ölçüleri | Doğruluk (Genel) |
|---|---|
| Normalizasyon yapılmış, boyut küçültme yapılmamış | %70.35    |
| Normalizasyon yapılmış, boyut küçültülmemiş | %72.5    |

MLP ağını optimum duruma getirmek için takip eden deneyler yapılmıştır: MLP üzerinde çevrimiçi öğrenme, toplu öğrenme yöntemi ve kısa-toplu öğrenme yöntemi kullanılarak birbiri ile bağlantılı olan iki deney yapılmıştır. Bu iki deneyde optimum öğrenme oranına yakınsamak için; ilk olarak farklı öğrenme oranları, ara-sonra-yakınsa öğrenme yaklaşımları kullanılarak (Denklem 4) uygulanmıştır. İkincisinde momentum katsayısı kullanılarak optimum değere yakınsanmaya çalışılmıştır. Denklem 4’de yineleme sayısının göstermektedir ve 1, 10, ..., 100.000 arasındaki değerleri, \(\eta_0=0.1\) ve \(\tau=10000\) değerlerini almıştır.

\[\eta(n) = \frac{\eta_0}{1 + \frac{n}{\tau}}\]

(4)

Deneyler 10-katı ÇD kullanılarak VS2 üzerinde gerçekleştirilmiştir. Bu deneylerin sonuçları Tablo 6’da gösterilmiştir. 10 katlı çapraz doğrulama için sabit bir öğrenme oranı olan \(\eta = 0.01\) kullanılmıştır.