# Progetto 2 : Correlazione nei genomi random tra HB e alcune distanze tra distribuzioni

Date delle stringhe generate randomicamente con delle opportune distribuzioni di probabilità dei simboli,
si studi la correlazione tra i valori di $HB$ (hapax bound) ottenuti su tali stringhe ed i corrispettivi parametri delle distribuzioni.


Si utilizzino le similiartià, distanze e divergenze tra distribuzioni viste a lezione.

Si generino delle sequenze randomiche 
variando la cardinalità dell'alfabeto su 3 possibili valori $4,64,1024$
e la lunghezza della sequenza in 8 possibili lunghezze $5000, 10000, 500000, 100000, 500000, 1000000, 5000000, 10000000$.

La generazione di tali sequenze deve avvenire attraverso lo script `generate_sequence.py`.
Tale script prende in input i seguenti parametri:
- cardinalità dell'alfabeto
- lunghezza della sequenza
- file su cui salvare la sequenza
- tipo di distribuzione
- eventuali parametri della distribuzione

Per la scelta delle distribuzioni e dei loro parametri, si usino le seguenti configurazioni:
- piuniform
- poisson 1.0
- gamma 3.0 1.0
- beta 0.5 0.5
- lognorm 0.0 0.5
- binomial 10 0.1
- gauss 1.0
- chi2 4
- pareto
- exp

Un esempio di utlizzo dello script per la generazione di una sequenza è il seguente:
```
python3 generate_sequence.py 4 10000 poisson.4.10k.txt poisson 1.0
```

