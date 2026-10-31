```markdown
# Teorem 2.2.5 $f: I \subseteq \mathbb{R} \rightarrow \mathbb{R}$ şeklinde tanımlı $f$ fonksiyonu $I^{\circ}$ üzerinde diferansiyelenebilen bir fonksiyon ve $q \geq 1$, $a < b$ olacak şekilde $a, b \in I^{\circ}$ iken $f' \in L[a, b]$ olsun. Eğer $|f'|^{q} [a, b]$ aralığında $n$-kesirli polinom konveks fonksiyon ise

$$
\left| \frac{f(a) + f(b)}{2} - \frac{1}{b - a} \int_{a}^{b} f(x) dx \right|
$$

$$
\leq \frac{b - a}{2} \left( \frac{1}{2} \right)^{2 - \frac{2}{q}} \left( \frac{|f'(a)|^{q}}{n} \sum_{i=1}^{n} M_{1}(i) + \frac{|f'(b)|^{q}}{n} \sum_{i=1}^{n} M_{2}(i) \right)^{\frac{1}{q}}
$$

$$
+ \frac{b - a}{2} \left( \frac{1}{2} \right)^{2 - \frac{2}{q}} \left( \frac{|f'(a)|^{q}}{n} \sum_{i=1}^{n} M_{2}(i) + \frac{|f'(b)|^{q}}{n} \sum_{i=1}^{n} M_{1}(i) \right)^{\frac{1}{q}}
$$

eşitsizliği sağlanır ki burada

$$
M_{1}(i) = \frac{i^{2} \left[ \frac{1}{2}^{1 + \frac{1}{i}} (5i + 1) + 1 - i \right]}{(i + 1)(2i + 1)(3i + 1)}
$$

ve

$$
M_{2}(i) = \frac{i \left[ \frac{1}{2}^{1 + \frac{1}{i}} i + 1 + i \right]}{(2i + 1)(3i + 1)}
$$

şeklindedir [33].

## 2.3 Farklı Konveks Fonksiyon Sınıfları ve Hermite-Hadamard Tipli eşitsizlikler

### Tanım 2.3.1 $f: I \rightarrow (0, \infty)$ fonksiyonuna, Eğer $\log f$ fonksiyonu konveks ise veya her $x, y \in I$ ve $t \in [0, 1]$ için

$$
f(tx + (1 - t)y) \leq f(x)^{t} f(y)^{1 - t}
$$

eşitsizliği sağlanırsa $AG$-konveks veya log-konveks denir [3, 21].

### Teorem 2.3.1 $f: I \subseteq \mathbb{R} \rightarrow \mathbb{R}$ $AG$-konveks bir fonksiyon $a, b \in I$ ve $a < b$ olsun. Bu taktirde $AG$-konveks veya log-konveks fonksiyonlar için Hermite-Hadamard eşitsizliği

$$
f \left( \frac{a + b}{2} \right) \leq \exp \left[ \frac{1}{b - a} \int_{a}^{b} \ln f(x) dx \right] \leq \sqrt{f(a) f(b)} \tag{2.3.1}
```