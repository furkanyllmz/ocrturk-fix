```markdown
# Tablo 1. Derin öğrenme yöntemleri ve kullanım alanları

| Derin Öğrenme Yöntemleri | Derin Öğrenme Yöntemlerinin Kullanıldığı Alanlar |
| :--- | :--- |
| Boltzmann makinesi | Sınıflandırma ve en iyileme |
| *Derin inanç ağları* | Sınıflandırma, robotik ve bilgisayar görsü |
| Derin İleri beslemeli ağlar | Regresyon, sınıflandırma, tahmin, robotik ve bilgisayar görsü |
| Evrişimli sinir ağları | Regresyon, sınıflandırma, robotik ve bilgisayar görsü |
| Yinelemeli sinir ağları | Regresyon, sınıflandırma, tahmin, robotik ve bilgisayar görsü |

Derin öğrenmenin birçok alanda uygulamaları vardır. Görüntü ve ses senkronizasyonu [25], fotoğraf çözünürlüğünü arttırma [26], gerçek zamanlı kişi konum analizi [27], fotoğraf açıklama [28], fotoğrafındaki insanların bakışlarında değişiklik yapma [29], gerçek zamanlı davranış analizi [30], fotoğraflardan yeni fotoğraf oluşturma [31], galaksi ve yanarında resimleri oluştururma[32, 33] görüntü alanında derin öğrenme çalışmaları arasında çeviride de derin öğrenme kullanılmaktadır [34]. Biyoloji alanında ise balina ve plankton sınıflandırması için derin öğrenme kullanılmaktadır [35-38]. Yeni görüntüler oluşturma [39], fotoğraf ve videolardan metin okuma [40] gibi alanlarda da derin öğrenme kullanılmaktadır. Bilgisayar oyunları[41], otomobarçalar[42] ve robotik [43,44] de derin öğrenmenin kullanıldığı alanlardır. Nesne tanıma [45], demografik yapının tahmini [46] ve seçim sonuçlarının tahmini [47] alanlarında da derin öğrenme uygulanmaktadır.

## 2.2.1. Sağlık Alanında Kullanılan Derin Öğrenme Yöntemlerinin Kullanım Alanları

Bu bölümde sağlık alanında kullanılan derin öğrenme yöntemlerinin kullanım alanları açıklandırarak, bu alanlarda yapılan çalışmalar incelenmiştir.

### 2.2.1.1. Biyoinformatik Alanında Kullanılan Derin Öğrenme Yöntemleri

Derin öğrenme yöntemleri, kanser teşhisi, gen seçimi ve sınıflandırması, gen çeşitliliği, ilaç tasarımı, bileşim protein etkileşimi, RNA ile protein ilişkisi ve DNA metilasyonu gibi biyoinformatik uygulamalarında kullanılmaktadır. Tablo 2'de biyoinformatik uygulamalarında kullanılan derin öğrenme yöntemleri ve hangi alanda kullanıldıkları gösterilmiştir.

**Tablo 2. Biyoinformatik alanında kullanılan derin öğrenme yöntemleri**

| Biyoinformatik Uygulamaları | Uygulanan Derin Öğrenme Metotları |
| :--- | :--- |
| Kanser teşhisi | Derin oto-kodlayıcılar |
| Gen seçimi ve sınıflandırması | Derin inanç ağları |
| Gen çeşitliliği | Derin sinir ağları |
| İlaç tasarımı | Derin sinir ağları |
| Bileşim-protein etkileşimi | Derin sinir ağları |
| RNA ile protein ilişkisi | Derin inanç ağları |
| DNA metilasyonu | |

Sağlık alanında 2013 yılında Fakoor ve ark. nn gen çıkarımı verilerini kullanarak farklı kanser türlerini belirlemek, kanser tanımlaması ve sınıflandırmasını geliştirmek için derin öğrenme yöntemlerinden DOK yöntemi kullanıldıkları bilinmektedir. Yapıkları çalışmada danışmısız özelik öğrenme yöntemi kullanarak özelik çıkarım için boyut azaltımı temel bir yaklaşım belirlemişlerdir [48].

Ibrahim ve ark. [49] elde ettiği deneysel sonuçlar, yaklaşımlın hepatoselüler karsinoma (HCC) klasik özelik seçim yöntemlerini % 9, akciğer kanseri % 6 ve meme kanserinde F1 ölçümde % 10'dan daha iyi bir performans gösterdiğini söylemişlerdir.

Khademi ve ark. nn göğüs kanserinin genetik teşhisi için yaptıkları çalışmada, mikro dizimli verilerden özelik çıkarmak ve eksik özellikleri uyarlamak ve görüntütyü gidermek için DİA ile olasılıksal grafik modellerden olan Bayes ağlarını birleştirmişlerdir [50]. Tip uygulamalarında tahmin modelleri oluşturmak için uygun olan meme kanseri prognozu ve tanı için olasılıksal bir grafik modeli (PGM) önermişlerdir. Kanserin temelde genetik bir hastalık olduğunu, mikro dizi ve klinik verilerin entegrasyonu, bir öngörü modelinin doğruluğunu artıracabileceğini ifade etmişlerdir. Bununla birlikte, mikro dizi verileri yüksek boyutlu olduğundan, genomik değişkenler de dahil olmak üzere, boyut ve küçük örneklem büyüklüğü problemlerinden dolayı yapı ve parametre öğrenmede zayıf sonuçlara neden olabilecekleri belirtilmiştir. Bu problemi, manifold öğrenme ve mikro dizi verisine DİA uygulayarak ele almışlardır. Klinik verilere yapı öğrenme algoritması uygulayarak klinik modelin yapısı otomatik olarak çıkartmışlar ve daha sonra, bu iki modeli softmax düğümlerini kullanarak entegre etmişlerdir. METABRIC ve NKI gibi gerçek dünya veri tabanları kullanılan kapsamlı deneyler, tümörleri sınıflandırmak ve rekürrens ve metastaz gibi olayları tahmin etmek için destek vektör makineleri (SVM'ler) ve k-en yakın komşuluk (k-nn) sınıflandırıcılarına yaklaşık umut verici sonuçları verdiği ifade etmişlerdir.

Quang ve ark. [51] genetik varyantların patojenitesini açıklamak için derin öğrenme yaklaşımı kullanıkları çalışmalarda lojistik regresyon, destekli vektör makinesi ve derin sinir ağlarından oluşan 3 farklı modeli karşılaştırmışlardır. Sonuçta SVM, LR ve DSA modellerinin sınıflandırma doğruluğu sırasıyla % 58, 2 , % 59, 8 ve % 66, 1'dir. Buna rağmen DSA 'nn doğruluğunun lineer olarak yetersiz olduğunu iddia etmişlerdir. İddialarına dayanak olarak da eğitim verilerinin yanlış etiklenmiş numuneler ile

```