class Solution:
    def averageValue(self, nums: List[int]) -> int:
        new_nums = [num for num in nums if num % 2 == 0 and num % 3 == 0]

        if len(new_nums) == 0:
            return 0
        else: 
            avg = sum(new_nums) / len(new_nums)
            return int(avg)
