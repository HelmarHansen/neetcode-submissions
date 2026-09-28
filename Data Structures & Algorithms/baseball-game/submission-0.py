class Solution:
    def calPoints(self, operations: List[str]) -> int:
        rec = []
        for op in operations:
            match op:
                case '+':
                    rec.append(rec[len(rec) - 1] + rec[len(rec) - 2])
                case 'D':
                    rec.append(rec[len(rec) - 1] * 2)
                case 'C':
                    rec.pop()
                case _:
                    rec.append(int(op))
        print(rec)
        return sum(rec)