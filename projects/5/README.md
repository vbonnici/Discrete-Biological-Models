# Progetto 5 : Divergenze e similarità tra genomi e pangenomi

Dati n genomi appartenenti alla stessa specie,
il pangenoma informazionale della specie è definito come
Dk(G1) U Dk(G2) U ... U Dk(Gn)$.

Si utilizzi la nozione di divergenza di Kullback–Leibler (KL) introdotta a lezione
applicata alla distribuzione della molteplicità di parola (word multiplicity distribution),
per studiare le variazioni di tale divergenza nell'includere un genoma in un pangenoma della stessa specie rispetto alla sua introduzione nel pangenoma di una specie differente da quella di appartenenza.
La moltepilcità di parola di un k-mer relativamente ad un pangenoma è definita come la media delle molteplicità del k-mer nei singoli genomi.

Devono essere prese in considerazioni le seguenti due lunghezze di parola k:
1) il minomo valore di LG tra i genomi presi in esame
2) il massimo valore k tale Dk(G1) = Dk(G2) = ... = Dk(Gn)

Nel primo caso, la divergenza KL deve essere calcolata prendendo in cosniderazione le frequenze di tutti i e soli i k-mer che occorrono in tutti i genomi analizzati, detto Dk(I) e dato dalla intersezione di  Dk(G1), Dk(G2) ... Dk(Gn). si ricorda che nell'escludere i k-mer di un genoma non presenti in tale intersezione, le frequenze vanno ricalcolate tale che la loro somma relativamente ad un genoma si mantenga uguale a 1.
Il valore di KL va quindi riscalato in modo da tenere conto dei k-mer che sono stati esclusi dalla intersezione. 
Indicando Dk(U) = Dk(G1) U Dk(G2) U ... U Dk(Gn), il valore finale di KL è dato dalla sequente formula: KL * ( Dk(I) / Dk(U) ) $.


si conduca lo studio su 4 gruppi di genomi appartenente a 4 ceppi di due specie diverse. si studino le differenze tra le distanze dei pangenomi tra ceppi e tra specie.

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
		
		if (k < 32){
			//if kmers are smaller than 32 nucleotides we can use the implicit integer representation given by the 3-bit encoding
			NumericUnionIntersection.UnionListerner listener = new NumericUnionIntersection.UnionListerner() {
				@Override
				public void intersection(B3Nucleotide[] kmer, int mult, int nof_seqs) {
					System.out.println("I\t"+B3Nucleotide.toString(kmer) +"\t"+ mult+"\t"+nof_seqs);
				}
				@Override
				public void union(B3Nucleotide[] kmer, int mult, int nof_seqs) {
					System.out.println("U\t"+B3Nucleotide.toString(kmer) +"\t"+ mult+"\t"+nof_seqs);
				}
			};
			NumericUnionIntersection union =  new NumericUnionIntersection( seqs , its, k, listener);
			union.union();
		}
		else{
			//otherwise we need to calculate the lexicographic order
			BigNumericUnionIntersection.UnionListerner listener = new BigNumericUnionIntersection.UnionListerner() {
				@Override
				public void intersection(B3Nucleotide[] kmer, int mult, int nof_seqs) {
					System.out.println("I\t"+B3Nucleotide.toString(kmer) +"\t"+ mult+"\t"+nof_seqs);
				}
				@Override
				public void union(B3Nucleotide[] kmer, int mult, int nof_seqs) {
					System.out.println("U\t"+B3Nucleotide.toString(kmer) +"\t"+ mult+"\t"+nof_seqs);
				}
			};
			BigNumericUnionIntersection union =  new BigNumericUnionIntersection( seqs , its, k, listener);
			union.union();
		}

	}
}

```
