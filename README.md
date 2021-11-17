# Alphabot
In questo repository si può trovare lo sviluppo di un progetto che consiste nel comandare un Alphabot tramite un sistema di client-server TCP.

## File
* **comandi.db** : E il database contenente tutti i movimenti composti.
* **libreria_robot.py** : Questo file contiene la classe Alphabot con tutti i metodi per far muovere il robot.
* **clientTCP.py** : Il client sarà il programma da scaricare sul proprio dispositivo e servirà ad inviare i comandi all'Alphabot.
*  **server_robot_1/2/3.py** : Il server sarà invece il programma da installare sull'Alphabot e servirà a ricevere i comandi dal client e di conseguenza esegurli. Ci sono tre versioni, dalla versione piu base a quella che comprende i movimenti composti.


## Movimenti
| Nome comando      | Descrizione                        | 
| :-------- | :--------------------------------- | 
| `a tempo`  | Questo comando consente di far muovere l'Alphabot nella direzione "avanti" per un determinato tempo   |
| `i tempo`  | Questo comando consente di far muovere l'Alphabot nella direzione "indietro" per un determinato tempo   | 
| `l tempo`  | Questo comando consente di far muovere l'Alphabot nella direzione "sinistra" per un determinato tempo   |
| `r tempo`  | Questo comando consente di far muovere l'Alphabot nella direzione "destra" per un determinato tempo  | 
| `aa`  | Questo comando consente di far muovere l'Alphabot nella direzione "avanti" con una accelerazione graduale  | 
| `s`  | Questo comando consente di far fermare l'Alphabot   | 


## Movimenti composti
| Nome comando      | Descrizione                        | 
| :-------- | :--------------------------------- | 
| `zig_zag`  | Questo comando consente di far muovere l'Alphabot con un movimento a zigzag   |
| `otto`  | Questo comando consente di far muovere l'Alphabot con un movimento a forma di otto   |
| `R_90`  | Questo comando consente di far muovere l'Alphabot nella direzione "destra" con un angolo di 90°    | 
| `L_90`  | Questo comando consente di far muovere l'Alphabot nella direzione "sinistra" con un angolo di 90°  |
| `R_180`  | Questo comando consente di far muovere l'Alphabot nella direzione "destra" con un angolo di 180°  | 
| `R_180`  | Questo comando consente di far muovere l'Alphabot nella direzione "sinistra" con un angolo di 180°  | 

## Partecipanti al progetto
* Federico Giraudo
* Samuele Gazzera
