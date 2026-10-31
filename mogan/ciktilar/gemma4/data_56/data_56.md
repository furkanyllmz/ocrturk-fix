# RİEMANN TOPLAMI

**SONUÇ:**

![Riemann Sum Diagram](https://cdn-uploads.huggingface.co/production/uploads/66973841205f6aefcdae9dca/S_vXpYmKzZkPjBqCgWnN_.png)

f fonksiyonunun $[a,b]$ nda hesaplanan Riemann toplamı A ise $y=f(x)$ eğrisinin altında kalan alan yaklaşık olarak 
$A=\Delta x . f(c_1)+\Delta x . f(c_2)+\Delta x . f(c_3)+\dots+\Delta x . f(c_n)=\sum_{k=1}^{n} \Delta x . f(c_k)$
Buna göre Riemann toplamı n nin sonsuza yaklaşması durumunda $y=f(x)$ ile x ekseni arasında kalan alanı vereceğinden $\lim_{n\to\infty} \sum_{k=1}^{n} \Delta x . f(c_k)$ limiti ile hesaplanır.
Ayrıca $\lim_{n\to\infty} \sum_{k=1}^{n} \Delta x . f(c_k)$ değerine f fonksiyonunun $[a,b]$ ndaki belirli integrali denir. $\lim_{n\to\infty} \sum_{k=1}^{n} \Delta x . f(c_k)=\int_{a}^{b} f(x)dx$