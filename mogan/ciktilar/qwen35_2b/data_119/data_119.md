```markdown
Tablo 6'da örneklem periyodunun çözümü doğruluğuna etkisi incelenmiştir. Çözümün
örneklem periyodu ts azaldıkça yöntemin doğruluğunun arttığı görülmektedir. Tablo 6'da 5inci
saniye için türev değerleri verilmiştir.

Tablo 6.Farklı örneklem periyotları için (ts) GL ortalama hata sonuçları

| | ts=0.1, t:0:20 | ts=0.5, t:0:20 | ts=1, t:0:20 |
| :--- | :--- | :--- | :--- |
| $f(t) = e^t$ | 0.0508 | 0.2822 | 0.5529 |
| $f(t) = \sin(t)$ | 0.0578 | 3.3335 | -0.52798 |
| $f(t) = t$ | $4.9738e^{-15}$ | 0.20008 | 0.4500 |
| $f(t) = t^2 + t + 1$ | 0.0118 | 0.0618 | 0.0890 |

Tablo7.t=5 için farklı kesir derecelerinin $f(t)$ fonksiyon değerleri

| $t = 5$ için | Fonksiyonlar |
| :--- | :--- |
| | $f(t) = e^t$ | $f(t) = \sin(t)$ | $f(t) = t$ | $f(t) = t^2 + t + 1$ |
| Kesir Derecesi | | | | |
| $D^{0.5}$ | 118,0080 | -0,6878 | 2,4609 | 18,2929 |
| $D^{0.8}$ | 102,8322 | -0,4086 | 1,4784 | 12,8719 |
| $D^{1.0}$ | 93,8150 | -0,2021 | 1 | 10 |
| $D^{1.2}$ | 85,5893 | 0,0073 | 0,6384 | 7,6352 |
| $D^{1.5}$ | 74,5852 | 0,3057 | 0,2734 | 4,8945 |

2.3 Laplace'ın Kuvvet Fonksiyonları Türev Genelleştirmesi

Lacroix tarafından 1982'de yazılan eserinde Laplace'ın kesir dereceli türevinin basit bir
tanımı olduğu yazılmaktadır. Burada $y = t^m$ kuvvet fonksiyonunun türevini ele alarak bir
genelleme yapılmasına çalışılmıştır[17]. Bu yöntem, kuvvet serisi açılımlarının bilinen fonksiyonlar
için çözümü üretebilmektedir. $y = t^m$nm mertebesi tamsayıi derece türevleri için denklem6'daki
eşitlik kullanılmıştır.

$$\frac{d^ny}{dt^n} = \frac{m!}{(m-n)!}t^{m-n} \tag{6}$$

Denklem6'daki eşitlikten yola çıkarak kuvvet fonksiyonunun $n$ türevi için gamma fonksiyonu
denklem7'deki gibi elde edilmiştir.

$$\frac{d^ny}{dt^n} = \frac{\Gamma(m+1)}{\Gamma(m-n+1)}t^{m-n} \tag{7}$$

$m$ven 'nin reel sayısı olması durumunda sürekli gamma fonksiyonu ile faktöriyel hesabının
mümkün olduğu önerilirse, $y = t^m$ifadesinin $\alpha \in R$ için kesir dereceli türevi bu genelleme
yardımı ile denklem8'deki gibi ifade edilmiştir.

$$D^\alpha y(x) = \frac{d^\alpha}{dt^\alpha}x^m = \frac{\Gamma(m+1)}{\Gamma(m-\alpha+1)}t^{m-\alpha} \tag{8}$$

Birçok temel fonksiyon, kuvvet serisi açılımları olarak gösterilebilmektedir. Bu fonksiyonlardan
bazılarının kuvvet serisi açılımları aşağıdaki gibidir.

$f(t) = e^t$ kuvvet serisi formunda denklem9'daki gibi ifade edilmiştir.

$$y = e^t = \sum_{k=0}^{\infty} \frac{t^k}{k!} = 1 + t + \frac{t^2}{2!} + \frac{t^3}{3!} \dots \dots \dots \tag{9}$$
```