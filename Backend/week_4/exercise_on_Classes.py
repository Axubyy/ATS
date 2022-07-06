# class Shapes:
#     def __init__(self, base, height, length, radius, num_sides):
#         self.num_sides = num_sides
#         self.base = base
#         self.height = height
#         self.length = length
#         self.radius = radius

#     def input_values(self):
#         self.sides = [float(input("Enter side " + str(i + 1) + " : ")) for i in range(self.n)]


class Triangle:
    def __init__(self):
        pass

    def area(self, base, height):
        return 0.5 * height * base

    def perimeter(self, side_a, side_b, side_c):
        return side_a + side_b + side_c


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

    def area(self):
        return 3.14 * self.radius ** 2


class Trapezium:
    def __init__(self):
        pass

    def area(self, a, b, h):
        return (a + b / 2) * h

    def perimeter(self, a, b, c, d):
        return a + b + c + d


triangle1 = Triangle()
trape = Trapezium()

round_circle = Circle(10)

print(triangle1.area(24, 35))
print(trape.perimeter(1, 2, 3, 4))
print(round_circle.area())
