
# Use integer variables to represent the data of the class—the numerator and the denominator.
# Provide a constructor that enables an object of this class to be initialized when it is declared. The
# constructor should contain default values, in case no initializers are provided, and should store the
# fraction in reduced form (i.e., the fraction
# 2 ---
# 4
# would be stored in the object as 1 in the numerator and 2 in the denominator). Provide methods for
# each of the following:
# a) Adding two RationalNumbers. The result should be stored in reduced form.
# b) Subtracting two RationalNumbers. The result should be stored in reduced form.
# c) Multiplying two RationalNumbers. The result should be stored in reduced form.
# d) Dividing two RationalNumbers. The result should be stored in reduced form.
# e) Printing RationalNumbers in the form a/b, where a is the numerator and b is the
# denominator.
# f) Printing RationalNumbers in floating-point format.


from fractions import Fraction

class RationalNumbers:
        def __init__(self,numerator_top = 1, denominator_bottom = 1) -> None:
                if denominator_bottom == 0:
                        raise ZeroDivisionError("Cannot have 0 denominator")
                self.numerator_top = int(numerator_top)
                self.denominator_bottom = int(denominator_bottom)
                
        @staticmethod
        def gcd( x, y ):
                """Computes greatest common divisor of two values"""
                while y:
                        z = x
                        x = y
                        y = z % y
                return x
        
        def __str__():
            return




# assign attribute values
# self.numerator = abs( top )
# self.denominator = abs( bottom )
# self.sign = ( top * bottom ) / ( self.numerator *
# self.denominator )
# self.simplify()
# Rational represented in reduced form
# class interface method
        def reduced_form( self ):
                common = RationalNumbers.gcd( self.numerator_top, self.denominator_bottom )
                self.numerator_top /= common
                self.denominator_bottom /= common
                return self.numerator_top / self.denominator_bottom
        
        def __neg__( self ):
                return RationalNumbers( -self.sign * self.numerator,self.denominator )
                # overloaded binary arithmetic operators
        def __add__( self, other ):
                return RationalNumbers(
                self.sign * self.numerator * other.denominator +
                other.sign * other.numerator * self.denominator,
                self.denominator * other.denominator )
        def __sub__( self, other ):
                return self + ( -other )
        def __mul__( self, other ):
               pass
        def __float__( self ):
                return self.sign * float( self.numerator ) / self.denominator