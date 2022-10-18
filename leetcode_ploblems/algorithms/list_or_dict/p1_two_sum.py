# 1. Two Sum

def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Given an array of integers nums and an integer target, return indices of
    the two numbers such that they add up to target.

    You may assume that each input would have exactly one solution, and you
    may not use the same element twice.

    You can return the answer in any order.

    Example 1:
        - Input: nums = [2,7,11,15], target = 9
        - Output: [0,1]
        - Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

    Example 2:
        - Input: nums = [3,2,4], target = 6
        - Output: [1,2]

    Example 3
        - Input: [3,3], target = 6
        - Output: [0,1]

    Constraints:
        - 2 <= nums.length <= 10^4
        - -10^9 <= nums[i] <= 10^9
        - -10^9 <= target <= 10^9
        - Only one valid answer exists.
    """

    # Check that the type of the array is a list
    if type(nums) != list:
        raise TypeError("The array must be a list")

    # Check that the type of the array is an integer
    if type(target) != int:
        raise TypeError("The array must be a an integer")

    # Check that the length of the array is between 2 and 10^4"
    if len(nums) < 2 or 10 ** 4 < len(nums):
        raise ValueError("The length of the array must be between 2 and 10^4")

    # Check that the length of the target is between -10^9 and 10^9"
    if target < -10 ** 9 or target > 10 ** 9:
        raise ValueError("The value of the target must be between "
                         "-10^9 and 10^9")

    for index, n in enumerate(nums):
        # Check that the type of array items are an integers
        if type(n) != int:
            raise TypeError("The array items must be an integers")

        # Check that the length of the array items is between -10^9 and 10^9"
        if n < -10 ** 9 or n > 10 ** 9:
            raise ValueError("The value of the array items must be between "
                             "-10^9 and 10^9")

        # Return indices of the two numbers such that they add up to target.
        if target - n in nums and index != nums.index(target - n):
            return [index, nums.index(target - n)]
