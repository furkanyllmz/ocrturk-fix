```markdown
<!-- Image (136, 31, 483, 378) -->

**Şekil 2.** En içten en dışa doğru katmanlar; tümör, fibroglandüler, yağ tabakası (adipose) ve deri (skin). Bir anten, yayılımı yapan anten ve diğerleri de alıcılardır [13].

Elektromanyetik alan bileşenleri Maxwell'in denklemlerini sağlar ve her meme katmanındaki radyasyon şartı kompleks dielektrik özellikleri ile tanımlanır [13]. Meme tarafından saçılan alanlar bu geometrinin fonksiyonlarıdır. Bu elektromanyetik alanları elde etmek için sonlu elemanlar ileri çözümüsü olarak COMSOL Multifizik kullanılmıştır.

Çoklu-frekans inversiyon problemide, frekansa göre meme dokularının dielektrik özelliklerinin belirlenmesi gerekmektedir. Bu çalışmada, oluşturulan modele birinci dereceden veya ikinci dereceden Debye formülasyonu geniş bir şekilde uygulanmış [14] ve bu model ölçülen verinin denklem katsayılarına adapte edilmiştir. Birinci-dereceden Debye modeli aşağıdaki gibidir:

$$
\epsilon_{rc}(\omega) = \epsilon_r(\omega) + i\frac{\sigma(\omega)}{\omega\epsilon_0} = \epsilon_\infty + \frac{\epsilon_s - \epsilon_\infty}{1-i\omega\tau} + i\frac{\sigma_s}{\omega\epsilon_0} \quad (1)
$$

$\epsilon_{rc}$ bağlı kompleks dielektrik sabiti, $\omega$ açısal frekans, $\epsilon_r$ bağlı dielektrik sabiti, $\sigma$ iletkenlik, $\epsilon_0$ boş-uzay dielektrik sabiti, $\epsilon_\infty$ sonsuz frekansta bağlı dielektrik sabiti, $\tau$ zaman sabiti (relaxation time constant) ve $\sigma_s$ statik iletkenliktir. Burada, bağlı dielektrik ve iletkenlik aşağıdaki gibidir:

$$
\epsilon_r(\omega) = \epsilon_\infty + \frac{\epsilon_s}{1+(\omega\tau)^2} \quad (2)
$$

$$
\sigma(\omega) = \omega^2\tau\epsilon_0 \frac{\epsilon_s - \epsilon_\infty}{1+(\omega\tau)^2} + \sigma_s \quad (3)
$$

Meme katmanlarının ve tümörün birinci-dereceden Debye formülasyonu için karakteristik parametreleri Çizelge 2'de gösterilmiştir.

**Çizelge 2.** Birinci-dereceden Debye parametreleri [13]

<!-- Table (510, 292, 856, 459) -->
\begin{tabular}{|l|l|l|l|}
\hline
Parametreler & $\epsilon_\infty$ & $\epsilon_s$ & $\sigma_s$ \\
\hline
Deri (Skin) & 15,3 & 40,1 & 0,4 \\
\hline
Yağ Tabakası (Adipose) & 3,18 & 5,02 & 0,043 \\
\hline
Fibroglandüler & 16,8 & 36,7 & 0,461 \\
\hline
Tümör (Tumor) & 18,8 & 46,8 & 0,803 \\
\hline
\end{tabular}

Şekil 2'de gösterilen meme katmanlarının geometrisi MATLAB'a uygulanmış ve COMSOL Multifizik programa aktarılmıştır. Bağlı dielektrik ve iletkenlik fonksiyonları (2) ve (3) nolu eşitliklerde olduğu gibi COMSOL'da analitik olarak tanımlanmışlardır. Sonuç olarak; MATLAB'a yazılan FDFD kodunun sonuçları ile COMSOL'da üretilen sonuçlar karşılaştırılmıştır ve nümerik sonuçlar elde edilmiştir.

Meme kanseri tedavisi için örnek bir meme oluşturarak bunun dielektrik özelliklerinin ölçümüyle ilgili bir çalışma yapılmıştır [15]. Birçok örnek modeller tümörün ve normal dokunun belirlin tanımlarını içermezler. Bu çalışma meme kanseri tedavisinde hipertermi için Şekil 3'de gösterilen somut bir meme-tümör örneği önermiştir. Bu somut meme ve tümör örneklerinin nasıl yapıldığıyla ilgili ayrıntılı bilgi ilgili çalışmada anlatılmıştır [15]. Ölçümler dielektrik spektroskopi metodu kullanılarak elde edilmiştir [10]. Dielektrik sabiti ve elektriksel iletkenlik ölçümleri, E5071B ENA Series Network Analyzer ve 85070 Dielectric Probe Kit kullanılarak gerçekleştirilmiştir. Dielectric Kit
```