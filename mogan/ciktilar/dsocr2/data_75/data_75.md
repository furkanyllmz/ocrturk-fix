**Tablo 1. Derin öğrenme yöntemleri ve kullanım alanları**

| **Derin Öğrenme Yöntemleri**    | **Derin Öğrenme Yöntemlerinin Kullanıldığı Alanlar**    |
|---|---|
| **Bölümname makinesi**    | Sınıflandırma ve en iyileme    |
| **Derin inanç ağları**    | Sınıflandırma, robotik ve bilgisayar görüşü    |
| **Derin ileri besleme ağları**    | Regresyon, sınıflandırma, tahmin, robotik ve bilgisayar görüşü    |
| **Evrensellik siniri ağları**    | Regresyon, sınıflandırma, tahmin, robotik ve bilgisayar görüştü    |

Derin öğrenmenin birçok alanda uygulamaları vardır. Görüntü ve ses senkronizasyonu [25], fotoğraf çözünürlüğünü arttırma [26], gerçek zamanlı kişi konum analizi [27], fotoğraf açıklama [28], fotoğrafaki insanların bakışlarında değişiklik yapma [29], gerçek zamanlı davranış analizi [30], fotoğraflardan yeni fotoğraf oluşturma [31], galaksiyaner radyoda resimleri oluşturma [32, 33] görüntü alanındaki derin öğrenme çalışmalarına örnek verilebilmektedir. Bununla birlikte farklı diller arasında çeviride de derin öğrenme kullanılmaktadır [34]. Biyoloji alanında ise balina ve plankton sınıflandırması için de derin öğrenme kullanılmaktadır [35-38]. Yeni görüntüler oluşturma [39], fotoğraf ve videolardan metin okuma [40] gibi alanlarda da derin öğrenme kullanılmaktadır. Bilgisayar oyunları[41], otomobiller [42] ve robotik [43, 44] derin öğrenmenin kullanıldığı alanlardır. Nesne tanıma [45], demografik yapının tahmini [46] ve seçim sonuçlarının tahmini [47] alanlarında da derin öğrenme uygulanmaktadır.

### 2.2.1. Sağlık Alanında Kullanılan Derin Öğrenme Yöntemlerinin Kullanım Alanları

Bu bölümde sağlık alanında kullanılan derin öğrenme yöntemlerinin kullanım alanları açıklanarak, bu alanlarda yapılan çalışmalar incelenmiştir.

#### 2.2.1.1. Biyoinformatik Alanında Kullanılan Derin Öğrenme Yöntemleri

Derin öğrenme yöntemleri, kanser teşhisi, gen seçimi ve sınıflandırması, gen çeşitliliği, ilaç tasarımı, bileşim protein etkileşimi, RNA ile protein ilişkisi ve DNA metilasyonu gibi biyoinformatik uygulamalarında kullanılmaktadır. Tablo 2’de biyoinformatik uygulamalarında kullanılan derin öğrenme yöntemleri ve hangi alanda kullanıldıkları gösterilmiştir.

**Tablo 2. Biyoinformatik alanında kullanılan derin öğrenme yöntemleri**

| **Biyoinformatik Uygulamaları**    | **Uygulanan Derin Öğrenme Metotları**    |
|---|---|
| Kanser teşhisi    | Derin to-modeller    |
| Gen seçimi ve sınıflandırma    | Derin inanç ağları    |
| Gen çeşitliliği    | Derin sinir ağları    |
| İlaç tasarımı    | Derin sinir ağları    |
| Bileşim-protein etkileşimi    | Derin sinir ağları    |
| RNA ile protein ilişkisi    | Derin inanç ağları    |
| DNA metilasyonu    |    |

Sağlık alanında 2013 yılında Fakoor ve ark. nın gen çıkarımı verilerini kullanarak farklı kanser türlerini belirlemek, kanser tanısını ve sınıflandırmasını geliştirmek için derin öğrenme yöntemlerinden DOK yöntemini kullandıkları bilinmektedir. Yaptıkları çalışmada danışmanız özellik öğrenimi yöntemini kullanarak özellik çıkarımı için boyut azaltımı temelli bir yaklaşım belirlemişlerdir [48].

Ibrahim ve ark. [49] elde ettiği deneysel sonuçlar, yaklaşımın hepatoselüler karsinoma (HCC) klasik özellik seçim yöntemlerini % 9, akciğer kanseri % 6 ve meme kanserinde F1 ölçümünde % 10’dan daha iyi bir performans gösterdiğini söylemişlerdir.

Kademi ve ark. nın göğüs kanserinin genetik teşhisi için yaptıkları çalışmada, mikro dizilimli verilerden özellik çıkarmak ve eksik özellikleri uyarlamak ve gürültüyü gidermek için DIA ile olasılıkla grafiksel modellerden olan Bayes ağlarını birleştirmişlerdir [50]. Tıp uygulamalarında tahmin modelleri oluşturmak için uygun olan meme kanseri prognozu ve tanısı için olasılıkla bir grafik modeli (PGM) önermişlerdir. Kanserin temelde genetik bir hastalık olduğunu, mikro dizi ve klinik verilerin entegrasyonu, bir öngörüş modelinin doğruluğunu artırabileceğini ifade etmişlerdir. Bununla birlikte, mikro dizi verileri yüksek boyutlu olduğundan, genomik değişkenler de dâhil olmak üzere, boyut ve küçük örneklem büyüklüğü problemlerinden dolayı yapı ve parametre öğrenmede zayıf sonuçlara neden olabileceğini belirtmişlerdir. Bu problemi, manifold öğrenme ve mikro dizi verisine DIA uygulamaları ile artmıştır. Klinik verilere yapı öğrenme algoritması uygulamaları klinik modelin yapısını otomatik olarak çıkartmışlar ve daha sonra, bu iki modeli softmax düğümlerini kullanarak entegre etmişlerdir. METABRIC ve NKI gibi gerçek dünya veri tabanlarını kullanan kapsamlı deneyler, tümörleri sınıflandırmak ve rekürans ve metastaz gibi olayları tahmin etmek için destek vektör makineleri (SVM’ler) ve k- en yakın komşuluk (k-nın) sınıflandırıcılarına kıyasla umut verici sonuçlar verdiğini ifade etmişlerdir.

Quang ve ark. [51] genetik varyantların patojenitesini açıklamak için derin öğrenme yaklaşımı kullandıkları çalışmalarında lojistik regresyon, destekli vektör makinesi ve derin sinir ağlarından oluşan 3 farklı modeli karşılaştırmışlardır. Sonuçta SVM, LR ve DSA modellerinin sınıflandırma doğrultusunda karşılaşılan 58, 2, 5, 59, 8 ve 66, 1’dir. Buna rağmen DSA’nın doğruluğunun