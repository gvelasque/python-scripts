# 169. Majority Element

import collections


def majority_element(nums: list[int]) -> int:
    """
    Given an array n of size n, return the majority element.

    The majority element is the element that appears more than [n/2] times.
    You may assume that the majority element always exists in the array.

    Example 1:
        - Input: nums = [3,2,3]
        - Output: 3

    Example 2
        - Input: nums = [2,2,1,1,1,2,2]
        - Output: 2

    Constraints
        - n == nums.length
        - 1 <= n <= 5*10^4
        - -2^31 <= nums[i] <= 2^31 -1
    """

    # Check that the type of the array is a list
    if type(nums) != list:
        raise TypeError("The array must be a list")

    # Check that the length of the array is between 1 and 5*10^4"
    if len(nums) < 1 or len(nums) > (5 * (10 ** 4)):
        raise ValueError(
            "The length of the array must be between 1 and 5*10^4")

    for n in nums:
        # Check that the type of array items are an integers
        if type(n) != int:
            raise TypeError("The array items must be an integers")

        # Check that the length of the array items is between -2^31
        # and 2^31 - 1"
        if n < -2 ** 31 or n > 2 ** 31 - 1:
            raise ValueError("The value of the array items must be between "
                             "-2^31 and 2^31 - 1")

    # This is the same as.
    # counter = {}
    # for n in nums:
    #    counter[n] = counter.get(n, 0) + 1
    # return max(counter.keys(), key=counter.get)
    counter = collections.Counter(nums)
    return max(counter.keys(), key=counter.get)
