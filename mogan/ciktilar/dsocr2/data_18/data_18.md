analysis values have been reviewed and compared with the global solar radiation calculated as the  
theoretica. Results show that ANN estimation based on meteorological data can be used with 99%  
accuracy in sunny and clear weather conditions and 96% in rainy and cloudy weather conditions in  
determining the amount of solar radiation. The presented approach can be used to determine the  
generation potential of existing and planned PV plants.  
Keywords: Solar Radiation, Artificial Neural Network (ANN), Meteorological Measurement, Daily Solar Radiation  

1. Giriş  
Solar radyosayon, güneşin birim alanı başına  
yaydığı ve elektromanyetik radyosayon şeklinde  
iletilen güç olarak tanımlanır[1]. Enerji sektörü  
açısından bakıldığında ise solar radyosayon  
miktarı; meteorolojik araştırmalar, binalarda  
kullanılan doğal aydınlatma sistemleri ve  
güneşten elektrik üretiminde kullanılan  
fotovoltaik sistemler gibi güneş enerjisine  
bağımlı olan projelerin boyutlandırılması ve  
performanslarının belirlenmesinde dikkate  
alınması gereken önemli bir değişkendir.  

Uydular ile gerçekleştirilen ölçümlerden  
dünya dışından gelen solar radyosayon  
miktarının mutlak değerinin 1361 W/m2 olduğu  
ve solar radyosayon değerinin klasik  
radymetrelerde gözlemlenen 1365 W/m2  
değerinden önemli ölçüde düşük olması  
gerektiği gözlemlenmiştir [2]. Fakat gezegen  
dışından gelen solar radyosayon atmosfer ile  
etkileşime girdiğinde zayıflar ve sabit olmaktan  
çıkar. Bu zayıflama atmosferdeki koruyucu  
madde ile etkileşime giren fotonların saçılması  
veya soğurulmasından kaynaklanmaktadır.  

Dünyadaki enerji ihtiyacı her geçen gün artış  
göstermektedir [3]. Bu nedenle ülkeler fosil  
yakıtların tükenmesine karşı önlem almak ve  
daha sürdürülebilir bir dünya hedefi ile elektrik  
üretiminde yenilenebilir enerji kaynaklarına  
yöneltmektedir. Yenilenebilir enerji kaynakları  
içerisinde Fotovoltaik (PV) sistemler güneş gibi  
sansız bir enerji kaynağına sahip olması  
nedeniyle önemli bir avantaja sahiptir [4-7].  
Fakat PV hücrelerin üreteceği elektrik miktarını  
maruz kaldıkları solar radyosayon seviyesi  
belirlemektedir.  

Teknolojideki ilerlemelerle rağmen PV  
hücrelerin verimliliği %11-28 civarındadır [8].  
Bu düşük verim dikkate alındığında, PV  
hücrelerden maksimum verim elde edilebilmek  
için yüksek solar radyosayon seviyesine sahip  
uygun lokasyonda çalıştırılması gereklidir.  

Solar radyosayon miktarı pirametre,  
pyroliometre ve solar metre gibi ölçüm cihazları  
yardımı ile ölçülebilmektedir. Bu cihazların  
maliyetlerinin yüksek olması nedeni ile dünya  
üzerindeki tüm noktalarda sol radyosayonun  
deneysel olarak ölçülmesi olanaklıdır. Bu  
zorluğun üstesinden gelebilmek için  
meteorolojik değişkenler ve sol radyosayon  
arasındaki ilişkiyi matematiksel olarak  
tanımlayan modeller ile verimliliğini ölçmek  
şartındadır. Bunun yanından gelen PV sistemlerin  
ekonomik anlaşılmasını geliştirmek için çeşitli  
olarak araştırılmıştır. Bu çalışma planlanan PV tesislerin  
ekonomik anlaşılmasını geliştirmek için çeşitli  
olarak araştırılması planlanan PV tesislerin  
ekonomik anlaşılmasını geliştirmek için çeşitli  

olarak araştırılması planlanan PV tesislerin  
ekonomik anlaşılmasını geliştirir. Bu çalışma  
planlanan PV tesislerin ekonomik anlaşılmasını  
geliştirmek için çeşitli çözümler kullanılmıştır. Bu  
çözümlerde kullanılan miktarın ve sıcaklığın  
uygunluğu ve/veya enfeksiyonunun belirlenmesi  
ile ekonomik anlaşılmasını sağlamada. Bu  
çözümlerdeki miktarın ve sıcaklığın en yüksek  
olduğu ve/veya enfeksiyonunun belirlenmesi  
ile ekonomik anlaşılmasını sağladığı sınırların  
ilk öncesinde kullanılmıştır [9-20]. Bu  
çözümlerde kullanılan miktarın ve sıcaklığın  
uygunluğu ve/veya enfeksiyonunun belirlenmesi  
ile ekonomik anlaşılmasını sağlamada. Bu  
çözümlerdeki miktarın ve sıcaklığın en yüksek  
olduğu ve/veya enfeksiyonunun belirlenmesi  
ile ekonomik anlaşılmasını sağladığı sınırların  
ilk öncesinde kullanılmıştır [9-20]. Bu  
çözümlerde kullanılan miktarın ve sıcaklığın  
uygunluğu ve/veya enfeksiyonunun belirlenmesi  
ile ekonomik anlaşılmasını sağlamada. Bu  
çözümlerdeki miktarın ve sıcaklığın en yüksek  
olduğu ve/veya enfeksiyonunun belirlenmesi  
ile ekonomik anlaşılmasını sağladığı sınırların  
ilk öncesinde kullanılmıştır [9-20]. Bu  
çözümlerde kullanılan miktarın ve sıcaklığın  
uygunluğu ve/veya enfeksiyonunun belirlenmesi  
ile ekonomik anlaşılmasını sağlamada. Bu  
çözümlerdeki miktarın ve sıcaklığın en yüksek  
olduğu ve/veya enfeksiyonunun belirlenmesi  
ile ekonomik anlaşılmasını sağladığı sınırların  
ilk öncesinde kullanılmıştır [9-20]. Bu  
çözümlerde kullanılan miktarın ve sıcaklığın  
uygunluğu ve/veya enfeksiyonunun belirlenmesi  
ile ekonomik anlaşılmasını sağlamada. Bu  
çözümlerdeki miktarın ve sıcaklığın en yüksek  
olduğu ve/veya enfeksiyonunun belirlenmesi  
ile ekonomik anlaşılmasını sağladığı sınırların  
ilk öncesinde kullanılmıştır [9-20]. Bu  
çözümlerde kullanılan miktarın ve sıcaklığın  
uygunluğu ve/veya enfeksiyonunun belirlenmesi  
ile ekonomik anlaşılmasını sağlamada. Bu  
çözümlerdeki miktarın ve sıcaklığın en yüksek  
olduğu ve/veya enfeksiyonunun belirlenmesi  
ile ekonomik anla