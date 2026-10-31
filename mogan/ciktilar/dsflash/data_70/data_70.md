**Tablo 4.** Farklı Boyut Küçültme Algoritmalarının Performansı (Performance of Different Feature Selection Algorithms)

<table>
  <thead>
    <tr>
      <th><b>Algoritma/ Doğruluk Ölçüleri</b></th>
      <th><b>Toplam Doğruluk (%)</b></th>
      <th><b>F-değerlendirme (Anormal sınıf)(%)</b></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>CFS</b></td>
      <td>58.39</td>
      <td>58.0</td>
    </tr>
    <tr>
      <td><b>İlinti Öznitelik Değerlendirme (Correlation Attribute Evaluation)</b></td>
      <td>56.20</td>
      <td>55.2</td>
    </tr>
    <tr>
      <td><b>Kazanım Oranı (Gain Ratio)</b></td>
      <td>58.02</td>
      <td>57.3</td>
    </tr>
    <tr>
      <td><b>Bilgi Kazanımı (Info Gain)</b></td>
      <td>60.94</td>
      <td>60.2</td>
    </tr>
    <tr>
      <td><b>PCA</b></td>
      <td>61.31</td>
      <td>60.1</td>
    </tr>
    <tr>
      <td><b>Relief Ranking</b></td>
      <td>56.56</td>
      <td>55.5</td>
    </tr>
    <tr>
      <td><b>Simetrik Belirsizlik (Symmetrical Uncertainty)</b></td>
      <td>58.75</td>
      <td>58.2</td>
    </tr>
    <tr>
      <td><b>Tek Kural Öznitelik (One Rule Attribute)</b></td>
      <td>60.58</td>
      <td>60.6</td>
    </tr>
  </tbody>
</table>

Bir başka deneyde literatürde görüntü sınıflandırma görevlerinde daha fazla tercih edilen çok katmanlı algılayıcı (MLP) VS2 üzerinde uygulanmıştır. Kullanılan MLP’nin girdi katmanı, bir adet gizli katmanı ve çıktı katmanı bulunmaktadır. Gizli katmanın 25 adet gizli birimi (\(M\)) bulunmaktadır. Gizli katman ve çıktı katmanın aktivasyon fonksiyonu hiperbolik tanjant ve maliyet fonksiyonu çapraz entropidir. Ağırlıklar [-1,1] aralığında düzgün dağılım kullanarak rastgele başlatılmıştır. Başlangıçta sabit bir öğrenme oranı olan \(\eta = 0.1\) kullanılmıştır. Optimum epok ve yineleme sayısını bulmak için erken durdurma kriteri kullanılmıştır. Bu kriterin çalışma prensibi takip eden adımlardan oluşmaktadır; veri setinin %80'i eğitim seti, %10'u doğrulama ve gerisi test seti olarak kullanılmıştır. En fazla 20 epok gerçekleştirilerek optimum sayıda epok ve yineleme, doğrulama veri seti kullanılarak bulunmuştur. Optimum sayıda yineleme ve epok bulunduğunda, sınıflandırma eğitim ve test setleri kullanılarak optimum değerler ile yapılmıştır. Bu deney için sınıflandırıcının kodu TensorFlow kullanılarak yazılmıştır (Abadi vd., 2016).

MLP ağı eğitilirken veri setinde ağda belli bir öznitelik grubuna ağırlık verilmemesi için minimum-maksimum normalizasyonu yapılmıştır. Ayrıca önceki deneylerde iyi sonuç veren boyut küçültme algoritması MLP için de denenmiştir. Tablo 5'de normalizasyon yapılan, boyut küçültme olan ve olmayan veri setleri kullanılarak MLP sınıflandırma ile 10 katlı ÇD sonuçları sunulmuştur. Tablodan da görüldüğü üzere boyut küçültme doğruluk sonuçlarını arttırmıştır.

**Tablo 5.** MLP ile 10-Katlı Çapraz Doğrulama Sonuçları (MLP Results for 10 Fold CV)

<table>
  <thead>
    <tr>
      <th><b>Görüntü/Doğruluk Ölçüleri</b></th>
      <th><b>Doğruluk (Genel)</b></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Normalizasyon yapılmış, boyut küçültme yapılmamış</b></td>
      <td>%70.35</td>
    </tr>
    <tr>
      <td><b>Normalizasyon yapılmış, boyut küçültülmüş</b></td>
      <td>%72.5</td>
    </tr>
  </tbody>
</table>

MLP ağını optimum duruma getirmek için takip eden deneyler yapılmıştır: MLP üzerinde çevrimiçi öğrenme, toplu öğrenme yöntemi ve kısa-toplu öğrenme yöntemi kullanılarak birbiri ile bağlantılı olan iki deney yapılmıştır. Bu iki deneyde optimum öğrenme oranına yaklaşmak için; ilk olarak farklı öğrenme oranları, ara-sonra-yakınsa öğrenme yaklaşımı kullanılarak (Denklem 4) uygulanmıştır. İkincisinde momentum katsayısı kullanılarak optimum değere yakınsanmaya çalışılmıştır. Denklem 4’de n yineleme sayısını göstermektedir ve 1, 10, ..., 100.000 arasındaki değerleri, \(\eta_0=0.1\) ve \(\tau=10000\) değerlerini almıştır.

\[
 \eta(n) = \frac{\eta_0}{1 + \frac{n}{\tau}} \qquad (4) 
\]

Deneyler 10-katlı ÇD kullanılarak VS2 üzerinde gerçekleştirilmiştir. Bu deneylerin sonuçları Tablo 6’da gösterilmiştir. 10 katlı çapraz doğrulama için sabit bir öğrenme oranı olan \(\eta = 0.01\) kullanılmıştır.