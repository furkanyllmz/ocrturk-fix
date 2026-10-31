```markdown
Transfer öğrenmenin üç çeşidi vardır:

1. Kaynak ve hedef görevlerin farklı olduğu endüktif
2. Kaynak ve hedef alanının farklı, görevlerin aynı olduğu transdüktif
3. Hedef öğrenmenin farklı ve verinin etiketli olmadığı yönetimsiz

Çalışmada kaynak ve hedef görevleri farklıdır, ayrıca her iki alanda da etiketli veri bulunmaktadır bu yüzden endüktif transfer öğrenme tekniği uygulanacaktır. Bu çalışmada transfer öğrenmenin tercih edilmesindeki iki ana sebebidir: (i) transfer öğrenmenin çok büyük veri setlerine ihtiyaç duymayması, (ii) sadece son katman ağlarığırlıkları eğitildiği için düşük hesaplama gücü ve eğitim süresinin oluşmasıdır.

Çalışmada transfer öğrenme, aşağıdaki adımlar ile uygulanmaktadır:

1. Kaggle'dan kask veri setini edin.
2. Ön eğitilmiş ağ seç.
3. Son katmanı probleme uygun olarak değildir.
4. Eğitim görüntülerindeki yeni sınıf sayısı belirlt (çalışmada 2).
5. Ağa uygun olarak görüntülerini yeniden boyutlandır, eğitim ayarlarını tamla (learning rate, batch size, epoch, weight decay, momentum, optimizer vs.) ve eğitimi gerçeğe çekleştir.
6. Eğitilen ağ test veri setinde değerlendirdir.

Transfer öğrenme işleminde ön eğitimli modelin seçilmesi ve problem boyutu, benzerliği adımlarına dikkat edilmelidir. Seçim işlemi ön eğitimli modelin hedef problemi ne kadar ilgili olduğuna bağlıdır. Hedef veri seti küçük (1.000 görüntüden daha az) ve kaynak veri seti benzer (inşaat alanı, şapkalar vs.) ise aşırı öğrenme şansını yüksektir. Bu yüzden çalışmada, hedef veri seti (inşaat alanında kasket) kaynak veri setinden (doğal resimler) farklıdır ve 1.000 sayısından fazla tutulmuştur.

### 2.6 Karşılaştırma metrikleri

Modellerin başarılarını değerlendirmek için literatürdeki diğer çalışmalara karşılaştırma yapmak için nesne tespit bağılamında kullanılan makine öğrenmesi metriklerini; TP(True Positive) görüntüden tespitini yapılması istenen nesneyi tespit etme, FP(False Positive) görüntüden tespitini yapılması istenmeyen nesneyi veya arka plan görüntüsünü tespit etme, FN(False Negative) görüntüden tespitini yapılması istenen nesneyi tespit edememektir. Bu 3 değer, test veri setindeki tüm görüntüler için hesaplanarak toplanıktan sonra sistemin başarı değerlerini veren aşağıdaki özellikler uygulanmaktadır.

Doğruluk = $\frac{TP}{TP + FP + FN}$ (6)

Doğruluk değeri, modelin doğru tahmin etti nesnelerin toplam nesne sayısına oranı ile hesaplanmaktadır. Bu değer dengelenmiş veri setlerde tek başına yeterli değildir.

Hassaslık = $\frac{TP}{TP + FP}$ (7)

Denklem (7)'de verilen Hassaslık, doğru tespitlerin gerçekten kaçın doğru olduğunu göstermektedir. Ayrıca yanlış tespit oranını veren FP'nin ağırlığı olduğu değerdir.

Denklem (8)'deki Duyarlılık ise doğru tespit edilmesini gereken nesnelerin ne kadarının doğru tespit edildiğini göstermektedir. Gözden kaçıran tespitler olan FNbu eşitlikte ağırlıklıdır.

$F1 Skor = 2 * \frac{Hassaslık * Duyarlılık}{Hassaslık + Duyarlılık}$ (9)

Son olarak Denklem(9) ile hesaplanan F1 Skor, Hassaslık ve Duyarlılığın harmonik ortalaması ve sadece FP veya FN'in oluşturduğu hatayı değil tüm modelin hata değerini görme açısından değerlidir. Literatürde doğruluk yerine F1 Skorun temel alınması da bu sebepten kaynaklanmaktadır.

### 3 Bulgular ve tartışma

Veri sayısının fazla olduğu eğitim ve derin öğrenme modeli epok değerinin yüksek olması aşırı öğrenmeye neden olabilir [72]. Bu yüzden görüntü sayısı 5.000, epok sayısı her 3 model için de 200 olarak belirlenmiştir. Model eğitimi başladığında, algoritma kayıp (yitim) değeri grafiğin kademi olarak azalması beklenir. Eğer azalma durursa model, öğrenmeyi kesmiş veya öğrenbileceği her şeyi zaten öğrenmiş demektir [73]. Bu durum gerçekleştiginde eğitim, kullanıcılar tarafından durdurulabilir.

Epok sayısının 200 tutulmasının yeterli olduğu erken dururma kriterini kullanmaklanmıştır. Erken dururma kriterinin kullanım amacı, model eğitimi kullanıcı yerine keserek eğitim boyunca oluşan en iyi ağrlığı bulmaya yöneliktir. YOLO V5 için denenen bu yönde 89. epoktan sonra 111 epokun gerekiz olduğu ortaya çıkmıştır. Olunan ağrlığın en iyi olduğu söylemiştir yani bu epokun sonraki eğitim, iyileşme yapmamıştır.

Deneylerin eşit şartlar altında gerçekleşmesi için YOLO V4, V5 ve Faster R-CNN transfer öğrenmeli/öğrenmesi;6 model eğitimi, Intel i7-8750H işlemci, 16 GB RAM özelliklerine sahip kişisel bilgisayarda PyTorch [74] çerçeve yazılımlarını kullanarak gerçekleştirilmiştir. PyTorch sayesinde kişisel bilgisayarı işlemci thread'leri parale çalıştırılabilir.

Şekil 3.4 ve 5'teki grafiklerde sırayla transfer öğrenme tekniğinin uygulanmadığı ve uygulandığı Faster R-CNN, YOLO V4 ve YOLO V5 modellerinin eğitim boyunca hesapladıkları yitim değerinin değişimini görmektedir. Her 3 grafikten anlaşılacağı üzere transfer öğrenmenin uygulanmadığı modellerin yitim değerleri her epok aralığında (10'luk), transfer öğrenmenin uygulandığı modellerin yitim değerlerine göre daha fazladır. Bu durumu bakarak transfer öğrenme tekniğinin, olması gereken (gerçek) ile tahmin edilen arasındaki farkın değeri olan yitimini düşürde daha başarılı olduğu söylenebilir.

```