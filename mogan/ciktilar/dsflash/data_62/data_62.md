TABLO I: İnce ayar veri kümesinden örnekler

<table>
  <thead>
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
      <td>
        <b>Kullanıcı:</b> Gökyüzü karanlık mı?<br>
        <b>Model:</b> Evet<br>
        <b>Kullanıcı:</b> Sokakta ne var?<br>
        <b>Model:</b> Araba<br>
        <b>Kullanıcı:</b> Caddede otobüs var mı?<br>
        <b>Model:</b> Hayır<br>
        <b>Kullanıcı:</b> Trafik sinyali sağda mı yoksa solda mı?<br>
        <b>Model:</b> Sol
      </td>
      <td>
        <b>Kullanıcı:</b> Kitabın ismini öğrenebilir miyim?<br>
        <b>Model:</b> Masumiyet Müzesi<br>
        <b>Kullanıcı:</b> Bu kitap hangi türde bir kitaptır?<br>
        <b>Model:</b> Aşk romanı<br>
        <b>Kullanıcı:</b> Bu kitabın yazarı kimdir?<br>
        <b>Model:</b> Orhan Pamuk
      </td>
      <td>
        <b>Kullanıcı:</b> Lüften bu bölge için kısa bir açıklama yapınız? [0.69, 0.35, 0.79, 0.69].<br>
        <b>Model:</b> Bu bir insan.<br>
        <b>Kullanıcı:</b> Lüften bu cümlenin tanımladığı bölgenin sınırlayıcı kutu koordinatını verin: tenis kortundaki beyaz çizgi.<br>
        <b>Model:</b> [0.0, 0.7, 0.9, 0.82]
      </td>
      <td>
        <b>Kullanıcı:</b> Lüften bu bölge için kısa bir açıklama yapınız? [0.3, 0.36, 0.62, 0.59].<br>
        <b>Model:</b> Fotoğrafçıya bakan bir bilgisayar ekranı.<br>
        <b>Kullanıcı:</b> Lüften bu cümlenin tanımladığı bölgenin sınırlayıcı kutu koordinatını verin: en sağdaki ekran.<br>
        <b>Model:</b> [0.3, 0.36, 0.62, 0.59]
      </td>
      <td>
        <b>Kullanıcı:</b> Sunulan görüntüyü temsil eden kompakt bir anlatı oluşturun.<br>
        <b>Model:</b> çiftler için toplu nikah töreni düzenlendi.
      </td>
    </tr>
  </tbody>
</table>

Şekil 1: Eğitimlere Ait Loss Grafikleri

Şekil 2: İnce Ayar Eğitimde Learning Rate’in Değişimi

A. Hakem: Dil Modeli

Bu çalışmanın yapıldığı Ağustos 2024 tarihinde çoğu ölçüme göre en iyi dil modeli olan OpenAI’in GPT-4o [15] modeli hakem olarak kullanılmıştır. Sorular, resimler ve modellerin verdikleri cevaplar hakem olarak belirlenen GPT-4o modeline verilerek modelin yanıta ne kadar doğru olduğuna göre 100 üzerinden bir puan vermesi istenmiştir. GPT-4o’ya puanlattırmak için kullanılan talimat formatı aşağıdaki gibidir:

{**görsel**}

**Soru:** {soru}

**Cevap:** {model-cevabı}

Bir görsel, görselle ilgili bir soru ve verilen cevap gösterilmiştir. Çok iyi kaliteli cevaplara 100, iyilere 80, ortalamalara 30, kötülere 0 puan ver. Sadece puanı tam sayı olarak yaz, hiçbir açıklama yapma.

Ardından GPT-4o’nun verdiği yanıt ile modelin o soruya ne kadar iyi yanıt verebildiği 100 üzerinden bir puan ile ölçülmüştür. GPT-4o modelinin yanıtları deterministik olmaması ve aynı cevaba farklı puanlar verebilmesi nedeniyle her soru için 5 kez değerlendirme yapılarak bu değerlendirmelerde verilen puanların ortalaması alınmıştır.

Bu puanlama için kullanılan test kümesi 4 alt kümeden oluşmaktadır: OCR, Kompleks, Tanımlama ve Detay. Bu kümelerin içeriği aşağıda açıklanmıştır:

*   **OCR:** Toplam 10 kitap içeren bu veri kümesi, her kitap için gerçek hayatta çekilmiş bir adet fotoğraf ile bir dijital kapak görselini içermektedir. Veri kümesi, kitabın kapağında yer alan yazıların ne olduğunu sorgulayan 20 sorudan oluşmaktadır.
*   **Kompleks:** Bu kategori, modelin görsel içeriklerle dayanarak üst düzeyde akıl yürütme ve çıkarımlar