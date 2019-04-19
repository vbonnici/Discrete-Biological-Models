<script type="text/javascript" async
src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.2/MathJax.js? 
config=TeX-MML-AM_CHTML"
</script>

# Progetto 1 :  hapaxicità su genomi randomici creati su varie distributioni di probabilità

Al variare della lunghezza di parola $$k$$, si calcolino gli indici di ripetitià e hapaxicità, ovvero:
1) numero di hapax
2) numero di repeat
3) percentuale di hapax rispetto a $$D_k$$
4) percentuale di repeat rispetto a $$D_k$$
5) molteplicità media (e deviazioni standard) dei soli repeat

Data una stringa di lunghezza $n$ costruita su un alfabeto di $m$ simboli, 
il valore di $k$ deve variare da 1 a $mrl + 1$ (maximum repeat length +1).

Si generino dei diagrami opportuni (che possono anche essere dei semplici diagrammi a barre) per la visualizzazione e comparazione di ognuna delle 5 distributioni elencate precedentemente. 
All'interno di tal diagrammi si evidenzi il valore $(lg_m n)$.


Si generino delle sequenze randomiche 
variando la cardinalità dell'alfabeto su 5 possibili valori $4,16,64,256,1024$
e la lunghezza della sequenza in 4 possibili lunghezze $10000, 100000, 1000000, 10000000$.

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
