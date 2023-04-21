class Account:
    def __init__(self, name: str) -> None:
        """
        Function to set up account object.
        :param name: Account name
        """
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:
        """
        Function to deposit an amount into the account.
        :param amount: Amount to deposit in float format.
        :return: Return True if function is successful, False if function fails.
        """
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount: float) -> bool:
        """
        Function to withdraw an amount from the account
        :param amount: Amount to withdraw in float format.
        :return: Return True if function is successful, False if function fails.
        """
        if amount <= 0:
            return False
        elif amount > self.__account_balance:
            return False
        else:
            self.__account_balance -= amount
            return True

    def get_balance(self) -> float:
        """
        Function to check the balance of the account.
        :return: Return account balance in float format.
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        Function to check the name of the account.
        :return: Return account name in string format.
        """
        return self.__account_name
