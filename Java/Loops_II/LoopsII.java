import java.util.*;
import java.io.*;

class Solution{
    public static void main(String []argh){
        Scanner in = new Scanner(System.in);
        int t=in.nextInt();
        for(int i=0;i<t;i++){
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();
            int actualResult = a + 1 * b;
            System.out.print(actualResult);
            for (int pot=1; pot<n; pot ++){
                actualResult += (int) Math.pow(2, pot) * b;
                System.out.print(" " + actualResult);
            }
            System.out.println();
        }
        in.close();
    }
}