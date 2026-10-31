```markdown
Tablo 6'da örnekleme periyodunun çözüm doğruluğuna etkisi incelenmiştir. Çözümün örnekleme periyodu $t_s$ azaldıkça yönetimin doğruluğunun arttığı görülmektedir. Tablo 6'da 5 inci saniye için türev değerleri verilmiştir.

Tablo 6. Farklı örnekleme periyotları için ($t_s$) GL ortalama hata sonuçları
<!-- Table (124, 135, 873, 259) -->
\begin{tabular}{|l|c|c|c|}
\hline
& $t_s=0.1, t:0:20$ & $t_s=0.5, t:0:20$ & $t_s=1, t:0:20$ \\
\hline
$f(t) = e^t$ & 0.0508 & 0.2822 & 0.5529 \\
\hline
$f(t) = \sin(t)$ & 0.0578 & 3.3335 & -0.52798 \\
\hline
$f(t) = t$ & $4.9738e^{-15}$ & 0.20008 & 0.4500 \\
\hline
$f(t) = t^2 + t + 1$ & 0.0118 & 0.0618 & 0.0890 \\
\hline
\end{tabular}

Tablo 7. $t = 5$ için farklı kesir derecelerin $f(t)$ fonksiyon değerleri
<!-- Table (122, 289, 873, 429) -->
\begin{tabular}{|l|l|c|c|c|c|}
\hline
\multicolumn{2}{|c|}{\multirow{2}{*}{$t = 5$ için}} & \multicolumn{4}{c|}{Fonksiyonlar} \\
\cline{3-6}
\multicolumn{2}{|c|}{} & $f(t) = e^t$ & $f(t) = \sin(t)$ & $f(t) = t$ & $f(t) = t^2 + t + 1$ \\
\hline
\multirow{5}{*}{\begin{tabular}[t]{@{}l@{}}Kesir\\ Derecesi\end{tabular}} & $D^{0.5}$ & 118,0080 & -0,6878 & 2,4609 & 18,2929 \\
\cline{2-6}
& $D^{0.8}$ & 102,8322 & -0,4086 & 1,4784 & 12,8719 \\
\cline{2-6}
& $D^{1.0}$ & 93,8150 & -0,2021 & 1 & 10 \\
\cline{2-6}
& $D^{1.2}$ & 85,5893 & 0,0073 & 0,6384 & 7,6352 \\
\cline{2-6}
& $D^{1.5}$ & 74,5852 & 0,3057 & 0,2734 & 4,8945 \\
\hline
\end{tabular}

## 2.3 Laplace'ın Kuvvet Fonksiyonları Türev Genelleştirmesi

Lacroix tarafından 1982'de yazılan eserde aslında Laplace'ın kesir dereceli türevinin basit bir tanımı olduğu yazılmaktadır ve bu çalışmada, $y = t^m$ kuvvet fonksiyonun türevini ele alarak bir genelleme yapılmaya çalışılmıştır[17]. Bu yöntem, kuvvet seri açılımları bilinen fonksiyonlar için çözümler üretilebilmektedir. $y = t^m$'nin $n$. mertebe tamsayı derece türevleri için denklem6'daki eşitlik kullanılmıştır.

$$
\frac{d^n y}{dt^n} = \frac{m!}{(m-n)!} t^{m-n} \quad (6)
$$

Denklem6'daki eşitlikten yola çıkarak kuvvet fonksiyonunun $n$. türevi için gamma fonksiyonu denklem7'deki gibi elde edilmiştir.

$$
\frac{d^n y}{dt^n} = \frac{\Gamma(m+1)}{\Gamma(m-n+1)} t^{m-n} \quad (7)
$$

$m$ ve $n$'nin reel sayı olması durumunda sürekli gamma fonksiyonu ile faktöriyel hesabının mümkün olduğu önerilirse, $y = t^m$ ifadesinin $\alpha \in R$ için kesir dereceli türevi bu genelleme yardımı ile denklem8'deki gibi ifade edilmektedir.

$$
D^\alpha y(x) = \frac{d^\alpha}{dt^\alpha} x^m = \frac{\Gamma(m+1)}{\Gamma(m-\alpha+1)} t^{m-\alpha} \quad (8)
$$

Birçok temel fonksiyon, kuvvet seri açılımları olarak gösterilebilmektedir. Bu fonksiyonlardan bazılarının kuvvet serisi açılımları aşağıdaki gibidir.

$f(t) = e^t$ kuvvet serisi formunda denklem9'daki gibi ifade edilmektedir.

$$
y = e^t = \sum_{k=0}^{\infty} \frac{t^k}{k!} = 1 + t + \frac{t^2}{2!} + \frac{t^3}{3!} + \dots \quad (9)
$$

```