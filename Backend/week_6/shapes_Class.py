from abc import ABC, abstractmethod


class Shapes(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def volume(self):
        pass


class TwoDimensional(Shapes):
    def __init__(self):
        super().__init__()

    def area(self):
        pass

    def perimeter(self):
        pass


class Triangle(TwoDimensional):
    def __init__(self,):
        super(Triangle, self).__init__()

    @staticmethod
    def area(base, height):
        return 0.5 * height * base

    @staticmethod
    def perimeter(side_a, side_b, side_c):
        return side_a + side_b + side_c


class Circle(TwoDimensional):
    def __init__(self, radius):
        super(Circle, self).__init__()
        self.radius = radius

    def perimeter(self):

        return 2 * 3.14 * self.radius

    def area(self):
        return 3.14 * self.radius ** 2


class Square(TwoDimensional):
    def __init__(self):
        super().__init__()

    @staticmethod
    def area(length):
        return length**2

    @staticmethod
    def perimeter(length):
        return 4*length


class ThreeDimensional(Shapes):
    def __init__(self):
        pass


class Sphere(ThreeDimensional):
    def __init__(self):
        super(Sphere, self).__init__()

    @staticmethod
    def area(radius):
        return 4 * 3.14 * radius

    @staticmethod
    def volume(radius):
        V = 4/3 * 3.14 * radius**3
        return V


class Tetrahedron(ThreeDimensional):
    def __init__(self):
        super(Tetrahedron, self).__init__()

    @staticmethod
    def area(edge):
        A = (3**1/2) * edge * 2
        return A

    @staticmethod
    def volume(area):
        V = area ** 3 / (6 * (2**1/2))
        return V


class Cube(ThreeDimensional):
    def __init__(self):
        super().__init__()
        # self.edge = 0

    @staticmethod
    def area(edge):
        return 6 * (edge**2)

    @staticmethod
    def volume(edge):
        return edge**3


bigSphere = Sphere()
print(bigSphere.area(2))

cube1 = Cube()
print(cube1.area(2))


triangle = Triangle()
print(triangle.area(2, 3))


circle1 = Circle(5)
print(circle1.area())

square = Square()
print(square.area(2))

td = TwoDimensional()
