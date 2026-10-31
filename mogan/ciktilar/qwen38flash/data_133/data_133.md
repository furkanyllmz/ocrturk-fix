```markdown
-Düzleştirme Katmanı (Flattening Layer): Matris verilerini tek sıralı girişlere dönüştürerek klasik sinir ağı modelleri için hazırlar.
-Tam Bağlantılı Katman (Fully-Connected Layer): Öğrenme sürecini kolaylaştırmak için ağırlıkları ve önyargıları ayarlar.

<!-- Image (116, 202, 854, 388) -->

Şekil 3.2 Çalışmada kullanılan CNN modeli ve veri setinin akış şeması

Model, üretilen 1000 sentetik görüntüden oluşan veri seti üzerinde yinelenmeli olarak eğitilmiştir. CNN algoritmasının eğitimi sırasında gerekli hiperparametreler optimize edilmiştir ve bu değerler Tablo 3.1'de sunulmaktadır. Modelin genelleştirme yeteneğini değerlendirmek ve aşırı öğrenme (overfitting) sorunlarını tespit etmek amacıyla, eğitilmiş model doğrulama ve test veri setleri üzerinde test edilmiştir. Bu adımlar, modelin genel performansını ve genelleme kapasitesini değerlendirmek açısından önemlidir.

Tablo 3.1 CNN modelinde optimize edilen hiperparametreler
<!-- Table (119, 713, 833, 966) -->
\begin{tabular}{ll}
\hline
\textbf{Katman Adı} & \textbf{Hiperparametreler} \\
\hline
2D Convolution\_1 & Number of filters:32, Size of kernels: \\
& 3x3, Strides:1x1, Activation: ReLU, \\
2D Convolution\_2 & Number of filters 64, Size of kernels: \\
& 3x3, Strides:1x1, Activation: ReLU \\
2D Max\_pooling & Size of pooling: 2 x 2, Strides: 2x2 \\
\hline
\end{tabular}
```