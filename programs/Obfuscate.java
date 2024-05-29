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

        File f = new File("F:\\" + fileName);
        if (!(f.exists())) {
            System.out.println("File not found. Make sure PATH is correct");
            return;
        }

        try{
            BufferedReader readFile = new BufferedReader(new FileReader(fileName));
            BufferedWriter writeFile = new BufferedWriter(new FileWriter(obfuscatedFile));

            String line = readFile.readLine();
            while (line != null) {
                String obfuscated_code = "";
                boolean singleComment = false;
                boolean multipleComment = false;
                boolean docstring = false;

                for (int i = 0; i < line.length(); i ++) {
                    char c = line.charAt(i);
                    if (singleComment) {
                        break;
                    } else if (multipleComment) {
                        if (i < line.length() - 1 && c == '*' && line.charAt(i + 1) == '/') {
                            multipleComment = false;
                            i++;
                        }
                    } else if (docstring) {
                        if (c == '"' && (i == 0 || line.charAt(i - 1) != '\\')) {
                            docstring = false;
                        }
                    } else {
                        if (c == '/') {
                            if (i < line.length() - 1 && line.charAt(i + 1) == '/') {
                                singleComment = true;
                                break;
                            } else if (i < line.length() - 1 && line.charAt(i + 1) == '*') {
                                multipleComment = true;
                                i++;
                                continue;
                            }
                        } else if (c == '"') {
                            docstring = true;
                        }
                    }
                    obfuscated_code += c;
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