```markdown
<!-- Image (388, 15, 608, 344) -->
Şekil 2. Bir bölgenin tek trafo bölgesine indirgemesi ve kayıpların tahmin edilmesi

Önerilen algoritma-2 yardımıyla karmaşık bölgeler tek tip trafo bölgesine indirgenebilir ve bölgenin yaklaşık teknik kayıpları hesaplanabilir. Güç sistemlerinde teknik kayıplar, hat uzunlukları, trafo yapısı ve bilgileri, gerilim ve güç değerleri bilinen şebekeler için tahmin edilebilir [16,17]. Bir dağıtım şebekesinde harcanan toplam enerji miktarı, tüm trafo bölgelerine eşit miktarda paylaştırlarak, eş değer trafo bölgeleri elde edilir. Paylaştırlan güç miktarlarına uygun bir iletken tayin edilerek yeni bir trafo bölgesi oluşturulur. Herhangi karmaşık bir şebekesi veya bir şehri tek trafo bölgesine indirgererek, teknik kayıpların analizleri bu sayede daha kolay bir şekilde gerçekleştirilir. Trafo kayıplarını hesaplarken, şebekelerin bir şehrin genel durumunu veya şehirde kullanılan trafo tiplerinin yaygınlık durumunun göz önüne alınması, yapılacak tahminin doğruluk oranını artıracaktır. Trafo bölgelerinin çok çeşitli olduğu bölgelerde yaygın kullanılan her çeşit trafo için, yeni trafo bölgeleri oluşturulabilir. Ancak harcanan enerji miktarları, hat uzunlukları, tayin edilen iletken özellikleri eşit (her bölge için eş değer) olacağından dolayı değişiklik gösterecek tek durum trafolar üzerinde meydana gelen kayıplar olacaktır (E1 değeri sabit, E2 değeri değişken olacaktır).

Algoritmalar ile elde edilen sonuçlar yapay sinir ağları (YSA) ile de desteklenmiştir [18-25]. Kullanılan YSA modelinde 5 adet giriş ve 2 adet çıkış bulunmaktadır. Girişler sırasıyla; şehrin toplam trafo gücü, toplam trafo sayısı, toplam hat uzunluğu, kayıp-kaçak oranı, faturalandırılın ve faturalandırılamayan enerjinin (tüm enerjinin) toplam miktarı şeklindedir. Çıkışlar ise toplam teknik kayıplar ve tahmin edilen kaçak kullanım miktarıdır. Oluşturulan YSA ağ yapısı şekil 3'te gösterildiği gibidir.

<!-- Image (278, 674, 718, 785) -->
Şekil 3. Kullanılan YSA ağ yapısı

İleri beslemeli geri yayılım (Feed-Forward Backprop) ağ tipi kullanılmıştır. En yüksek doğruluk oranı, nöron sayıları sırasıyla 10 ve 8 olan iki gizli katmanın kullanılmasıyla elde edilmiştir. Nöron sayılarının belirlenmesinde, kabul görmüş herhangi bir yöntem olmadığı için nöron sayıları deneme yanılma yoluyla belirlenmiştir. Aktivasyon fonksiyonu olarak en yaygın kullanılan aktivasyon fonksiyonu sigmoid fonksiyon seçilmiştir. Birden fazla eğitim fonksiyonları kullanılmış ve eğitim fonksiyonlarının performansları birbirleri ile karşılaştırılmıştır.

## 2.2. Kullanılan eğitim fonksiyonları

Önerilen algoritmalar birden fazla eğitim fonksiyonu ile eğitilmiş; eğitim ve test sonuçları birbirleri ile kıyaslanmıştır.

```