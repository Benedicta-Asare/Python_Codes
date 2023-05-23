class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squares = [value**2 for value in nums]
        squares.sort()
        return squares
