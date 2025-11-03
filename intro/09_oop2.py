class Point:
    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.x = x
        self.y = y

    def __str__(self):
        return "(%.2f, %.2f)" % (self.x, self.y)

    def __repr__(self):
        return "(%f, %f)" % (self.x, self.y)

    def magnitude(self):
        return (self.x**2 + self.y**2) ** 0.5

    def distance_to(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        else:
            raise TypeError("Unsupported operand type(s): Point and " + str(type(other)))

    def __sub__(self, other):
        if isinstance(other, Point):
            return Point(self.x - other.x, self.y - other.y)
        else:
            raise TypeError("Unsupported operand type(s): Point and " + str(type(other)))

    def __mul__(self, other):
        if isinstance(other, Point):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, (int, float)):
            return Point(self.x * other, self.y * other)
        else:
            raise TypeError("Unsupported operand type(s): Point and " + str(type(other)))

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("Division by zero is not allowed")
            return Point(self.x / other, self.y / other)
        else:
            raise TypeError("Unsupported '/' operands type: Point and " + str(type(other)))


def main():
    p1 = Point()
    print(p1)
    d = {"p2": Point()}
    print(d)
    p1.x = 3
    p1.y = 4
    print(p1.magnitude())
    d["p2"].x = 1
    d["p2"].y = 1
    print(p1.distance_to(d["p2"]))
    p2 = Point(2, 3)
    print(p1.distance_to(p2))
    p3 = Point(y=2)
    print("p3 =", p3)
    print("p1 = %s, p2 = %s, p1 + p2 = %s" % (p1, p2, p1 + p2))
    print("p1 = %s, p2 = %s, p1 - p2 = %s" % (p1, p2, p1 - p2))
    print("p1 = %s, p2 = %s, p1 * p2 = %s" % (p1, p2, p1 * p2))
    print("p1 = %s, p2 = %s, p1 * 2 = %s" % (p1, p2, p1 * 2))
    print("p1 = %s, p2 = %s, p1 / 2 = %s" % (p1, p2, p1 / 2))
    print("p1 = %s, p2 = %s, p1 / 2 = %s" % (p1, p2, p1 / 0))



if __name__ == "__main__":
    main()
