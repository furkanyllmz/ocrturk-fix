```markdown
Ortaya koyduğumuz bu çalışma ile metin sınıfıma yöntemlerinden biri olan “Çok Sınıfı Sınıfıma” probleminin Türkçe dili için BERT derin öğrenme tekniği kullanarak çözülmesi hedeflenmiş ve gerçekleştirilmiştir. Birçok eğitimden geçmiş farklı veri setleri ve doğrulama kümesi ile kapsamlı bir başarm tablosu (Tablo 10) elde edilmiştir. Elde edilen bu başarm tablosu ile gelecekteki “Çok Sınıfı Sınıfıma” problemlerinin Türkçe dili için BERT derin öğrenme tekniği uygulanarak gerçekleştirilecek çalışmalara ışık tutulması ve daha yüksek başarı oranlarına ulaşması temenni edilmektedir.

## 2. Materyal ve Yöntem (Material and Method)

Günümüzde lisans eğitimini tamamlayan çoğu öğrenci, daha iyi bir gelecek için ikinci bir yeterlilik almaya karar verir ve lisans üstü eğitimine başlar. Yüksek lisans, lisans eğitimine dayalı eğitim-öğretim ve araştırmanın sonuçlarını ortaya koymaya amaçlayan bir yükseköğretdir. Yüksek lisans eğitimliği, kişinin eğitim aldığı branşta uzmanlaşması ve bu durumu bilimsel bir tezle ispat etmesiyle tamamlanır. Her yıl sayısı mezun veren yüksek lisans programları ile sayısız bilimsel tez akademimize kazandırılmaktadır.

Bir diğer önemli konu ise fikri ve sanayi mülkiyet haklarından biri olan patenttir. Bir buluşa sahip olan kişinin, buluşa konu olan ürününü, belirlenen süre boyunca üretme, kullanma, satma ya da ithal etme hakkına sahip olması durumuna patent hakkı adı verilir. Bu hakın somut göstergesi olan belge ise patent adını taşır. Günümüzde bilgiye dayalı faaliyetlerin artması ile birlikte patent önemi daha da artmıştır.

Tez ve patentlerin ortak noktası, ortaya konulan eser bir kategoriye ait olmasıdır. Hem tez yazarı hem de patent yazarı, çalışmalarındaki içeriği kategorisi kendileri belirlemektedir. Internet üzerinden erişime açık olan bu iki alanda da kategorisi belirlenmiş birçok eser mevcuttur. Günümüz teknolojisiyle yapay zeka teknolojisi ile metinlerin kategorilerinin belirlenmesi sağlanabilmektedir. Bu çalışma buradan yola çıkarak özellikle Türkçe dilinde yazılan bilimsel metinlerin BERT derin öğrenme tekniği uygulanarak çoklu sınıfıma sınıfıma konumlandırılması konusunu edinmiştir. İlk aşama olarak bir veri seti oluşturulmuştur. Oluşturan veri seti üzerinde ön işleme (Pre-processing) gerçekleştirilmiştir. Ön işlemeden geçirilen veri seti için eğitim ve doğrulama setleri belirlenmiştir. Sonrasında BERT derin öğrenme tekniği uygulanarak bir performans metriği olan F1 skorı elde edilmiştir. Çalışmaya ait aşamalar ve sistemin genel görünümünü içeren diyagram Şekil 1 üzerinde görülebilir. Devamındaki bölümlerde ise çalışmanın ayrıntıları detaylı bir şekilde sunulmuştur.

Şekil 1. Sistem Genel Görünümü (System Overview)

## 2.1. Metin Sınıfıma (Text Classification)

Metin sınıfıma sorunu, $B = \{b_1, b_2, ..., b_n\}$ kümesindeki her bir belgenin (metin), önceden tanımlanmış $S = \{s_1, s_2, ..., s_m\}$ kümesindeki sınıflara ait olup olmadığının belirlenmesidir. Yani her $(b_j, s_i) \in B \times S$ çifti için doğru ya da yanlış biçimde bir mantıksal değer üretilemektedir. (Tantug, 2016) Metin sınıfıma, verilerden kolayca iç görü elde etmeye olanak sağlayacağı için yapay zeka gün geçtikçe daha da önemli bir parçası haline gelmiştir. Veriler belirli bir şekilde düzenlenmişçe bu verilerden değer elde etmek zordur. Metin etiketleme veya metin kategorizasyonu olarak da bilinen metin sınıfıma, veri olarak ele alınan metni organize gruplar halinde kategorize etme işlemidir. Bir Doğal Dil İşleme alt konusu olan metin sınıfıma ile metin analiz edilir ve ardından içeriğine göre önceden tanımlanmış bir dizi etikete veya kategoriyeye atanabilir. Bu atama sonucunda metin kategorilere ayrılmış olur ve düzensiz veri düzenlenerek kullanılmak üzere bir değer elde edilir.

Metin sınıfıma için kullanılan başlıca yöntemler bir sonraki konu başlığına ayrıntılı bir şekilde ele alınmıştır.

Metin sınıfıma için kullanılan başlıca yöntemler bir sonraki konu başlığına ayrıntılı bir şekilde ele alınmıştır.

```