# 1365. How Many Numbers Are Smaller Than the Current Number

def smaller_numbers_than_current(nums: list[int]) -> list[int]:
    """
    Given the array nums, for each nums[i] find out how many numbers in the
    array are smaller than it. That is, for each nums[i] you have to count
    the number of valid j's such that j != i and nums[j] < nums[i].

    Return the answer in an array.

    Example 1:
        - Input: nums = [8,1,2,2,3]
        - Output: [4,0,1,1,3]
        - Explanation: For nums[0]=8 there exist four smaller numbers than it
        (1, 2, 2 and 3). For nums[1]=1 does not exist any smaller number than
        it. For nums[2]=2 there exist one smaller number than it (1). For
        nums[3]=2 there exist one smaller number than it (1). For nums[4]=3
        there exist three smaller numbers than it (1, 2 and 2).

    Example 2:
        - Input: nums = [6,5,4,8]
        - Output: [2,1,0,3]

    Example 3:
        - Input: nums = [7,7,7,7]
        - Output: [0,0,0,0]

    Constraints:
        - 2 <= nums.length <= 500
        - 0 <= nums[i] <= 100
    """

    # Check that the type of the array is a list
    if type(nums) != list:
        raise TypeError("The array must be a list")

    # Check that the length of the array is between 2 and 500"
    if len(nums) < 2 or 500 < len(nums):
        raise ValueError(
            "The length of the array must be between 2 and 500")

    for n in nums:
        # Check that the type of array items are an integers
        if type(n) != int:
            raise TypeError("The array items must be an integers")

        # Check that the length of the array items is between 0 and 500"
        if n < 0 or n > 100:
            raise ValueError("The value of the array items must be between "
                             "0 and 500")
    sorted_nums = sorted(nums)
    return [sorted_nums.index(i) for i in nums]
