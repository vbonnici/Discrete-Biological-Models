# Progetto 8 : Segmentazione e similarità genomica

si considerino due genomi di lunghezza comparabile, si studino delle misure di similairtà confrontando segmenti dei due genomi ottenuti con opportune tecniche di segmentazione.

Si prendano in cosiderazione le seguenti techiniche di segmentazione
1) segmentazione a lunghezza fissa: si stabilisce una lunghezza fissa dei segmenti, quindi si segmentano i due genomi
2) segmentazione a dizionario: si considera una lunghezza di parola k tra 3 e 6, quindi si estraggono dei segmenti disgiunti ma contigui (senza vuoti intermedi) tale che ogni segmento contiene tutte le possibili parole di lunghezza k (il cui numero totale è di 4 elevato a k)

A seguito della segmentazione, si consideri come nozione di distanza di Jaccard generalizzata introdotta a lezione sulle distribuzioni di moltepicità di parola (word multiplicity distribution) estratte dai due segmenti da confrontare.

Sia m il numero di segmenti creati, il calcolo della distanza produce un vettore di m valori di Jaccard. Si trasformi tale vettore in una distribuzione, quindi se ne calcoli l'entropia.

Si applichino tali misure al confronto di almeno 10 genomi scelti opportunamente tale che sia possibile evidenziare le misure calcolate tra genomi considerati simili (ad esempio genomi dello stesso ceppo batterico) e genomi considerati diversi (ad esempio tra genomi di specie batteriche distinte).
Si applichi tali techinche per il confronto di eucarioti semplici.
