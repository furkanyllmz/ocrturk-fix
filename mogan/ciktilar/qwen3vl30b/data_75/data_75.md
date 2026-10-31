```html
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>Derin Öğrenme Yöntemleri</th>
      <th>Derin Öğrenme Yöntemlerinin Kullanıldığı Alanlar</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Boltzmann makinesi</td>
      <td>Sınıflandırma ve en iyileme</td>
    </tr>
    <tr>
      <td>Derin inanç ağları</td>
      <td>Sınıflandırma, robotik ve bilgisayar görüşü</td>
    </tr>
    <tr>
      <td>Derin ileri beslemeli ağlar</td>
      <td>Regresyon, sınıflandırma, tahmin, robotik ve bilgisayar görüşü</td>
    </tr>
    <tr>
      <td>Evrişimli sinir ağları</td>
      <td>Regresyon, sınıflandırma, robotik ve bilgisayar görüşü</td>
    </tr>
    <tr>
      <td>Yinelemeli sinir ağları</td>
      <td>Regresyon, sınıflandırma, tahmin, robotik ve bilgisayar görüşü</td>
    </tr>
  </tbody>
</table>

Derin öğrenmenin birçok alanda uygulamaları vardır. Görüntü ve ses senkronizasyonu [25], fotoğraf çözünürlüğünü artırma [26], gerçek zamanlı kişi konum analizi [27], fotoğraf açıklama [28], fotograftaki insanların bakışlarında değişiklik yapma [29], gerçek zamanlı davranış analizi [30], fotoğraflardan yeni fotoğraf oluşturma [31], galaksi ve yarandag resimleri oluşturma[32, 33] görüntü alanındaki derin öğrenme örnekleribilmektedir. Bununla birlikte farklı diller arasında çeviri de derin öğrenme kullanılmaktadır [34]. Biyoloji alanında ise balina ve plankton sınıflandırması için de derin öğrenme kullanılmaktadır [35-38]. Yeni görüntüleri oluşturma [39], fotoğraf ve videolardan metin okuma [40] gibi alanlarda da derin öğrenme kullanılmaktadır. Bilgisayar oyunları[41], otonom araçlar[42] ve robotik [43,44] de derin öğrenmenin kullandığı alanlardır. Nesne tanima [45], demografik yapının tahmini [46] ve seçim sonuçlarının tahmini [47] alanlarında da derin öğrenme uygulanmaktadır.

<h2>2.2.1. Sağlık Alanında Kullanılan Derin Öğrenme Yöntemlerinin Kullanım Alanları</h2>

Bu bölümde sağlık alanında kullanılan derin öğrenme yöntemlerinin kullanım alanları açıklanarak, bu alanlarda yapılan çalışmalar incelenmiştir.

<h3>2.2.1.1. Biyoinformatik Alanında Kullanılan Derin Öğrenme Yöntemleri</h3>

Derin öğrenme yöntemleri, kanser teşhisi, gen seçimi ve sınıflandırması, gen çeşitliliği, ilaç tasarımı, bileşim protein etkileşimi, RNA ile protein ilişkisi ve DNA metilasyonu gibi biyoinformatik uygulamalarında kullanılmaktadır. Tablo 2’de biyoinformatik uygulamalarda kullanılan derin öğrenme yöntemleri ve hangi alanda kullanıldıkları gösterilmiştir.

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>Biyoinformatik Uygulamaları</th>
      <th>Uygulanan Derin Öğrenme Metotları</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Kanser teşhisi</td>
      <td>Derin oto-kodlayıcılar</td>
    </tr>
    <tr>
      <td>Gen seçimi ve sınıflandırması</td>
      <td>Derin inanç ağları</td>
    </tr>
    <tr>
      <td>Gen çeşitliliği</td>
      <td>Derin sinir ağları</td>
    </tr>
    <tr>
      <td>İlaç tasarımı</td>
      <td>Derin sinir ağları</td>
    </tr>
    <tr>
      <td>Bileşim-protein etkileşimi</td>
      <td>Derin sinir ağları</td>
    </tr>
    <tr>
      <td>RNA ile protein ilişkisi</td>
      <td>Derin inanç ağları</td>
    </tr>
    <tr>
      <td>DNA metilasyonu</td>
      <td></td>
    </tr>
  </tbody>
</table>

Sağlık alanında 2013 yılında Fakoor ve ark. nn gen çıkarmı verilerini kullanarak farklı kanser türlerini belirlemek, kanser tanısını ve sınıflandırmasını geliştirmek için derin öğrenme yöntemlerinden DOK yöntemini kullandıkları bilinmektedir. Yaptıkları çalışmada danışmansız özellik öğrenimi yöntemini kullanarak özellik çıkarmı için boyut azaltımı temelli bir yaklaşım belirlemişlerdir [48].

Ibrahim ve ark. [49] elde ettiği deneyssel sonuçlar, yaklaşımın hepatoselüler karsinoma (HCC) klasik özellik seçim yöntemlerini % 9, akciğer kanseri % 6 ve meme kanserinde F1 ölçümünde % 10’dan daha iyi bir performans gösterdiği söylenmiştir.

Khademi ve ark. nn göğüs kanserinin genetik teşhisi için yapıtları çalışmadı, mikro dizilimli verilerden özellik çıkarmak ve eksik özelliklerleri uyarlamak ve gürültülü gidermek için DİA ile olasılıksal grafiksel modellerden olan Bayes ağlarını birleştirmişlerdir [50]. Tıp uygulamalarında tahmin modelleri oluşturmak için uygun olan meme kanseri prognozu ve tanısı için olasılıksal bir grafik modeli (PGM) önermişlerdir. Kanserin temelde genetik bir hastalık olduğuunu, mikro dizi ve klinik verilerin entegrasyonu, bir öngörü modelinin doğruluğunu artırabileceği ifade etmişlerdir. Bununla birlikte, mikro dizi verileri yüksek boyutlu olduğuundan, genomik değişkenler de dahil olmak üzere, boyut ve küçük örnekler büyük ölçüde problemlerinden dolayı yapı ve parametre öğrenmede zayıf sonuçlara neden olabileceğini belirtmişlerdir. Bu problemler, manifold öğrenme ve mikro dizi verisine DİA uygulayarak ele almışlardır. Klinik verilere yapı öğrenme algoritması uygulayarak klinik modelin yapısını otomatik olarak çıkartmışlar ve daha sonra, bu iki modeli softmax düğümlerini kullanarak entegre etmişlerdir. METABRIC ve NKI gibi gerçek dünya veri tabanlarını kullanan kapsamlı deneyler, tümörleri sınıflandırmak ve rekürrens ve metastaz gibi olayları tahmin etmek için destek vektör makineleri (SVM’ler) ve k-en yakın komşuluk (k-nn) sınıflandırıcılarına kıyasla umut verici sonuçlar verdigini ifade etmişlerdir.

Quang ve ark. [51] genetik varyantların patojenitesini açıklamak için derin öğrenme yaklaşımı kullandıkları çalışmalarında lojistik regresyon, destekli vektör makinesi ve derin sinir ağlarından oluşan 3 farklı modeli karşılaştırmışlardır. Sonuçta SVM, LR ve DSA modellerinin sınıflandırma doğrulukları sırasıyla % 58, 2 , % 59, 8 ve % 66, 1’dır. Buna rağmen DSA ‘nın doğruluğunun lineer olarak yetersiz olduğuunu iddia etmişlerdir. İddialarına dayanak olarak da eğitim verilerinin yanlış etiketlenmiş numuneler ile
```