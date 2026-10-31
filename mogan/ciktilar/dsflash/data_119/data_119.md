Tablo 6'da örnekleme periyodunun çözüm doğruluğuna etkisi incelenmiştir. Çözümün örnekleme periyodu ts azaldıkça yöntemin doğruluğunun arttığı görülmektedir. Tablo 6'da 5 inci saniye için türev değerleri verilmiştir.

Tablo 6.Farklı örnekleme periyotları için (ts) GL ortalama hata sonuçları

<table>
  <thead>
    <tr>
      <th></th>
      <th>ts=0.1, t:0:20</th>
      <th>ts=0.5, t:0:20</th>
      <th>ts=1, t:0:20</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>\(f(t) = e^t\)</td>
      <td>0.0508</td>
      <td>0.2822</td>
      <td>0.5529</td>
    </tr>
    <tr>
      <td>\(f(t) = \sin(t)\)</td>
      <td>0.0578</td>
      <td>3.3335</td>
      <td>-0.52798</td>
    </tr>
    <tr>
      <td>\(f(t) = t\)</td>
      <td>4.9738e⁻¹⁵</td>
      <td>0.20008</td>
      <td>0.4500</td>
    </tr>
    <tr>
      <td>\(f(t) = t^2 + t + 1\)</td>
      <td>0.0118</td>
      <td>0.0618</td>
      <td>0.0890</td>
    </tr>
  </tbody>
</table>

Tablo7.\(t = 5\) için farklı kesir derecelerin \(f(t)\) fonksiyon değerleri

<table>
  <thead>
    <tr>
      <th rowspan="2">\(t = 5\) için</th>
      <th rowspan="2">Kesir Derecesi</th>
      <th colspan="4">Fonksiyonlar</th>
    </tr>
    <tr>
      <th>\(f(t) = e^t\)</th>
      <th>\(f(t) = \sin(t)\)</th>
      <th>\(f(t) = t\)</th>
      <th>\(f(t) = t^2 + t + 1\)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="5"></td>
      <td>\(D^{0.5}\)</td>
      <td>118,0080</td>
      <td>-0,6878</td>
      <td>2,4609</td>
      <td>18,2929</td>
    </tr>
    <tr>
      <td>\(D^{0.8}\)</td>
      <td>102,8322</td>
      <td>-0,4086</td>
      <td>1,4784</td>
      <td>12,8719</td>
    </tr>
    <tr>
      <td>\(D^{1.0}\)</td>
      <td>93,8150</td>
      <td>-0,2021</td>
      <td>1</td>
      <td>10</td>
    </tr>
    <tr>
      <td>\(D^{1.2}\)</td>
      <td>85,5893</td>
      <td>0,0073</td>
      <td>0,6384</td>
      <td>7,6352</td>
    </tr>
    <tr>
      <td>\(D^{1.5}\)</td>
      <td>74,5852</td>
      <td>0,3057</td>
      <td>0,2734</td>
      <td>4,8945</td>
    </tr>
  </tbody>
</table>

2.3 Laplace'ın Kuvvet Fonksiyonları Türev Genelleştirmesi

Lacroix tarafından 1982'de yazılan eserde aslında Laplace'ın kesir dereceli türevinin basit bir tanımı olduğu yazılmaktadırve bu çalışmada,\(y = t^m\) kuvvet fonksiyonun türevini ele alarak bir genelleme yapılmaya çalışılmıştır[17]. Bu yöntem, kuvvet seri açılımlarılabilen fonksiyonlar için çözümler üretilebilmektedir. \(y = t^m\)nin. mertebe tamsayı derece türevleri için denklem6'daki eşitlik kullanılmıştır.

\[
 \frac{d^n y}{dt^n} = \frac{m!}{(m-n)!} t^{m-n} \qquad (6) 
\]

Denklem6'daki eşitlikten yola çıkarak kuvvet fonksiyonunun \(n\). türevi için gamma fonksiyonu denklem7'deki gibi elde edilmiştir.

\[
 \frac{d^n y}{dt^n} = \frac{\Gamma(m+1)}{\Gamma(m-n+1)} t^{m-n} \qquad (7) 
\]

\(m\) ven 'nin reel sayı olması durumunda sürekli gamma fonksiyonu ile faktöriyel hesabının mümkün olduğu önerilirse, \(y = t^m\)ifadesinin \(\alpha \in R\) için kesir dereceli türevi bu genelleme yardımı ile denklem8'deki gibi ifade edilmektedir.

\[
 D^\alpha y(x) = \frac{d^\alpha}{dt^\alpha} x^m = \frac{\Gamma(m+1)}{\Gamma(m-\alpha+1)} t^{m-\alpha} \qquad (8) 
\]

Birçok temel fonksiyon, kuvvet seri açılımları olarak gösterilebilmektedir. Bu fonksiyonlardan bazılarının kuvvet seri açılımları aşağıdaki gibidir.

\(f(t) = e^t\)kuvvet serisi formunda denklem9'daki gibi ifade edilmektedir.

\[
 y = e^t = \sum_{k=0}^{\infty} \frac{t^k}{k!} = 1 + t + \frac{t^2}{2!} + \frac{t^3}{3!} \dots \dots \qquad (9) 
\]