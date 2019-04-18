import igtools.common.sequence.B3LLSequence;
import igtools.dictionaries.elsa.NELSA;


public class shownelsa{
public static void main(String[] args){
try{

B3LLSequence b3seq = B3LLSequence.load("seq.3bit");
NELSA nelsa = new NELSA();
nelsa.load("seq.nelsa");
nelsa.setSequence(b3seq);


for(int i=0; i<b3seq.length(); i++){
System.out.println(i + "\t"+ nelsa.sa()[i] + "\t" + nelsa.lcp()[i] +"\t"+ nelsa.ns()[i] );
}

}catch(Exception e){
System.out.println(e);
}

}
}
