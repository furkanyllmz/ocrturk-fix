```html
<html><body>
<div class="image" data-bbox="237 23 760 220"><img data-bbox="237 23 760 220"/></div> 
 <p>Şekil 1. Simetrik kripto sistem</p> 
 <h2>2. Ön Hazırlık</h2> 
 <h3>Tanım 2.1.</h3> 
 <p>Bir f fonksiyonu tüm t&gt;0 için tanımlı, α bir sabit ve M pozitif bir tamsayı olmak üzere f fonksiyonu $e^{-\alpha t}|f(t)| \leq M$ şeklinde yazılabiliryorsa bu f fonksiyonuna üstel mertebeli fonksiyon denir ve buradan</p> 
 <div class="formula"><img data-bbox="100 424 255 448"/><div>$$|f(t)| \leq Me^{\alpha t}$$</div></div> 
 <p>(2.1)</p> 
 <p>f(t) üstel fonksiyon ise t→∞ için f(t)=∞ olur [1].</p> 
 <h3>Tanım 2.2.</h3> 
 <p>t≥0 ve t,s∈R olmak üzere f(t) üstel fonksiyonu için</p> 
 <div class="formula"><img data-bbox="100 605 400 650"/><div>$$F(s)=\int_{0}^{\infty}e^{-st}f(t)dt$$</div></div> 
 <p>(2.2)</p> 
 <p>ise F fonksiyonuna f fonksiyonunun Laplace dönüşümü denir [1]. Tanım 2.1 ve Tanım 2.2 den hareketle f(t) fonksiyonu için Laplace dönüşümünü genişleterek yeni bir dönüşüm fonksiyonunu şu şekilde tanımlayalım;</p> 
 <h3>Tanım 2.3.</h3> 
 <p>Tüm t≥0 reel sayıları için f(t)’ nin bir dönüşümü</p> 
 <div class="formula"><img data-bbox="100 865 400 910"/><div>$$F(h)=T[f(t)]=\int_{0}^{\infty}\frac{1}{h}e^{-\frac{t}{h}}f(t)dt$$</div></div> 
 <p>(2.3)</p> 
 <p>şeklinde tanımlanır.(Genişletilmiş Laplace dönüşümü) f(t)=T⁻¹[F(h)] ile de f(t)’ nin ters dönüşümü gösterilir. Elde edilen Genişletilmiş</p> 
 <p>Laplace dönüşümü aşağıdaki standart sonuçlara sahiptir; [3,4]</p> 
 <div class="formula"><img data-bbox="500 295 898 340"/><div>$$\begin{aligned}&amp;1.T\{t^{n}\}=\frac{n!}{s^{n+1}}\Rightarrow T^{-1}\left\{\frac{1}{s^{n+1}}\right\}=\frac{t^{n}}{n!}\\&amp;2.T\{t^{n}e^{st}\}=\frac{n!.h^{n}}{(1-sh)^{n+1}}\Rightarrow\quad T^{-1}\left\{\frac{h^{n}}{(1-sh)^{n+1}}\right\}=\frac{t^{n}.e^{st}}{n!}\quad(t\geq0)\end{aligned}$$</div></div> 
 <p>(2.4)</p> 
 <h2>3. Uygulama</h2> 
 <h3>3.1. Şifreleme</h3> 
 <p>“FIRAT” mesajını göndermek istediğimizi farz edelim;</p> 
 <p>Öncelikle $e^t$ ile genişletilen Taylor serisini göz önüne alalım. Taylor serisi;</p> 
 <div class="formula"><img data-bbox="500 555 898 625"/><div>$$\begin{aligned}f(x)&amp;=f(a)+\frac{f^{\prime}(a)}{1!}(x-a)+\frac{f^{\prime\prime}(a)}{2!}(x-a)^{2}+\cdots+\frac{f^{n}(a)}{n!}(x-a)^{n}+\cdots\\&amp;=\sum_{n=0}^{\infty}\frac{f^{n}(a)}{n!}(x-a)^{n}\end{aligned}$$</div></div> 
 <p>dir. Buradan;</p> 
 <div class="formula"><img data-bbox="500 695 898 739"/><div>$$e^{t}=1+\frac{t}{1!}+\frac{t^{2}}{2!}+\frac{t^{3}}{3!}+\cdots=\sum_{n=0}^{\infty}\frac{t^{n}}{n!}$$</div></div> 
 <p>(3.2)</p> 
 <p>serisini $t^3$ ile genişletersek</p> 
 <div class="formula"><img data-bbox="500 770 898 814"/><div>$$t^{3}e^{t}=t^{3}+\frac{t^{4}}{1!}+\frac{t^{5}}{2!}+\frac{t^{6}}{3!}+\cdots=\sum_{n=0}^{\infty}\frac{t^{n+3}}{n!}$$</div></div> 
 <p>olur. Buradan da;</p> 
 <div class="formula"><img data-bbox="500 845 898 889"/><div>$$f(t)=\sum_{n=0}^{\infty}K_{n}\frac{t^{n+3}}{n!}$$</div></div> 
 <p>(3.4)</p> 
 <p>elde edilir. Alfabenin harfleri sıfırdan başlanarak numaralandırılırsa “FIRAT” düz metni</p> 
</body></html>
```