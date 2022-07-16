# 1 - Create a Computation class with a default constructor(without parameters) allowing to perform various calculations on integers numbers.
# 2 - Create a method called Factorial() which allows to calculate the factorial of an integer. Test the method by instantiating the class.
# 3 - Create a method called Sum() allowing to calculate the sum of the first n integers 1 + 2 + 3 + .. + n. Test this method.
# 4 - Create a method called testPrim() in the Calculation class to test the primality of a given integer. Test this method.
# 4 - Create  a method called testPrims() allowing to test if two numbers are prime between them.
# 5 - Create a tableMult() method which creates and displays the multiplication table of a given integer. Then create an allTablesMult() method to display all the integer multiplication tables 1, 2, 3, ..., 9.
# 6 - Create a static listDiv() method that gets all the divisors of a given integer on new list called  Ldiv. Create another listDivPrim() method that gets all the prime divisors of a given integer.

class Computations:
    def __init__(self) -> None:
        pass

    @staticmethod
    def factorial(num):
        if num <= 1:
            return 1
        return num * Computations.factorial(num-1)

    @staticmethod
    def sum_integer(*args):
        return sum(args)

    def testPrim(self, num):
        for i in range(0, num):
            if num % i == 0:
                return False
            else:
                return True

    def testPrims(self, num1, num2):
        is_num1_prime = self.testPrim(num1)
        is_num2_prime = self.testPrim(num2)

        return all(is_num1_prime, is_num2_prime)

    def tableMult(self, num):
        for i in range(20):
            print(num * i)
            break
        return

    def allTablesMult(self):
        for i in range(10):
            self.tableMult(i)

        return

    @staticmethod
    def listDiv(num):
        Ldiv = []

        for i in range(num):
            if num % i == 0:
                Ldiv.append(i)

        return Ldiv

    @staticmethod
    def listDivPrime(nums: list):
        LPrimeDiv = []
        for num in nums:
            if Computations().testPrim(num):
                LPrimeDiv.append(num)

        return LPrimeDiv
