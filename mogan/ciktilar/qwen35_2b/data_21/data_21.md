```markdown
Tek tabaka ya da tek eleman içeren bazı başarılı
ağlar oluşturulabilmesine rağmen çoğu uygulamalar en
az üç tabaka (girdi tabakası, gizli tabaka ve çıktı
tabakası) içeren ağlara ihtiyaç duymaktadır. Girdi
tabakası, dışardan girdileri alan nöronları içerir.
Ayrıca, önemli olan bir nokta, girdi tabakasındaki
nöronların girdi değerleri üzerinde bir işlem
uygulamamasıdır. Sadece girdi değerlerini bir sonraki
tabakaya ileter ve bu yüzden de bazı araştırmacılar
tarafından girdi tabakası ağlarının tabaka sayısına
dahil edilmezler. Çıktı tabakası ise çıktılarını dışarıya
iletten nöronları içeren tabakadadır. Girdi ve çıktı
tabakaları birer tabakadan oluşurken bu iki tabaka
arasında birden fazla gizli tabaka bulunabilir. Bu
gizli tabakalar çok sayıda nöron içerir ve bu nöronlar
tamamen ağ içindeki diğer nöronlarla bağlantılıdır.
Çoğu ağ türünde, gizli tabakadaki bir nöron sadece bir
önceki tabakanın tüm nöronlarından sinyal alır. Nöron
işlemini yaptıktan sonra ise çıktısını bir sonraki tabakanın
tüm nöronlarına gönderir. Bu yapı ağ çıktısı için bir
ileri besleme patikası oluşturur. Bir nörondan diğerine
olan iletişim hattı, sinir ağları için önemli bir parçadır.
Bazı ağlarda, bir nöron aynı tabakadaki başka nöronlara
engel oluşturabilir. Bu, yanal engelleme veya rekabet
olarak adlandırılır ve en çok çıktı tabakasında kullanılır.
Diğer bir bağlantı şekli ise geri yayınimdır. Geri
yayımın, bir tabakanın çıktısının önceki tabaka
gönderilmesi olup Şekil 3'te yanal engelleme ve
rekabet kavramlarıyla birlikte örneklenmiştir.

# Yöntem

İleri beslemeli geri yayım mimarisi 1970'li
yillarda geliştirilmiştir. Bu mimarinin geliştirilmesinde
birbirlerinden bağımsız olarak birkaç araştırmacının
katıkları olmuştur. Asıl katkı ise Rumelhart, Hinton
ve Williams (1986) tarafından yapılmıştır. Ortaya
çıkışından sonra, hem etkilii hem de çok kullanılması
olmayanlardan dolayı büyük bir popülerite kazanmış ve
hala en çok kullanılan ağ türü olarak bilinmektedir
(Yurtoğlu 2005). Çok sayıda farklı uygulama alanında
kullanılmakta olup en büyük özelliği doğal olmayan
yapı içerdeki problemlerde de etkil olabilmektedir.
Tipik bir geri yayım ağ mimarisinde de bir girdi tabakası,
bir çıktı tabakası ve bu iki tabaka arasında en az bir
adet gizli tabaka bulunur. Gizli tabaka sayısı için
herhangi bir kısıt olmamakla birlikte genellikle bir ya
da iki gizli tabaka kullanılmaktadır. Çalışmada kullanılan;
bir girdi tabakası, bir gizli tabaka ve bir çıktı
tabakası içeren bir geri yayım ağının genel yapısı
Şekil 4'te örneklenmiştir.

Şekil 4'te, tabakalar halinde düzenlenmiş
dairesel işlem elemanlarını yani nöronları temsil
edilmektedir. Girdi tabakasında üç adet nöron
bulunmaktadır. Yani ağa girdi olarak üç değişik
tanımlamaktadır. Bunun dışında gizli tabakada iki, çıktı
tabakasında ise üç adet nöron bulunmaktadır.
Dolayısıyla, ağdan üç değişikken olarak çıktı
alınmaktadır. Girdi tabakasından, gizli tabakaya
iletilen değerler "Ağırıklar 1" ağır seti ile, gizli
tabakadan çıktı tabakasına iletilen değerler ise
"Ağırıklar 2" ağır seti ile ağırlandırılmaktadır.
Geri yayım ise sadece eğitim sürecinde kullanılır.
Dolayısıyla eğitim sürecindeki bilgi akışı Şekil 4'teki
tüm oklar ile gösterilmektedir.

Savalan barajı haznesini simüle etmek için
kullanılan 34 yıl süreli aylık ortalama akım verilerin
ağı yönlendirmesinde yardımcı olmak üzere Neuro

Şekil 2. YSA'ların genel yapısı

Girdi Tabakası

Gizli Tabaka
(Birden fazla olabilir)

Çıktı Tabakası

```