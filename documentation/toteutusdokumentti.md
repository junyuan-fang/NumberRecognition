# Toteutusdokumentti
NumberRecognition-sovelluksen koodi on sijoitettu hakemistoihin seuraavasti:   
![image](https://github.com/junyuan-fang/NumberRecognition/blob/main/documentation/pakkauskaavio.png)   
* Käyttöjärjestelmä([UI](https://github.com/junyuan-fang/NumberRecognition/tree/master/src/ui))
* Sovelluslogiikka([Services](https://github.com/junyuan-fang/NumberRecognition/tree/master/src/services))
* Tiedon tallennus([Repositories](https://github.com/junyuan-fang/NumberRecognition/tree/master/src/repositories))
## Ohjelman rakenne
Ohjelman käynnistettäessä ```MnistRepository``` olio käsittelee ```.gz``` tiedostoja [mnist](https://github.com/junyuan-fang/NumberRecognition/blob/master/src/repositories/mnist.py) apufunktioiden avulla , ja tallentaa käsiteltyjä tiedostoja ```.pkl``` muotoon seuraavaa käynnistystä varten. ```Knn```olio pyytää kaikki tarvittavat tiedot ```MnistRepository``` oliosta, ja suorittaa numeroiden tunnistusta.

## Saavutetut aika- ja tilavaativuudet
Operaatiot riippuvat kuvien koosta ja määrästä.
```
knn(train_set, test_img_pixel_location):
    for train_img, train_label in train_set:
      distance = calculate(test_img_pixel_location, train_img)
      update_k_neighbours(train_label, distance)
    return result()

calculate(test_img_pixel_location, train_img):
    dist = max_dist
    for y_test,x_test in test_img_pixel_location:
      pixel_found = False
      while !False:
        pixel_found = next_outside_circle(y_test, x_test)
    return dist()
```
Olkoon 
* k = naapurit, 
* n = kuvan koko = 784, 
* m = opetusjoukon koko  


Tällöin
* ```calculate(test_img_pixel_location, train_img))``` aikavaativuus on ```O(n²)``` pahimmassa takauksessa test_img_pixel_location on koko test_img, ja samalla pitää käydä joka kerta koko train_image läpi.
* ```update_k_neighbours(train_label, distance)``` aikavaativuus on ```O(log(k))```, tässä on käytetty 'maxheap', pävittämällä suurinta arvoa pienemmäksi, saadaan lähimmät naapurit
* ```result()``` aikavaativuus on ```O(k)```
* ```knn(train_set, test_img_pixel_location)``` aikavaativuus on ```O(mn² + mlog(k) + k)```
* Koska k arvot ovat yleensä pieniä, tällöin  aikavaativuus on ```O(mn²)```

## Puutteet ja parannusehdotukset
Kyseessä on aika raskas algoritmi, koko opetusjoukon läpikäyminen kestää todella kauan aika. KD-Tree ja Ball-Tree pystyvät hieman parantamaan suorituskykyä, ja nämä ovat vaihtoehtoisia tietorakenteita. 

## Lähteet
[A Modifed Hausdorf Distance for Object Matching](https://citeseerx.ist.psu.edu/viewdoc/download;jsessionid=6F7642FDC63869C9A005AB4B14ED484E?doi=10.1.1.1.8155&rep=rep1&type=pdf)

[The MNIST Database](http://yann.lecun.com/exdb/mnist/)
