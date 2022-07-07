



class ComplexNumbers:
    def __init__(self, real_a= 0, imaginary_a = 0,real_b = 0,imaginary_b = 0) -> None:
        self.real_a = float(real_a)
        self.imaginary_a = float(imaginary_a)
        self.real_b = float(real_b)
        self.imaginary_b = float(imaginary_b)
        
    
    def add_complex(self):
         return f"{self.real_a + self.real_b} + {self.imaginary_a + self.imaginary_b}i"
         

    def subtract_complex(self):

            return f"{self.real_a - self.real_b} + {self.imaginary_a - self.imaginary_b}i"

    @staticmethod
    def print_normal_form_(real, imaginary):
        
        return f"{real,imaginary}"

    def __str__(self) -> str:
        return ""




class Complex_Num:
    def __init__( self, real = 0, imaginary = 0 ):
        self.realPart = real
        self.imaginaryPart = imaginary
        
    def __add__( self, second_val ):
            real = self.realPart + second_val.realPart
            imaginary = self.imaginaryPart + second_val.imaginaryPart
            
            return Complex_Num( real, imaginary )
    def __sub__( self, second_val ):
        real = self.realPart - second_val.realPart
        imaginary = self.imaginaryPart - second_val.imaginaryPart
        return Complex_Num( real, imaginary )
    def __str__(self) -> str:
        return f"{self.realPart} + {self.imaginaryPart}i"

    @staticmethod
    def print_normal_form_(real, imaginary):
        
        return tuple(real,imaginary)
   



# z1 = ComplexNumbers(2, 3,2,4)
# z2 = ComplexNumbers()

z1 = Complex_Num(2, 3)
z2 = Complex_Num(2,4)
print(z1.__add__(z2))
print(z1.__sub__(z2))
print(z1.print_normal_form_(2,3))
