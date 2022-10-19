# 7. Reverse Integer


def reversed_int(num: int) -> int:
    """
    Given a signed 32-bit integer x, return 'num' with its digits reversed. If
    reversing 'num' causes the value to go outside the signed 32-bit integer
    range [-231, 231 - 1], then return 0.

    Assume the environment does not allow you to store 64-bit integers (
    signed or unsigned).

    Example 1:
      - Input: x = 123
      - Output: 321
    Example 2:
      - Input: x = -123
      - Output: -321
    Example 3:
      - Input: x = 120
      - Output: 21
    Constraints:
      - -2^31 <= x <= 2^31 - 1
    """
    if num.bit_length() > 32:
        raise ValueError("The range has to be between -2^31 <= x <= 2^31 - 1")

    if type(num) != int:
        raise TypeError("The array must be a integer")

    result = 0
    operator = num

    if num < 0:
        operator = -operator

    while operator > 0:
        remainder = operator % 10
        result = result * 10 + remainder
        operator //= 10
    return result if num > 0 else -result
