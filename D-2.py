from math import sqrt


class Rectangle:

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        result = self.height*self.width
        return f"{result:.2f}"

    def diagonal(self):
        result = sqrt(self.height**2 + self.width**2)
        return f"{result:.2f}"


if __name__ == "__main__":
    rectangle1 = Rectangle(height=5, width=6)
    print(rectangle1.area())  # 30.00
    print(rectangle1.diagonal())  # 7.81

    rectangle2 = Rectangle(height=3, width=3)
    print(rectangle2.area())  # 9.00
    print(rectangle2.diagonal())  # 4.24

