modeller değerlendirmeye alınmıştır. Değerlendirmeye alınan modeller arasında, kullanıcı tarafından verilen talimat yerine getirebilme, verilen soruya karşı bir cevap çıktısı üretme, eksik verilen cümlelerin devamını getirebilme gibi çoklu metin dil kabiliyetlerini yerine getirebilme şartına bakılmıştır. Bu görevlerde bozuk ve anlamsız çıktı üretecek bir şekilde başarısız ve yetersiz olarak ayırt edilebilen modeller karşılaştırmaya dahil edilmemiştir. Bu kapsamda, Türkçe Bert modelleri \[6\], \[7\] ve TURNA \[8\] GPT tabanlı olmadıkları ve MASK tabanlı oldukları için; Main ise sürümünün açık kaynaklı olmaması nedeniyle bu karşılaştırmaya dahil edilmemiştir.

### B. Seçilen Modeller

Performansları karşılaştırılan dil modelleri Tablo \[9\]de verilmiştir.

---

### TABLO I: KARŞILAŞTIRILAN DİL MODELLERİ

| Model    | Parametre Sayısı | Yayınlanma Türü | TR Fine-Tuned | Base Model | Açıklamalar    |
|---|---|---|---|---|---|
| Mistral-7B-Instruct-v0.2    | 7.24 Milyar    | 05/01/2024    | Mistral-7B-Instruct-v0.2 | Mistral-7B-Instruct-v0.2 | SFT Training ve Freeze yöntemleri kullanılarak alacağıp-gap-tar talimatlarına göre finetune edilmiş bir versiyondur. |
| Llama-2-7b-chat-turkish-instructions | 6.74 Milyar    | 11/08/2023    | Llama-2-7B-chat | Llama-2-7B-chat | Türkçe talimatlar veri kümesinde finetune edilmiş bir versiyondur.    |
| Trendyol-LLM-7b-chat-v0.1 \[10\] | 6.84 Milyar    | 07/02/2024    | Trendyol-LLM-7b-base-v0.1 | Trendyol-LLM-7b-base-v0.1 | Base modeli temel alınarak 180 binlik Türkçe talimat veri seti üzerinde LoRa kullanılarak finetune edilmiş bir versiyondur.    |
| Trendyol-LLM-7b-base-v0.1 \[12\] | 6.84 Milyar    | 07/02/2024    | Trendyol-LLM-7B-base-v0.1 | Trendyol-LLM-7B-base-v0.1 | Optimize edilmiş bir transformer mimarisi kullanılan autoregressive dil modeller. LoRa kullanılarak 10 milyar token üzerinde finetune edilmiştir.    |
| mGPT \[13\]    | 1.3 Milyar    | 15/04/2022    | mGPT    | mGPT    | Wikipedia ve C4 Corpus kullanılarak 25 dil alınesinde dillbilimsel olarak çeşitli 61 dilde tanımlanan edilmiş bir metinlinge dill edilmiştir.    |
| Deepseek-llm-7b-chat \[14\] | 7.0 Milyar    | 29/11/2023    | Deepseek-llm-7b-base | Deepseek-llm-7b-base | Base model kullanılarak Talimat veri kümesinde finetune edilmiş metinlinge bir dil modellidir.    |
| open chat\_3.5 \[15\]    | 7.0 Milyar    | 20/09/2023    | Mistral-7B-v0.1    | Mistral-7B-v0.1    | Pekiştirmeli öğrenme modeli ilham alan C-RLFT tekniği ile finetune edilmiş metinlinge bir dil modellidir.    |

---

### III. KARŞILAŞTIRMA VERİ KÜMELERİ

Soru cevaplama çok farklı görevler için ortak bir format sağlamaktadır. Bu sebeple dil modellerinin karşılaştırılmasında en yaygın olarak kullanılan yöntemlerdendir. Seçilmiş talimat veri kümesi, çok farklı alanlardan soru içermektedir. Bu şekilde, her bir modelin bu sorulardaki cevaplarını hem otomatik değerlendirmelerle hem de oylama yolu ile karşılaştırılmaktadır. Model, aynı veri kümesiyle eğitilmediği sürece çıktıların cevaplarla örtüşmesi her zaman söz konusu değildir. Soru-cevap kümesinden örnekler Tablo \[9\]de verilmiştir.

---

### TABLO II: SORU-CEVAP KÜMESİ ÖRNEĞİ

| Soru    | Cevap    |
|---|---|
| Bir elma ağacında 10 elma var. Bir rüzgar eseri ve ağacın 2 elma düşüyor. Kaç elma ağacı kalmış olur? | Ağacı 8 elma kalmış olur.    |
| Saç bakımı için üç basit yöntem açıklayın.    | Düzenli kesim, doğal ürünlerle nazik temizlik, derin nemlendirme tedavileri.    |
| Sosyal ilişkileri geliştirmek ve yeni araçlardan etkin bir stratejiler sun. | İlgili alanlara uygun etkinliklere katılır, geliştirilen stratejileri tanımlar ve inisiyatif alır.    |

---

### TABLO III: BAĞLAMDA ÖĞRENME VERİ KÜMESİ ÖRNEĞİ

| Soru    | Seçenekler    | Cevap    |
|---|---|---|
| Güneş sistemindeki hangi geçenekten en uzun yıla sahiptir? | "Güneş" en yakın geçenekten en uzun yıla sahiptir. En uzun güneşin sahip geçenekten en uzun yıla sahiptir. | Güneş" en uzun geçenekten en uzun yıla sahiptir.    |
| Singapur'da sıkça güneş miktarı düşüşü? | "Hayır, Singapur"da yalnızca sıkça düşüşü.    | "Hayır, Singapur"da yalnızca sıkça düşüşü.    |

---

### BAĞLAMDA ÖĞRENME PERFORMANSININ ÖLÇÜMÜNDE ARC \[16\], HellaSwag \[17\], TruthfulQA \[18\], MMLU \[19\] veri setleri yaygın olarak kullanılmaktadır. Bu veri setleri ile ilgili bilgiler Tablo \[20\]de verilmiştir. Veri setlerinin bilgileri olması son derece önemlidir. Veri setlerinin kullanımı ve kullanış mekanizmaları önemlidir. Soru cevaplarına veri kümesi ise açık kaynak olan bir Türkçe veri kümesinden 20 düzgün ve anlamlı 1000 tane örnek ayıklanarak oluşturulmuştur. Bu veri kümesinin modellerin eğitiminde kullanılmış olma ihtimali yüzünden ayrıca, 300 tane yeni soru-cevap ikili hazırlanıp bir veri kümesi daha oluşturulmuştur. Oluşturulan veri kümeleri, araştırmacılarla paylaşılacaktır.

---

### TABLO IV: BAĞLAMDA ÖĞRENME VERİ KÜMELERİ

| İ