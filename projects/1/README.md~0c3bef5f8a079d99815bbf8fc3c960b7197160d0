# Progetto 1 :  hapaxicità su genomi randomici creati su varie distributioni di probabilità

Al variare della lunghezza di parola <img src="/projects/1/tex/63bb9849783d01d91403bc9a5fea12a2.svg?invert_in_darkmode&sanitize=true" align=middle width=9.075367949999992pt height=22.831056599999986pt/>, si calcolino gli indici di ripetitià e hapaxicità, ovvero:
1) numero di hapax
2) numero di repeat
3) percentuale di hapax rispetto a <img src="/projects/1/tex/8daec2445e7b537498820d34172b49d0.svg?invert_in_darkmode&sanitize=true" align=middle width=20.87562509999999pt height=22.465723500000017pt/>
4) percentuale di repeat rispetto a <img src="/projects/1/tex/8daec2445e7b537498820d34172b49d0.svg?invert_in_darkmode&sanitize=true" align=middle width=20.87562509999999pt height=22.465723500000017pt/>
5) molteplicità media (e deviazioni standard) dei soli repeat

Data una stringa di lunghezza <img src="/projects/1/tex/55a049b8f161ae7cfeb0197d75aff967.svg?invert_in_darkmode&sanitize=true" align=middle width=9.86687624999999pt height=14.15524440000002pt/> costruita su un alfabeto di <img src="/projects/1/tex/0e51a2dede42189d77627c4d742822c3.svg?invert_in_darkmode&sanitize=true" align=middle width=14.433101099999991pt height=14.15524440000002pt/> simboli, 
il valore di <img src="/projects/1/tex/63bb9849783d01d91403bc9a5fea12a2.svg?invert_in_darkmode&sanitize=true" align=middle width=9.075367949999992pt height=22.831056599999986pt/> deve variare da 1 a <img src="/projects/1/tex/788280252c764b9192dec7b580cf8394.svg?invert_in_darkmode&sanitize=true" align=middle width=55.844801099999984pt height=22.831056599999986pt/> (maximum repeat length +1).

Si generino dei diagrami opportuni (che possono anche essere dei semplici diagrammi a barre) per la visualizzazione e comparazione di ognuna delle 5 distributioni elencate precedentemente. 
All'interno di tal diagrammi si evidenzi il valore <img src="/projects/1/tex/fafab2539b310b030881d83f501e0681.svg?invert_in_darkmode&sanitize=true" align=middle width=48.208002149999984pt height=24.65753399999998pt/>.


Si generino delle sequenze randomiche 
variando la cardinalità dell'alfabeto su 5 possibili valori <img src="/projects/1/tex/f5937f269fbad6a86bfcd5e162932b1a.svg?invert_in_darkmode&sanitize=true" align=middle width=127.85404499999997pt height=21.18721440000001pt/>
e la lunghezza della sequenza in 4 possibili lunghezze <img src="/projects/1/tex/03623501b708f51685aab17cf7658bc2.svg?invert_in_darkmode&sanitize=true" align=middle width=235.61709434999995pt height=21.18721440000001pt/>.

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
