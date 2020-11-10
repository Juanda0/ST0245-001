import java.io.*;
import java.util.Scanner;
import java.util.ArrayList;
import java.util.Arrays;

public class Lector{    
    public static ArrayList<Graph> leerDataset(){
        Scanner s = new Scanner(System.in);
        ArrayList<Graph> lg = new ArrayList<Graph>();
        int i = 0; 
        int arcos = 0;
        Graph g = null;
        String num = null;
        boolean aux = false;
        while(true){

            num = aux ? num : s.nextLine();
            switch(i){                
                case 0:
                aux = false;
                arcos = 0;
                g = new GraphAL(Integer.parseInt(num));
                i++;
                break;                
                case 1:
                arcos = Integer.parseInt(num);
                i++;
                break;
                case 2:                    
                String[] a = num.split(" ");
                g.addArc(Integer.parseInt(a[0]), Integer.parseInt(a[1]), 0);
                arcos--;
                if(arcos == 0){
                    i++;
                }
                break;
                default:
                lg.add(g);
                if(num.equals("0")){                        
                    return lg;
                }
                i = 0;
                aux = true;                
                break;
            }
        }
    }   //Complejidad O(n) 

}