
import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;

public class Lector{    
    public static void correr(String[] args) {
        ArrayList<String[]> matriz = leerTXT();
        for(String[] a : matriz){           
            System.out.println(Arrays.asList(a));
        }
    }

    public static ArrayList<String[]> leerTXT(){
        ArrayList<String[]> datos = new ArrayList<String[]>();
        File archivo = new File("JAJAJAJA.txt");//4_train_balanced_135000.csv y 0_test_balanced_5000.csv
        try {
            Reader r = new FileReader(archivo);
            BufferedReader lector = new BufferedReader(r);
            String linea;
            int numFila = 0;
            while ((linea = lector.readLine())!=null){ //O(n)
                if(numFila > 1){
                    datos.add(linea.split(" ")); //O(n * m)
                }
                numFila++;
            } 
            lector.close();
        } 
        catch (IOException e) {
            e.getMessage();
        }
        return datos;
    }   //Complejidad de O(n * m)    
    
}