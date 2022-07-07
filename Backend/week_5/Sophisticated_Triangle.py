# Create a more sophisticated Rectangle class than the one you created in Exercise 7.6. This
# class stores only the x-y coordinates of the upper left-hand and lower right-hand corners of the rect-
# angle. The constructor calls a set function that accepts two tuples of coordinates and verifies that each
# of these is in the first quadrant, with no single x or y coordinate larger than 20.0. Methods calculate
# the length, width, perimeter and area. The length is the larger of the two dimensions. In-
# clude a predicate method isSquare that determines whether the rectangle is a square. Write a driver
# program to test the class.


class Sophisticated_triangle:
    def __init__(self, *args) -> None:
        print(args)
        self._coordinates = args 

    @property
    def set_coordinates(self):
        return self._coordinates
    
    @set_coordinates.setter
    def set_coordinates(self, *args):
        """Set width value"""
        for i in range(0,len(args)):
            if args[i] < 20.0 :
                self._coordinates[i] = args[i]
            else:
                raise ValueError("Invalid argument value(s), values must not be greater than 20 : %d", args)


    def length(self,*args):
        # max_val = args[0]
        # for i in range(len(args)):
        #     if args[i] > max_val:
        #         max_val = args[i]
        # self.__length = max_val
        args = self._coordinates
        if args[0] > args[2]:
            self.__length = args[0]
        else:
            self.__length =args[2]
        return self.__length

    def width(self,*args):
        args = self._coordinates
        if args[1] > args[3]:
            self.__width = args[1]
        else:
            self.__width =args[3]
        return self.__width

    def area(self):
        args = self._coordinates
        return args[0] * args[1] * args[2] * args[3]

    def perimeter(self):
        args = self._coordinates
        return args[0] + args[1] + args[2] + args[3]
    
    def isSquare(self):
        args = self._coordinates
        if args[0] == args[1] == args[2] == args[3]:
            return True
        else:
            return False



class Triangle_S:
    def __init__(self, vals_1,vals_2) -> None:
        
        self.cord_a = vals_1[0]
        self.cord_b = vals_1[1]
        self.cord_c = vals_2[0]
        self.cord_d = vals_2[1]



    def length(self):
        if self.cord_a > self.cord_c:
            self.__length = self.cord_a
        else:
            self.__length = self.cord_c
        return self.__length

    def width(self):
        if self.cord_b > self.cord_d:
            self.__width = self.cord_b
        else:
            self.__width = self.cord_d
        return self.__width

    def area(self):
       
        return self.cord_a * self.cord_b * self.cord_c * self.cord_d

    def perimeter(self):
        
        return self.cord_a + self.cord_b + self.cord_c + self.cord_d
    
    def isSquare(self):
        
        if self.cord_a == self.cord_b == self.cord_c == self.cord_d:
            return True
        else:
            return False










# s_Rect = Sophisticated_triangle((4, 6),(5,8))

# print(s_Rect.isSquare())
# print(s_Rect.length())
# print(s_Rect.width())

s_Rect = Triangle_S((4, 6),(5,8))

print(s_Rect.isSquare())
print(s_Rect.length())
print(s_Rect.width())
print(s_Rect.area())
print(s_Rect.perimeter())