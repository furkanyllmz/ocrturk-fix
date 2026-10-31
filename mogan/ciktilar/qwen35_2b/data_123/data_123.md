```markdown
# Şekil 3.1. $N$ tane dikdörtgensel bölgeye ayrılmış yaprağın yüzey alanı

k'ıncı dikdörtgensel bölgenin alanı

$$a_{k}=\text{taban } x \text{ yükseklik}=\Delta x f(x_{k})=\left(\frac{1}{N}\right)\left(\frac{k}{N}\left(1-\frac{k}{N}\right)\right)$$

şekilde yazılabilir ve ayrıca tüm dikdörtgenlerin alanları toplamı

$$\sum_{k=1}^{N} a_{k}=\sum_{k=1}^{N} \Delta x f(x_{k})=\sum_{k=1}^{N}\left(\frac{1}{N}\right)\left(\frac{k}{N}\left(1-\frac{k}{N}\right)\right)$$

şekilde yazılabilir ve gerekli düzenlemeler yapılsa

$$\sum_{k=1}^{N} a_{k}=\sum_{k=1}^{N}\left(\frac{k}{N}\left(1-\frac{k}{N}\right)\right)=\left(\frac{1}{N^{2}}\right) \sum_{k=1}^{N} k-\left(\frac{1}{N^{3}}\right) \sum_{k=1}^{N} k^{2}$$

$$=\left(\frac{1}{N^{2}}\right)\left(\frac{N(N+1)}{2}\right)-\left(\frac{1}{N^{3}}\right)\left(\frac{(2 N+1) N(N+1)}{6}\right)$$

$$=\left(\frac{1}{2}\right)\left(\frac{(N+1)}{N}\right)-\left(\frac{1}{6}\right)\left(\frac{(2 N+1)(N+1)}{N^{2}}\right)$$

(3.1)

elde edilir. Burada gerçek alanın hesaplanabilmesi için sonsuz tane $N$ bölmeye ayrılması gerekir. Bu yüzden (3.1) ifadesinin $N \rightarrow \infty$ limiti alınmalıdır.

$$\lim _{N \rightarrow \infty}\left(\frac{1}{2}\right)\left(\frac{(N+1)}{N}\right)-\lim _{N \rightarrow \infty}\left(\frac{1}{6}\right)\left(\frac{(2 N+1)(N+1)}{N^{2}}\right)=\frac{1}{2}-\frac{1}{6} 2=\frac{1}{6}$$

Böylece tüm yaprağın alanı bu alanın 2 katı yani

$$\frac{1}{6} 2=\frac{1}{3}$$

şekilde bulunur [5].

Limiti alınan fonksiyonlar pozitife ve negatif olma durumu gibi birçok durumda karşımıza çıkabilir. Bu tip limitler için özel bir ad kullanılmaktadır. 'Sonlu Yaklaşımın Limitleri Teorisi' olarak adlandırılan bu yaklaşış matematikçi Bernhard Riemann tarafından ortaya konulmuştur [6].
```