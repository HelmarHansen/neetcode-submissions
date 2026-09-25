class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols, boxes = [set() for _ in range(9)], [set() for _ in range(9)], [set() for _ in range(9)]


        for i, row in enumerate(board):
            for j, col in enumerate(row):
                boxIndex =  3 * (i // 3) + j // 3
                if col == ".":
                    continue
                if col in rows[i] or col in cols[j] or col in boxes[boxIndex]:
                    print(col, i, j, boxIndex)
                    print(boxes[boxIndex])
                    return False
                print("pos", i, j, boxIndex)
                rows[i].add(col)
                cols[j].add(col)
                boxes[boxIndex].add(col)
                #print("rows", rows[i])
                #print("cols", cols[j])
                print("boxes", boxes)
        return True
