# Testausdokumentti
## Yksikkötestauksen kattavuusraportti
![image](https://github.com/junyuan-fang/NumberRecognition/blob/main/documentation/kattavuusraportti.png)
## Mitä on testattu, miten tämä tehtiin?
Yksikköteisteillä on testattu [KNN-luokka](https://github.com/junyuan-fang/NumberRecognition/blob/main/src/services/knn.py), [mnist](https://github.com/junyuan-fang/NumberRecognition/blob/main/src/repositories/mnist.py) apukunktioiden toiminnallisuutta, ja [mnist_data_repository-luokka](https://github.com/junyuan-fang/NumberRecognition/blob/main/src/repositories/mnist_data_repository.py)  
Esim. Etäisyyden laskenta, numeron tunnistus, syötteiden oikeellisuus, tiedostojen käsitteleminen, luominen, tallentaminen ja avaaminen...
## Minkälaisilla syötteillä testaus tehtiin (vertailupainotteisissa töissä tärkeää)?
Tiedoston lukemisen testissä on käytetty samanlaisia polkuja kuin ohjelman suorituksessa.  
Syötteitä ovat mahdollisimman pieniä, koska suuret datat ovat vaikea generoida, kuten luokkitelun vaiheessa generoitun kuvamatriisi koko on 3x3, ja hiirestä piiretyn numero on  kokellut täysin musta- ja valkoisella kuvamatriisilla.
## Miten testit voidaan toistaa?
  * Lukee ensin käyttöohjeen ympäristön [asentaminen](https://github.com/junyuan-fang/NumberRecognition/blob/main/documentation/K%C3%A4ytt%C3%B6ohje.md).
  * ```pytest src``` suorittaa yksikkötestiä
  * ```coverage run --branch -m pytest src```  sitten  ```coverage report -m``` saadaan raportin testikattavuudesta  
tai
  * ```poetry run invoke html``` suoritta testejä, genenoi testikattavuuden raportti ja avaa raportti 'google-chrome' selaimella

## Ohjelman toiminnan empiirisen testauksen tulosten esittäminen graafisessa muodossa.
Suoritusaika voidaan testata main_tui.py:lla [ohje](https://github.com/junyuan-fang/NumberRecognition/blob/main/documentation/K%C3%A4ytt%C3%B6ohje.md).

| Testing range | Training range | Testing range x Training range|  [D22](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.1.8155&rank=5&q=hausdorff&osm=&ossid=) kulunut aika (s) | [D23](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.1.8155&rank=5&q=hausdorff&osm=&ossid=) kulunut aika (s) |
|-----|-----|-----|-----|-----|
| 20	| 50	| 1000	| 4.735	|4.752 |
| 20	| 100	| 2000	| 9.557	| 9.809 |
| 20	| 200	| 4000	| 19.661	| 19.392 |
| 20	| 2500	| 50000	| 246.595	| 247.984 |
| 20	| 10000	| 200000	| 985.475	| 988.49 |

| ![img](https://github.com/junyuan-fang/NumberRecognition/blob/main/documentation/D22.png) | ![img](https://github.com/junyuan-fang/NumberRecognition/blob/main/documentation/D23.png) |
|-----|-----|


Huomataan, että [D23](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.1.8155&rank=5&q=hausdorff&osm=&ossid=) ja [D22](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.1.8155&rank=5&q=hausdorff&osm=&ossid=) ovat melkein yhtä nopeita, mutta D23 tuotta hieman [parempaa](https://github.com/junyuan-fang/NumberRecognition/blob/main/documentation/report.pdf) tulosta. 

Kaikki 60 000 x 10 000 kuvien vertailu kestää noin 3000 x 985.475s ≈ 821.299h ≈ 34.2179vrk.
Ohjelma on ajettu ThinkPad T14 gen2 läppärillä
