class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        size = 9
        rows = [set() for _ in range(size)]
        cols = [set() for _ in range(size)]
        boxes = [set() for _ in range(size)]

        for r in range(size):
            for c in range(size):
                val = board[r][c]

                if val == '.':
                    continue
                # check columns
                if val in cols[c]:
                    return False
                cols[c].add(val)

                # check rows
                if val in rows[r]:
                    return False
                rows[r].add(val)

                # check 3x3 boxes
                box_index = (r // 3) * 3 + (c // 3)
                if val in boxes[box_index]:
                    return False
                boxes[box_index].add(val)
        return True


        
