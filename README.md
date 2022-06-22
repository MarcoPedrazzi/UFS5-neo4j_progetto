# UFS5-neo4j_progetto

## Percorsi Montani 
##### ===================================================


Applicazione che serve a pianificare le gite in montagna.
In particolare:
	- consigliare i percorsi in base alla difficoltà, alla durata, e al numero di persone in un gruppo.
	
L'applicazione deve gestire:
Punti di interesse per le gite in montagna:

* Rifugi, dove dormire di notte.
	- nome
	- capacità_max
* Sentieri
	- indice di difficoltà
	- tempo di percorrenza medio
	- numero
* Punti panoramici
	- altezza s.l.m.
* Punti di partenza / arrivo dei sentieri

1. proporre il percorso entro distanze definite per un certo numero di persone. Es "percorso tra 24h e 48h per 5 persone e 1 rifugio"
2. inserire e cancellare gli elementi: rifugi, percorsi, ecc...

## Progetto

##### ===================================================

### Gruppo composto da Pedrazzi Marco, Luca Cavioni, Antonio Santucci, Gabriele Cortinovis.

##### ===================================================



* nodi:
	- rifugio:
		* label:
			- rifugio
			- partenza
		* attributi
			- nome
			- capacità
	- punto panoramico:
		* label:
			- punto panoramico
			- partenza
		* attributi
			- altitudine
			- nome
	- punto di interesse:
		* label:
			- punto di interesse
			- partenza
		* attributi
			- nome
* archi:
	- sentiero:
		* label:
			- sentiero
			
		* attributi
			- codice
			- durata (h)
			- difficoltà -facile medio difficile-