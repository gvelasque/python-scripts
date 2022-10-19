# 1528. Shuffle String

def shuffle_string(word: str, indices: list[int]) -> str:
    """
    Given a string "word" and an integer array "indices" of the same length.

    The string "word" will be shuffled such that the character at the ith
    position moves to indices[i] in the shuffled string.

    Return the shuffled string.

    Example 1:
        - Input: word = "codeleet", indices = [4,5,6,7,0,2,1,3]
        - Output: "leetcode"
        - Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.

    Example 2:
        - Input: word = "abc", indices = [0,1,2]
        - Output: "abc"
        - Explanation: After shuffling, each character remains in its position.

    Example 3:
        - Input: word = "aiohn", indices = [3,1,4,2,0]
        - Output: "nihao"

    Example 4:
        - Input: word = "aaiougrt", indices = [4,0,2,6,7,3,1,5]
        - Output: "arigatou"

    Example 5:
        - Input: word = "art", indices = [1,0,2]
        - Output: "rat"

    Constraints:
        - s.length == indices.length == n
        - 1 <= n <= 100
        - word contains only lower-case English letters.
        - 0 <= indices[i] < n
        - All values of indices are unique (i.e. indices is a permutation
        of the integers from 0 to n - 1).
    """

    # Check that the type of the word is a str
    if type(word) != str:
        raise TypeError("The word must be a str")

    # Check that the type of the array is a list
    if type(indices) != list:
        raise TypeError("The array must be a list")

    # Check all values of indices are unique
    if len(set(indices)) != len(indices):
        raise ValueError("The values of indices must be unique")

    # Check that the length of the word and indices are between 1 and 100"
    if len(word) < 1 or len(indices) < 1:
        raise ValueError("The length of the word and indices must be "
                         "between 1 and 100")

    if len(word) > 100 or len(indices) > 100:
        raise ValueError("The length of the word and indices must be "
                         "between 1 and 100")

    # Check word contains only lower-case English letters.
    if not word.islower() or not word.isalpha():
        raise ValueError("The word must be lower-case English letters.")

    for i in indices:
        # Check that the type of array items(indices) are integers
        if type(i) != int:
            raise TypeError("The array items(indices) must be integers")

        # Check that the length of the array items(indices) are
        # between 1 and 100"
        if i < 0 or i > 100:
            raise ValueError("The value of the array items(indices) must "
                             "be between 0 and 100")

    # zip() --> takes iterables (zero or more), aggregates them in a tuple
    return "".join(dict(sorted(zip(indices, word))).values())
