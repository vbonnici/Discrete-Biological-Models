# Progetto 7 : Elongazione di parola su classi distinte di regioni genomiche

Si applichi un algoritmo di riconoscimento di parole salienti ottenuto per elongazione di semi di parole a classi di regioni genomiche con conosciute differenze biologiche (esempio genomi completi, esoni, introni, promotri, long repeat, etc...).


Una volta estratti insiemi di parole da tali regioni, se ne studi la similarità.


L'algoritmo di elengazione è fornito tramite la classe `igtools.cli.elongation.RDDLRElongation` del framework IGTools. 
Il tool prende in input
- i file 3bit e NELSA della sequenza da analizzare
- una misura da utilizzare per il calcolo della significativà 
- il verso di elongazione
- la lunghezza dei semi da cui partire
- la moteplicità minima delle parole estratte

Si fissi la misura da utilizzare a `kl` e la molteplicità minima a 2.
Si faccia variare la lunghezza dei semi da 1 a 12,
e si estragga nei versi `L2R` ed `R2L`, quindi si prenda lunione degli insiemi ottenuti facendo variare i due parametri.
si escludano dall'insieme risultate le parole che sono prefisso di un'altra parola dell'insieme.

---

Il cacolo delle unioni e l'esclusione delle parole prefisso è lasciata libera,

