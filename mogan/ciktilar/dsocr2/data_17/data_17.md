are used for the prediction of power outputs obtained from PV panels monthly. Particle Swarm Optimization (PSO), Back-  
Propagation (BP), Clonal Selection Algorithm (CSA) are used to train ANN to predict six different PV panel located in different  
angles from 10 to 60 degrees. Three different popular evaluation methods which are called mean absolute percentage error (MAPE),  
root mean square error (RMSE), varyans (R2) used to compare the ANN results. PSO is almost  
most successful algorithm as a training method when it is compared with BP and CSA. It is seen for the some of the results belong to  
a few months that BP is slightly better than PSO.  

Keywords: Photovoltaic Panel, Power Prediction, ANN, Back-propagation; PSO, Clonal Selection Algorithm  

# 1. Giriş  

Dünyada ve onun küçük bir yansıması olarak Türkiye’de; gelişen teknoloji beraberinde aynı oranda artan bir enerji ihtiyacını  
ortaya çıkarmaktadır. Bu ihtiyacın giderilmesi için kullanılan kaynaklar incelendiğinde, bölgesel olarak farklılıklar olsa da fosil yakıt  
türlerinin ön plana çıktığı görülmektedir. Türkiye’ye ait yıllık katsayılar net toplam ENERJİ İhracatı 2023 yılında 66.7’si fosil yakıtlarından  
%25.3’ü hidrolikten, %8.1’i ise jeo- termal, rüzgar, güneş enerjisi ve diğer kaynaklardan elde edilmektedir[1,2]. Gelişen ihtiyaçlara  
cevap verebilmektedir ama devletler mevcut politikalarını gözden geçirerek, gerek türeme olasılığı, gerekse çevreye etkileri  
düşünülerek fosil yakıtların alternatif olan enerji kaynaklarını ve üretim yöntemlerini araştırmaya başlamışlardır.  

Elektrik enerjisi elde etmek için kullanılan yöntemlerden biri de FV paneller yardımıyla güneş enerjisinden yararlanmaktır.  
Özellikle güneş enerjisi, diğer enerji kaynaklarına göre temiz, sessiz, ekonomik, güvenilir ve tükenmez olması nedeniyle son  
zamanlarda daha da önemli hale gelmiştir [3]. FV panellerden üretilen enerji, coğrafi konum, mevsimsel değişimler ve çevresel  
koşullar gibi faktörlere göre değişiklikler gösterebilmektedir. Buna bağlı olarak FV panellerin eğim açısının aylık, mevsimsel ve yıllık  
olarak değişirilmesi ile panellerden en yüksek gücün elde edilmesi sağlanabilmektedir. Güncel ve modern güç sistemlerinin güvenli  
ve ekonomik olarak işletilmesi için üretim planlamaları gerçek zamanlı, günlük, haftalık, aylık ve yıllık olarak yapılabilmektedir.  
Bundan dolayı, FV panel istasyonları gibi yenilenebilir güç tesislerinin güç çıkış değerlerinin ve yük eğilimlerinin kestirilmesi temel  
bir süreç olarak ortaya çıkmaktadır.  

Solar güç istasyonlarının verimliliğinin çıkış gücü, farklı hava koşullarına göre değişimler gösterdiği bilinen bir gerçekir. Bu  
neden denizden, su zemininde ve genel güç çıkış değerlerinin tahmin edilmesine yönelik çalışmaların önemli ölçüde artığı  
görülmektedir. Günümüzde FV panellerin güç tahmini için yaygın olarak kullanılan iki temel yaklaşım bulunmaktadır [4]. Bunlardan  
birincisi, solunum, mikroelementler ve metalik maddeleri kullanılarak elde edilen bazı parametreler gibi çevresel  
parametrelerin tahmini yardımıyla FV sistemlerindeki aktif güç tesislerinin hesaplanmasıdır. Diğerisi ise, FV sistemlerin aktif güç çıkışlarının  
doğrudan tahmin edilmesidir [5]. Solar ışınım verilerinin saatlik olarak tahmin edilmesi çok zor olduğundan dolayı, Kudo vd.[5]’un  
çalışmasında aktif güç çıkışı, daha önce ölçülen akım ve gerilim verilerine bağlı olarak doğrudan tahmin edilmiştir.  

Literatürde, şimdiyet kadar FV panel güç çıkışlarının tahmini için birçok yöntem önerilmiştir. Lorenz vd. [4] ve Kudo vd. [5] hava  
durumu verileri kullanarak FV panel güç çıkışı karakteristiklerini ortaya koyan, çoklu doğrusal regresyon yöntemleri ve YSA  
modelleri kullanılarak elde edilen sol ışınım tahminlerini karşılaştırmalı bir çalışma ile sunmuşlardır. Junseok vd. [6] ve Li vd. [7],  
Markov zincirleri kullanarak olasılıkla bir yaklaşım ile FV sistemlerindeki üretim merkezlerinde enerji depolama birimleri üzerine çalışma  
yapmışlardır. Ran vd. [8] ve Shi vd. [9] ise çalışmalarında, bir makine öğrenmesi yöntemi olan Destek Vektör Makineleri ile FV panel  
güç çıkışlarının tahmin edilmesine yönelik çalışmalar yürütülmüştür. Wang [10] çalışmasında, yukarıdaki çalışmaların dışında, FV  
güç çıkışlarının tahmin edilmesinde en uygun metodun YSA olduğu bazı çalışmalarda ortaya koymuştur. Kou vd. [11] çalışmalarında,  
GY kullanarak eğitilen YSA yapısı ile meteoroloji verilerinin de kullanılması sayesinde sol panel çıkış gücü tahmini yapmışlardır.  
Zhang vd. [12], PSO evrimsel algoritmasını bir bütün haline getirerek yaygın sinir ağını eğiticiyi çalışmalarında, ışının  
değerlerini de girdi olarak kullanmış ve solar radyasyon tahmin çıkarımları elde etmişlerdir. Qasrawi [13], farklı bölgelere  
yerleştirilen güneş panellerinden alınan panel çıktıları ve uygulamalara bağlı olarak çıkan FV panel için yaygın olan ve GY (Levenberg-  
Marquardt) ile eğitilmiş YSA tasarlanmışlardır. Sisteme girdi olarak nem, solar ışının, güneş ışınının, bu yöntem, kullanılan  
verimliliği, Tensi, Tarihi ve ağırlığı değişikliklerinin belirlenmesi ve FV panel için yaygın olan ve GY (Levenberg-  
Marquardt) ile eğitilmiş YSA tasarlanmışlardır. Sisteme girdi olarak nem, solar ışının, güneş ışınının, bu yöntem, kullanılan  
verimliliği, Tensi, Tarihi ve