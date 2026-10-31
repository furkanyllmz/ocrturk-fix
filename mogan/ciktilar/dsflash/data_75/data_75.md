*Tablo 1. Derin öğrenme yöntemleri ve kullanım alanları*

<table>
  <thead>
    <tr>
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
      <td>Sınıflandırma, robotik ve bilgisayar görüsü</td>
    </tr>
    <tr>
      <td>Derin ileri beslemeli ağlar</td>
      <td>Regresyon, sınıflandırma, tahmin, robotik ve bilgisayar görüsü</td>
    </tr>
    <tr>
      <td>Evrişimli sinir ağları</td>
      <td>Regresyon, sınıflandırma, robotik ve bilgisayar görüsü</td>
    </tr>
    <tr>
      <td>Yinelemeli sinir ağları</td>
      <td>Regresyon, sınıflandırma, tahmin, robotik ve bilgisayar görüsü</td>
    </tr>
  </tbody>
</table>

Derin öğrenmenin birçok alanda uygulamaları vardır. Görüntü ve ses senkronizasyonu [25], fotoğraf çözünürlüğünü artırma [26], gerçek zamanlı kişi konum analizi [27], fotoğraf açıklama [28], fotoğraftaki insanların bakışlarında değişiklik yapma [29], gerçek zamanlı davranış analizi [30], fotoğraflardan yeni fotoğraf oluşturma [31], galaksi ve yanardağ resimleri oluşturma[32, 33] görüntü alanındaki derin öğrenme çalışmalarına örnek verilebilmektedir. Bununla birlikte farklı diller arasında çeviriye de derin öğrenme kullanılmaktadır [34]. Biyoloji alanında ise balina ve plankton sınıflandırması için de derin öğrenme kullanılmaktadır [35-38]. Yeni görüntüler oluşturma [39], fotoğraf ve videolardan metin okuma [40] gibi alanlarda da derin öğrenme yöntemleri kullanılmaktadır. Bilgisayar oyunları[41], otomom araçlar[42] ve robotik [43,44] de derin öğrenmenin kullanıldığı alanlardır. Nesne tanıma [45], demografik yapının tahmini [46] ve seçim sonuçlarının tahmini [47] alanlarında da derin öğrenme uygulanmaktadır.

2.2.1. **Sağlık Alanında Kullanılan Derin Öğrenme Yöntemlerinin Kullanım Alanları**

Bu bölümde sağlık alanında kullanılan derin öğrenme yöntemlerinin kullanım alanları açıklanarak, bu alanlarda yapılan çalışmalar incelenmiştir.

2.2.1.1. **Biyoinformatik Alanında Kullanılan Derin Öğrenme Yöntemleri**

Derin öğrenme yöntemleri, kanser teşhisi, gen seçimi ve sınıflandırması, gen çeşitliliği, ilaç tasarımı, bileşim protein etkileşimi, RNA ile protein ilişkisi ve DNA metilasyonu gibi biyoinformatik uygulamalarında kullanılmaktadır. Tablo 2’de biyoinformatik uygulamalarında kullanılan derin öğrenme yöntemleri ve hangi alanda kullanıldıkları gösterilmiştir.

*Tablo 2. Biyoinformatik alanında kullanılan derin öğrenme yöntemleri*

<table>
  <thead>
    <tr>
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
      <td>RNA ile protein İlişkisi</td>
      <td>Derin inanç ağları</td>
    </tr>
    <tr>
      <td>DNA metilasyonu</td>
      <td></td>
    </tr>
  </tbody>
</table>

Sağlık alanında 2013 yılında Fakoor ve ark. nın gen çıkarımı verilerini kullanarak farklı kanser türlerini belirlemek, kanser tanısını ve sınıflandırmasını geliştirmek için derin öğrenme yöntemlerinden DOK yöntemini kullandıkları bilinmektedir. Yaptıkları çalışmada danışmansız özellik öğrenimi yöntemini kullanarak özellik çıkarımı için boyut azaltımı temelli bir yaklaşım belirlemişlerdir [48].

İbrahim ve ark. [49] elde ettiği deneysel sonuçlar, yaklaşımın hepatoselüler karsinoma (HCC) klasik özellik seçim yöntemlerini % 9, akciğer kanseri % 6 ve meme kanserinde F1 ölçümünde % 10’dan daha iyi bir performans gösterdiğini söylemişlerdir.

Khademi ve ark. nın göğüs kanserinin genetik teşhisi için yaptıkları çalışmada, mikro dizilimli verilerden özellik çıkarmak ve eksik özellikleri uyarlamak ve gürültüyü gidermek için DİA ile olasılıksal grafiksel modellerden olan Bayes ağlarını birleştirmişlerdir [50]. Tıp uygulamalarında tahmin modelleri oluşturmak için uygun olan meme kanseri prognozu ve tanısı için olasılıksal bir grafik modeli (PGM) önermişlerdir. Kanserin temelde genetik bir hastalık olduğunu, mikro dizi ve klinik verilerin entegrasyonu, bir ön görü modelinin doğruluğunu artırabileceğini ifade etmişlerdir. Bununla birlikte, mikro dizi verileri yüksek boyutlu olduğundan, genomik değişkenler de dâhil olmak üzere, boyut ve küçük örneklem büyüklüğü problemlerinden dolayı yapı ve parametre öğrenmede zayıf sonuçlara neden olabileceğini belirtmişlerdir. Bu problemi, manifold öğrenme ve mikro dizi verisine DİA uygulayarak ele almışlardır. Klinik verilere yapı öğrenme algoritması uygulayarak klinik modelin yapısını otomatik olarak çıkarmışlar ve daha sonra, bu iki modeli softmax düğümlerini kullanarak entegre etmişlerdir. METABRIC ve NKI gibi gerçek dünya veri tabanlarını kullanan kapsamlı deneyler, tümörleri sınıflandırmak ve rekürrens ve metastaz gibi olayları tahmin etmek için destek vektör makineleri (SVM’ler) ve k-en yakın komşuluk (k-nn) sınıflandırıcılarına kıyasla umut verici sonuçlar verdiğini ifade etmişlerdir.

Quang ve ark. [51] genetik varyantların patojenitesini açıklamak için derin öğrenme yaklaşımı kullandıkları çalışmalarında lojistik regresyon, destekli vektör makinesi ve derin sinir ağlarından oluşan 3 farklı modeli karşılaştırmışlardır. Sonuçta SVM, LR ve DSA modellerinin sınıflandırma doğrulukları sırasıyla % 58, 2 , % 59, 8 ve % 66, 1’dir. Buna rağmen DSA ’nın doğruluğunun linear olarak yetersiz olduğunu iddia etmişlerdir. İddialarına dayanak olarak da eğitim verilerinin yanlış etiketlenmiş numuneler ile