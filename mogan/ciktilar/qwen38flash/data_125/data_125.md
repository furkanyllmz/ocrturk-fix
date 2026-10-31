```markdown
Bütün bu aşamalardan sonra, üç karakterden kısa sözcükler de metinlerden atılmış ve sonrasında tüm sözcükler küçük harfli olacak hale dönüştürülerek derlem eğitim için son halini almıştır. Orijinal haber gövdesi ve başlığı ile ön işlenmiş haber gövdesi ve başlığı için birer örnek sırasıyla Tablo 4 ve Tablo 5'te verilmiştir.

## 2.3. Transformatör Mimarisi (Architecture of Transformer)

Transformatör mimarisinin DDİ çalışmalarında kullanılan diğer mimarilerden en büyük farklılıkların biri verileri işlediği zaman adımındaki farklılıktır. Önceki RNN, LSTM ve GRU mimarilerinde sözcük dizileri, yani haber gövdesi, $t-1$ zaman adımından gelen gizli durum ile $t$ zamanındaki girdi vektörünün işleme sokulması mantığı üzerine tasarlanmaktadır [25]. Transformatör mimarisinde ise bütün dizi aynı zaman adımında bir matris olarak modele girdi olarak alınır. Doğal dil üzerindeki çalışmalarda önceki mimariler ile kullanılan kodlayıcı-kod çözücü yapısı ise ortak olarak Transformatör mimarisinde de kullanılmaktadır. Yine RNN, LSTM ve GRU mimarilerindeki tekrarlayan sinir hücre yapılarının yerini, iki alt katmandan oluşan $N$ adet Transformatör kodlayıcı ve kod çözücü blokları almaktadır. Transformatör mimarisi günümüzde, doğal dil ile alakalı problemlerin çözümünde RNN, LSTM ve GRU gibi mimarilere göre daha çok tercih edilir duruma gelmiştir. Bunun nedeni, çalışmalarda Transformatör mimarisini kullanarak diğer mimarilere göre daha başarılı sonuçlar elde edilmesi ve mimari olarak hala geliştirilmeye devam edilmesidir. Transformatör mimarisinin bahsedilen önceki mimarilerden yapı olarak birçok farklılığı daha bulunmaktadır. Günümüzde mimari olarak farklı geliştirilmeler yapılmış, farklı Transformatör mimarileri de mevcuttur. Fakat bu çalışmada orijinal makalede kullanılan ve gerekli yetenekleri sunabilen Şekil 5'teki temel Transformatör mimarisi tercih edilmiştir.

Transformatörlerde farklılık gösteren yapılardan operasyonel olarak ilk sırada yer alan konumsal kodlama metodudur [26]. Deterministik bilgisayar sistemleri doğal dili insanlar gibi metinsel veya fonetik olarak algılayamamaktadır. Bu sebeple mevcut verimizi bilgisayarın anlayabileceği sayısal değerler şeklinde ifade etmemiz gerekmektedir. Bu ihtiyaçtan kaynaklı modelin eğitimi aşamasında, derlem içeriğinden oluşturulan sözlüğün sözcük gösterimi oluşturulmalıdır. Sözlüğü oluşturan sözcüklerin her biri, gösterimden belirlenen boyutta, sayıda, kendisinin en yakınına konumlanan diğer sözcüklerle skaler değerler şeklinde ifade edilen temsili vektörleri oluşturmaktadır. Bu temsil vektörleri, bilgisayar sistemlerinin doğal dili anlayacak şekilde sayısallaştırılmasında en önemli adımlardan biridir. Buraya kadar olan kısım diğer mimarilerde de ortak olarak bulunmaktadır. Transformatör mimarisi ise konumsal metot ile her sözcüğün cümledeki konum bilgisini ve sözcük temsillerinin konumlarını kullanarak, Eş. 1 ve Eş. 2'deki formül sayesinde konumsal değer matrisini oluşturur. Daha sonra mevcut girdi dizi matrisi ile konumsal değer matrisi toplanır. Bu sayede bağlama bağlı olarak gramer yapısının çözümlenmesi sağlanmış olur. Aynı zamanda eş sesli sözcüklerin cümledeki konumuna göre hangi anlamı ifade ettiği bilgisayar tarafından anlaşılabilir olmaktadır. Ayrıca Şekil 6'da, örnek olarak 32 sözcükten oluşan ve sözcük temsil boyutu 64 olan bir girdi dizi matrisi için cümlenin konumsal değer matrisi gösterilmiştir.

$$
P E_{(p o s, 2 i)}=\sin \left(p o s / 10000^{2 i / d_{\text {model }}}\right)
$$

(1)

$$
P E_{(p o s, 2 i+1)}=\cos \left(p o s / 10000^{2 i / d_{\text {model }}}\right)
$$

(2)

Transformatör mimarisinin, önceki mimarilerden farklılaşmasının operasyonel olarak bir sonraki faktörü ise çok başlı öz dikkat mekanizmasıdır. Bu mekanizma kısmen LSTM ve GRU gibi mimarilerde ek katman olarak modele eklenen dikkat mekanizmasının bir türevidir. Fakat Transformatör mimarisi, kodlayıcı ve kod çözücü bloklarının alt katmanlarında çok başlı öz dikkat mekanizması kavramı ile daha kapsamlı hesaplama yeteneğine sahip olmaktadır. Bu adımda cümle içindeki her sözcüğün diğer sözcüklerle olan dikkat matrisi Şekil 7'deki gibi Eş. 3'teki hesaplamalar yapılarak ağırlıklar güncellenir. Bu hesaplamalarda sorgu (Q), anahtar (K) ve değer (V) matrisleri parametre olarak kullanılır. İlk başta bu üç parametre Q, K ve V aynı dizi matrisleriyken eğitim aşamasında farklılaşarak

Tablo 4. Ön işlenmiş haber ve başlık örneği-1 (Pre-processed news and headline sample-1)
<!-- Table (130, 578, 868, 760) -->
\begin{tabular}{|l|l|}
\hline Orijinal metin & Ön işlenmiş metin \\
\hline Özel yetkili Ankara 12. Ağır Ceza Mahkemesi, 28 Şubat soruşturmasını yürüten savcıların itirazı üzerine, nöbetçi hâkimlikçe serbest bırakılan emekli Orgeneral Teoman Koman ile emekli Korgeneraller & özel yetkili ankara ağır ceza mahkemesi şubat soruşturmasını yürüten savcıların itirazı üzerine nöbetçi hâkimlikçe serbest bırakılan emekli orgeneral teoman koman emekli korgeneraller engin alan \\
Haber Engin Alan ve Kamuran Orhon hakkında "yakalama kararı" çıkarttı. Mahkeme kararın gerekçesini "zanlılara atılı suçun niteliği" olarak belirtti. MHP'den milletvekili seçilen Alan, Balyoz davasından tutuklu bulunuyor. & Kamuran Orhon hakkında yakalama kararı çıkarttı mahkeme kararın gerekçesini zanlılara atılı suçun niteliği belirtti MHP den milletvekili seçilen alan balyoz davasından tutuklu bulunuyor \\
\hline Başlık 28 Şubat komutanlarına yakalama kararı çıktı & \#\#\# şubat komutanlarına yakalama kararı çıktı \\
\hline
\end{tabular}

Tablo 5. Ön işlenmiş haber ve başlık örneği-2 (Pre-processed news and headline sample-2)
<!-- Table (130, 798, 868, 981) -->
\begin{tabular}{|l|l|}
\hline Orijinal metin & Ön işlenmiş metin \\
\hline Türk Hava Yolları'nın 2016'nın ilk iki ayındaki yolcu sayısı geçen yılın aynı dönemine göre yüzde 11.2 artışla 9.2 milyona ulaştı. Bu rakam 2015'te 8.3 milyon olmuştu. Yolcu sayısındaki artış iç hatlarda yüzde 12.6, dış hatlarda yüzde 10.2 oranında gerçekleşti. Dış Hatlar Business/Comfort Class yolcu sayısı ve Dıştan Dışa Transfer Yolcu sayılarında da Ocak-Şubat 2015 dönemine kıyasla sırasıyla yüzde 5.8 ve 20.9 artış sağlandı. Doluluk oranı 3 puanlık düşüş ile yüzde 73.3 oldu. & Türk hava yolları ilk ayındaki yolcu sayısı geçen yılın aynı dönemine yüzde artışla milyona ulaştı rakam milyon olmuştu yolcu sayısındaki artış iç hatlarda yüzde dış hatlarda yüzde oranında gerçekleşti dış hatlar business/comfort class yolcu sayısı dıştan dışa transfer yolcu sayılarında ocak şubat dönemine kıyasla sırasıyla yüzde artış sağlandı doluluk oranı puanlık düşüş yüzde oldu \\
\hline Başlık THY yolcu sayısını 9.2 milyona çıkardı & THY yolcu sayısını \#\#\# milyona çıkardı \\
\hline
\end{tabular}
```