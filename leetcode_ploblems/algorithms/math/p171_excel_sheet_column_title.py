# 171. Excel Sheet Column Number

def title_to_number(column_title: str) -> int:
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
        - Output: "ZY"

    Constraints:
        - 1 <= columnNumber <= 231 - 1
    """
    result = 0

    # Return the value of the s as an integer.
    for i in column_title:
        result = ((result * 26) + ord(i) - ord('A') + 1)
    return result
