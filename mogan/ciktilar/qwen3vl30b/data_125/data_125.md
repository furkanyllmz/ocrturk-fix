```html
<p>Bütün bu aşamalardan sonra, üç karakterden kısa sözcükler de metinlerden atılmış ve sonrasında tüm sözcükler küçük harfli olarak hale dönüştürülmerek derlem eğitim için son halini almıştır. Orjinal haber gövdesi ve başlığı ile ön işlemeiş haber gövdesi ve başlığı için birer örnek sırasıyla Table 4 ve Table 5'te verilmiştir.</p>
<h3>2.3. Transformator Mimarisi (Architecture of Transformer)</h3>
<p>Transformator mimarisinin DDI çalışmasında kullanılan diğer mimarilerden en büyük farklarından biri verileri işlediği zaman adımındaki farklılıktır. Önceki RNN, LSTM ve GRU mimarilerinde sözcük dizileri, yani haber gövdesi, t-1 zaman adımından gelen gizli durum ile t zamanındaki girdi vektörünün işleme sokulması mantığı üzerine tasarlanmaktadır [25]. Transformator mimarisinde ise bütün dizi aynı zaman adımında bir matris olarak modele girdi olarak alınır. Doğal dil üzerindeki çalışmalarda önceki mimariler ile kullanılan kodlayıcı-kod çözücü yapısı ise ortak olarak Transformator mimarisinde de kullanılmaktadır. Yine RNN, LSTM ve GRU mimarilerinde tekrarlanan sinir hücre yapılarının yerini, iki alt katmandan oluşan N adet Transformator kodlayıcı ve kod çözücü blokları almaktadır. Transformator mimarisi günümüzde, doğalgilile alakalı problemlerin çözümünde RNN, LSTM ve GRU gibi mimarilere göre daha çok tercih edilir duruma gelmiştir. Bunun nedeni, çalışmalarda Transformator mimarisi kullanılarak diğer mimarilere göre daha başarılı sonuçlar elde edilmesi ve mimari olarak hala geliştirilmeye devam edilmesidir. Transformator mimarisinin bahsedilen önceki mimarilerden yapı olarak birçok farklılık daha bulunmaktadır. Günümüzde mimari olarak farklı geliştirilmeler yapılmış, farklı Transformator mimarileri de mevcuttur. Fakat bu çalışmada orijinal makalede de kullanılan ve gerekli yetenekleri sunabilen Şekil 5'teki temel Transformator mimarisi tercih edilmiştir.</p>
<p>Transformatörlerde farklılık gösteren yapılardan operasyonel olarak ilk sırada yer alan konumsal kodlama metodudur [26]. Deterministik bilgisayar sistemleri doğal dili insanlar gibi metinsel veya fonetik olarak algılayamamaktadır. Bu sebeple mevcut verimizi bilgisayarn anlayabileceği sayısal değerler şeklinde ifade etmemiz gerekmektedir. Bu ihtiyaçtan kaynaklı modelin eğitim aşamasında, derlemin içeriğinden oluşturulan sözlüğün sözcük gösterimi oluşturulmalıdır. Sözlüğü oluşturan sözcüklerin her biri, gösterilen belirlenen boyutta, sayıda, kendsinin en yakınına konumlanan diğer sözcüklerle skaler değerler şeklinde ifade edilen tensil vektörleri oluştururlarmaktadır. Bu tensil vektörler, bilgisayar sistemlerinin doğal dili anlayacak şekilde sayısallaştırılması en önemli adımlardan biridir. Buraya kadar olan kısım diğer mimarilerde de ortak olarak bulunmaktadır. Transformator mimarisi ise konumsal metot ile her sözcüğün cümledeki konum bilgisini ve sözcük temsillerinin konumlarını kullanılarak, Es. 1 ve Es. 2'deki formül sayesinde konumsal değer matrisini oluşturur. Daha sonra mevcut girdi dizi matrisi ile konumsal değer matrisi toplanır. Bu sayede bağlama bağlı olarak gramer yapısının çözümlenmesi sağlanmış olur. Aynı zamanda eş sesli sözcüklerin cümledeki konumuna göre hangi anlama ifade ettiği bilgisayar tarafından anlaşabilir olmaktadır. Ayrıca Şekil 6'da, örnek olarak 32 sözcükten oluşan ve sözcük tensil boyutu 64 olan bir girdi dizi matrisi için cümlelenmiş konumsal değer matrisi gösterilmiştir.</p>
$$
PE_{(pos,2i)} = \sin(pos/10000^{2i/d_{model}}) \quad (1)
$$
$$
PE_{(pos,2i+1)} = \cos(pos/10000^{2i/d_{model}}) \quad (2)
$$
<p>Transformator mimarisinin, önceki mimarilerden farklılaşmasının operasyonel olarak bir sonraki faktörü ise çok başlı öz dikkat mekanizmasıdır. Bu mekanizma kısmen LSTM ve GRU gibi mimarilerde ek katman olarak modele eklenen dikkat mekanizmasının bir türevidir. Fakat Transformator mimarisi, kodlayıcı ve kod çözücü bloklarının alt katmanlarında çok başlı öz dikkat mekanizması kavramı ile daha kapsamlı hesaplama yeteneğine sahip olmaktadır. Bu adımda cümle içindeki her sözcüğün diğer sözcüklerle olan dikkat matrisi Şekil 7'deki gibi Es. 3'teki hesaplamalar yapılarak ağrılıklar güncellenir. Bu hesaplamalarda sorgu (Q), anahtar (K) ve değer (V) matrisleri parametre olarak kullanılır. İlk başta bu üç parametre Q, K ve V aynı dizi matrisleriyken eğitim aşamasında farklılaşarak</p>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th colspan="2">Table 4. Ön işlemeş haber ve başlık örneği-1 (Pre-processed news and headline sample-1)</th>
    </tr>
    <tr>
      <th>Orjinal metin</th>
      <th>Ön işlemeş metin</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Özel yetkili Ankara 12. Ağır Ceza Mahkemesi, 28 Şubat soruşturmasının yürüten savcılarn itirazı üzerine, nöbetçi hâkimlikçe serbest bırakılan emekli Orgeneral Teoman Koman ile emekli Korgeneral Engin Alan ve Kamuran Orhon hakkında "yakalama kararı" çıkarttı. Mahkeme kararın gereksinisi "zanlılara atlı suçun niteliği" olarak belirtti. MHP'den milletvekili seçilen Alan, Balyoz davasından tutuklu bulunuyor.</td>
      <td>özel yetkili Ankara ağır ceza mahkemesi şubat soruşturmasının yürüten savcılarn itirazı üzerine nöbetçi hâkimlikçe serbest bırakılan emekli Orgeneral Teoman koman emekli korgeneraller engin alan Kamuran Orhon hakkında yakalama kararı çıkarttı mahkeme kararın gereksinisi zanlılara atlı suçun niteliği belirtti MHP den milletvekili seçilen alan balyoz davasından tutuklu bulunuyor</td>
    </tr>
    <tr>
      <td>Başlık 28 Şubat komutanlarına yakalama kararı çıktı</td>
      <td>### şubat komutanlarına yakalama kararı çıktı</td>
    </tr>
  </tbody>
</table>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th colspan="2">Table 5. Ön işlemeş haber ve başlık örneği-2 (Pre-processed news and headline sample-2)</th>
    </tr>
    <tr>
      <th>Orjinal metin</th>
      <th>Ön işlemeş metin</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Türk Hava Yolları'nın 2016'nın ilk iki ayındaki yolcu sayısı geçen yılın aynı döneme göre yüzde 11.2 artışla 9.2 milyona ulaştı. Bu rakam 2015'te 8.3 milyon olmuştu. Yolcu sayısındaki artış iç hatlarda yüzde 12.6, dış hatlarda yüzde 10.2 oranında gerçekleşti. Dış Hatlar Business/Comfort Class yolu sayısı ve Diştan Dışa Transfer Yolcu sayılarında da Ocak-Şubat 2015 dönemi ne kıyasla sırasıyla yüzde 5.8 ve 20.9 artış sağlandı. Doluluk oranı 3 puanlık düşüş ile yüzde 73.3 oldu.</td>
      <td>Türk hava yolları ilk ayındaki yolcu sayısı geçen yılın aynı döneme yüzde artışla milyona ulaştı rakam milyon olmuştu yolcu sayısındaki artış hatlarda yüzde artış hatlarda yüzde oranında gerçekleşti dış hatlar business/comfort class yolcu sayısı diştan dışa transfer yolcu sayılarında ocak şubat döneme kıyasla sırasıyla yüzde 5.8 ve 20.9 artış sağlandı doluluk oranı puanlık düşüş yüzde oldu</td>
    </tr>
    <tr>
      <td>Başlık THY yolcu sayısı 9.2 milyona çıkardı</td>
      <td>THY yolcu sayısı ### milyona çıkardı</td>
    </tr>
  </tbody>
</table>
```