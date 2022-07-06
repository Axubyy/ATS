# Create a class Rectangle. The class has attributes __length and __width, each of
# which defaults to 1. It has methods that calculate the perimeter and the area of the rectangle. It
# has set and get methods for both __length and __width. The set methods should verify that
# __length and __width are each floating-point numbers larger than 0.0 and less than 20.0. Write
# a driver program to test the class.
class Rectangle:
    def __init__(self,length,width) -> None:
        self.__length = length
        self.__width = width

    @property
    def set_length(self):
        return self.__length
    
    @set_length.setter
    def set_length(self,length):
        """Set length value"""
        if 0.0 < length < 20.0 and type(length) == float:
            self.__length = length
        else:
                raise ValueError("Invalid length value: %d" %length)


    @property
    def set_width(self):
        return self.__width
           
    @set_width.setter        
    def set_width( self, width ):
            """Set width value"""
            if 0 < width < 20.0 and type(width) == float:
                self.__width = width
            else:
                raise ValueError("Invalid width value: %d" %width)

    def area(self):
        return self.__length * self.__width

    def perimeter(self):
        return self.__length + self.__width

    def __str__(self) -> str:
         return ""


tri1 = Rectangle(10,4)
print(tri1.area())
print(tri1.perimeter())
