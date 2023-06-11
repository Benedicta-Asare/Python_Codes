class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str_num = ''.join([str(i) for i in digits])
        n = int(str_num)
        n += 1
        x = [int(digit) for digit in str(n)]
        return x
