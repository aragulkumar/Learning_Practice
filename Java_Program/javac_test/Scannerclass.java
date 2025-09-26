package javac_test;
import java.util.Scanner;




public class Scannerclass {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (sc.hasNext()) {
            System.out.println(sc.next());
        }
        sc.close();
    }

    
}
