import java.util.*;
public class Main
{

    public static void printVertexDFS(Graph g, int source){
        boolean [] checked = new boolean[g.size()+1];
        System.out.println("Partiendo del vertice "+source+" se alcanza:");
        System.out.println("graph Matriz {");
        auxPrintVertexDFS(g, source, checked, new ArrayList());
        System.out.println("}");
    }

    private static void auxPrintVertexDFS(Graph g, int source, boolean[] checked, ArrayList<String> impresos){
        ArrayList<Integer> next = g.getSuccessors(source);        
        checked[source] = true;        
        //System.out.println(source);

        //Caso base
        if(next.size() == 0){
            return;
        }

        //Caso recursivo
        for(int neighbor: next){
            String a = "\t\""+source+"\""+" -- \""+neighbor+"\"";
            String b = "\t\""+neighbor+"\""+" -- \""+source+"\"";
            if(!impresos.contains(a)){
                System.out.println(a);  
                impresos.add(a);
                impresos.add(b);
            }
            if(!checked[neighbor]){                
                auxPrintVertexDFS(g, neighbor, checked, impresos);
            }
        }
    }

    public static void printVertexBFS(Graph g, int source){
        boolean [] checked = new boolean[g.size()+1];
        checked[source] = true;
        System.out.println("Partiendo del vertice "+source+" se alcanza:");
        System.out.println(source);
        Queue<Integer> cola = new LinkedList<Integer>();
        auxPrintVertexBFS(g, source, checked, cola);
    }

    private static void auxPrintVertexBFS(Graph g, int source, boolean[] checked, Queue cola){
        ArrayList<Integer> next = g.getSuccessors(source);   

        //Caso base
        if(next.size() == 0){
            return;
        }

        //Caso recursivo       
        for(int neighbor: next){
            if(!checked[neighbor]){  
                cola.add(neighbor);
                System.out.println(neighbor);
                checked[neighbor] = true; 
            }
        }

        while (cola.size() != 0){
            int sig = (int)cola.poll();
            auxPrintVertexBFS(g, sig, checked, cola);
        }        
    }

    public static void main(){
        ArrayList<String[]> datos = Lector.leerTXT();
        Set<String> vertices = new HashSet();
        //Set<String> id2 = new HashSet();
        //Set<String> weight = new HashSet();

        for(String[] s : datos){            
            vertices.add(s[0]);
            vertices.add(s[1]);
            //weight.add(s[2]);
        }

        Graph graph = new GraphAL(vertices.size());
        for(String[] s : datos){
            int source = Integer.parseInt(s[0]);
            int destination = Integer.parseInt(s[1]);
            int weight = Integer.parseInt(s[2]);
            graph.addArc(source, destination, weight);
        }
        printVertexDFS(graph, 1);
        //printVertexDFS(graph, 4);
    }
}
