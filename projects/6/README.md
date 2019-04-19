# Progetto 6 : Usare l'indice di coding C_3 per distinguere RNA codificanti per proteina con RNA non codificanti

Sia $R(S,k,d)$ il valore di ricorrenza medio calcolato su tutti i k-meri (di lunghezza $k$) di una sequenza genomica $S$ a distanza di ricorrenza $d$. Ovvero, $R(S,k,d)$ è il valore della average RDD per la distanza di ricorrenza $d$.

Il valore dell'indice $C_3$ è dato dalla seguente formula 
$ C_3(S,k)  = \sum_{d} |R(S,k,d)| - \frac{|R(S,k,-1)| + |R(S,k,d+2)| }{2} $
per tute le distanze di ricorrenza $d$ multiple di 3, a partire da 6 fino al valore massimo possibile espresso dalla aRDD presa in esame.

Il valore di $C_3$ è una indicazione della prevelenza di una 3-periodicità nella distribuzione.


si applici tale indice nello distringuere RNA codificante per proteina e non in organismi eucarioti semplici e in batteri. In particolare si studi se è possibile definire un valore soglia che sia pplicabile nel distinguere i due tipi di RNA e se ne misuri la bontà attraverso le misure di sepcificità, sensitività e accuratezza.

---
 La tecnica per l'estrazione delle aRDD è lasciata libera.
