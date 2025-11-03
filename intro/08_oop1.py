class Point:
    x = 0
    y = 0


def main():
    p1 = Point()
    print(p1.x, p1.y)
    Point.x = 10
    print(p1.x, p1.y)
    p2 = Point()
    print(p2.x, p2.y)
    p1.x = 20
    print(p1.x, p2.x)
    del p1.x
    print(p1.x, p2.x)
    Point.w=30
    print(p1.w, p2.w)


if __name__ == "__main__":
    main()
