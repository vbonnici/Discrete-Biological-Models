# Progetto 1.1 :  hapaxicità su genomi randomici creati su varie distributioni di probabilità

A partire da una collezione di sequenze randomiche, si calcolino gli indici di ripetitià e hapaxicità per ognuna delle sequenze, ovvero:
1) indice HB (hapax bound)
2) indice RB (Repeat Bound)

Si generino dei diagrami opportuni (che possono anche essere dei semplici diagrammi a barre) per la visualizzazione e comparazione di ognuna delle 5 distributioni elencate precedentemente. 
All'interno di tal diagrammi si evidenzi il valore lg_m(n) (ovvero, logaritmo in base m di n).


Si generino delle sequenze randomiche 
variando la cardinalità dell'alfabeto su 5 possibili valori 4,16,64,256,1024
e la lunghezza della sequenza in 4 possibili lunghezze 10000, 100000, 1000000, 10000000.

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
