
import java.util.*;
public class Punto21
{
    public static String verificarColorBFS(Graph g, int source){
        int [] coloreado = new int[g.size()+1];
        coloreado[source] = 1;
        Queue<Integer> cola = new LinkedList<Integer>();
        return verificarColorBFSAux(g, source, coloreado, cola, 2) ? "BICOLOREABLE." : "NO BICOLOREABLE.";        
    }

    private static boolean verificarColorBFSAux(Graph g, int source, int[] coloreado, Queue cola, int colorActual){
        ArrayList<Integer> next = g.getSuccessors(source);   
        boolean answer = true;
        
        //Caso base        
        if(next.size() == 0){
            return true;
        }

        //Caso recursivo       
        for(int neighbor: next){
            if(coloreado[neighbor] == 0){
                cola.add(neighbor);
                coloreado[neighbor] = colorActual; 
            }
            else if(coloreado[neighbor] != colorActual ){
                return false;
            }
        }
        
        colorActual = colorActual == 1 ? 2:1;
        while (cola.size() != 0){         
            int sig = (int)cola.poll();
            answer =  answer && verificarColorBFSAux(g, sig, coloreado, cola, colorActual); //O(n^2)
            if(!answer){
                break;
            }
        } 
        return answer;
    }//O(n^2) siendo n el numero de vertices

    public static void main(){        
        ArrayList<Graph> lg = Lector.leerDataset();
        for(Graph g : lg){
            System.out.println(verificarColorBFS(g, 1));
        }//O(n^2) siendo n el numero de vertices
    }
}