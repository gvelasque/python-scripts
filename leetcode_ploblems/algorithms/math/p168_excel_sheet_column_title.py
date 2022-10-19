# 168. Excel Sheet Column Title

def convert_to_title(column_number: int) -> str:
    """
    Given an integer columnNumber, return its corresponding column title as
    it appears in an Excel sheet.

    For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...

    Example 1:
        - Input: columnNumber = 1
        - Output: "A"

    Example 2:
        - Input: columnNumber = 28
        - Output: "AB"

    Example 3:
        - Input: columnNumber = 701
        - Output: "ZY":
    """
    result, capitals = [], []

    # Returns uppercase letters
    for x in range(ord('A'), ord('Z') + 1):
        capitals.append(chr(x))

    while column_number > 0:
        result.append(
            # Gets each letter in reverse order.
            capitals[(column_number % 26) - 1])
        column_number = (column_number - 1) // 26
    result.reverse()
    return ''.join(result)
