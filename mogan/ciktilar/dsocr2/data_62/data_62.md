TABLO I: İnce ayar veri kümesinden örnekler

| GQA    | CosmosVQA    | VG    | COCO    | CC3M    |
|---|---|---|---|---|
| **Kullanıcı:** Gökyüzü karanlık mı?    | **Kullanıcı:** Kitabın ismini öğrenebilir miyim?    | **Kullanıcı:** Lütfen bu bölge için kısa bir açıklama yapınız: [0.69, 0.35, 0.79, 0.69].    | **Kullanıcı:** Lütfen bu bölge için kısa bir açıklama yapınız [0.3, 0.36, 0.62, 0.59].    | **Kullanıcı:** Sunulan görüntüyü temsil eden kompakt bir anlatı oluşturun.    |
| **Model:** Evet    | **Model:** Masumiyet Müzesi    | **Model:** Bu bir insan.    | **Model:** Fotoğrafçıya bakan bir bilgisayar ekranı.    | **Model:** çiftler için toplu nikah töreni düzenlendi.    |
| **Kullanıcı:** Sokakta ne var?    | **Kullanıcı:** Bu kitap hangi türde bir kitaptır?    | **Kullanıcı:** Lütfen bu cümlenin tanımladığı bölgenin sınırlayıcı kutu koordinatını verin: tenis kurtarındaki beyaz çizgi.    | **Kullanıcı:** Lütfen bu cümlenin tanımladığı bölgenin sıralayıcı kutu koordinatını verin: en sağdaki ekran.    |    |
| **Model:** Araba    | **Model:** Aşk romanı    | **Model:** [0.0, 0.7, 0.9, 0.82]    | **Model:** [0.3, 0.36, 0.62, 0.59]    |    |
| **Kullanıcı:** Caddele otobüs var mı?    | **Kullanıcı:** Bu kitabın yazar kimdir?    |    |    |    |
| **Model:** Hayır    | **Model:** Orhan Pamuk    |    |    |    |
| **Kullanıcı:** Trafik sinyali sağda mı yoksa sola mı?    |    |    |    |    |
| **Model:** Sol    |    |    |    |    |

---

### İnce Ayar Loss Grafiği

- **Layang-Layang (0.0, 0.0, 0.0, 0.0)**
- **Adım (0.0, 0.0, 0.0, 0.0)**

---

### İnce Ayar Learning Rate Scheduler

- **Learning Rate (0.0, 0.0, 0.0, 0.0)**

---

### Şekil 1: Eğitimlere Ait Loss Grafikleri

**Şekil 1: Eğitimlere Ait Loss Grafikleri**

**Şekil 1: Eğitimlere Ait Loss Grafikleri**

**Şekil 1: Eğitimlerle Ait Loss Grafikleri**

---

### A. Hakem: Dil Modeli

Bu çalışmanın yapıldığı Ağustos 2024 tarihinde çoğu ölçüme göre en iyi dil modeli olan OpenAI’ın GPT-4o [15] modeli hakem olarak kullanılmıştır. Sorular, resimler ve modellerin verdikleri cevaplar hakem olarak belirlenen GPT-4o modeline verilerek modelin yanıtı ne kadar doğru olduğuna göre 100 üzerinden bir puan vermesi istenmiştir. GPT-4o’ya puanlattırmak için kullanılan talimat formatı aşağıdaki gibidir:

- **görsel**

  **Soru:** {soru}

  **Cevap:** {model-cevabı}

  **Bir görsel, görselle ilgili bir soru ve verilen cevap gösteril**

---

### Şekil 2: İnce Ayar Eğitimde Learning Rate’in Değişimi

**Şekil 2: İnce Ayar Eğitimde Learning Rate’in Değişimi**

**Şekil 2: İnce Ayar Eğitimde Learning Rate’in Değişimi**

**Şekil 1: Eğitimlere Ait Loss Grafikleri**

**Şekil 1: Eğitimlere Ait Loss Grafikleri**

**Şekil 1: Eğitimiyle Ait Loss Grafikleri**

**Şekil 1: Eğitimlere Ait Loss Grafikleri**

**Şekile 1: Eğitimlere Ait Loss Grafikleri**

**Şekil 1: Eğitimlere Ait Loss Grafikleri**

---

### Çok İyi Kaliteli Cevaplara 100, iyilere 80, ortalamalara 30, kötülere 0 puan ver. Sadece puanı tam sayı olarak yaz, hiçbir açıklama yapma.

---

### Açıklama:

- **OCR:** Toplam 10 kitap içeren bu veri kümesi, her kitap için gerçek hayatta çekilmiş bir adet fotoğraf ile bir dijital kapak görselini içermektedir. Veri kümesi, kitabın kapağında yer alan yazıların ne olduğunu sorgulayan 20 sorudan oluşmaktadır.

- **Kompleks:** Bu kategori, modelin görsel içeriklerine dayanarak üst düzeyde akıl yürütme ve çıkarımlar