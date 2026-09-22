class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num1 = int("".join(map(str, digits)))
        total = num1 +1 

        res = [int(digit) for digit in str(total)]
        return res

        
        