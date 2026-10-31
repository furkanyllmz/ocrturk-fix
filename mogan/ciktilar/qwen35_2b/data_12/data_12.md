```markdown
# Şekil 2. En içten en dışa doğru katmanlar; tüber, fibroglandular, yağ tabakası (adipose) ve deri (skin). Bir anten, yayılım yapan anten ve diğerleri de alınlardır [13].

time constant) ve $\sigma_{s}$ statik iletenliklidir. Burada, bağlı dielektrik ve iletken aşağıdaki gibidir:

$$
\begin{aligned}
\varepsilon_{r}(\omega) &= \varepsilon_{\infty} + \frac{\varepsilon_{s}}{1+(\omega\tau)^{2}} \\
\sigma(\omega) &= \omega^{2}\tau\varepsilon_{0}\frac{\varepsilon_{s}-\varepsilon_{\infty}}{1+(\omega\tau)^{2}} + \sigma_{s}
\end{aligned}
\tag{2}
\tag{3}
$$

Meme katmanlarının ve tüberün birinci-dereceden Debye formülasyonu için karakteristik parametreleri Çizelge 2'de gösterilmiştir.

## Çizelge 2. Birinci-dereceden Debye parametreleri [13]

| Parametreler | $\varepsilon_{\infty}$ | $\varepsilon_{s}$ | $\sigma_{s}$ |
| :--- | :---: | :---: | :---: |
| Deri (Skin) | 15,3 | 40,1 | 0,4 |
| Yağ Tabakası (Adipose) | 3,18 | 5,02 | 0,043 |
| Fibroglandular | 16,8 | 36,7 | 0,461 |
| Tüber (Tumor) | 18,8 | 46,8 | 0,803 |

Şekil 2'de gösterilen meme katmanlarının geometrisi MATLAB'da uygulanmış ve COMSOL Multizifik programına aktarılmıştır. Bağlı dielektrik ve iletken fonksiyonları (2) ve (3) nolü eşitliklerde olduğu gibi COMSOL'da analitik olarak tanımlanmışlardır. Sonuç olarak; MATLAB'da yazılan FFD kodunun sonuçları ile COMSOL'da üretilen sonuçlar karşılaştırılmıştır ve numrik sonuçlar elde edilmiştir.

Meme kanseri tedavisini için örnek bir meme oluşturarak bunun dielektrik özelliklerinin ölçümüyle ilgili bir çalışma yapılmıştır [15]. Birçok örnek modeller tüberün ve normal dokunun belirgin tanımları içermezler. Bu çalışma meme kanseri tedavisinde hipertermi için Şekil 3'de gösterilen somut bir meme-tüber örneği önemlidir. Bu somut meme ve tüber örneklerinin nasıl yapıldığıyla ilgili ayrıntılı bilgi ilgili çalışmada anlatılmıştır [15]. Ölçümler dielektrik spektroskopisi metodu kullanılarak elde edilmiştir [10]. Dielektrik sabiti ve elektrisel iletken ölçümleri, E5071B ENA Series Network Analyzer ve 85070 Dielectric Probe Kit kullanarak gerçekleştirilmiştir. Dielectric Kit

```