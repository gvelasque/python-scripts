def find_max_consecutive_ones(nums: list[int]) -> int:
    """
    Given a binary array nums, return the maximum number of consecutive 1's
    in the array.

    Example 1:
        - Input: nums = [1,1,0,1,1,1]
        - Output: 3
        - Explanation: The first two digits or the last three digits are
        consecutive 1s. The maximum number of consecutive 1s is 3.

    Example 2:
        - Input: nums = [1,0,1,1,0,1]
        - Output: 2

    Constraints:
        - 1 <= nums.length <= 105
        - nums[i] is either 0 or 1.
    """
    counter, max_count = 0, []

    for i in nums:
        if i == 1:
            counter += 1
        else:
            max_count.append(counter)
            counter = 0
    else:
        max_count.append(counter)
    return max(max_count)
