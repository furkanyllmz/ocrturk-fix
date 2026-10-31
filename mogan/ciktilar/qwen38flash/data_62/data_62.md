```markdown
TABLO I: İnce ayar veri kümesinden örnekler
<!-- Table (67, 94, 943, 345) -->
\begin{tabular}{|p{0.18\textwidth}|p{0.18\textwidth}|p{0.18\textwidth}|p{0.18\textwidth}|p{0.18\textwidth}|}
\hline
\textbf{GQA} & \textbf{CosmosVQA} & \textbf{VG} & \textbf{COCO} & \textbf{CC3M} \\
\hline
\textbf{Kullanıcı:} Gökyüzü karanlık mı? & \textbf{Kullanıcı:} Kitabın ismini öğrenebilir miyim? & \textbf{Kullanıcı:} Lütfen bu bölge için kısa bir açıklama yapınız: [0.69, 0.35, 0.79, 0.69]. & \textbf{Kullanıcı:} Lütfen bu bölge için kısa bir açıklama yapınız: [0.3, 0.36, 0.62, 0.59]. & \textbf{Kullanıcı:} Sunulan görüntüyü temsil eden kompakt bir anlatı oluşturun. \\
\textbf{Model:} Evet & \textbf{Model:} Masumiyet Müzesi & \textbf{Model:} Bu bir insan. & \textbf{Model:} Fotoğrafa bakan bir bilgisayar ekranı. & \textbf{Model:} çiftler için toplu nikah töreni düzenlendi. \\
\textbf{Kullanıcı:} Sokakta ne var? & \textbf{Kullanıcı:} Bu kitap hangi türde bir kitaptır? & \textbf{Kullanıcı:} Lütfen bu cümlenin tanımladığı bölgenin sınırlayıcı kutu koordinatını verin: tenis kortundaki beyaz çizgi. & \textbf{Kullanıcı:} Lütfen bu cümlenin tanımladığı bölgenin sınırlayıcı kutu koordinatını verin: en sağdaki ekran. & \\
\textbf{Model:} Araba & \textbf{Model:} Aşk romanı & \textbf{Model:} [0.0, 0.7, 0.9, 0.82] & \textbf{Model:} [0.3, 0.36, 0.62, 0.59] & \\
\textbf{Kullanıcı:} Caddede otobüs var mı? & \textbf{Kullanıcı:} Bu kitabın yazarı kimdir? & & & \\
\textbf{Model:} Hayır & \textbf{Model:} Orhan Pamuk & & & \\
\textbf{Kullanıcı:} Trafik sinyali sağda mı yoksa solda mı? & & & & \\
\textbf{Model:} Sol & & & & \\
\hline
\end{tabular}

İnce Ayar Loss Grafiği
<!-- Image (97, 381, 444, 503) -->
Ön Eğitim Loss Grafiği
<!-- Image (97, 519, 443, 641) -->
Şekil 1: Eğitimlere Ait Loss Grafikleri

A. Hakem: Dil Modeli

Bu çalışmanın yapıldığı Ağustos 2024 tarihinde çoğu öl-
çüme göre en iyi dil modeli olan OpenAi'nin GPT-4o [15]
modeli hakem olarak kullanılmıştır. Sorular, resimler ve mo-
dellerin verdikleri cevaplar hakem olarak belirlenen GPT-4o
modeline verilerek modelin yanıtta ne kadar doğru olduğuna
göre 100 üzerinden bir puan vermesi istenmiştir. GPT-4o'ya
puanlattırmak için kullanılan talimat formatı aşağıdaki gibidir:
\textbf{\{görsel\}}
\textbf{Soru: \{soru\}}
\textbf{Cevap: \{model-cevabı\}}
Bir görsel, görselle ilgili bir soru ve verilen cevap gösteril-
İnce Ayar Learning Rate Scheduler
<!-- Image (522, 381, 933, 530) -->
Şekil 2: İnce Ayar Eğitimde Learning Rate'in Değişimi

mıştır. Çok iyi kaliteli cevaplara 100, iyilere 80, ortalamalara
30, kötülere 0 puan ver. Sadece puanı tam sayı olarak yaz,
hiçbir açıklama yapma.

Ardından GPT-4o'nun verdiği yanıt ile modelin o soruya
ne kadar iyi yanıt verebildiği 100 üzerinden bir puan ile ölçül-
müştür. GPT-4o modelinin yanıtları deterministik olmaması ve
aynı cevaba farklı puanlar verilebilmesi nedeniyle her soru için
5 kez değerlendirme yapılarak bu değerlendirmelerde verilen
puanların ortalaması alınmıştır.

Bu puanlama için kullanılan test kümesi 4 alt kümeden
oluşmaktadır: OCR, Kompleks, Tanımlama ve Detay. Bu kü-
melerin içeriği aşağıda açıklanmıştır:

*   **OCR:** Toplam 10 kitap içeren bu veri kümesi, her
    kitap için gerçek hayatta çekilmiş bir adet fotoğraf ile
    bir dijital kapak görselini içermektedir. Veri kümesi,
    kitabın kapağında yer alan yazıların ne olduğunu sor-
    gulayan 20 sorudan oluşmaktadır.
*   **Kompleks:** Bu kategori, modelin görsel içeriklere
    dayanarak üst düzeyde akıl yürütme ve çıkarımlar
```