# Käyttöohje
Kaikki komennot suoritetaan [NumberRecognition](https://github.com/junyuan-fang/NumberRecognition) hekemistossa.  
Tässä ohjessä oletetaan python 3.8 tai uudempi versio on asennettu 
## Ympäristön asentaminen
  1. ```pip3 install poetry```
  2. ```poetry install```
  3. ```poetry shell``` siirrytään virtuaaliympäristön sisään

## GUI ohjelman käynnistäminen
```poetry run invoke start```:lla tai ```python3 src/main.py```:lla käynnistetään ohjelman

  ### Aloitusnäkymä
  Input on oletetuisesti MNIST
  
![image](https://user-images.githubusercontent.com/61732233/147495335-866696c5-ad3e-408f-8ac9-47c3745da49c.png)
  
  ### parametrit
  * Input määrittää miten syötteitä otetaan. Tässä meidän ohjelmassa syötteitä ovat MNIST ja hiirestä piiretyn kuvia
  * Method määrittää miten kahden numeron välinen etäisyys lasketaan. [D22](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.1.8155&rank=5&q=hausdorff&osm=&ossid=), [D23](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.1.8155&rank=5&q=hausdorff&osm=&ossid=)  
  * K-neighbors:n arvo määrittää kuinka monta naapuria yhden numeron tunnistamiseen käytetään.
  * Grayscale:n arvoa ei näy, mutta sen oletusarvo on 73
  * Training size määrittää kuinka montaa numeroa käytetään testattvan numeron luokittelemiseksi.
  
  ### MNIST
  'Random image' ottaa kuva MNIST testijoukosta satunnaisesti
  
  ![image](https://user-images.githubusercontent.com/61732233/147497331-f99370fe-e80b-47e8-af3a-1c10442774d2.png)

  'Recognization' tunnistaa testijoukosta otetun kuva
  
  ![image](https://user-images.githubusercontent.com/61732233/147497444-e5c4fad1-5d77-4cea-81df-f8f21f52dcdd.png)
  
  'clear' tyhjentää kuvaa ja tulosta
  
  ![image](https://user-images.githubusercontent.com/61732233/147497528-f39f941c-e079-4306-bfa5-f1f1399f7cff.png)

  ### Mouse
  'input'->'mouse' 
  
  ![image](https://user-images.githubusercontent.com/61732233/147497656-4bbf4000-5d53-42d7-be2a-fbb1cda1cc26.png)

  Hiirellä piirretiin '6', ohjelma tunnistaa luvun oikein
  
  ![image](https://user-images.githubusercontent.com/61732233/147497719-5cb9bc66-654d-410b-9b6f-e76ae6aa709a.png)

  
  
## TUI, GUI sijaan
```poetry run invoke tui```:lla tai ```python3 src/main_tui.py```:lla käynnistetään TUI käyttöliittymä, missä on numeron tunnistamisen lisäksi suorituksessa käytetyn aika ja oikeallisuuden prosentti.
Ohejlman ajaessa löytyy lisää ohjeita.
