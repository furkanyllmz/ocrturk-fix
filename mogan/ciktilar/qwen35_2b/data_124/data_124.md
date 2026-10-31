```markdown
$\sum_{i=1}^{n}\left(\frac{4 i^{2}}{n^{2}}\right) \frac{2}{n}=\sum_{i=1}^{n} \frac{8 i^{2}}{n^{3}}=\frac{8}{n^{3}} \sum_{i=1}^{n} i^{2}=\frac{8}{n^{3}}\left(\frac{(n(n+1)(2 n+1)}{6}\right)$

$$=\frac{8}{n^{3}}\left(\frac{2 n^{3}+3 n^{2}+n}{6}\right)$$

$$=\frac{16 n^{3}+24 n^{2}+n}{6 n^{3}}=\frac{8}{3}+\frac{4}{n}+\frac{1}{6 n^{2}}$$

elde edilir. Burada $n \rightarrow \infty$ için limit

$$\lim _{n \rightarrow \infty} \sum_{i=1}^{n} f\left(x_{i}\right) \Delta x=\lim _{n \rightarrow \infty}\left(\frac{8}{3}\right)+\lim _{n \rightarrow \infty}\left(\frac{4}{n}\right)+\lim _{n \rightarrow \infty}\left(\frac{1}{6 n^{2}}\right)=\frac{8}{3}+0+0=\frac{8}{3}$$

Burada oluşturulan alt aralıklar bu aralıklardaki $x^{*}$ noktaları nasıl seçirse seçilsin, alt aralıkların sayısı sonsuza ve genişlikleri sıfıra yaklaşırken elde edilen sonuç bir sayıya yaklaşacaktır. Bu durumda, limit işlemi $[a, b]$ aralığında tanımlı belirli integral ifadesine götürücektir.

## Tanım 3.2. (Belirli Integral)

$f(x),[a, b]$ aralığında tanımlı bir fonksiyon olmak üzere bu fonksiyonun belirli integrali, limitin var olması şartıyla,

$$\int_{a}^{b} f(x) d x=\lim _{n \rightarrow \infty} \sum_{i=1}^{n} f\left(x_{i}\right) \Delta x$$

şekilde verilir. Eğer limit var ise $f(x)$ fonksiyonu $[a, b]$ aralığında integrallenebilir denir [8].

Integral sembolü, ‘toplam’ anlamına gelen ‘sum’ kelimesinin baş harfi olan $S$ harfinin stilize edilmiş şeklidir. Burada aslında yükseklikleri $f(x)$, genişlikleri $d x$ (sıfırdan büyük ama sonsuz küçük) olan temsilî dikdörtgenlerin alanları toplanmaktadır [6].

## Tanım 3.3 (Üst Darboux Integrali ve Alt Darboux Integrali)

$f, [a, b]$ üzerinde tanımlı ve sınırlı bir fonksiyon olsun.

$$\int_{a}^{\bar{b}} f(x) d x=\inf _{s \geq f}\left\{\int_{a}^{b} s(x) d x: s \in M[a, b]\right\}$$

$$\int_{a}^{\bar{b}} f(x) d x=\inf _{t \leq f}\left\{\int_{a}^{b} t(x) d x: t \in M[a, b]\right\}$$

sayılarına sırası ile, Üst Darboux Integrali ve Alt Darboux Integrali denir [7].

## Tanım 3.4 (Riemann Anlamında İntegrallenebilir)
```