class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        add = 0
        while n > 0:
            digit = n % 10
            product *= digit
            add += digit
            n //= 10
        return product - add
