



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
        
        return f"{real,imaginaryi}"

    def __str__(self) -> str:
        return ""




z1 = ComplexNumbers(2, 3,2,4)
z2 = ComplexNumbers()

print(z1.add_complex())
print(z2.print_normal_form_(1,2))