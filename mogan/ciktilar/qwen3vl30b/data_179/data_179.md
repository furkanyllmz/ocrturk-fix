```html
<p>Tanım 2.14 (Gamma Fonksiyonu): $k > 0$ için</p>
$$
\Gamma(k) = \int_{0}^{\infty} e^{-t} x^{k-1} dx
$$
<p>olarak tanımlanır (Kannappan, 2009).</p>
<p>Ayrıca Araştırma Bulguları kısmında sıkça kullandığımız bu fonksiyonun bazı özelliklerinden bahsedecek olursak $n$ pozitif tamsayı olmak üzere</p>
$$
\Gamma(n) = (n-1)!
$$
$$
\Gamma(n+1) = n\Gamma(n)
$$
$$
\Gamma\left(\frac{1}{2}\right) = \sqrt{\pi}
$$
<p>şeklindedir (Kannappan, 2009).</p>
<p>Tanım 2.15 (Beta Fonksiyonu):</p>
$$
\beta(\mu_1, \mu_2) = \int_{0}^{1} t^{\mu_1-1}(1-t)^{\mu_2-1} dt, \quad \mu_1, \mu_2 > 0
$$
<p>şeklindedir. Bu eşitlik Euler tipi Beta fonksiyonu ya da birinci çeşit Euler integrali olarak adlandırılır (Dragomir et al., 1999).</p>
<p>Burada Gamma ve Beta fonksiyonları arasındaki ilişki</p>
$$
\beta(\mu_1, \mu_2) = \frac{\Gamma(\mu_1)\Gamma(\mu_2)}{\Gamma(\mu_1 + \mu_2)}
$$
<p>şeklindedir (Kannappan, 2009).</p>
<p>Tanım 2.16 (Riemann-Liouville Kesirli Mertebeden İntegrali): $\mu \in L_1[a, b]$ olsun. $a \geq 0$ iken $\alpha > 0$ için Riemann-Liouville kesirli mertebeden integrali aşağıdaki gibi tanımlanır:</p>
$$
J_{a+}^{\alpha} \mu(x) = \frac{1}{\Gamma(\alpha)} \int_{a}^{x} (x-t)^{\alpha-1} \mu(t) dt, \quad x > a,
$$
$$
J_{b-}^{\alpha} \mu(x) = \frac{1}{\Gamma(\alpha)} \int_{x}^{b} (t-x)^{\alpha-1} \mu(t) dt, \quad x < b,
$$
(2.1)
<p>Burada, $\Gamma(\alpha) = \int_{0}^{\infty} t^{\alpha-1} e^{-t} dt$ Gamma fonksiyonu ve $J_{a+}^{0} \mu(x) = J_{b-}^{0} \mu(x) = \mu(x)$ eşitliği sağlanır. Ayrıca $\alpha = 1$ seçilirse kesirli integral klasik integrale indirgenir (Miller and Ross, 1993).</p>
<p>Tanım 2.17 (Riemann-Liouville Değişken Mertebeden Kesirli İntegrali): $C([a, b])$, $[a, b] \subset \mathbb{R}$ aralığında tanımlı gerçek değerli sürekli fonksiyonların uzayını göstermek üzere $g \in C([a, b])$, $\mu : [\theta_1, \theta_2] \to (0, 1)$ fonksiyonu için değişken mertebeden Riemann-Liouville kesirli integrali;</p>
$$
J_{\theta_1}^{\mu(z)} g(x) = \frac{1}{\Gamma(\mu(z))} \int_{\theta_1}^{x} (x-s)^{\mu(z)-1} g(s) ds
$$
<p>şeklindedir. (Valarmathi and Gowrisankar, 2023)</p>
```