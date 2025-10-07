 
// Importa IOException para manejar errores de E/S
import java.io.*;       // Importa todas las clases de java.io (FileReader, FileWriter, Streams, etc.)
import java.nio.file.Path;  // Importa Path de NIO para manejar rutas de archivos
import java.nio.file.Paths; // Añadido: Paths.get es compatible con JDK 8+


public class getionarCSV {

    public static void main(String[] args) {
        System.out.println(System.getProperty("user.dir"));
    }

 // FICHEROS DE TEXTO (con buffer)
    public void TextoConBuffer() {
        try {
            // --- ESCRITURA CON BUFFER ---
            Path pathTxtBuf = Paths.get("listings.csv"); // Path para archivo de texto con buffer (compatible con JDK 8)
            BufferedWriter bw = new BufferedWriter(new FileWriter(pathTxtBuf.toFile())); // BufferedWriter permite escribir líneas

            bw.write("Línea 1"); // Escribimos primera línea
            bw.newLine();        // Salto de línea
            bw.write("Línea 2"); // Escribimos segunda línea
            bw.flush();          // Guardamos los cambios
            bw.close();          // Cerramos el BufferedWriter

            // --- LECTURA CON BUFFER ---
            BufferedReader br = new BufferedReader(new FileReader(pathTxtBuf.toFile())); // BufferedReader permite leer líneas completas
            String linea; // Variable para almacenar cada línea
            System.out.println("Leyendo con BufferedReader:");
            while ((linea = br.readLine()) != null) { // Leemos hasta el final del archivo
                System.out.println(linea);           // Mostramos cada línea
            }
            br.close(); // Cerramos el BufferedReader

        } catch (IOException e) { // Captura errores de E/S
            e.printStackTrace(); // Muestra información detallada del error
        }

    }
}