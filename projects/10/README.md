# Progetto 10 : Confronto di genomi/pangenomi tramite grafi di de Bruijn 

Si utilizzano i grafi di de Bruijn per il confronto di genomi e/o pangenomi.
La lunghezza di parola k con la quale costruire il grafo deve essere il valore minimo di LG tra i genomi presi in considerazione.

Un volta costruiti i grafi di due genomi/pangenomi da confrontare, si studino le proprietà dei percorsi all'interno di tali grafi che non sono presenti in entrambi i genomi/pangenomi.
Proprietà necessarie da valutare sono la distribuzione delle lunghezze di tali percorsi e la distribuzione dei gradi dei nodi contenuti in essi.

Si applichino tali misure al confronto di almeno 10 genomi scelti opportunamente tale che sia possibile evidenziare le misure calcolate tra genomi considerati simili (ad esempio genomi dello stesso ceppo batterico) e genomi considerati diversi (ad esempio tra genomi di specie batteriche distinte).
Si applichi tali techinche per il confronto di eucarioti semplici.

---

Le modilaità di estrazione e confronto dei grafi di de Bruijn è lasciata libera,
tuttavia si ricorda che è possibile estrarre tali grafi grazie ad alcune funzionalità del framework IGTools.
Infatti, tramie la struttura dati NELSA è possibile e numerare tutti e soli i k-mer contenuti in una sequenza genomica, inoltre è possibile eseguire delle operazioni di ricerca all'interno della struttura.

Il seguente codice illustra come enumerare tuti i k-mer di una sequenza per cui sono stati precalcolati il 3bit e il NELSA e come per ogni k-mer estrarre i sui successori nel grafo di de Bruijn.


```java
import igtools.common.nucleotide.B3Nucleotide;
import igtools.common.sequence.B3LLSequence;
import igtools.dictionaries.elsa.IELSAIterator;
import igtools.dictionaries.elsa.NELSA;

class es{
public static void main(String[] args){
try{

B3LLSequence b3seq = B3LLSequence.load("seq.3bit");
NELSA nelsa = new NELSA();
nelsa.load("seq.nelsa");
nelsa.setSequence(b3seq);


int k = 2;
B3Nucleotide[] kmer = new B3Nucleotide[2];
B3Nucleotide[] successor = new B3Nucleotide[2];
B3Nucleotide[] extensions = {B3Nucleotide.A, B3Nucleotide.C, B3Nucleotide.G, B3Nucleotide.T};

IELSAIterator it = nelsa.begin(k);
IELSAIterator successor_it;
while(it.next()){
	it.kmer(kmer);
	
	for(int i=1; i<k; i++){
		successor[i-1] = kmer[i];
	}
	for(B3Nucleotide  ext : extensions){
		successor[k-1] = ext;
		successor_it = nelsa.find(successor);
		if(successor_it != null){
			System.out.println( B3Nucleotide.toString(kmer) + " precedes " + B3Nucleotide.toString(successor));
		}
	}
	
}

}catch(Exception e){
	System.out.println(e);
}
}
}
```
