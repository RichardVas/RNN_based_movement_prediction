# RNN_based_movement_prediction
<br/>
Az alábbi repozitori tartalmazza az általam megvalósított mozgás predikciós rendszer forráskódját. <br/>
Továbbá készítettem egy demó videót, amely bemutatja a hálózat működését kapott videó forrás feldolgozása során. <br/>



## Program működése
<br/>
A hálózat predikciókat végez a detektált objektumokon, amint azok elérik a szükséges küszöbértékeket. Ezen esetben ez 10 konzekvens lépés.

![ezgif-1-0a55ba2315](https://user-images.githubusercontent.com/58149185/169697908-4a02898b-15ed-405f-b596-286302f55387.gif)

## Teszt videó
<br/>
A youtube videó megosztó portálra feltöltöttem egy videót, amelyben a program működését tesztelem egy városi közegben.<br/>
Az alábbi videó jól demonstrálja a program előnyeit és hátrányait. <br/>
Képes valós időben prediktálni, és közel pontos eredménnyel. A hátránya ennek a gyorsaságnak a pontosság.<br/>
<a href="https://www.youtube.com/watch?v=wctoWwyD7w8"><img src="https://img.youtube.com/vi/wctoWwyD7w8/0.jpg" alt="Leaf-varos-LSTM"></a>
 
A hálózat hátránya, ha az objektum követő algortimusom nem képes lépést tartani a követendő objektumokkal. Ugyanis ha egy objektum távol van a kamerától vagy kis méretűek és egymás hátán vannak egy szűk keresztmetszeten( utca végén lévő autók), akkor nem mindig tudja őket megkülömböztetni.

## Predikciós eredmények
<br/>
A hálózat gyorsan képes prediktálni több objektumon is, anélkül hogy hátráltatná a framek feldolgozását.
![mean_rtt](https://user-images.githubusercontent.com/58149185/169698259-0c21e863-2a06-44ac-99da-cf6c47842912.jpg)
 
Képes gyorsan, közel pontos értékeket prediktálni, amennyiben megfelelő inputok és előfeltételek adottak.
![41](https://user-images.githubusercontent.com/58149185/163893786-132072fa-55e3-4194-acd6-1f5bbc3d2baf.png)
<br/>
![44](https://user-images.githubusercontent.com/58149185/163893796-3b4fdb83-57fa-4c32-b140-a118b6a677fc.png)

