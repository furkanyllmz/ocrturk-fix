```markdown
# 2.3. Transformör Mimarisı (Architecture of Transformer)

Transformör mimarisinde kullanılan diğer mimarilerden en büyük farklarından biri verileri işledi zaman adımımdaki farklılıktır. Önceki RNN, LSTM ve GRU mimarilerinde sözcük dizileri, yani haber gövdesi, t-I zaman adımımdan gelen gizli durum ile $t$ zamanındaki giri vektörünün işleme sokulması mantığı üzerine tasarlanmaktadır [25]. Transformör mimarisinde ise bütün dizi aynı zaman adımı bir matris olarak modele girdi olarak alınır. Doğal dil üzerinde çalışmalarda önceki mimarilerle kullanılan kodlayıcı-kod çözücü yapıısı ise ortak olarak Transformör mimarisinde de kullanılmaktadır. Yine RNN, LSTM ve GRU mimarilerinde tekrarlayan sinir hücre yapılırların yerini, ilk alt katmandan oluşan $N$ adet Transformör kodlayıcı ve kod çözücü blokları almaktadır. Transformör mimarisini günümüzde, doğal dil ile alakalı problemlerin çözümünde RNN, LSTM ve GRU gibi mimarilere göre daha çok tercih edilir durum gelmiştir. Bunun nedeni, çalışmalarda Transformör mimarisini kullanarak diğer mimarilere göre daha başarılı sonuçlar elde edilmesi ve mimari olarak hala geliştirmeye devam edilmektedir. Transformör mimarisini bahsedilen önceki mimarilerden yapı olarak bir çok farklılığı daha bulunmaktadır. Günümüzde mimari olarak farklı geliştirilmişler yapılmış, fakat Transformör mimarilerini de mevcuttur. Fakat çalışmada orijinal makalede de kullanılan ve gerçek yetenekleri sunabilen Şekil 5'teki temel Transformör mimarisini tercih edilmiştir.

Transformörlerde farklı gösteren yapılandıran operasyonel olarak ilk sırada yer alan konumsal kodlama metodudur [26]. Deterministik bilgisayar sistemleri doğal dili insan gibi metinsel veya fonetik olarak algılayamamaktadır. Bu sebeple mevcut verimizi bilgisayaran anlayabileceği sayısal değerler şeklinde ifade etmemiz gerekmektedir. Bu ihtiyacın kaynaklı modelin eğitimi aşamasında, derlemin içinde oluşturulan sözlüğün sözcük gösterimi oluşturulmalıdır. Sözlüğü oluşturulan sözcüklerin her biri, gösterimden belirlenen boyutta, sayıda, kendisinin en yakınlık konumlanan diğer sözcüklerle skaler değerler şeklinde ifade edilen temsil vektörleri oluşturulmaktadır. Bu temsil vektörleri, bilgisayar sistemlerinin doğal dili anlayacak şekilde sayısal olarak temsil edilebilir. Burada kadar olan kısmı diğer mimarilerde de ortak olarak bulunmaktadır. Transformör mimarisini ise konumsal metot ile her sözcüğün cümledeki konum bilgisini ve sözcük temsillerinin konumlarını kullanarak, Eş. 1 ve Eş. 2'deki formül sayesinde konumsal değer matrisi oluşturur. Daha sonra mevcut giri dizi matrisi ile konumsal değer matrisi toplanır. Bu sayede bağlama bağlı olarak gramer yapısını çözümüyle sağlanmıştır. Aynı zamanda eş sesli sözcüklerin cümledeki konumuna göre hangi anlamı ifade ettiğini bilgisayar tarafından anlaşılabilir olmaktadır. Ayrıca Şekil 6'da, örnek olarak 32 sözcükten oluşan ve sözcük temsil boyutu 64 olan bir giri dizi matrisi için cümledeki konumsal değer matrisi gösterilmiştir.

$$
\begin{aligned}
PE(pos,2i) &= \sin(pos/10000^{2i/d_{model}}) \\
PE(pos,2i+1) &= \cos(pos/10000^{2i/d_{model}})
\end{aligned}
$$

Transformör mimarisinin, önceki mimarilerden farklılaşmasının operasyonel olarak bir sonraki faktörü ise çok başlı öz dikkat mekanizmasıdır. Bu mekanizma kısmen LSTM ve GRU gibi mimarilerde ek katman olarak modele eklenen dikkat mekanizmasını bir türevidir. Fakat Transformör mimarisini, kodlayıcı ve kod çözücü bloklarının alt katmanlarında çok başlı öz dikkat mekanizması kavramı ile daha kapsamlı hesaplama yeteneği elde olmaktadır. Bu adımı cümle içindeki her sözcüklerle olan dikkat matrisi Şekil 7'deki gibi Eş. 3'teki hesaplama yapılarak ağır şekilde güncellenir. Bu hesaplarda sorgu (Q), anahtar (K) ve değer (V) matrisleri parametre olarak kullanılır. İlk başta bu üç parametre Q, K ve V aynı dizi matrislerken eğitim aşamasında farklılaşarak

Tablo 4. Ön işlenmiş haber ve başlık örneği-1

| | |
| :--- | :--- |
| **Orijinal metin** | **Ön işlenmiş metin** |
| Özel yetkilili Ankara 12. Ağır Ceza Mahkemesi, 28 Şubat soruşturmasını yürüten savcılarının itirazı üzerine, nöbetçi hâkimlikçe serbest bırakılan emekli Orgeneral Teoman Koman ile emekli Korgeneraller Engin Alan ve Kamuran Orhon hakkında "yakalama kararı" çıkardı. Mahkeme kararın gerekçesini "zanlılara atlı suç niteliği" olarak belirti. MHP'den milletvekili seçilen Alan, Balyoz davasından tutuklu bulunuyor. | özel yetkilili Ankara ağır ceza mahkemesi şubat soruşturmasını yürüten savcılarının itirazı üzerine nöbetçi hâkimlikçe serbest bırakılan emekli Orgeneral Teoman koman emekli korgeneraller engin alan Kamuran Orhon hakkında yakalama kararı çıkarttı mahkeme kararın gerekçesini zanlılara atlı suç niteliği belirti MHP den milletvekili seçilen Alan, Balyoz davasından tutuklu bulunuyor |
| Başlık | 28 Şubat komutanlarına yakalama kararı çıktı |
| | ### şubat komutanlarına yakalama kararı çıktı |

Tablo 5. Ön işlenmiş haber ve başlık örneği-2 (Pre-processed news and headline sample-2)

| | |
| :--- | :--- |
| **Orijinal metin** | **Ön işlenmiş metin** |
| Türk Hava Yolları'nın 2016'nın ilk iki ayındaki yolcu sayısı geçen yılın aynı dönemine göre yüzde 11,2 artışla 9,2 milyona ulaştı. Bu rakam 2015'te 8,3 milyon olmuştu. Yolcu sayısıdaki artış iç hatlarda yüzde 12,6, dış hatlarda yüzde 10,2 oranında gerçekleşti. Diş Hatlar Business/Comfort Class yolcu sayısı ve Dıştan Dışa Transfer Yolcu sayılarında da Ocak-Şubat 2015 dönemine kiyasla sırasıyla yüzde 5,8 ve 20,9 artış sağlandı. Doluluk oranı 3 puanlık düşüş ile yüzde 73,3 oldu. | Türk hava yollar ilk ayındaki yolcu sayısı geçen yıl aynı dönemine yüzde artışla milyon ulaştı. Yolcu sayısıdaki artış iç hatlarda yüzde artışla dış hatlarda yüzde oranında gerçekleşti. Diş Hatlar Business/Comfort Class yolcu sayısı ve Dıştan Dışa Transfer Yolcu sayılarında da Ocak-Şubat 2015 dönemine kiyasla sırasıyla yüzde artış sağlandı doluluk oranı puanlık düşüş yüzde oldu. |
| Başlık | THY yolcu sayısı 9,2 milyona çıktı |
| | THY yolcu sayısı ### milyona çıktı |

```