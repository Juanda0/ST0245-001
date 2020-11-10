
import javafx.util.Pair;
import java.util.ArrayList;
import java.util.LinkedList;

public class GraphAL extends Graph
{
    private ArrayList<LinkedList<Pair<Integer,Integer>>> grafo;

    public GraphAL(int size) {
        super(size);
        grafo = new ArrayList<>();
        for (int i = 0; i < size+1; i++) {
            grafo.add(new LinkedList<>());
        }
    }

    public void addArc(int source, int destination, int weight){
        grafo.get(source).add(new Pair<>(destination,weight));
        //grafo.get(destination).add(new Pair<>(source,weight));//Esta linea genera un arco inverso, por lo que hace que a fin de cuentas el grafo no sea dirigido
    }

    public int getWeight(int source, int destination) {
        int peso = 0;
        for (Pair<Integer, Integer> pareja : grafo.get(source)) {
            if (pareja.getKey() == destination)
                peso = pareja.getValue();
        }
        return peso;
    }

    public ArrayList<Integer> getSuccessors(int vertice){
        ArrayList<Integer> sucesores = new ArrayList<>();
        grafo.get(vertice).forEach(p -> sucesores.add(p.getKey())); //O(n)
        return sucesores;
    }

}