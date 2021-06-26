import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {

        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        String reverse = "";
        char[] characters = A.toCharArray();
        for(int index=(A.length()-1); index >= 0; index --){
            reverse += characters[index];
        }
        if (A.equals(reverse)){
            System.out.println("Yes");
        } else{
            System.out.println("No");
        }
    }
}
