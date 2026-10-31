```html
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>Kaynak</th>
      <th>Büyüklük</th>
      <th>Türkçe içerik</th>
      <th>Açıklama</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Common Crawl<sup>1</sup></td>
      <td>yaşlık 3.15 milyar web sayfası (380 TiB) [8]</td>
      <td>%0.7897 [9]</td>
      <td>Kâr amacı gütmeyen kuruluş.</td>
    </tr>
    <tr>
      <td>BookCorpus [10]</td>
      <td>11,000 kitap, 985 milyon kelime.</td>
      <td>bilinmiyor</td>
      <td>OpenAI'nın ilk GPT modeli için kullanıldı.</td>
    </tr>
    <tr>
      <td>C4 ve T5 [11]</td>
      <td>745 GB.</td>
      <td>Sadece İngilizce veri.</td>
      <td>Common Crawl verisinin temizlenmiş hali. Google tarafından yayımlanmıştır.</td>
    </tr>
    <tr>
      <td>Openwebtext</td>
      <td>8 milyon doküman, 38GB veri.</td>
      <td>Sadece İngilizce veri.</td>
      <td>GPT-2'nin eğitildiği Webtext'e alternatif olarak hazırlanmıştır.</td>
    </tr>
    <tr>
      <td>RedPajama [12]</td>
      <td>1.2 Trilyon belirtke.</td>
      <td>bilinmiyor</td>
      <td>Diger büyük kaynaklardan veriseti oluşturmayı sağlayan proje.</td>
    </tr>
    <tr>
      <td>Vikipedi</td>
      <td>731 MB.</td>
      <td>Sadece Türkçe veri.</td>
      <td>Bu çalışmada kullanılmamıştır.</td>
    </tr>
  </tbody>
</table>

Tablo 1: Açık erişimli metin kaynakları.

tilmiş T5, BERT, BART, GPT-2 ve BLOOM gibi önemli modeller yer almaktadır.

**Türkçe metinlerden veriseti oluşturma.** Hali hazırda açık erişimle sunulan verisetlerinde Türkçe içeriğin hiç olmaması ya da çok az yer alması nedeniyle büyük dil ağları araştırmalarında kullanmak üzere sıfırdan bir veriseti oluşturmak elzem olmaktadır. Bu çalışmada yer alan deneyleri yürütmek için böyle bir veriseti sadece Vikipedi (Wikipedia Türkçe sürümü) makaleleri kullanılarak gerçekleştirilmiştir. Bunun için, güncel ve sıkıştırılmış trwiki² arşivi indirilmiş ardından bir Python betiği yardımıyla json formatında verisete oluşturulmuştur. 731 MB büyüklüğündeki bu veride ön işleme ve temizlik yapıldıktan sonra farklı uzunluklarda toplam 818.454 adet metin elde edilmiştir. Bu metinler, tiktoken modülü [16] ile belirtkeleştirilince 296.1 milyon adet belirtke oluşmuştur. Bu sonuç GPT-2 modelinin de belirtkeleştirildiği 50 bin ögeden oluşan r50k_base dil kodlaması kullanıldığında elde edilen sayıdır. GPT-3.5 ve GPT-4'te kullanılan 100 bin ögeli c1100k_base kullanılacak olursa oluşan sayı 242.6 milyon olmaktadır. Bunun Türkçe için daha uygun olduğu düşünülebilir.

**Belirtkeleştirme (Tokenization)** Sözcüksel analizde bir girdi metni oluştururan parçaların sınıflandırılması ve ayırt edilmesi işlemidir. Oluşturulan belirtkeler takip eden bir başka işleme kullanılırlar. Girdi verisettinden yer alan bütün veri belirtkelere ayrılarak bir sözvarlığı seti oluşturulur. Büyük dil modellerinin eğitilmesinde kullanılan verisetleri üzerinde çoğunlukla Byte-Pair Encoding (BPE) belirtkeleştirme algoritması uygulanmaktadır.

## 3 Modellerinin eğitimleri ve ince ayarlanmaları

**Açık erişimli büyük dil modelleri.** Ticari büyük dil modelleri dışında bazı şahıs ve kurumlar tarafından kaynagı paylaşılan büyük dil modelleri mevcuttur. Bunlar arasında, Meta şirketı tarafından yayımlanan LLaMa [17] modelinin 7, 13, 33 ve 65 milyar parametre içeren varyantları bulunmaktadır. Bu modeller 1 ve 1.4 trilyon belirtke (token) ile eğitilmiştir. Malesef eğitim verisette yer alan 20

<sup>2</sup>https://dumps.wikimedia.org/trwiki/20230520/
```