# 258. Add Digits

def sum_digit(num: int) -> int:
    total = 0
    # Return the sum of the digits
    while num > 0:
        total = total + (num % 10)
        num = num // 10
    return total


def add_digits(num: int) -> int:
    """
    Given an integer num, repeatedly add all its digits until the result has
    only one digit, and return it.

    Example 1:
        - Input: num = 38
        - Output: 2ç
        - Explanation: The process is 38 --> 3 + 8 --> 11, 11 --> 1 + 1 -->
        2, Since 2 has only one digit, return it.

    Example 2:
        - Input: num = 0
        - Output: 0

    Constraints:
    - 0 <= num <= 231 - 1

    Follow up: Could you do it without any loop/recursion in O(1) runtime?
    """

    while num > 9:
        num = sum_digit(num)
    return num
