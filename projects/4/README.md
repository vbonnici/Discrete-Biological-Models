# Progetto 4 : Caratterizzazione di pangenomi di specie

Dati $n$ genomi appartenenti alla stessa specie,
il pangenoma informazionale della specie è definito come
Dk(G1) U Dk(G2) U ... U Dk(Gn).

La lunghezza di parola k deve essere uguale al minimo valore di LG per i vari genomi.

Si utilizzino le nozioni di similarità, distanza e divergenza introdotte a lezione,
applicate alla distribuzione della molteplicità di parola (word multiplicity distribution),
per studiare le variazioni di tale distribuzione al variare del numero di genomi tenuti in considerazione.
La moltepilcità di parola di un k-mer relativamente ad un pangenoma è definita come la media delle molteplicità del k-mer nei singoli genomi.

Si correlino tali similarità/distanze/divergenze con la dimensione del dizionario ottenuto.

Si applichi l'analisi a due casi di studio scelti opportunamente, e comunque non inferiore a 10 genomi per ogni gruppo (specie).

---

La tecnica per l'estrazione di pangenomi è lasciata libera, anche se è consigliato l'utilizzo del framework IGTools.
Tramite il framework IGTools è possibile calcola l'unione dei dizionari estratti da due o più strutture dati NESA memorizzate su disco nel seguente modo:

```java

import igtools.common.nucleotide.B3Nucleotide;
import igtools.common.sequence.B3LLSequence;
import igtools.dictionaries.elsa.IELSAIterator;
import igtools.dictionaries.elsa.OnDiskNELSAIteratorV2;
import igtools.dictionaries.elsa.NELSA;
import igtools.dictionaries.intersection.BigNumericUnion;
import igtools.dictionaries.intersection.BigNumericUnionIntersection;
import igtools.dictionaries.intersection.NumericUnion;
import igtools.dictionaries.intersection.NumericUnionIntersection;


public class EsSets {
	public static void main(String[] args){
		int nof_seqs = 2:
		String[] seq_paths = ["seq1.3bit", "seq2.3bit"];
		String[] nelsa_paths = ["seq1.nelsa", "seq2.nelsa"];


		B3LLSequence[] seqs = new B3LLSequence[nof_seqs];

		for(int i=0; i<nof_seqs; i++){
			seqs[i] = B3LLSequence.load(seq_paths[i]);
		}

		//!!! this must be chosen according to LG values !!!
		int k = 6; 

		IELSAIterator[] its = new IELSAIterator[nof_seqs];

		for(int i=0; i<nof_seqs; i++){
			//the OnDiskNELSAIteratorV2 iterates over kmers without loading the NELSA in main memory, but jut the 3-bit sequence
			its[i] = new OnDiskNELSAIteratorV2(seqs[i], nelsa_paths[i], k);
		}
		

		//set-theoretic operations take the advantage of suffix order over the suffix arrays
		//moreover, they compare kmers by means of their position in the lexicographic order, rather than using string comparison
		//in this way, kmers are coverted into integers, and integers are compared several times
		//time is saved w.r.t. string comparison, just because objects are compared several times
		
		NumericUnion.UnionListerner listener = new NumericUnion.UnionListerner() {
			@Override
			public void intersection(B3Nucleotide[] kmer) {
				//included in the interface just for compatibility with the other operators 
			}
			@Override
			public void union(B3Nucleotide[] kmer, int mult) {
				System.out.println("U\t"+B3Nucleotide.toString(kmer));
			}
		};
		NumericUnion union = null;
		if(k < 32)
			union = new NumericUnion(seqs , its, k, listener);
		else 
			union = new BigNumericUnion(seqs, its, k, listener);
		union.union();

	}
}

```
