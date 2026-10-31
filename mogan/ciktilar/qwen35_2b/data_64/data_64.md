```markdown
Ağaç yapısı yapraklar ve karar düğümlerinden oluşur. Kökten başlayarak her karar düğümü girdiye bir bölme sınaması uygular ve sonunda göre dallardan biri alınır. Bir yaprağa ulaşıldığında arama durur. Burada örnek hangi sınıfı ait olduğuna karar verilir.

Kara ağacı kurallardan oluşan bir kural tabana dönüştürülebilir ve kuralların yorumlanmasını kolaylaştırır. Kara ağacı öğrenmesi parametrik değildir, böylece ağaç ihtiyaç duyulduğunda büyür (Alpaydın, 2019). Bu gibi durumlar karar ağaçlarının avantajları arasında yer alır.

### Rastgele Orman

Rastgele ormanlar, birçok karar ağacının bir araya gelerek oluşturduğu bir ensemble (topluluk) yöntemidir. Her bir karar ağacı, farklı bir alt veri kümesi ve özellik kümesiyle eğitilir. Böylece, genellikle daha güçlü, daha kararlı ve daha az aşırı öğrenmeye eğilimli modeller üretilir.

Rastgele orman algoritmasına göre ilk olarak eğitim verisinden örnekler alarak farklı alt kümeler oluşturulur. Her bir alt küme için bir karar ağacı oluşturulur. Bu süreçte her düğüm için rastgele bir özellik alt kümesi kullanılır. Bu durum aşırı uyum riskini azaltır. Sonraki aşamada tahmin edilen her bir hedef için oylar hesaplanır ve en yüksek oyu alan tahmin seçilir.

Rastgele orman algoritması hem regresyon hem de sınıflandırma problemlerinde kullanılabilir. Bu algoritma aşırı uyum problemini önlemedektir. Ayrıca mevcut özellikler arasında en önemli özelliği tanımlamak için de kullanılabilir (Çebi, 2020). Bu özellikler rastgele orman algoritmasının avantajları olarak gösterilir.

### K-En Yakın Komşular (KNN)

Makine öğrenmesinde, sınıflandırma ve regresyon problemlerini çözmek için kullanılan basit ve etkili bir algoritmadır. Temel yaklaşım, bir veri noktasını etkiletemek veya tahmin etmek için, ona en yakın olan k komşusunun etkilerini veya değerlerini kullanmaktır. En yakın noktalar bulunarken euklid, manhattan ve minkowski uzaklık değerlerine bakılır.

KNN algoritması uygulanması kolay bir algoritmaya sahip olması, sınıflandırma ve regresyon için kullanılabilmesi avantajları olarak görülmektedir. Ancak, bağımsız değişkenlerin artmasıyla birlikte yavaşlaması, yüksek hafıza ihtiyacı, örnek sayısının artması paralel olarak tahmin süresinin artması dezavantajları olarak karşımıza çıkmaktadır (Atıcılı 2022).

### Destek Vektör Makinesi

Makine kavramsal olarak şu fikri uygular: giriş vektörleri, çok yüksek boyutlu bir özelliğe doğrusal olmayan bir şekilde eşlenir. Bu özelliğin uzayında doğrusal bir karar yüzeyi oluşturulur. Karar yüzeyinin özellikleri, makinenin yüksek genelleme yeteneği kazanmasını sağlar (Cortes, 1995). Destek vektör makinesi, veri noktaları arasındaki en büyük marjı (mesafe) maksimize etmeye çalışarak noktaları birbirinden en iyi şekilde ayıran, bir karar sınırlar belirler. Veri doğrusal ayrılıbırsa bir hiper düzlem bulur, eğer veri doğrusal ayrılırsa veriyi çok boyutlu özelliğe dönüştürerek doğrusal ayırlırlabilir hale getirir.

### Naive Bayes

Naive Bayes sınıflandırıcı, olasılığa dayalı bir makine öğrenimi sınıflandırma algoritmasıdır ve Bayes teoremini esas alır. Sınıflandırıcı bir eleman için her durumun olasılığını hesaplar ve olasılık değeri en yüksek olana göre sınıflandırılır (Hatipoğlu 2023). Test kümesindeki bir veri eğitim kümesinde gözlemlenemiyorsa tahmin yapmaz. Bayes sınıflandırıcı, her özneliğin birbirinden koşulsal bağımsız olduğu ve öğrenilmek istenen kavramın tüm bu özneliklere koşulsal bağlı olduğu bir Bayes ağısı olarak da düşünülabilir (Anonim, 2023).
```