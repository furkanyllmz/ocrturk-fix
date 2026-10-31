# Tablo 1. Literatürden SKK yöntemi kullanılarak birleştirilen malzeme ve işlem parametreleri

| Malzeme | Takım ilerleme hızı (mm/dk) | Takım dönme hızı (dev/dk) | Karıştırıcı uç geometrisi |
|---|---|---|---|
| HDPE [11] | 45,75,115    | 1500, 2000, 3000    | Silindirik    |
| HDPE [12] | 15    | 1200-2000    | Silindirik    |
| PLA [13]  | 20, 30, 40    | 700, 1400, 2000    | Silindirik, vida ve konik |
| PLA/Al [14] | 20, 30, 40    | 800, 1100, 1400    | Silindirik    |
| PLA [15]  | 10, 14, 20    | 800, 1400, 2000    | Konik pin    |
| PLA [16]  | 3, 6, 9    | 600, 1000, 1400    | Kesik koni ve silindirik  |
| PE [17]   | 16, 29, 44    | 900, 1280, 1700    | Vida M10, M12, M14    |
| HDPE [18] | 20, 40, 63    | 500, 710, 1000, 1400, 2000 | Silindirik    |
| PE-PP [19] | 8, 10, 12.5    | 900, 1860, 2920    | Vida, kare, üçgen, düz ve silindir |
| PP [20]   | 8    | 2000    | Kare, konik vida, dört ağızlı vida |

---

## 2.1 Filament malzemeleri

3B yazıcılarda sarf malzemeleri olarak genel kullanım amacıyla PLA (polilaktik asit), ABSP, PETG gibi filamentler, mühendislik işleri veya daha özel sektörlerin kullanımı için ise farklı çeşitlerde kompozit filamentler bulunmaktadır.

PLA; hem filament oluşturan ana malzeme olarak hem de içerisine dolgu eklenmesi sayesinde geliştirilebilir olması sebebiyle çok tüketilen bir malzemedir. PLA filamentler; düşük sıcaklıklarda basılması, tabla ısıtmasına ihtiyaç duyulmaması ve baskı sırasında oluşabilecek hataların azlığı nedeniyle tercih edilmektedir. PLA; mısır, patates, şeker kamışı vb. yenilebilir kaynaklardan üretilebilen organik bir malzeme olduğu için insan sağlığına zararsızdır ve belli şartlarda doğada ayrışabilen biyopolimerlerdendir [21-23]. Bu özelliklerinden dolayı petrol bazlı polimerlere (polipropilen (PP), düşük yoğunluklu polietilen (LDPE), polistiren (PS) ve poliamid (PA)) alternatif olarak kullanılmaktadır [24, 25]. PLA filamentler, farklı uygulamalarda kullanılabilmesi için çeşitli dolgu malzemeleri eklenerek modifiye edilmektedir. Eklemeli imalatta sarf malzeme olarak kullanılan filamentlerin çeşitleri her geçen gün artmaktadır. SKK metodunda kaynak kalitesini etkileyen fazla sayıda parametre elde edilen ve eklenen her parametre ciddi sayıda deney sayısını arttırdığı için yapılan çalışma malzeme olarak PLA-CF ve PLA Wood ile sınırlandırılmıştır. Bu çalışmada, karbon fiber katkılı PLA (PLA-CF) ve ahşap katkılı PLA (PLA Wood) olmak üzere iki kompozit termoplastik filament kullanılmıştır. PLA-CF filament, karbon fiber takviyeli (%15) PLA kompozit filamenttir. Ana matris içinde yer alan karbon lifler kristalleşmeyi iyileştirerek sade PLA’ya kıyasla daha iyi mekanik ve termal özellikler göstermeye önemi sağlamaktadır [22, 26]. PLA Wood ise, %30 oranında ağaç lifi (çam, sedir, bambu, meşe ve zeytin vb.) içeren kompozit PLA filamenttir. Düşük mekanik ve termal özellikler göz önünde kalıntılıdır. Özellikle görseliğin önemli olduğu mimari ve ev dekorasyon modelleri ürünlerinde tercih edilmektedir [27]. PLA-CF ve PLA Wood filamentlerin özellikleri Tablo 2’de verilmiştir.

---

### Tablo 2. Filamentlerin teknik özellikleri

| Mekanik Özellikler | PLA-CF [28] | PLA-Wood [29] |
|---|---|---|
| Çap ölçüsü (mm)  | 1.75    | 1.75    |
| Marka    | Filameon    | Filameon    |
| Renk    | Siyah    | Açık Kahverengi |
| Çekme Müşaviri (MPa) | 55    | 47    |
| Yoğunluk (g/cm3) | 1.23    | 1.13    |

---

### 2.2 Deney numunelerinin üretimi

Deneylerde, eriyik yığma modelleme prensibi ile çalışan Ender 3-S1 3B yazıcı kullanılarak SKK için 72x114x5 mm ölçülerinde plakalar (Şekil 2a) ve filamentlerin mekanik özelliklerinin belirlenmesi için ASTM D638-10 [30] standartlarına uygun numuneler (Şekil 2b) basılmıştır. PLA-CF ve PLA Wood numunelerin baskı parametreleri sırasıyla; nozul sıcaklığı 215/220 °C, tabla sıcaklığı 65/65 °C, basım hızı 45/50 mm/sn ve basım yönü XYZ olarak kullanılmıştır. Numuneler, katman kalınlığı 0.2 mm ve %100 doluluk oranında basılmıştır. Her malzeme için 5 adet çekme numunesi basılarak çekme mukavemetlerinin ortalaması alınmıştır.

---

### Şekil 2. SKK kaynağı plaka ve çekme numune ölçüleri (mm)

---

### 2.3 Sürtünme karıştırma kaynağı işlemleri

SKK yönteminde malzeme çiftlerinin birleştirilmesinde kaynak kalitesi işlem parametrelerinden doğrudan etkilenmektedir. Kaynak kalitesini etkileyen başlıca işlem parametreleri takım ilerleme hızı [31], takım dönme hızı [32-34], takım omuz şekli [35], karıştırıcı uç geometrisi [36, 37] ve eğim açısı [38] olarak sıralanabilir. İşlem parametreleri kaynak bölgesinde sürtünmeden kaynaklı üretilen ısı miktarı...