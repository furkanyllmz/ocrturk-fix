```markdown
Hava kiriliği tehlikeli boyutlara ulaşırken hava kiriliği ile mücadele etmek elzem olmaktadır. Bu amaca sürekli ölçümler yapılmaktadır. Kriter olarak ölçülmesi gereken kirleticiler ise, Karbon monoksit (CO), Kükürt dioksit (SO₂), Ozon (O₃), Partikül madde (PM), Azot oksitleri (NOX) olarak belirlenmektedir.

Günümüzde yapay zekada yaşayan gelişmeler sadece bilgisayar bilimcileri değil diğer bilim dallarında çalışan araştırmacılarda ilgisini çekmeye başlamıştır. Hava kiriliği tahmininde yapay zekanın kullanılması literatürde önemli bir yer tutmaya başlamıştır.

Literatürde, O₃ konsantrasyonları modellemesi için makine öğrenmesi ve derin öğrenme tabanlı farklı çalışmalar bulunmaktadır. Makine öğrenmesi doğal olmayan ve yüksek boyutlu veri kümeleri üzerinden kararlı ve performansı yüksek bilgi çıkarmayı yapılmaktadır (Bilgin, 2021; Yıldırım vd., 2021). Makine öğrenmesi yöntemlerinden çok katmanlı algılacı (ÇKA) (Paoli vd., 2011; Chattopdyhay vd., 2019; Yang vd., 2021; Bekesiene vd., 2021; Makarova vd., 2021), destek vektör makineleri (DVM) (Chelani, 2010; Tanaskuli, 2019; Mehdpour ve Memarianfard, 2019), lineer regresyon (Alipio, 2020; Allu vd., 2020; Matasović vd., 2021), Xgboost (Ding vd., 2020; Liu vd., 2020; Ma vd., 2021) yöntemleri ile çalışmaları mevcuttur.

Büyük veri analizi ve Grafik İşleme Biriminin (GPU) kullanılmasından bu yana, derin öğrenme büyük ilgi görmekte ve makine öğrenmesinin uygulanması her alana uygulanmaktadır (Çağil ve Yıldırım, 2020; Darendeli ve Yılmaz, 2021). Derin öğrenme yöntemleri ile yapılan çalışmalarda derin sinir ağları (DSA) (Wang vd., 2020; Felix vd., 2021), oto kodlayıcı (Nghiem vd., 2021), özinelemeli sinir ağları (Adnane vd., 2021), Uzun Kısa Süreli Bellek (LSTM) (Alghieh vd., 2021; Ekinci vd. 2021; Zhang vd., 2021), konvolüsyonel sinir ağları (CNN) (Eslami vd., 2020; Sayeed vd., 2021) kullanılmaktadır.

Bu çalışmanın amacı saatlik O₃ konsantrasyonları modellemesinde makine öğrenmesi ve derin öğrenme yaklaşımlarının etkinliğini değerlendirmektedir. Bu amaçla kiriliği sebep olan parametrelerden (PM10, SO₂, NO, NO₂ ve O₃) oluşan zaman serisi veri kümeleri kullanarak Xgboost, YSA ve Uzun Kısa Süreli Bellek (LSTM) yöntemleri karşılaştırılmıştır. Yapılan deneylerde ozon seviyesini tahmin etmede LSTM yönteminin diğer iki makine öğrenmesi yönteminin kıyasla daha başarılı olduğu gözlemlenmiştir.

Makalen geri kalan kısmı ikinci bölümde veri kümesi ve uygulanan yöntemlerin anlatıldığı materyal ve yöntem kısmıdır. Üçüncü bölümde veri önleme, kullanılan hata metrikleri, modellerin tasarımı ve elde edilen deney sonuçları ayrıntılı şekilde verilmiştir. Son bölümde ise sonuçlar ve öneriler yer almaktadır.

## 2. Materyal ve Yöntemler (Materials and Methods)

### 2.1. Veri kümesi (Dataset)

Marmara bölgesinde özellikle Kocaeli ve Sakarya illerinin sanayilerinin gelişmesi ile birlikte bu illerde hava kiriliği oldukça yüksektir. Bu çalışmada, Kocaeli ve Sakarya ile birlikte sanayinin yoğun olmadığı Çanakkale illeri için T.C. Çevre ve Şehircilik Bakanlığı Hava Kalitesi İzleme Ağından¹ sürekli ölçümler yapılarak elde edilen verilerden oluşan bir veri kümesi oluşturulmuştur.

İstasyonda ölçülen meteorolojik parametreler 10 µm'nin altındaki parçacıkları ifade eden PM10, azot oksitlerden NO, NO₂, NOX, SO₂ ve O₃ şeklinde sınıflandırılır. Bu parametreler içerisinde O₃ konsantrasyonunu tahmin etmek için PM10, SO₂, NO, NO₂ ve O₃ parametrelerine dayalı bir tahmin yapılması hedeflenmiştir. Kocaeli, Sakarya ve Çanakkale illeri için 2018 Kasım ile 2021 Kasım arası saatlik ölçülen zaman serisi değerleri kullanılmıştır. 4 saatlik bir pencere boyutu ile (yani 4 zaman noktası) 5. saat için O₃ konsantrasyonlarının tahmini gerçekleştirilmiştir.

### 2.2. Yöntemler (Methods)

#### 2.2.1. Xgboost (Xgboost)

Xgboost (Chen vd., 2016) karar ağacı temelli topluluk öğrenme algoritmasıdır. Algoritmanın çalışma mantığı, değişkenlere farklı ağlar kullanarak elde edilen ağ topluluklar çıkarmakla yapmaktadır. İlk etapta tüm değişkenler eşit ağlara sahiptir. Ağaç topluluğu büyümeye başladığında, problem bilgisine bağlı olarak ağlar zor durumlarda kendini düzenleyebilme yeteneği kazanmaktadır. Fazla uyumu azaltan ve genel performansı artıran çeşitli düzenlemeler içermektedir (Ekinci vd., 2020). Bu özelliğinden dolayı “düzenli arttırma” tekniği olarak da ismindirilmektedir. Xgboost algoritması çeşitli düzenlemeler ile doğruluğa artıran, paralel işlemle hızlı sonuçlar verebilen, eksik değerlerin kullanımı için standart bir yapıya sahip olan, yükseltme işleminin yeneleme aşamalarının her birinde çarpaz doğrulama yapan bir algoritmadır.

#### 2.2.2. Yapay Sinir Ağları (Artificial Neural Networks)

Beyin insan vücudunun yapı taşları olup girdileri sinyal şeklinde alan, işleyen ve çıkış sinyallerini gönderen biyolojik sinir ağdır. Beyin temel birimi nörondur. Beyin 200 milyar nörondan oluşmaktadır. Nöronlar dendrit, soma, akson ve sinapsis olmak üzere dört temel kısımdan oluşmaktadır. Nöron, dendritlerden sinyal

¹ http://sim.csab.gov.tr/Services/AirQuality/

```