```html
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>Model</th>
      <th>Parametre Sayısı</th>
      <th>Yayınlanma Tarihi</th>
      <th>TR Fine-Tuned</th>
      <th>Base Model</th>
      <th>Açıklamalar</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Mistral-7B-Instruct-v0.2-turkish [9]</td>
      <td>7.24 Milyar</td>
      <td>05/01/2024</td>
      <td>✓</td>
      <td>Mistral-7B-Instruct-v0.2</td>
      <td>SFT Training ve Freeze yöntemleri kullanılarak alpaca-gpt4-tr talimatlarına göre finetune edilmiş bir versiyondur.</td>
    </tr>
    <tr>
      <td>Llama-2-7b-chat-turkish-instructions [10]</td>
      <td>6.74 Milyar</td>
      <td>11/08/2023</td>
      <td>✓</td>
      <td>Llama-2-7B-chat</td>
      <td>Türkçe talimatlar veri kümesinde finetune edilmiş bir versiyondur.</td>
    </tr>
    <tr>
      <td>Trendyol-LLM-7b-chat-v0.1 [11]</td>
      <td>6.84 Milyar</td>
      <td>07/02/2024</td>
      <td>✓</td>
      <td>Trendyol-LLM-7b-base-v0.1</td>
      <td>Base modeli temel alınarak 180 binlik Türkçe talimat veri seti üzerinde LoRa kullanılarak finetune edilmiş bir versiyondur.</td>
    </tr>
    <tr>
      <td>Trendyol-LLM-7b-base-v0.1 [12]</td>
      <td>6.84 Milyar</td>
      <td>07/02/2024</td>
      <td>✓</td>
      <td>Llama-2-7B</td>
      <td>Optimize edilmiş bir transformer mimarisi kullanan autoregressive dil modelidir. LoRa kullanılarak 10 milyar token üzerinde finetune edilmiştir.</td>
    </tr>
    <tr>
      <td>mGPT [13]</td>
      <td>1.3 Milyar</td>
      <td>15/04/2022</td>
      <td>—</td>
      <td>—</td>
      <td>Wikipedia ve C4 Corpus kullanılarak 25 dil ailesinden dilbilimsel olarak çeşitli 61 dilde pretrain edilmiş bir multilingual dil modelidir.</td>
    </tr>
    <tr>
      <td>Deepseek-llm-7b-chat [14]</td>
      <td>7.0 Milyar</td>
      <td>29/11/2023</td>
      <td>—</td>
      <td>deepseek-llm-7b-base</td>
      <td>Base model kullanılarak Talimat veri kümesinde finetune edilmiş multilingual bir dil modelidir.</td>
    </tr>
    <tr>
      <td>open_chat_3.5 [15]</td>
      <td>7.0 Milyar</td>
      <td>20/09/2023</td>
      <td>—</td>
      <td>Mistral-7B-v0.1</td>
      <td>Pekştirilmiş öğrenmeden ilham alan C-RLFT tekniği ile finetune edilmiş , multilingual bir dil modelidir.</td>
    </tr>
  </tbody>
</table>

<p>B. Seçilen Modeller</p>
<p>Performansları karşılaştırılan dil modelleri Tablo I'de verilmiştir.</p>
<p>TABLO I: KARŞILAŞTIRILAN DIL MODELLERİ</p>
<p>modeller değerlendirilmeye alınmıştır. Değerlendirmeye alınan modeller arasında, kullanıcı tarafından verilen talimatı yerine getirebilme, verilen soruya karşı bir cevap çıktısı üretme, eksik verilen cümlelin devamını getirebilme gibi çoklu metin dil kabil yetlerini yerine getirebilme şartına bakılmıştır. Bu görevlerde bozuk ve anlamsız çıktı üreterek bariz şekilde başarısız ve yetersiz olarak ayrıt edilebilen modeller karşılaştırmaya dahil edilmemiştir. Bu kapsamda, Türkçe Bert modelleri [6], [7] ve TURNA [8] GPT tabanlı olmadıkları ve MASK tabanlı oldukları için; Main ise sürümünün açık kaynaklı olmaması nedeniyle bu karşılaştırmaya dahil edilmemiştir.</p>
<p>veri kümesi, çok farklı alanlardan soru içermektedir. Bu şekilde, her bir modelin bu sorulardaki cevaplarını hem otomatik değerlendirilmelerle hem de oylama yolu ile karşılaştırmaktadır. Model, aynı veri kümesiyle eğitilmediği sürece çıktıların cevaplarla örtüşmesi her zaman söz konusu değildir. Soru-cevap kümesinden örnekler Tablo II'de verilmiştir.</p>
<p>TABLO II: SORU-CEVAP KÜMESİ ÖRNEĞİ</p>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>Soru</th>
      <th>Cevap</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Bir elma ağacında 10 elma var. Bir rüzgar esiyor ve ağaçtan 2 elma düşüyor. Kaç elma ağaçta kalmış olur?</td>
      <td>Ağaçta 8 elma kalmış olur.</td>
    </tr>
    <tr>
      <td>Şaç bakımı için üç basit yöntem açıklayın.</td>
      <td>Düzenli kesim, doğal ürünlerle nazik temizlik, derin nemlendirme tedavileri.</td>
    </tr>
    <tr>
      <td>Sosyal ilişkileri geliştirmek ve yeni arkadaşlar edinmek için stratejiler sun.</td>
      <td>Ilgi alanlarına uygun etkinliklere katıl, güler yüzlü iletişim kur, aktif dinleme pratiği yap, sosyal medyayı etkili kullan ve inisiyatif al.</td>
    </tr>
  </tbody>
</table>
<p>Bağlamda öğrenme veri kümelerinde modellin eğitilmeden sadece örnekler göstererek cevaplama kabiliyeti ölçülmüştür. Veri kümesinden örnekler Tablo III'de verilmiştir.</p>
<p>TABLO III: BAĞLAMDA ÖĞRENME VERİ KÜMESİ ÖRNEĞİ</p>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>Soru</th>
      <th>Seçenekler</th>
      <th>Cevap</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Güneş sistemindeki hangi gezegen en uzun yıla sahiptir?</td>
      <td>"Güneş'e en yakın gezegen.", "En uzun güne sahip gezegen.", "En çok uydusu olan gezegen.", "Güneş'e en uzak gezegen."</td>
      <td>Güneş'e en uzak gezegen.</td>
    </tr>
    <tr>
      <td>Singapur'da sakız çiğnemek yasa dışı mı?</td>
      <td>"Hayır, Singapur'da yalnızca sakız ithal etmek ve satmak yasa dışıdır.", "Evet, Singapur'da sakız çiğnemek yasaktır."</td>
      <td>Hayır, Singapur'da yalnızca sakız ithal etmek ve satmak yasa dışıdır.</td>
    </tr>
  </tbody>
</table>
<p>Bağlamda öğrenme performanslarının ölçümünde ARC [16], HellaSwag [17], TruthfulQA [18], MMLU [19] veri setleri yaygın olarak kullanılmaktadır. Bu veri setleri ile ilgili bilgiler Tablo IV'de verilmiştir. Veri setlerinin ingilizce olmasından dolayı her veri kümesinden örneklemeye yapılp Türkçe'ye çevrilmştir.</p>
<p>Soru cevaplama veri kümesi ise açık kaynak olan bir Türkçe veri kümesinden [20] düzgün ve anlamlı 1000 tane örnek ayıklanarak oluşturulmuştur. Bu veri kümesinin modellerin eğitiminde kullanılması olma ihtimali yüzünden ayrıca, 300 tane yeni soru-cevap ikilisi hazırlanıp bir veri kümesi daha oluşturulmuştur. Oluşturulan veri kümeleri, araştırmacılarla paylaşılmaktadır.</p>
<p>TABLO IV: BAĞLAMDA ÖĞRENME VERİ KÜMELERİ</p>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>İsmi/Türü</th>
      <th>Test</th>
      <th>Train</th>
      <th>Validation</th>
      <th>dev</th>
      <th>Shot NO.</th>
      <th>Seçmeli</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>ARC</td>
      <td>400</td>
      <td>812</td>
      <td>—</td>
      <td>—</td>
      <td>25</td>
      <td>Evet</td>
    </tr>
    <tr>
      <td>ARC</td>
      <td>—</td>
      <td>891</td>
      <td>641</td>
      <td>—</td>
      <td>10</td>
      <td>Hayır</td>
    </tr>
    <tr>
      <td>HellaSwag</td>
      <td>—</td>
      <td>—</td>
      <td>635</td>
      <td>—</td>
      <td>0</td>
      <td>Evet</td>
    </tr>
    <tr>
      <td>TruthfulQA</td>
      <td>—</td>
      <td>—</td>
      <td>—</td>
      <td>—</td>
      <td>—</td>
      <td>—</td>
    </tr>
    <tr>
      <td>MMLU</td>
      <td>662</td>
      <td>—</td>
      <td>—</td>
      <td>30</td>
      <td>5</td>
      <td>Evet</td>
    </tr>
  </tbody>
</table>
<p>III. KARŞILAŞTIRMA VERİ KÜMELERİ</p>
<p>Soru cevaplama çok farklı görevler için ortak bir format sağlamaktadır. Bu sebeple dil modellerinin karşılaştırılmasında en yaygın olarak kullanılan yöntemlerdendir. Seçilmiş talimat</p>
<p>IV. KARŞILAŞTIRMA ÖLÇÜTLERİ</p>
<p>Bu çalışmada, Türkçe dil modellerinin performanslarının kapsamlı bir şekilde değerlendirilmesi amacıyla üç farklı ölçüt kullanılmıştır. Bu ölçütler, modellerin Türkçe dilini ne kadar iyi anladıklarını ve dili kullanma becerilerini ölçmek</p>
```