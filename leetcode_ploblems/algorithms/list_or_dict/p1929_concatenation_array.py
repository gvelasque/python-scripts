# 1929. Concatenation of Array

def concatenation_array(nums: list[int]) -> list[int]:
    """
    Given an integer array nums of length n, you want to create an array
    ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i]
    for 0 <= i < n (0-indexed).

    Specifically, ans is the concatenation of two nums arrays.

    Return the array ans.

    Example 1:
        - Input: nums = [1,2,1]
        - Output: [1,2,1,1,2,1]
        - Explanation: [nums[0],nums[1],nums[2], nums[0],nums[1],nums[2]]

    Example 2:
        - Input: nums = [1,3,2,1]
        - Output: [1,3,2,1,1,3,2,1]
        - Explanation: [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],
            nums[2],nums[3]]

    Constraints:
        - n == nums.length
        - 1 <= n <= 1000
        - 1 <= nums[i] <= 1000
    """

    # Check that the type of the array is a list
    if type(nums) != list:
        raise TypeError("The array must be a list")

    # Check that the length of the array is between 1 and 1000"
    if len(nums) < 1 or 1000 < len(nums):
        raise ValueError("The length of the array must be between 1 and 1000")

    for n in nums:
        # Check that the type of array items are an integers
        if type(n) != int:
            raise TypeError("The array items must be an integers")

        # Check that the length of the array items is between 1 and 1000"
        if n < 1 or n > 1000:
            raise ValueError("The value of the array items must be between "
                             "1 and 1000")

    return nums * 2
