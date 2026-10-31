```html
<html><body>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th colspan="5">TABLO I: İnce ayar veri kümesinden örnekler</th>
    </tr>
    <tr>
      <th>GQA</th>
      <th>CosmosVQA</th>
      <th>VG</th>
      <th>COCO</th>
      <th>CC3M</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Kullanıcı: Gökyüzü karanlık mı? Model: Evet Kullanıcı: Sokakta ne var? Model: Araba Kullanıcı: Caddede otobüs var mı? Model: Hayır Kullanıcı: Trafik sinyali sağda mı yoksa solda mı? Model: Sol</td>
      <td>Kullanıcı: Kitabın ismini öğrenebilir miyim? Model: Masumiyet Müzesi Kullanıcı: Bu kitap hangi türde bir kitaptır? Model: Aşk romanı Kullanıcı: Bu kitabın yazarı kimdir? Model: Orhan Pamuk</td>
      <td>Kullanıcı: Lütfen bu bölge için kısa bir açıklama yapınız: [0.69, 0.35, 0.79, 0.69]. Model: Bu bir insan. Kullanıcı: Lütfen bu cümlenin tanımladığı bölgenin sınırlayıcı kutu koordinatını verin: tenis kortundaki beyaz çizgi. Model: [0.0, 0.7, 0.9, 0.82]</td>
      <td>Kullanıcı: Lütfen bu bölge için kısa bir açıklama yapınız: [0.3, 0.36, 0.62, 0.59]. Model: Fotoğrafçıya bakan bir bilgisayar ekranı. Kullanıcı: Lütfen bu cümlenin tanımladığı bölgenin sınırlayıcı kutu koordinatını verin: en sağdaki ekran. Model: [0.3, 0.36, 0.62, 0.59]</td>
      <td>Kullanıcı: Sunulan görüntüyü temsil eden kompakt bir anlattı oluşturun. Model: çiftler için toplu nikah töreni düzenlendi.</td>
    </tr>
  </tbody>
</table>
<div class="figure" style="text-align: center"><img/></div>
<div class="figure" style="text-align: center"><img/></div>
<p>Şekil 1: Eğitimlere Ait Loss Grafikleri</p>
<p>Şekil 2: İnce Ayar Eğitimde Learning Rate’in Değişimi</p>
<p>A. Hakem: Dil Modeli</p>
<p>Bu çalışmanın yapıldığı Ağustos 2024 tarihinde çoğu ölçüme göre en iyi dil modeli olan OpenAi’nin GPT-4o [15] modeli hakem olarak kullanılmıştır. Sorular, resimler ve modellerin verdikleri cevaplar hakem olarak belirlenen GPT-4o modeline verilerek modelin yanıtına kadar doğru olduğuna göre 100 üzerinden bir puan vermesi istenmiştir. GPT-4o’ya puanlattırmak için kullanılan talimat formatı aşağıdaki gibidir:</p>
<p>{görsel}</p>
<p>Soru: {soru}</p>
<p>Cevap: {model-cevabı}</p>
<p>Bir görsel, görselle ilgili bir soru ve verilen cevap gösteril-</p>
<p>mıştır. Çok iyi kaliteli cevaplara 100, iyilere 80, ortalamalara 30, kötülere 0 puan ver. Sadece puanı tam sayı olarak yaz, hiçbir açıklama yapma.</p>
<p>Ardından GPT-4o’nun verdiği yanıt ile modelin o soruya ne kadar iyi yanıt verebildiğini 100 üzerinden bir puan ile ölçül- miştir. GPT-4o modelinin yanıtları deterministik olmaması ve aynı cevaba farklı puanlar verilebilmesi nedeniyle her soru için 5 kez değerlendirme yapılarak bu değerlendirmelerde verilen puanların ortalaması alınmıştır.</p>
<p>Bu puanlama için kullanılan test kümesi 4 alt kümenden oluşmaktadır: OCR, Kompleks, Tanımlama ve Detay. Bu kümelerin içeriği aşağıda açıklanmıştır:</p>
<ul>
<li><p>OCR: Toplam 10 kitap içeren bu veri kümesi, her kitap için gerçek hayatta çekilmiş bir adet fotoğraf ile bir dijital kapak görselini içermektedir. Veri kümesi, kitabın kapagında yer alan yazıların ne olduğunu sor- gulayan 20 sorudan oluşmaktadır.</p></li>
<li><p>Kompleks: Bu kategori, modelin görsel içeriklere dayanarak üst düzeyde akıl yürütme ve çıkarımlar</p></li>
</ul>
</body></html>
```