# 1470. Shuffle the Array

def shuffle_array(nums: list[int], n: int) -> list[int]:
    """
    Given the array nums consisting of 2n elements in the form
    [x1,x2,...,xn,y1,y2,...,yn].

    Return the array in the form [x1,y1,x2,y2,...,xn,yn].

    Example 1:
        - Input: nums = [2,5,1,3,4,7], n = 3
        - Output: [2,3,5,4,1,7]
        - Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the
        answer is [2,3,5,4,1,7].

    Example 2:
        - Input: nums = [1,2,3,4,4,3,2,1], n = 4
        - Output: nums = [1,4,2,3,3,2,4,1]

    Example 3:
        - Input: nums = [1,1,2,2], n = 2
        - Output: [1,2,1,2]

    Constraints:
        - 1 <= n <= 500
        - nums.length == 2n
        - 1 <= nums[i] <= 10^3
    """

    # Check that the type of the array is a list
    if type(nums) != list:
        raise TypeError("The array must be a list")

    # Check that the type of n is a list
    if type(n) != int:
        raise TypeError("The n must be a integer")

    # Check that the length of the array is 2n elements"
    if len(nums) != 2 * n:
        raise ValueError(
            "The length of the array must be 2n elements")

    # Check that the length of n is between 1 and 500"
    if n < 1 or 500 < n:
        raise ValueError(
            "The length of the array must be between 1 and 500")

    for i in nums:
        # Check that the type of array items are an integers
        if type(i) != int:
            raise TypeError("The array items must be an integers")

        # Check that the length of the array items is between 1 and 10^3"
        if i < 1 or i > 10 ** 3:
            raise ValueError("The value of the array items must be between "
                             "1 and 10^3")

    shuffle = []
    for i, j in zip(nums[:n], nums[n:]):
        shuffle += [i, j]

    return shuffle
