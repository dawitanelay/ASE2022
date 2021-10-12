import calculator as c

class FooCalculator:
    """docstring for ."""

    def __init__(self):
        pass
    def sum (self,m,n):
        return c.sum(m,n)
    def devide (self,m,n):
        return c.devide(self,m,n)

print('dawit')

cal1 = FooCalculator()

print(cal1.sum(4,7))
