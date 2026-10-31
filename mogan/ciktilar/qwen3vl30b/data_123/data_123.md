```html
<p>Şekil 3.1. N tane dikdörtgensel bölgeye ayrılmış yaprağın yüzey alanı</p>
<p>k'inci dikdörtgensel bölgenin alanı</p>
$$
a_{k} = \text{taban } x \text{ yükseklik } = \Delta x f(x_{k}) = \left(\frac{1}{N}\right)\left(\frac{k}{N}\left(1 - \frac{k}{N}\right)\right)
$$
<p>şeklinde yazılabilir ve ayrıca tüm dikdörtgenlerin alanları toplamı</p>
$$
\sum_{k=1}^{N} a_{k} = \sum_{k=1}^{N} \Delta x f(x_{k}) = \sum_{k=1}^{N} \left(\frac{1}{N}\right)\left(\frac{k}{N}\left(1 - \frac{k}{N}\right)\right)
$$
<p>şeklinde yazılabilir ve gerekli düzenlemeler yapılırrsa</p>
$$
\begin{aligned}
\sum_{k=1}^{N} a_{k} &= \sum_{k=1}^{N} \left(\frac{k}{N}\left(1 - \frac{k}{N}\right)\right) = \left(\frac{1}{N^{2}}\right)\sum_{k=1}^{N} k - \left(\frac{1}{N^{3}}\right)\sum_{k=1}^{N} k^{2} \\
&= \left(\frac{1}{N^{2}}\right)\left(\frac{N(N+1)}{2}\right) - \left(\frac{1}{N^{3}}\right)\left(\frac{(2N+1)N(N+1)}{6}\right) \\
&= \left(\frac{1}{2}\right)\left(\frac{(N+1)}{N}\right) - \left(\frac{1}{6}\right)\left(\frac{(2N+1)(N+1)}{N^{2}}\right)
\end{aligned}
$$
<p>elde edilir. Burada gerçek alanın hesaplanabilmesi için sonsuz tane N bölmeye ayrılmışa gerekir. Bu yüzden (3.1) ifadesinin $N \to \infty$ limiti alınmalıdır.</p>
$$
\lim_{N \to \infty} \left(\frac{1}{2}\right)\left(\frac{(N+1)}{N}\right) - \lim_{N \to \infty} \left(\frac{1}{6}\right)\left(\frac{(2N+1)(N+1)}{N^{2}}\right) = \frac{1}{2} - \frac{1}{6}2 = \frac{1}{6}
$$
<p>Böylece tüm yaprağın alanı bu alanın 2 katı yani</p>
$$
\frac{1}{6}2 = \frac{1}{3}
$$
<p>şeklinde bulunur [5].</p>
<p>Limiti alınan fonksiyonlar pozitif ve negatif olma durumu gibi birçok durumda karşımıza çıkabilir. Bu tip limitler için özel bir ad kullanılmaktadır. 'Sonlu Yaklaşımların Limitleri Teorisi' olarak adlandırılan bu yaklaşım matematikçi Bernhard Riemann tarafından ortaya konulmuştur [6].</p>
```