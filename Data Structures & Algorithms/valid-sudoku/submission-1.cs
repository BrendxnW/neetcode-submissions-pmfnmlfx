public class Solution {
    public bool IsValidSudoku(char[][] board) {

        Dictionary<int, HashSet<int>> rows = new();
        Dictionary<int, HashSet<int>> cols = new();
        Dictionary<(int, int), HashSet<int>> squares = new();

        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                char digit = board[r][c];

                if (digit == '.') {
                    continue;
                }

                rows[r] = rows.GetValueOrDefault(r, new HashSet<int>());
                cols[c] = cols.GetValueOrDefault(c, new HashSet<int>());
                squares[(r / 3, c / 3)] = squares.GetValueOrDefault((r / 3, c / 3), new HashSet<int>());

                if (rows[r].Contains(digit) ||
                    cols[c].Contains(digit) ||
                    squares[(r / 3, c / 3)].Contains(digit)) {
                        return false;
                    }

                rows[r].Add(digit);
                cols[c].Add(digit);
                squares[(r / 3, c / 3)].Add(digit);

            }
        }
        return true;

    }
}
