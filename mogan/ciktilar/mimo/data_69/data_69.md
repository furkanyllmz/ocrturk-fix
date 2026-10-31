bulunmaktadır.
**2.2. ROI Alınması (ROI Detection)**

Önerilen yöntem üç ana görevi içermektedir: görüntü iyileştirilmesi, öznitelik çıkarımı ve sınıflandırma. Mamogramların düşük görüntü kalitesini iyileştirmek ve belirsiz tümör bölgelerini daha belirgin yapmak için, orijinal mamogram görüntüleri üzerinde görüntü iyileştirme teknikleri kullanılmıştır. Öznitelik çıkarımı, iyileştirilmiş mamogram görüntülerinden elde edilen görüntülere uygulanmıştır. Bir sonraki adımda, bir sınıflandırıcı, seçilen bölgeyi temsil eden özniteliklerin bir ROI'ye veya sağlıklı bir dokuya ait olup olmadığına karar vermiştir. Önerilen yöntemin adımlarını özetleyen bir akış diyagramı Şekil 2'de gösterilmiştir.

```mermaid
flowchart TD
    A[Görüntülerin iyileştirilmesi] --> B[Mamogram alt bölgelerinin kesimi (ROI)]
    B --> C[2B-DWT]
    B --> D[MLP ve CNN ile sınıflandırma]
    C --> E[Tüm Wavelet bileşenleri]
    C --> F[Yakınsama Bileşeni]
    E --> G[Haralick Öznitelikleri]
    F --> H[HOG Öznitelikleri]
    G --> I[Öznitelik normalizasyonu (min-maks)]
    H --> I
    I --> J[Öznitelik seçimi - PCA]
    J --> K[Sınıflandırma - MLP]
```

**Şekil 2.** Önerilen ROI algılama yönteminin akış diyagramı

**2.3. Görüntü İyileştirilmesi (Image Enhancement)**

Mamogramdaki tümör bölgelerini vurgulamak için bir takım görüntü geliştirme teknikleri denenmiştir. Bu teknikler: histogram denkleştirme, genişleme süzgeci (dilation) ve CLAHE işlemleridir (Şekil 3). Görüntü iyileştirme işlemlerini uygulamak için Python'un OpenCV kütüphanesi kullanılmıştır (Bradski vd., 2008).

**Şekil 3.** Orijinal mamogram ve görüntü iyileştirme teknikleri uygulanmış mamogramlar (a) orijinal mamogram (b) histogram denkleştirme uygulanmış mamogram (c) genişleme süzgeci uygulanmış mamogram (d) CLAHE uygulanmış mamogram

**2.3.1 Histogram Denkleştirme (Histogram Equalization)**

Evrensel karşıtlığı ayarlamak için histogram eşitleme kullanılmıştır. Histogram denkleştirme için, öncelikle histogramdan yararlanarak aşağıdaki gibi birikimli histogramlar çıkarılmaktadır:

$$s_k = T(r_k) = \frac{L-1}{MN} \sum_{i=0}^{k} n_i \quad (1)$$