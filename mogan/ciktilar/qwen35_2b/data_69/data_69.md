```markdown
# 2.2. ROI Algılaması (ROI Detection)

Önerilen yöntem üç ana görevi içermektedir: görüntü iyileştirmesi, öznelik çıkarımı ve sınıflandırmaya. Mamogramların düşük görüntü kalitesini iyileştirmek ve belirsiz tümör bölgelerini daha belirgin yapmak için, orijinal mamogram görüntüleri üzerinde görüntü iyileştirme teknikleri kullanılmıştır. Öznelik çıkarımı, iyileştirilmiş mamogram görüntülerinden elde edilen görüntülere uygulanmıştır. Bir sonraki adımda, bir sınıflandırcı, seçilen bölgeyi temsil eden özneliklerin bir ROI'ye veya sağlığa bir dokuya ait olup olmadına karar vermiştir. Önerilen yöntemin adımlarını özetleyen bir akış diyagramı Şekil 2'de gösterilmiştir.

## Şekil 2. Önerilen ROI algılama yönteminin akış diyagramı

<!-- Image (100, 100, 800, 700) -->

## 2.3. Görüntü İyileştirmesi (Image Enhancement)

Mamogramdaki tümör bölgelerini vurgulamak için bir takım görüntü geliştirme teknikleri denemiştir. Bu teknikler: histogram denklemştirme, genişleme süzgeci (dilation) ve CLAHE işlemleridir (Şekil 3). Görüntü iyileştirme işlemlerini uygulamak için Python'un OpenCV kütüphaneleri kullanılmıştır (Bradski vd., 2008).

## Şekil 3. Orijinal mamogram ve görüntü iyileştirme teknikleri uygulanan mamogramlar (a) orijinal mamogram (b) histogram denklemştirme uygulanan mamogram (c) genişleme süzgeci uygulanan mamogram (d) CLAHE uygulanan mamogram

## 2.3.1 Histogram Denklemştirme (Histogram Equalization)

Evrensel karşıtlığı ayarlamak için histogram eşitleme kullanılmıştır. Histogram denklemştirme için, öncelikle histogramdan yararlanılarak aşağıdaki gibi birikimli histogramlar çıkarılmaktadır:

$$s_k = T(r_k) = \frac{L - 1}{MN} \sum_{i=0}^{k} n_i \quad (1)$$
```