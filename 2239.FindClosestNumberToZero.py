from typing import List


def findClosestNumber(nums: List[int]) -> int:
        number = nums[0]
        for num in nums[1:]:
            
            abs_number = abs(number)
            abs_num = abs(num)
            if abs_num < abs_number:
                number = num
            elif abs_num == abs_number:
                if num > 0:
                    number = num
            
        return number

result1 = findClosestNumber([-4, -2, 1, 4, 8])
result2 = findClosestNumber([-4, -1, 1])

assert result1 == 1, f"Should be 1, but it is {result1}"
assert result2 == 1, f"Should be 1, but it is {result2}"