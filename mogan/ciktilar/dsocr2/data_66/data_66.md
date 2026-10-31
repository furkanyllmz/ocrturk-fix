Transfer öğrenmenin üç çeşidi vardır:  
1. Kaynak ve hedef görevlerinin farklı olduğu endüktif  
2. Kaynak ve hedef alanının farklı, görevlerin aynı olduğu transdüktif  
3. Hedef öğrenmenin farklı ve verinin etkilediği gözetimsiz  

**Çalışmada kaynak ve hedef görevleri farklıdır, ayrıca her iki alanda da etkili veri bulunmaktadır. Bu yüzden endüktif transfer öğrenme tekniği uygulanacaktır.**  
Bu çalışmada transfer öğrenmenin etkili değişkeni aşağıda verilen 4 öğrenme çok büyük veri setlerine ihtiyaç duymaması, (i) sadece son katman ağırlıkları eğitildiği için düşük hesaplama gücü ve eğitim süresinin oluşmasıdır.  

**Çalışmada transfer öğrenme, aşağıdaki adımlar ile uygulanmaktadır:**  
1. Kaggle’dan kısa veri setini edin.  
2. Ön eğitimi aşağı seç.  
3. Son katmanı problemle uygun olarak değiştirin.  
4. Eğitim görüntülerindeki yeni sınıf sayısını belirtin. (çalışmada 2).  
5. Ağa uygun olarak görüntüleri yeniden boyutlandır, eğitim ayarlarını tamamla (learning rate, batch size, epoch, weight decay, momentum, optimizer vs.) ve eğitimi gerçekleştirin.  
6. Eğitilen ağa test veri setinde değerlendirin.  

Transfer öğrenme işleminde ön eğitimi modelin seçilmesi ve problem boyutu, benzerliği adımlarına dikkat edilmelidir. Seçim işlemi ön eğitimi modelin hedef probleminde ne kadar ilgili olduğuna bağlıdır. Hedef veri seti küçük (1.000 görüntüden daha az) ve kaynak veri setine benzer (inşaat alanı, şapkalar vs.) ise aynı öğrenme şansı yüksektir. Bu yüzden çalışmada, hedef veri seti (inşaat alanında kısbet) kaynak veri setinden (doğal resimler) farklıdır ve 1.000 sayısından fazla tutulmuştur.  

---

### 2.6 Karşılaştırma metrikleri  

Modellerin başarılarını değerlendirmek ve literatürdeki diğer çalışmalarla karşılaştırmak için nesne tespiti bağlamında uygulanan makine öğrenmesi metriklerinden;  
**TP (True Positive)** görüntüden tespiti yapılması istenen nesneyi tespit etme,  
**FP (False Positive)** görüntüden tespiti yapılması istenmeyen nesneyi veya arka plan görüntüsünü tespit etme,  
**FN (False Negative)** görüntüden tespiti yapılması istenen nesneyi tespit edememez. Bu 3 değer, test veri setindeki tüm görüntüler için hesaplanarak toplandıktan sonra sistemin başarı değerlerini veren aşağıdaki eşitlikler uygulanmaktadır.  

\[Doğruluk = \frac{TP}{TP + FP + FN}\]  

(6)  

Doğruluk değeri, modelin doğru tahmin ettiği nesnelerin toplam nesne sayısına oranı ile hesaplanmaktır. Bu değer dengesiz veri setlerinde tek başına yeterli değildir.  

\[Hassaslık = \frac{TP}{TP + FP}\]  

(7)  

---

**Denklem (7)’de verilen Hassaslık, doğru tespitlerin gerçekte kaçının doğru olduğunu göstermektedir.** Ayrıca yanlış tespit oranını veren  
\[FP’nin ağırlıklı olduğu değildir.\]  

\[Duyarlılık = \frac{TP}{TP + FN}\]  

(8)  

**Denklem (8)’deki Duyarlılık ise doğru tespit edilmesi gereken nesnelerin ne kadar oranının doğru tespit edildiğini göstermektedir.** Gözden kaçırılan tespitler olan  
\[FN’bu eşitlikte ağırlıklıdır.\]  

\[Hassaslık * Duyarlılık = Hassaslık + Duyarlılık\]  

(9)  

Son olarak Denklem (9)’de hesaplanan F1 Skor, Hassaslık ve Duyarlılığın harmonik ortalamasıdır ve sadece  
\[FP’ye kadar FN’nin oluşturduğu hata\]  
değil tüm modelin hata değerini görmektedir. Literatürde doğruluk yerine F1 Skorun temel alınması da bu sebepten kaynaklanmaktadır.  

---

### 3. Bulgular ve tartışma  

Veri sayısının fazla olduğu eğitim ve veri öğrenme modeli eşitken olması aşırı öğrenmeye neden olabilir [72]. Bu yüzden görüntü sayısı 5.000, eşit sayısı her 3 model için de 200 olarak belirlenmiştir. Model eğitimi başladığında, algoritma kayıp (yitim) değeri grafiğinin kademeli olarak azalması beklenir. Eğer azalma durursa model, öğrenmeyi kesmiş veya öğrenebileceği her şeyi zaten öğrenmiş demektir [73]. Bu durum gerçekleştirdiğinde eğitim, kullanıcı tarafından durdurulabilir.  

Eşitlik sayısının 200 tutulmasının yeterli olduğu erken durdurma kriteri kullanılarak kanıtlanmıştır. Erken durdurma kriterinin kullanım amacı, model eğitimi kullanıcı yerine keserek eğitim boyunca oluşan en iyi ağırlığı bulmaya yöneliktir. YOLO V5 için denen bu yöntemde 89. epoktan sonraki 111 epoğun gereksiz olduğu ortaya çıkmıştır. Oluşan ağırlığın en iyi olduğunu söylemiştir yani bu epoktan sonraki eğitim, iyileşme yapmamıştır.  

Deneylerin eşit şartlar altında gerçekleşmesi için YOLO V4, V5 ve Faster R-CNN transfer öğrenmeli/öğrenmesiz;6 model eğitimi, Intel i7-8750H işlemci, 16 GB RAM özelliklerine sahip kişisel bilgisayarda PyTorch [74] çerçeve yazılım kullanılarak gerçekleştirilmiştir. PyTorch sayesinde kişisel bilgisayarın işlemci thread’leri paralel çalıştırılabilmiştir.  

**Şekil 3.4 ve 5’teki grafiklerde sırasıyla transfer öğrenme tekniğinin uygulanmadığı ve uygulamadığı Faster R-CNN, YOLO V4 ve YOLO V5 modellerinin eğitim boyunca hesapladıkları yitim değerinin değişimini görmekteyiz. Her 3 grafikten anlaşılacağı üzere transfer öğrenmenin