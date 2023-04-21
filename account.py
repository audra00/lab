class Account:

    def __init__(self, name) -> None:
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount) -> bool:
        """
        Method to deposit money into an account.
        :param amount: How much is being deposited into the account
        :return: Boolean value True or False depending on if money was successfully deposited in the account
        """
        if (amount <= 0):
            return False

        else:
            self.__account_balance += amount
            return True

    def withdraw(self, amount) -> bool:
        """
        Method to withdraw money from an account.
        :param amount: How much is being withdrawn from the account
        :return: Boolean value True or False depending on if money was successfully withdrawn from the account
        """
        if (amount <= 0):
            return False

        if (amount > self.__account_balance):
            return False

        else:
            self.__account_balance -= amount
            return True

    def get_balance(self) -> float:
        """
        Method to tell the account's balance to the user.
        :return: Balance in the account
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        Method to give the name of the account owner to the user.
        :return: Name of the account owner
        """
        return self.__account_name
