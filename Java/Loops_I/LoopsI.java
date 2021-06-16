public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(bufferedReader.readLine().trim());

        for (int actualMult = 1; actualMult <= 10; actualMult++){
            System.out.println(N + " x " + actualMult + " = " + N * actualMult);
        }

        bufferedReader.close();
    }
}