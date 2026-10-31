```markdown
Bu tipteki sinir ağlarına daha fazla sayıda gizli katman (ikiden fazla) eklenmesiyle doğrusal olmayan karmaşık ilişkilerin de tespit edebilmesi sağlanmıştır ve elde edilen bu sinir ağlarına derin sinir ağları (DSA) adı verilmistir. DSA'lar hem (işaretli veriler varsa) denetimli, hem de kümelenme gibi denetimsiz öğrenme problemleri için kullanılabilir. DSA'lar yaygın olarak sınıflandırma ve regresyon amacıyla kullanılmakta ve başarılı sonuçlar elde edilmesini sağlamaktadır. Ancak öğrenme süreçleri oldukça yavaş olabilmektedir (Ravi vd., 2017).

## 2.2. Derin Oto-Kodlayıcılar

Oto-kodlayıcılar, problem çözümü için gerekli öznelik kümesinin verilen otomatik olarak çıkarılması amacıyla ortaya atılmış sinir ağlarıdır. Bir oto-kodlayıcı, girdi vektörüne bir sınıf etiketi vermek yerine onu yeniden oluşturmak için eğrilemektedir (Ravi vd., 2017).

Derin öğrenmenin konusu olan derin oto-kodlayıcılar ise, çok boyutlu veriyi temsil etmek için birden fazla oto-kodlayıcının biri üstüne kümelenmesiyle oluşan mimarilerdir (Hinton ve Salakhutdinov, 2006). Literatürde, derin oto-kodlayıcıların birçok farklı türü önerilmiştir.

Derin oto-kodlayıcıların amacı, öznelik kümesini otomatik çıkarmak veya veri boyutu sayısını azaltmaktır (Hinton ve Salakhutdinov, 2006). Bu yöntemde öğrenme için işaretli veri kümesine ihtiyaç yoktur, yani denetimsiz bir öğrenme yöntemiidir. Ancak yöntem uygun ağırlıklar bulabilmek için bir ön-öğrenme aşamasına ihtiyaç duymaktadır. Bu ön-öğrenme aşamasında son konfigürasyona uygun yaklaşıklık ağlıklar yöntemi sağlanmaktadır (Ravi vd., 2017).

## 2.3. Derin İnanç Ağları

Derin inanç ağları (Hinton vd., 2006) ve bir sonraki bölümde tanıtlacak olan derin Boltzmann makineleri, sınırlandırmış Boltzmann makinesi adı verilen bir algoritmaya (Hinton ve Sejnowski, 1986) dayanmaktadır. SBM algoritması stokastik bir sinir aği olarak tanımlanmakta ve bu ağlarda Gaussian gibi belirli bir dağılıma sahip stokastik birimler kullanılmaktadır. Öğrenme sürecinde ise Gibbs örneklemesi gibi ağırlıklarını adım adım ayarlayan yöntemler kullanılmaktadır.

Derin inanç ağları birden fazla SBM'nin bileşkesi olarak algılanabilir (Hinton vd., 2006). Her bir SBM'nin gizli katmanı, bir sonraki SBM'nin görünür katmanına bağlıdır ve en üst seviyede yansıız bağlantılar vardır. Derin inanç ağları hem denetimli hem de denetimsiz öğrenme amacıyla kullanılabilir. Bu ağı başlatmak için katman-katman bir ağgözü algoritma ile öğrenme gerçekleştirilmektedir (Ravi vd., 2017).

## 2.4. Derin Boltzmann Makinesi

Boltzmann makinelerine dayalı bir diğer derin öğrenme yöntemi de derin Boltzmann makineleridir (Salakhutdinov ve Larochelle, 2010). Derin inanç ağlarından farklı; derin Boltzmann makinelerinde ağın tüm katmanları arasında yansıız bağlantılarının olmasıdır. Bir diğer fark ise derin Boltzmann makinelerinde zaman karmaşıklığının daha fazla olması bu nedenle de büyük veri kümelerinde öğrenme sürecinin yavaş olmasıdır (Ravi vd., 2017).

## 2.5. Yineleyen Sinir Ağları

Yineleyen sinir ağları (Williams ve Zipser, 1989), veri akışlarını (stream of data) analiz edebilen gizli katmanlara sahip sinir ağlarıdır ve çıktıının bir önceki hesaplamalara bağlı olduğu problemlerin çözümü için çok uygundur (Ravi vd., 2017). Yineleyen sinir ağları bu nedenle özellikle doğal dil işleminin değişik problemlerinin çözümünde oldukça başarılı olmuştur (Ravi vd., 2017). Yineleyen sinir ağlarında öğrenme sırasında ortaya çıkan bazı problemler nedenleri, bu ağların uzun kısa-dönem bellek (Long Short-Term Memory - LSTM) (Hochreiter ve Schmidhuber, 1997) gibi farklı sürümleri literaturee girmiştir.
```