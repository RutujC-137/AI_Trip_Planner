class Calculator:
    @staticmethod
    def multiply(a: int,b: int)-> int:
        """
        Multiply two integers

        Args:
            a(int): The first Integer.
            b(int): The second integer.

        Returns:
            int: The product of a and b.

        """
        return a*b
    
    @staticmethod
    def calculate_total(*x: float)->float:
        """
        Calculate sum of the given list of numbers

        Args:
            x(list): list of floating numbers 
        returns:
            float: The sum of numbers in the list x 
        
        """

        return sum(x)
    
    @staticmethod
    def calculate_daily_budget(total: float, days: int )-> float:
        """
        Calculate daily Budget

        Args:
            Total(float): Total cost.
            days(int): Total number of days
        Returns:
            float: Expense for a single day
        """

        return total/days if days>0 else 0
    