# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.


# input [3,2,4], target 6
# answer [1, 2]


def two_sum(nums: list, target: int) -> list:
    for i, num in enumerate(nums):
        for j, arr_num in enumerate(nums[i + 1 :]):
            if num + arr_num == target:
                return [i, j + i + 1]
    return []


assert two_sum([3, 2, 4], 6) == [1, 2], "should be [1,2]"
assert two_sum([2, 7, 11, 13], 9) == [0, 1], "should be [0,1]"
assert two_sum([3, 3], 6) == [0, 1], "should be [0,1]"
assert two_sum([3, 2, 3], 6) == [0, 2], "should be [0,2]"
