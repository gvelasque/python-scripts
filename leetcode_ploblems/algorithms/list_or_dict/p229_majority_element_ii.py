# 229. Majority Element II

import collections


def majority_element(nums: list[int]) -> list[int]:
    """
    Given an integer array of size n, find all elements that appear more
    than [n/3] times.

    Example 1:
        - Input: nums = [3,2,3]
        - Output: [3]

    Example 2
        - Input: nums = [1]
        - Output: [1]

    Example 3
        - Input: nums = [1,2]
        - Output: [1,2]

    Constraints
        - 1 <= n <= 5*10^4
        - -10^9 <= nums[i] <= 10^9
    """

    # Check that the type of the array is a list
    if type(nums) != list:
        raise TypeError("The array must be a list")

    # Check that the length of the array is between 1 and 5*10^4"
    if len(nums) < 1 or 5 * 10 ** 4 < len(nums):
        raise ValueError(
            "The length of the array must be between 1 and 5*10^4")

    for n in nums:
        # Check that the type of array items are an integers
        if type(n) != int:
            raise TypeError("The array items must be an integers")

    valid_items = []
    for n, times in collections.Counter(nums).items():
        # Check that the type of array items are an integers
        if type(n) != int:
            raise TypeError("The array items must be an integers")
        # Check that the value of the array items is between -10^9 and 10^9"
        if n < -10 ** 9 or n > 10 ** 9:
            raise ValueError("The value of the array items must be between "
                             "-10^9 and 10^9")
        # Find all elements that appear more than [n/3] times.
        if len(nums) / 3 < times:
            valid_items.append(n)
    return valid_items
