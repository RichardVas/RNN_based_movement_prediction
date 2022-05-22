# RNN_based_movement_prediction
<br/>
Az alábbi repozitori tartalmazza az általam megvalósított mozgás predikciós rendszer forráskódját. <br/>
Továbbá készítettem egy demó videót, amely bemutatja a hálózat működését kapott videó forrás feldolgozása során. <br/>



## Program működése
<br/>
A hálózat predikciókat végez a detektált objektumokon, amint azok elérik a szükséges küszöbértékeket. Ezen esetben ez 10 konzekvens lépés.

![ezgif-1-0a55ba2315](https://user-images.githubusercontent.com/58149185/169697908-4a02898b-15ed-405f-b596-286302f55387.gif)

## Prediktált videók
<br/>
A youtube videó megosztó portálra feltöltöttem egy videót, amelyben a program működését tesztelem egy városi közegben.<br/>
Az alábbi videó jól demonstrálja a program előnyeit és hátrányait. <br/>
Képes valós időben prediktálni, és közel pontos eredménnyel. A hátránya ennek a gyorsaságnak a pontosság.<br/>

### Statikus felvétel - Autópálya
<br/>
Ebben a videóban látható egy statikus kamerás felvétel feldolgozása, melynek során a hálózat konziztensen és közel pontosan képes prediktálni
az elhaladó járműveket.

<a href="https://www.youtube.com/watch?v=O9J_ounBBoQ"><img src="https://img.youtube.com/vi/O9J_ounBBoQ/0.jpg" alt="LSTM_highway_20090"></a>

### Város Menet
<br/>
Általánosan elmondható, hogy az egyik legnagyobb kihívást a detektálandó objektumok mennyisége jelenti. Az alábbi felvétel remek példa
arra, hogy a hálózat határait feszegessük. Hiszen egy zsúfolt kis keresztmetszetű utcán számos objektum található nagyon közel egymáshoz.
<a href="https://www.youtube.com/watch?v=Kcl_V-ZWQX4"><img src="https://img.youtube.com/vi/Kcl_V-ZWQX4/0.jpg" alt="LSTM_varos202203181053"></a>

### Győr Óriáskereék
<br/>
Az alábbi felvétel remekül demonstrálja egy átlagosan zsúfolt, normális menetet.
Ez a videó tekinthető az normának, ehhez érdemes visszonyítani további méréseket.<br/>
<a href="https://www.youtube.com/watch?v=DFgua-2BfqY"><img src="https://img.youtube.com/vi/DFgua-2BfqY/0.jpg" alt="LSTM_oriaskerek202203181052"></a>
 
A hálózat hátránya, ha az objektum követő algortimusom nem képes lépést tartani a követendő objektumokkal. Ugyanis ha egy objektum távol van a kamerától vagy kis méretűek és egymás hátán vannak egy szűk keresztmetszeten( utca végén lévő autók), akkor nem mindig tudja őket megkülömböztetni.

## Predikciós eredmények
<br/>
A hálózat gyorsan képes prediktálni több objektumon is, anélkül hogy hátráltatná a framek feldolgozását.
![mean_rtt](https://user-images.githubusercontent.com/58149185/169698259-0c21e863-2a06-44ac-99da-cf6c47842912.jpg)
 
Képes gyorsan, közel pontos értékeket prediktálni, amennyiben megfelelő inputok és előfeltételek adottak.
![41](https://user-images.githubusercontent.com/58149185/163893786-132072fa-55e3-4194-acd6-1f5bbc3d2baf.png)
<br/>
![44](https://user-images.githubusercontent.com/58149185/163893796-3b4fdb83-57fa-4c32-b140-a118b6a677fc.png)

