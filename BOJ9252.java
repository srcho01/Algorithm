import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ9252 {

    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s1 = br.readLine();
        String s2 = br.readLine();

        LCS(s1, s2);
    }

    private static void LCS(String s1, String s2) {

        int[][] dp = new int[s1.length() + 1][s2.length() + 1];
        int[][] lcs = new int[s1.length() + 1][s2.length() + 1];

        for (int i=1; i<=s1.length(); i++) {
            for (int j=1; j<=s2.length(); j++) {
                if (s1.charAt(i-1) == s2.charAt(j-1)) {
                    dp[i][j] = dp[i-1][j-1] + 1;
                    lcs[i][j] = 0;
                } else {
                    if (dp[i-1][j] > dp[i][j-1]) {
                        dp[i][j] = dp[i-1][j];
                        lcs[i][j] = 1;
                    } else {
                        dp[i][j] = dp[i][j-1];
                        lcs[i][j] = 2;
                    }
                }
            }
        }

        System.out.println(dp[s1.length()][s2.length()]);
        print(s1, lcs, s1.length(), s2.length());
        System.out.println(sb.reverse());

    }

    private static void print(String s, int[][] lcs, int i, int j) {
        if (i == 0 || j == 0) return;

        if (lcs[i][j] == 0) {
            sb.append(s.charAt(i-1));
            print(s, lcs, i-1, j-1);
        } else if (lcs[i][j] == 1) {
            print(s, lcs, i-1, j);
        } else if (lcs[i][j] == 2) {
            print(s, lcs, i, j-1);
        }
    }

}
