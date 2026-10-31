# Geometri

\[\varepsilon_r(\omega) = \varepsilon_\infty + \frac{\varepsilon_s}{1 + (\omega \tau)^2}\]
\[\sigma(\omega) = \omega^2 \tau \varepsilon_0 \frac{\varepsilon_s - \varepsilon_\infty}{1 + (\omega \tau)^2} + \sigma_s\]

(2)  
(3)  

Meme katmanlarının ve tümörün birinci-dereceden Debye formülasyonu için karakteristik parametreleri Çizelge 2’de gösterilmiştir.

## Çizelge 2. Birinci-dereceden Debye parametreleri

[13]

| Parametreler    | \(\varepsilon_\infty\) | \(\varepsilon_s\) | \(\sigma_s\) |
|---|---|---|---|
| Deri (Skin)    | 15,3    | 40,1    | 0,4    |
| Yağ Tabakası (Adipose) | 3,18    | 5,02    | 0,043    |
| Fibroglandular    | 16,8    | 36,7    | 0,461    |
| **Tümör (Tumor)**    | 18,8    | 46,8    | 0,803    |

Şekil 2’de gösterilen meme katmanlarının geometrisi MATLAB’da uygulanmış ve COMSOL Multifiz kramarına aktarılmıştır. Bağlı dielektrik ve iletkenlik fonksiyonları (2) ve (3) nolu eşitliklerde olduğu gibi COMSOL’da analitik olarak tanımlanmışlardır. Sonuç olarak; MATLAB’da yazılan FDFD kodunun sonuçları ile COMSOL’da üretilen sonuçlar karşılaştırılmıştır ve nümerik sonuçlar elde edilmiştir.

Meme kanseri tedavisi için örnek bir meme oluşturarak bunun dielektrik özelliklerinin ölçümüyle ilgili bir çalışma yapılmıştır [15]. Birçok örnek modeller tümörün ve normal dokunun belirgin tanımlarını içermezler. Bu çalışma meme kanseri tedavisinde hipertermi için Şekil 3’de gösterilen somut bir meme-tümör örneği önermiştir. Bu somut meme ve tümör örneklerinin nasıl yapıldığına ilgili ayrıntılı bilgi ilgili çalışmada anlatılmıştır [15]. Ölçümler dielektrik spektroskopi metodu kullanılarak elde edilmiştir [10]. Dielektrik sabiti ve elektriksel iletkenlik ölçümleri, E5071B ENA Series Network Analyzer ve 85070 Dielectric Probe Kit kullanılarak gerçekleştirilmiştir. Dielectric Kit