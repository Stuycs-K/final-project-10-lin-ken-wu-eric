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
        String obfuscatedFile = Base64.getEncoder().encodeToString(fileName.substring(0,fileName.length()-5).getBytes()).replace("==","") + ".java";
        // String fileName2 = fileName.substring(0,fileName.length()-5);

        try{
            BufferedReader readFile = new BufferedReader(new FileReader(fileName));
            BufferedWriter writeFile = new BufferedWriter(new FileWriter(obfuscatedFile));

            String line = readFile.readLine();
            boolean multipleComment = false;
            Random randomNum = new Random(20);

            while (line != null) {
                String obfuscated_code = "";
                boolean singleComment = false;
                int r = randomNum.nextInt(10) ;
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
        String newStr = "";
        int curIn = 0;
        Pattern varFinder = Pattern.compile("\\b(?!%s|main|System|out|println|print|static|String|boolean|private|void|float|double|int|class|public|return|if|else|for|while|do|switch|case|default|break|continue|new|this|super|try|catch|finally|throw|throws|import|package|interface|extends|implements|abstract|final|native|strictfp|synchronized|transient|volatile|assert|enum|goto|const|instanceof|true|false|null)([a-zA-Z_][a-zA-Z0-9_]*)\\b");
        Matcher match = varFinder.matcher(str);
        while (match.find()){
            String keyWord = match.group(1);
            String encoded = Base64.getEncoder().encodeToString(keyWord.getBytes()).replace("=","");
            newStr += str.substring(curIn,match.start());
            newStr += encoded;
            curIn = match.end();
        }
        newStr += str.substring(curIn);
        
        Random randNum = new Random();
        int trashCodeNum = randNum.nextInt(10) + 1;
        String junkCode = "";
        for (int i = 0; i < trashCodeNum; i++){
            junkCode += "int ";
            junkCode += randString(randNum);
            junkCode +=  "= ";
            junkCode += randNum.nextInt(100);
            junkCode += "; for (int i = 0; i < 100; i++){int j = 0;}";
        }

        Pattern keyFinder = Pattern.compile("\\b(main)\\b");
        Matcher keyMatch = keyFinder.matcher(str);
        while (keyMatch.find()){
            newStr += obfuscate(junkCode);
        }
        return newStr;
    }

    public static String randString(Random rand){
        String str = "";
        String letters = "abcdefghiASFDLSAJjklmnopqrstuvwxyzZIEWQORJFSDKLFNZVXALFHQOAJ";
        for (int i = 0; i < 8; i ++){
            str += letters.charAt(rand.nextInt(letters.length()));
        }
        return str;
    }

}
