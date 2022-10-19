# 67. Add Binary


def add_binary(a: str, b: str) -> str:
    """
    Given two binary strings a and b, return their sum as a binary string.

    Example 1:
        Input: a = "11", b = "1"
        Output: "100"
    Example 2:
        Input: a = "1010", b = "1011"
        Output: "10101"
    Constraints:
        1 <= a.length, b.length <= 104
        a and b consist only of '0' or '1' characters.
        Each string does not contain leading zeros except for the zero itself.
    """

    if len(a) < 1 or len(a) > 104:
        raise ValueError("The range a has to be between 1 <= a <= 104")

    if len(b) < 1 or len(b) > 104:
        raise ValueError("The range a has to be between 1 <= a <= 104")

    for char in a:
        if char not in ['0', '1']:
            raise ValueError("a consist only of '0' or '1' characters.")

    for char in b:
        if char not in ['0', '1']:
            raise ValueError("b consist only of '0' or '1' characters.")

    carry, result = 0, ""
    a, b = list(a), list(b)
    while len(a) != 0 or len(b) != 0:
        print(a, b, carry)
        if a:
            carry += int(a.pop())
        if b:
            carry += int(b.pop())
        result += str(carry % 2)
        carry //= 2
    return result[::-1]
