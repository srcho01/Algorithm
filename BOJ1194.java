import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ1194 {

    static char[][] maze;
    static int n, m;

    static Queue<int[]> q;
    static boolean[][][] visited;

    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        maze = new char[n][m];
        q = new LinkedList<>();
        visited = new boolean[64][n][m];

        for (int i = 0; i < n; i++) {
            String line = br.readLine();
            for (int j = 0; j < m; j++) {
                char ch = line.charAt(j);
                maze[i][j] = ch;
                if (ch == '0') {
                    q.add(new int[]{i, j, 0, 0});
                    visited[0][i][j] = true;
                    maze[i][j] = '.';
                }
            }
        }

        System.out.println(bfs());
    }

    static int bfs() {
        while (!q.isEmpty()) {
            int[] polled = q.poll();
            int x = polled[0], y = polled[1];
            int dist = polled[2];
            int keys = polled[3];

            for (int k = 0; k < 4; k++) {
                int nx = x + dx[k];
                int ny = y + dy[k];

                if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
                if (maze[nx][ny] == '#' || visited[keys][nx][ny]) continue;

                if (maze[nx][ny] == '1') {
                    return dist + 1;
                } else if (maze[nx][ny] == '.') {
                    visited[keys][nx][ny] = true;
                    q.add(new int[]{nx, ny, dist + 1, keys});
                } else if ('a' <= maze[nx][ny] && maze[nx][ny] <= 'f') {
                    int nextKeys = keys | (1 << (maze[nx][ny] - 'a'));
                    if (!visited[nextKeys][nx][ny]) {
                        visited[nextKeys][nx][ny] = true;
                        q.add(new int[]{nx, ny, dist + 1, nextKeys});
                    }
                } else if ('A' <= maze[nx][ny] && maze[nx][ny] <= 'F') {
                    int targetKey = maze[nx][ny] - 'A';
                    if (((keys >> targetKey) & 1) == 1){
                        visited[keys][nx][ny] = true;
                        q.add(new int[]{nx, ny, dist + 1, keys});
                    }
                }
            }
        }

        return -1;
    }

}
