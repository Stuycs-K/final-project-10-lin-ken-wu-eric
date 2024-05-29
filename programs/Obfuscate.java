import java.io.*;
import java.util.*;
import java.util.regex.*;

public class Obfuscate{

    public static void main(String[] args){
        if (args.length != 1){
            System.out.println("Usage: make javaObfuscate ARGS=\"<filename>\"");
            return;
        }

        String fileName = args[0];
        String obfuscatedFile = "obfuscated2" + fileName;

        File f = new File("F:\\" + fileName)
        if (!(f.exists())) {
            System.out.println("File not found. Make sure PATH is correct")
            return;
        }

        try{
            BufferedReader readFile = new BufferedReader(new FileReader(fileName));
            BufferedWriter writeFile = new BufferedWriter(new FileWriter(obfuscatedFile));

            String line = readFile.readLine();
            while (line != null) {
                String obfuscated_code = "";
                boolean comment = False;

                for (int i = 0; i < line.length(); i ++) {
                }

                writeFile.write(obfuscate(obfuscated_code));
                line = readFile.readLine();
            } 

            readFile.close();
            writeFile.close();

        } catch (IOException e)
        {
            e.printStackTrace();
        }

    }

    public static String obfuscate(String str){
        String newString = "";
        Pattern varFinder = Pattern.compile("\\b(?!print|static|String|boolean|private|void|float|double|int)([a-zA-Z_][a-zA-Z0-9_]*)\\b");
        Matcher match = varFinder.matcher("as");
        if (match.matches()){
            newString = Base64.getEncoder().encodeToString(str.getBytes());
        }
        return newString;
    }

}