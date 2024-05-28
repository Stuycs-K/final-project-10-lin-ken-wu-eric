import java.io.*;
import java.util.*;

public class Obfuscate{

    public static void main(String[] args){
        if (args.length != 1){
            System.out.println("Usage: make javaObfuscate ARGS=\"<filename>\"");
            return;
        }

        String fileName = args[0];
        String obfuscatedFile = "obfuscated" + fileName;

        try{
            BufferedReader readFile = new BufferedReader(new FileReader(fileName));
            BufferedWriter writeFile = new BufferedWriter(new FileWriter(obfuscatedFile));

            String line = readFile.readLine();
            while (line != null){
                writeFile.write(line);
                writeFile.newLine();
                line = readFile.readLine();
            } 

            readFile.close();
            writeFile.close();

        } catch (IOException e)
        {
            e.printStackTrace();
        }

    }

}