class Solution:
    def calPoints(self, operations: List[str]) -> int:
        records = []
        for item in operations:
            if item == "+":
                score = records[-1] + records[-2]
                records.append(score)
            elif item == "D":
                records.append(records[-1] * 2)
            elif item == "C":
                records.pop()
            else:
                records.append(int(item))

        return sum(records) 
