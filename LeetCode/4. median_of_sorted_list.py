class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        n = len(nums)

        if n % 2 == 0:
            a = nums[n//2]
            b = nums[n//2 - 1]
            median = (a + b)/2
        else:
            median = nums[n//2]
        return median
