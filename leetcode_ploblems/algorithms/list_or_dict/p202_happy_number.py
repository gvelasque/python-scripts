# 202. Happy Number

def pdi(num: int, base: int = 10) -> int:
    total = 0

    # Return perfect digital invariant (PDI).
    while num > 0:
        total = total + pow(num % base, 2)
        num = num // base
    return total


def is_happy(n: int) -> bool:
    """
    Write an algorithm to determine if a number n is happy.

    A happy number is a number defined by the following process:
    
        - Starting with any positive integer, replace the number by the sum
        of the squares of its digits.
        - Repeat the process until the number equals
        1 ( where it will stay), or it loops endlessly in a cycle which does
        not include 1.
        - Those numbers for which this process ends in 1 are happy.

    Return true if n is a happy number, and false if not.

    Example 1:
        - Input: n = 19
        - Output: true
        - Explanation:
        12 + 92 = 82,
        82 + 22 = 68,
        62 + 82 = 100,
        12 + 02 + 02 = 1

    Example 2:
        - Input: n = 2
        - Output: false

    Constraints:
        - 1 <= n <= 231 - 1
    """
    sequence = []

    # check if number is greater than one and is not in sequence.
    while n > 1 and n not in sequence:
        sequence.append(n)  # add number in the sequence.
        n = pdi(n)
    return n == 1
