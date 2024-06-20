import java.util.Scanner;

public class BOJ5212 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int row = sc.nextInt();
        int col = sc.nextInt();
        sc.nextLine();

        char[][] map = new char[row][col];
        for (int i=0; i<row; i++) {
            String line = sc.nextLine();
            for (int j=0; j<col; j++) {
                map[i][j] = line.charAt(j);
            }
        }

        sc.close();

        char[][] newMap = new char[row][col];
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                int cnt = 0;
                newMap[i][j] = map[i][j];
                if (map[i][j] == 'X') {
                    if (i - 1 < 0 || map[i-1][j] == '.') cnt++;
                    if (i + 1 >= row || map[i+1][j] == '.') cnt++;
                    if (j - 1 < 0 || map[i][j-1] == '.') cnt++;
                    if (j + 1 >= col || map[i][j+1] == '.') cnt++;
                    if (cnt >= 3) newMap[i][j] = '.';
                }
            }
        }

        int rowStart = 0;
        int rowEnd = row;
        int colStart = 0;
        int colEnd = col;

        Loop1:
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (newMap[i][j] == 'X') {
                    rowStart = i;
                    break Loop1;
                }
            }
        }

        Loop2:
        for (int i = row-1; i >= 0; i--) {
            for (int j = 0; j < col; j++) {
                if (newMap[i][j] == 'X') {
                    rowEnd = i;
                    break Loop2;
                }
            }
        }

        Loop3:
        for (int j = 0; j < col; j++) {
            for (int i = 0; i < row; i++) {
                if (newMap[i][j] == 'X') {
                    colStart = j;
                    break Loop3;
                }
            }
        }

        Loop4:
        for (int j = col-1; j >= 0; j--) {
            for (int i = 0; i < row; i++) {
                if (newMap[i][j] == 'X') {
                    colEnd = j;
                    break Loop4;
                }
            }
        }

        for (int i = rowStart; i <= rowEnd; i++) {
            for (int j = colStart; j <= colEnd; j++) {
                System.out.print(newMap[i][j]);
            }
            System.out.println();
        }
    }
}