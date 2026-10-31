**3. Sonuçlar ve Tartışmalar (Results and Discussions)**

Derlemin LSTM, GRU ve Transformatör mimarisi tabanlı kodlayıcı-kod çözücü modelle 25 dönem boyunca eğitilmesi sonucu, kayıp fonksiyonu değerleri Şekil 8’de gösterilmiştir. Kayıp fonksiyonu, derin öğrenme mimarilerinde eğitim esnasında hedef ile model tarafından tahmin edilen çıktı arasındaki hatanın hesaplanarak en aza indirilmesini amaçlayan araçtır [25]. Yani hedef ile tahmin arasındaki gradyan eğiminin hesaplanmasıdır. Bu çalışmada eğitim esnasındaki kayıp fonksiyon değerleri LSTM, GRU ve Transformatör mimarileri için sırasıyla $1,03$, $0,55$ ve $2,49$ olarak ölçülmüştür.

Eğitilen model ile derlemdeki doğrulama için ayrılan haberler kullanılarak, bu haberlere başlık üretilmeye çalışılmıştır. Eğitime girmeyen doğrulama verileri ile sistem tarafından üretilen başlıklardan iki tanesi, orijinal haber ve başlık metinleriyle birlikte eğitilen modeller kullanılarak oluşturulan yeni başlıkların gösterildiği Tablo 7 ve Tablo 8’de örnek olarak verilmiştir. Çalışmanın değerlendirmesinde özellikle metin özetleme problemlerinde kullanılan ROUGE ölçüm metriği kullanılmıştır. Eş. 4’teki Rouge Recall değeri BLEU metriği olarak, Eş. 5’teki Rouge Precision değeri ROUGE metriği olarak değerlendirilmektedir. Eş. 6’daki Rouge F1 Score değeri ise ROUGE ve BLEU değerlerinin harmonik ortalaması ile elde edilmektedir [32]. Bu metrikler hesaplanırken TorchMetric kütüphanesindeki ilgili modül kullanılmıştır [33].

$$\text{Rouge Recall} = \frac{\text{Çakışan Sözcük Sayısı}}{\text{Referans Başlıktaki Toplam Sözcük Sayısı}} \eqno(4)$$

$$\text{Rouge Precision} = \frac{\text{Çakışan Sözcük Sayısı}}{\text{Sistemin Ürettiği Başlıktaki Toplam Sözcük Sayısı}} \eqno(5)$$

$$\text{Rouge F1 Score} = 2 * \frac{\text{Rouge Recall} \times \text{Rouge Precision}}{\text{Rouge Recall} + \text{Rouge Precision}} \eqno(6)$$

Derlemden doğrulama için ayrılan veriler kullanılarak, genel olarak özetleme görevlerinin başarının ölçülmesi için kullanılan ROUGE-

![Graph showing loss function values over training epochs for LSTM, GRU, and Transformer models](https://cdn-uploads.huggingface.co/production/uploads/66a2f6e8d8b8f8f8f8f8f8f8/image.png)
*Şekil 8. Modelin eğitim doğruluk oranı (Training accuracy rate of the model)*

**Tablo 7.** Doğrulama verisi ile üretilen başlık-1 (Headline produced with validation data-1)

<table>
  <tr>
    <td>Haber</td>
    <td>Erzurum'da iki siyasi parti taraftarları arasında çıkan olayda 3 kişi ile olaya müdahale eden 1 polis yaralandı. Dün akşam saatlerinde Yakutiye ilçesi Mahallebaşı semtinde ticari taksiyle tur atarak bir partinin sembol işaretini yaptığı ile sürülen taksici, karşıt parti taraflarının saldırısına uğradı. Bunun üzerine kaçmaya çalışan taksici ve yanındakilerle karşı taraf arasında taşlı sopalı kavga yaşandı. Olay yerine gelen polis, yaklaşık 50 kişinin karıştığı olaya müdahale etti. Soruşturma başlatılan olayda yaralanan 3 kişi ile polis, hastaneye kaldırıldı.</td>
  </tr>
  <tr>
    <td>Başlık</td>
    <td>Erzurum’da Tehlikeli Gerginlik</td>
  </tr>
  <tr>
    <td colspan="2">Üretilen başlıklar</td>
  </tr>
  <tr>
    <td>LSTM</td>
    <td>pkk lılar mezarlığa bile patlatıcı döşemiş</td>
  </tr>
  <tr>
    <td>GRU</td>
    <td>Erzurum da ak partili başkan in acı haberi</td>
  </tr>
  <tr>
    <td>Transformatör</td>
    <td>ak parti seçim aracına saldırı ### yaralı</td>
  </tr>
</table>

**Tablo 8.** Doğrulama verisi ile üretilen başlık-2 (Headline produced with validation data-2)

<table>
  <tr>
    <td>Haber</td>
    <td>Adana'da cinsel ilişki isteğini reddeden eski çalışma arkadaşı 27 yaşındaki Ayça Tekin'i öldürdüğü iddiasıyla yargılanan 20 yaşındaki Abdullah Koyuncu, ömür boyu hapis cezasına çarptırılırken, herhangi bir ceza indirimi uygulanmadı.</td>
  </tr>
  <tr>
    <td>Başlık</td>
    <td>Ayça'nın Katiline İndirimsiz Müebbet</td>
  </tr>
  <tr>
    <td colspan="2">Üretilen başlıklar</td>
  </tr>
  <tr>
    <td>LSTM</td>
    <td>hamile kadına şiddete karşı sağır ya da vardır</td>
  </tr>
  <tr>
    <td>GRU</td>
    <td>hastanede taciz iddiasına soruşturma</td>
  </tr>
  <tr>
    <td>Transformatör</td>
    <td>cinsel saldırıya ### yıl hapis cezası</td>
  </tr>
</table>