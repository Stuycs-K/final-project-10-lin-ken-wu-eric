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

        try{
            BufferedReader readFile = new BufferedReader(new FileReader(fileName));
            BufferedWriter writeFile = new BufferedWriter(new FileWriter(obfuscatedFile));

            String line = readFile.readLine();
            boolean multipleComment = false;

            while (line != null) {
                String obfuscated_code = "";
                boolean singleComment = false;
                
                for (int i = 0; i < line.length(); i++) {
                    char c = line.charAt(i);
        
                    if (singleComment) {
                        continue;
                    } else if (multipleComment) {
                        if (i < line.length() - 1 && c == '*' && line.charAt(i + 1) == '/') {
                            multipleComment = false;
                            i++;
                        }
                    } else {
                        if (c == '/') {
                            if (i < line.length() - 1 && line.charAt(i + 1) == '/') {
                                singleComment = true;
                                continue;
                            } else if (i < line.length() - 1 && line.charAt(i + 1) == '*') {
                                multipleComment = true;
                                i++;
                                continue;
                            }
                        } else {
                            obfuscated_code += c;
                        }
                    }
                }
                
                writeFile.write(obfuscated_code + " \n");
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
        int curIn = 0;
        Pattern varFinder = Pattern.compile("\\b(?!print|static|String|boolean|private|void|float|double|int|class|public|return|if|else|for|while|do|switch|case|default|break|continue|new|this|super|try|catch|finally|throw|throws|import|package|interface|extends|implements|abstract|final|native|strictfp|synchronized|transient|volatile|assert|enum|goto|const|instanceof|true|false|null)([a-zA-Z_][a-zA-Z0-9_]*)\\b");
        Matcher match = varFinder.matcher(str);
        while (match.finds()){
            String keyWord = match.group(1);
            String encoded = Base64.getEncoder().encodeToString(match.getBytes());
           
        }
        
        return newString;
    }

}