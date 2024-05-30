public class obRecursion {
    public static void main(String a[]) {
      System.out.println(b(4));
    }
    
    public static int b(int i) {
            if (i == 0){
                return 0;
            }
                return b(i - 1) + 2;
        }
}