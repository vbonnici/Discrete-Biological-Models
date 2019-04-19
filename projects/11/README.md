# Progetto 11 : TAD (topological association domains) e creodi

Si confronti la parentesizzazione indotta dai domini topologici ottenuti tramite mappe di contatto cromosomico (TAD) e la parentesizzazione indotta da creodi.

Si esegua l'analisi si due genomi scelti liberamente, di cui almeno uno eucariota.

L'algoritmo per l'estrazione di creodi è fornito dalla classe implementata nel file `EsCreods.java`.
Tale classe prende in input i file contenenti la sequenza in formato 3bit e il file contenente la stuttura dati di indicizazione nelsa, più la lunghezza dei semi da cui partire per la ricerca dei creodi. Esso stampa a video i creodi trovati, uno per ogni riga che inizia con "ITE CREOD". Tale riga inoltre contiene la lunghezza della testa del creodo e la sequenza intera (testa più coda) del creodo.

Si ricoda che tale file è compilabile tramite il comando
```
javac -cp igtools.jar EsCreods.java
```

si ricorda anche che tramite la Struttura dati NELSA è possibile ottenere le posizioni dei k-mer (creodi) all'interno del genoma.
Tale funzionalità è fornita dal metodo find della struttura dati ed un suo esempio di utilizzo è mostrato di seguito.

```java
import igtools.common.nucleotide.B3Nucleotide;
import igtools.common.sequence.B3LLSequence;
import igtools.dictionaries.elsa.IELSAIterator;
import igtools.dictionaries.elsa.NELSA;

class es2{
public static void main(String[] args){
try{

B3LLSequence b3seq = B3LLSequence.load("seq.3bit");
NELSA nelsa = new NELSA();
nelsa.load("seq.nelsa");
nelsa.setSequence(b3seq);


B3Nucleotide[] kmer = B3Nucleotide.toB3("ACA");
int[] positions;
IELSAIterator it = nelsa.find(kmer);
if(it != null){
	positions = it.positions();
	for(int i=0; i<positions.length; i++){
		System.out.println(positions[i]);
	}
}
}catch(Exception e){
	System.out.println(e);
}
}
}
```




