# RNN_based_movement_prediction
<br/>
Az alábbi repozitori tartalmazza az általam megvalósított mozgás predikciós rendszer forráskódját. <br/>
Továbbá készítettem egy demó videót, amely bemutatja a hálózat működését kapott videó forrás feldolgozása során. <br/>



## Program működése
<br/>
A hálózat predikciókat végez a detektált objektumokon, amint azok elérik a szükséges küszöbértékeket. Ezen esetben ez 10 konzekvens lépés.

![traffic_g](https://user-images.githubusercontent.com/58149185/163892850-e5447c70-0aeb-4a1f-9016-5e9b3a4d7b36.gif)

## Teszt videó
<br/>
A youtube videó megosztó portálra feltöltöttem egy videót, amelyben a program működését tesztelem egy városi közegben.<br/>
Az alábbi videó jól demonstrálja a program előnyeit és hátrányait. <br/>
Képes valós időben prediktálni, és közel pontos eredménnyel. <br/>
A hátránya ennek a gyorsaságnak a pontosság.
 <a href="https://www.youtube.com/watch?v=wctoWwyD7w8"><img src="https://img.youtube.com/vi/wctoWwyD7w8/0.jpg" alt="Leaf-varos-LSTM"></a>
 
A hálózat hátránya, ha az objektum követő algortimusom nem képes lépést tartani a követendő objektumokkal. Ugyanis ha egy objektum távol van a kamerától <br/>
vagy kis méretűek és egymás hátán vannak egy szűk keresztmetszeten( utca végén lévő autók), akkor nem mindig tudja őket megkülömböztetni.

## Predikciós eredmények
<br/>
A hálózat gyorsan képes prediktálni több objektumon is, anélkül hogy hátráltatná a framek feldolgozását.
![mean_rtt](https://user-images.githubusercontent.com/58149185/163893726-20899f8c-fbc0-45e2-baf8-02a092c2ac2e.jpg)

Képes gyorsan, közel pontos értékeket prediktálni, ha megfelelő inputokat kapott.
![41](https://user-images.githubusercontent.com/58149185/163893786-132072fa-55e3-4194-acd6-1f5bbc3d2baf.png)
![44](https://user-images.githubusercontent.com/58149185/163893796-3b4fdb83-57fa-4c32-b140-a118b6a677fc.png)

