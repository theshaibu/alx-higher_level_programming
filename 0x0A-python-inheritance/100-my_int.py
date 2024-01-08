class MyInt(int):
    """
    MyInt class that inherits from int with inverted == and != operators.
    """

    def __eq__(self, other):
        """
        Inverts the behavior of the equality operator.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Inverts the behavior of the inequality operator.
        """
        return super().__eq__(other)

