```markdown
# Tablo 4. Farklı Boyut Küçültme Algoritmalarının Performansı (Performance of Different Feature Selection Algorithms)

| Algoritma/ Doğruluk Ölçüleri | Toplam Doğruluk (%) | F-değerlendirme (Anormal sınıf) (%) |
| :--- | :--- | :--- |
| CFS | 58.39 | 58.0 |
| İlinti Öznitelik Değerlendirme (Correlation Attribute Evaluation) | 56.20 | 55.2 |
| Kazanım Oranı (Gain Ratio) | 58.02 | 57.3 |
| Bilgi Kazanımı (Info Gain) | 60.94 | 60.2 |
| PCA | 61.31 | 60.1 |
| Relief Ranking | 56.56 | 55.5 |
| Simetrik Belirsizlik (Symmetrical Uncertainty) | 58.75 | 58.2 |
| Tek Kural Öznitelik (One Rule Attribute) | 60.58 | 60.6 |

Bir başka deneyde literatürde görüntü sınıflandırma görevlerinde daha fazla tercih edilen çok katmanlı algılıcı (MLP) VS2 üzerinde uygulanmıştır. Kullanılan MLP'nin girişi katmanı ve çıktı katmanı bulunmaktadır. Gizli katmanın 25 adet gizli birimi (M) bulunmaktadır. Gizli katman ve çıktı katmanının aktivasyon fonksiyonu hiperbolik tanjant ve maliyet fonksiyonu çapraz entropidir. Ağırlıklar [-1,1] aralığında düzgün dağılım kullanarak rastgele başlatılmıştır. Başlangıçta sabit bir öğrenme oranı olan $\eta = 0.1$ kullanılmıştır. Optimum epok ve yineleme sayısını bulmak için erken dururma kriteri kullanılmıştır. Bu kriterin çalışma prensibi takip eden adımlardan oluşmaktadır; veri setinin %80'i eğitim seti, %10'u doğrulama ve geri test seti olarak kullanılmıştır. En fazla 20 epok gerçekleştirilerek optimum sayıda epok ve yineleme, doğrulama veri seti kullanılarak bulunmuştur. Optimum sayıda yineleme ve epok bulunduğunda, sınıflandırma eğitim ve test setleri kullanılarak optimum değerler ile yapılmıştır. Bu deney için sınıflandırıcının kodu TensorFlow kullanılarak yazılmıştır (Abadi vd., 2016).

MLP ağı eğitirken veri setinde aşağıda belli bir öznitelik grubuna ağırlık verilmemesi için minimum-maksimum normalizasyonu yapılmıştır. Ayrıca önceki deneylerde iyi sonuç veren boyut küçültme algoritması MLP için de denemiştir. Tablo 5'de normalizasyonu yapılan, boyut küçültme olan ve olmayan veri setleri kullanılarak MLP sınıflandırma ile 10 katlı ÇD sonuçları sunulmuştur. Tablodan da görüldüğü üzere boyut küçültme doğruluk sonuçlarını artırmıştır.

## Tablo 5. MLP ile 10-Katlı Çapraz Doğrulama Sonuçları (MLP Results for 10 Fold CV)

| Görüntü/Doğruluk Ölçüleri | Doğruluk (Genel) |
| :--- | :--- |
| Normalizasyon yapılmış, boyut küçültme yapılmamış | %70.35 |
| Normalizasyon yapılmış, boyut küçültülmüş | %72.5 |

MLP ağı optimum duruma getirmek için takip eden deneyler yapılmıştır: MLP üzerinde çevrimiçi öğrenme, toplu öğrenme yöntemi ve kısa-toplu öğrenme yöntemi kullanarak birbirini ile bağlantılı olan iki deney yapılmıştır. Bu iki deneyde optimum öğrenme oranına yakınsamak için; ilk olarak farklı öğrenme oranları, ara-sonra-yakınsa öğrenme yaklaşımı kullanılarak (Denklem 4) uygulanmıştır. İkincisinde momentum katsayısı kullanılarak optimum değere yakınsanmaya çalışılmıştır. Denklem 4'de yineleme sayısını göstermektedir ve 1, 10, ..., 100.000 arasındaki değerler, $\eta_0=0.1$ ve $\tau=10000$ değerlerini almıştır.

$$ \eta(n) = \frac{\eta_0}{1 + \frac{n}{\tau}} \tag{4} $$

Deneyler 10-katlı ÇD kullanılarak VS2 üzerinde gerçekleştirilmiştir. Bu deneylerin sonuçları Tablo 6'da gösterilmiştir. 10 katlı çapraz doğrulama için sabit bir öğrenme oranı olan $\eta = 0.01$ kullanılmıştır.
```