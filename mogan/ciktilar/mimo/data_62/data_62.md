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
        <strong>Kullanıcı:</strong> Gökyüzü karanlık mı?<br>
        <strong>Model:</strong> Evet<br>
        <strong>Kullanıcı:</strong> Sokakta ne var?<br>
        <strong>Model:</strong> Araba<br>
        <strong>Kullanıcı:</strong> Caddede otobüs var mı?<br>
        <strong>Model:</strong> Hayır<br>
        <strong>Kullanıcı:</strong> Trafik sinyali sağda mı yoksa solda mı?<br>
        <strong>Model:</strong> Sol
      </td>
      <td>
        <strong>Kullanıcı:</strong> Kitabın ismini öngörebilir miyim?<br>
        <strong>Model:</strong> Masumiyet Müzesi<br>
        <strong>Kullanıcı:</strong> Bu kitap hangi türde bir kitaptır?<br>
        <strong>Model:</strong> Aşk romanı<br>
        <strong>Kullanıcı:</strong> Bu kitabın yazarı kimdir?<br>
        <strong>Model:</strong> Orhan Pamuk
      </td>
      <td>
        <strong>Kullanıcı:</strong> Lütfen bu bölge için kısa bir açıklama yapınız: [0.69, 0.35, 0.79, 0.69].<br>
        <strong>Model:</strong> Bu bir insan.<br>
        <strong>Kullanıcı:</strong> Lütfen bu cümlenin tanımladığı bölgenin sınırlayıcı kutu koordinatlarını verin: tenis kortundaki beyaz çizgi.<br>
        <strong>Model:</strong> [0.0, 0.7, 0.9, 0.82]
      </td>
      <td>
        <strong>Kullanıcı:</strong> Lütfen bu bölge için kısa bir açıklama yapınız: [0.3, 0.36, 0.62, 0.59].<br>
        <strong>Model:</strong> Fotoğrafa bakan bir bilgisayar ekranı.<br>
        <strong>Kullanıcı:</strong> Lütfen bu cümlenin tanımladığı bölgenin sınırlayıcı kutu koordinatlarını verin: en sağdaki ekran.<br>
        <strong>Model:</strong> [0.3, 0.36, 0.62, 0.59]
      </td>
      <td>
        <strong>Kullanıcı:</strong> Sunulan görüntüyü temsil eden kompakt bir anlatım oluşturun.<br>
        <strong>Model:</strong> çiftler için toplu nikah töreni düzenlendi.
      </td>
    </tr>
    <tr>
      <td><img src="gqa_image.jpg" alt="GQA image"></td>
      <td><img src="cosmosvqa_image.jpg" alt="CosmosVQA image"></td>
      <td><img src="vg_image.jpg" alt="VG image"></td>
      <td><img src="coco_image.jpg" alt="COCO image"></td>
      <td><img src="cc3m_image.jpg" alt="CC3M image"></td>
    </tr>
  </tbody>
</table>

<img src="loss_graphs.jpg" alt="Loss Graphs">
Şekil 1: Eğitimlere Ait Loss Grafikleri

<img src="lr_scheduler.jpg" alt="Learning Rate Scheduler">
Şekil 2: İnce Ayar Eğitimde Learning Rate'in Değişimi

A. Hakem: Dil Modeli

Bu çalışmanın yapıldığı Ağustos 2024 tarihinde çoğu ölçüme göre en iyi dil modeli olan OpenAI'ın GPT-4o [15] modeli hakem olarak kullanılmıştır. Sorular, resimler ve modellerin verdikleri cevaplar hakem olarak belirlenen GPT-4o modeline verilerek modelin yanıtına ne kadar doğru olduğuna göre 100 üzerinden bir puan vermesi istenmiştir. GPT-4o'ya puanlatmak için kullanılan talimat formatı aşağıdaki gibidir:

{görsel}
Soru: {soru}
Cevap: {model-cevabı}

Bir görsel, görselle ilgili bir soru ve verilen cevap gösterilmiştir. Çok iyi kaliteli cevaplara 100, iyilere 80, ortalamalara 30, kötülere 0 puan ver. Sadece puanı tam sayı olarak yaz, hiçbir açıklama yapma.

Ardından GPT-4o'nun verdiği yanıt ile modelin o soruya ne kadar iyi yanıt verebildiği 100 üzerinden bir puan ile ölçülmüştür. GPT-4o modelinin yanıtları deterministik olmaması ve aynı cevaba farklı puanlar verilebilmesi nedeniyle her soru için 5 kez değerlendirme yapılarak bu değerlendirmelerde verilen puanların ortalaması alınmasıdır.

Bu puanlama için kullanılan test kümesi 4 alt kümeden oluşmaktadır: OCR, Kompleks, Tanımlama ve Detay. Bu kümelerin içeriği aşağıda açıklanmıştır:

*   **OCR:** Toplam 10 kitap içeren bu veri kümesi, her kitap için gerçek hayatta çekilmiş bir adet fotoğraf ile bir dijital kapak görselini içermektedir. Veri kümesi, kitabın kapağında yer alan yazıların ne olduğunu sorulayan 20 sorudan oluşmaktadır.
*   **Kompleks:** Bu kategori, modelin görsel içeriklere dayanarak üst düzeyde akıl yürütme ve çıkarımlar