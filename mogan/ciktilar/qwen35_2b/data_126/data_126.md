```markdown
# 3. Sonuçlar ve Tartışmalar (Results and Discussions)

Derlemin LSTM, GRU ve Transformör mimarisi tabanlı kodlayıcı-közümlü modelde 25 dönem boyunca eğitilmesi sonucu, kayıp fonksiyonu değerleri Şekil 8'de gösterilmiştir. Kayıp fonksiyon, derin öğrenme mimarilerinde eğitim esnasında hedef ile model tarafından tahmin edilen çıktı arasındaki hatanın hesaplanarak en aza indirilmesini amaçlayan araçtır [25]. Yani hedef ile tahmin arasındaki gradyan eğiminin hesaplanmasıdır. Bu çalışmada eğitim esnasındaki kayıp fonksiyon değerleri LSTM, GRU ve Transformör mimarileri için sırasıyla 1,03, 0,55 ve 2,49 olarak ölçülmüştür.

Eğitilen model ile derlemdeki doğrulama için ayrılan haberler kullanılarak, bu haberlere başlık üretmeye çalışılmıştır. Eğitime girmeyen doğrulama verileri ile sistem tarafından üretilen başlıklarından iki tanesi, original haber ve başlık metinleriyle birlikte eğitilen modellerle birlikte oluşturulmuş yeni başlıkların gösterildiği Tablo 7 ve Tablo 8'de örnek olarak verilmiştir. Çalışmanın

değerlendirmesinde özellikle metin düzenleme problemlerinde kullanılan ROUGE ölçüm metriği kullanılmıştır. Eş. 4'teki Rouge Recall değeri BLEU metriği olarak, Eş. 5'teki Rouge Precision değeri ROUGE metriği olarak değerlendirilmiştir. Eş. 6'daki Rouge F1 Score değeri ise ROUGE ve BLEU değerlerinin harmonik ortalaması ile elde edilmiştir [32]. Bu metrik hesaplanırken TorchMetric kutuphanesindeki ilgili modül kullanılmıştır [33].

$$
\begin{aligned}
\text{Rouge Recall} &= \frac{\text{Çağışan Sözcük Sayısı}}{\text{Referans Başlıktağı Toplam Sözcük Sayısı}} \\
\text{Rouge Precision} &= \frac{\text{Çağışan Sözcük Sayısı}}{\text{Sistem Üretildiği Başlıktağı Toplam Sözcük Sayısı}} \\
\text{Rouge F1 Score} &= 2 * \frac{\text{Rouge Recall} \times \text{Rouge Precision}}{\text{Rouge Recall} + \text{Rouge Precision}}
\end{aligned}
$$

Derlemeden doğrulama için ayrılan veriler kullanılarak, genel olarak özetleme görevinin başarımının ölçülmesi için kullanılan ROUGE-

## Tablo 7. Doğrulama verisi ile üretilen başlık-1 (Headline produced with validation data-1)

| | |
| :--- | :--- |
| **Haber** | Erzurum'da iki siyasi parti taraftarları arasında çıkan olayda 3 kişi ile olaya müdahale eden 1 polis yaralandı. Dün akşam saatlerinde Yakutiye ilçesi Mahallebaşı semtinde ticari taksisi tur atarak bir partinin sembol işareti yaptığı ileride sürülen taksici, karış parti taraftarlarının saldırısına uğradı. Bunun üzerine kaçmaya çalışan taksici ve yanındakikiler ile karış taraf arasında taşlı sopalı kavga yaşandı. Olay yerine gelen polis, yaklaşık 50 kişinin karıştıği olaya müdahale etti. Soruşturma başlatılan olayda yaralanan 3 kişi ile polis, hastaneye kaldırıldı. |
| **Başlık** | Erzurum'da Tehlikeli Gerginlik |
| **Üretilen başlıklar** | |
| | **LSTM** | pkk ıllar mezarlığa bile patlatıcı dösemiş |
| | **GRU** | Erzurum da ak parti başkanı in acı haberı |
| | **Transformör** | ak parti seçim aracına saldırı ### yaralı |

## Tablo 8. Doğrulama verisi ile üretilen başlık-2 (Headline produced with validation data-2)

| | |
| :--- | :--- |
| **Haber** | Adana'da cinsel ilişki isteği reddeden eski çalışma arkadaş 27 yaşındaki Ayça Tekin'in öldürdüğü iddiasıyla yargılan 20 yaşındaki Abdullah Koyuncu, ömür boyu hapis cezası çarptırılırken, herhangi bir ceza indirimi uygulanmadı. |
| **Başlık** | Ayça'nın Katiline indirimsiz Müebbet |
| **Üretilen başlıklar** | |
| | **LSTM** | hamile kadına şiddete karşı sağır ya da vardır |
| | **GRU** | hastanede taciz iddiasına soruşturma |
| | **Transformör** | cinsel saldırıya ### yıl hapis cezası |

```