$$\sum _ { i = 1 } ^ { n } \left( { \frac { 4 i ^ { 2 } } { n ^ { 2 } } } \right) { \frac { 2 } { n } } = \sum _ { i = 1 } ^ { n } { \frac { 8 i ^ { 2 } } { n ^ { 3 } } } = { \frac { 8 } { n ^ { 3 } } } \sum _ { i = 1 } ^ { n } i ^ { 2 } = { \frac { 8 } { n ^ { 3 } } } \left( { \frac { n ( n + 1 ) ( 2 n + 1 ) } { 6 } } \right)$$

$$= { \frac { 8 } { n ^ { 3 } } } \left( { \frac { 2 n ^ { 3 } + 3 n ^ { 2 } + n } { 6 } } \right)$$

$$= { \frac { 1 6 n ^ { 3 } + 2 4 n ^ { 2 } + n } { 6 n ^ { 3 } } } = { \frac { 8 } { 3 } } + { \frac { 4 } { n } } + { \frac { 1 } { 6 n ^ { 2 } } }$$

elde edilir. Burada $n \to \infty$ için limit

$$\lim _ { n \to \infty } \sum _ { i = 1 } ^ { n } f ( x _ { i } ) \Delta x = \lim _ { n \to \infty } \left( { \frac { 8 } { 3 } } \right) + \lim _ { n \to \infty } \left( { \frac { 4 } { n } } \right) + \lim _ { n \to \infty } \left( { \frac { 1 } { 6 n ^ { 2 } } } \right) = { \frac { 8 } { 3 } } + 0 + 0 = { \frac { 8 } { 3 } }$$

Burada oluşturulan alt aralıklar bu aralıklardaki $x ^ { * }$ noktaları nasıl seçilirse seçilsin, alt aralıkların sayısı sonsuza ve genişlikleri sıfıra yaklaşırken elde edilen sonuç bir sayıya yakınsayacaktır. Bu durumda, limit işlemi $[ a , b ]$ aralığında tanımlı belirli integral ifadesine götürecektir.

**Tanım 3.2. (Belirli İntegral)**

$f ( x )$, $[ a , b ]$ aralığında tanımlı bir fonksiyon olmak üzere bu fonksiyonun belirli integrali, limitin var olması şartıyla,

$$\int _ { a } ^ { b } f ( x ) d x = \lim _ { n \to \infty } \sum _ { i = 1 } ^ { n } f ( x _ { i } ) \Delta x$$

şeklinde verilir. Eğer limit var ise $f ( x )$ fonksiyonu $[ a , b ]$ aralığında integrallenebilir denir [8].

Integral sembolü, ‘toplam’ anlamına gelen ‘sum’ kelimesinin baş harfi olan $S$ harfinin stilize edilmiş şeklidir. Burada aslında yükseklikleri $f ( x )$, genişlikleri $d x$ (sifirdan büyük ama sonsuz küçük) olan temsili dikdörtgenlerin alanları toplanmaktadır [6].

**Tanım 3.3 (Üst Darboux İntegrali ve Alt Darboux İntegrali)**

$f$, $[ a , b ]$ üzerinde tanımlı ve sınırlı bir fonksiyon olsun.

$$\overline { { \int _ { a } ^ { b } } } f ( x ) d x = \inf _ { s \geq f } \left\{ \int _ { a } ^ { b } s ( x ) d x : \ s \in M [ a , b ] \right\}$$

$$\underline { { \int _ { a } ^ { b } } } f ( x ) d x = \inf _ { t \leq f } \left\{ \int _ { a } ^ { b } t ( x ) d x : \ t \in M [ a , b ] \right\}$$

sayılarına sırası ile, Üst Darboux İntegrali ve Alt Darboux İntegrali denir [7].

**Tanım 3.4 (Riemann Anlamında İntegrallenebilme)**