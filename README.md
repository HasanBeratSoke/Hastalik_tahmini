# Tahlil Sonucuna Göre Şeker hastalığı Tahmini
## KNN (K-Nearest Neigbors) algoritması nedir ?
KNN ( K-Nearest Neighbours ) sınıflandırma ve regresyon proplemleri için kullanılan bir algoritmadır.

Algoritmada bir gruplandırma yapıyoruz mesela bu örnekte `seker hastasimi` mı ? yoksa `sağlıklı` bir birey mi ? diye bir sınıflandırma yapıldı.


### Nasıl Çalışır ?

Kısaca, Sınıflandırma işleminde bulunucak örnek veri noktasının bulunduğu sınıfın yani öğrenim kümesinde ve en yakın komşusunun bakarak sınıflandırma yapar.

KNN (K-Nearest Neighbors) Algoritması iki temel değer üzerinden tahmin yapar;

• **Distance (Uzaklık):** Tahmin edilecek noktanın diğer noktalara uzaklığı hesaplanır.
![Untitled](https://github.com/HasanBeratSoke/Hastalik_tahmini/blob/main/img/%C4%B1mgknn.png)

• **K (komuşuluk sayısı):** En yakın kaç komşu üzerinden hesaplama yapılacağını söyleriz. K değeri sonucu direkt etkileceyecektir. K 1 olursa overfit etme olasılığı çok yüksek olacaktır. Çok büyük olursada çok genel sonuçlar verecektir. Bu sebeple optimum K değerini tahmin etmek problemin asıl konusu olarak karşımızda durmaktadır. K değerinin önemini aşağıdaki grafik çok güzel bir şekilde göstermektedir. Eğer K=3 ( düz çizginin olduğu yer) seçersek sınıflandırma algoritması ? işareti ile gösterilen noktayı, kırmızı üçgen sınıfı olarak tanımlayacaktır. Fakat K=5 (kesikli çizginin olduğu alan) seçersek sınıflandırma algoritması, aynı noktayı mavi kare sınıfı olarak tanımlayacaktır.

![Untitled](https://github.com/HasanBeratSoke/Hastalik_tahmini/blob/main/img/%C4%B1mg.png)

**k degerını 7 verildiğinde %81 doğruluk oranı ile tahmin etmiştir**
``` python
# k degerini kac vermeliyim 

sayac = 1
for k in range(1,11):
    knn_yeni = KNeighborsClassifier(n_neighbors=k)
    knn_yeni.fit(x_train, y_train)
    print(k ,'%',round( knn_yeni.score(x_test, y_test)*100,0))
    sayac+=1
```
```1 % 69.0
2 % 74.0
3 % 79.0
4 % 76.0
5 % 80.0
6 % 79.0
7 % 81.0
8 % 79.0
9 % 79.0
10 % 79.0
```
Veri Setine [buradan](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database) ulaşabilirsiniz.
