# 1672. Richest Customer Wealth

def richest_customer_wealth(accounts: list[list[int]]) -> int:
    """
    You are given a customer x accounts integer grid accounts where
    accounts[i][j] is the amount of money the ith customer has in the jth
    bank. Return the wealth hat the richest customer has.

    A customer's wealth is the amount of money they have in all their bank
    accounts. The richest customer is the customer that has the maximum wealth.

    Example 1:
        - Input: accounts = [[1,2,3],[3,2,1]]
        - Output: 6
        - Explanation: 1st customer has wealth = 1 + 2 + 3 = 6, 2nd customer
        has wealth = 3 + 2 + 1 = 6 Both customers are considered the richest
        with a wealth of 6 each, so return 6.

    Example 2:
        - Input: accounts = [[1,5],[7,3],[3,5]]
        - Output: 10
        - Explanation: 1st customer has wealth = 6, 2nd customer has
        wealth = 10, 3rd customer has wealth = 8, The 2nd customer is the
        richest with a wealth of 10.

    Example 3:
        - Input: accounts = [[2,8,7],[7,1,3],[1,9,5]]
        - Output: 17

    Constraints:
        - customer == accounts.length ---> customer length
        - accounts == accounts[i].length ---> Length of each customer accounts
        - 1 <= customer, accounts <= 50
        - 1 <= accounts[i][j] <= 100 ---> Wealth of each accounts
    """

    # Check that the type of accounts is a list
    if type(accounts) != list:
        raise TypeError("The accounts must be a list")

    # Check that the length of accounts is greater than or equal that one
    if len(accounts) < 1:
        raise ValueError("The length of accounts must be greater than "
                         "or equal that one")

    customers_wealth = []
    for customer_account in accounts:
        # Check that the type of customers accounts is a list
        if type(customer_account) != list:
            raise TypeError("The customers accounts must be a list")
        # Check that the length of customers accounts is less than or equal 50
        if 50 < len(customer_account):
            raise ValueError("The length of customer_account must be "
                             "less than or equal 50")

        # Check the type and length of account wealth
        for account_wealth in customer_account:
            # Check that the type of account wealth is an integer
            if type(account_wealth) != int:
                raise TypeError("The type of account wealth must be an integer")
            # Check that the length of account wealth is between 1 and 100"
            if account_wealth < 1 or 100 < account_wealth:
                raise ValueError("The length of account wealth must be "
                                 "between 1 and 100")

        customers_wealth.append(sum(customer_account))

    return max(customers_wealth)
