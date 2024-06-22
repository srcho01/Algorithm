import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class BOJ2493 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(br.readLine().trim());
        Stack<Integer[]> stack = new Stack<>();
        for (int i = 0; i < n; i++) {
            int num = Integer.parseInt(st.nextToken());

            while (!stack.isEmpty()) {
                Integer[] item = stack.peek();
                int topId = item[0];
                int top = item[1];

                if (top > num) {
                    sb.append(topId + 1).append(" ");
                    break;
                }
                stack.pop();
            }
            if (stack.isEmpty()) {
                sb.append("0 ");
            }
            stack.push(new Integer[]{i, num});
        }

        System.out.println(sb.toString().trim());

        br.close();
    }
}
