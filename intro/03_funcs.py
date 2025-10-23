from functools import reduce


lam1 = lambda: print("I`m a lambda")
x = 10
lam2 = None
lam3 = None
lam4 = None


def make_lam2() -> None:
    global lam2
    lam2 = lambda: print("x =", x)


def make_lam3() -> None:
    global lam3
    x = 20
    lam3 = lambda: print("x =", x)


def make_lam4() -> None:
    global lam4
    x = 40
    lam4 = lambda: print("x =", x)
    lam4()
    x = 50


def apply(lam, data):
    return lam(data)


def main():
    lam1()
    (lambda: print("I`m a IIFE"))()
    x = 30
    make_lam2()
    lam2()
    make_lam3()
    lam3()
    make_lam4()
    lam4()
    lam5 = lambda a, b: a + b
    print("lam5(2, 3) =", lam5(2, 3))
    data = (1, 2, 3, 4, 5)
    mean_a = lambda d: reduce(lambda a, b: a + b, d, 0) / len(d)
    mean_g = lambda d: reduce(lambda a, b: a * b, d, 1) ** (1 / len(d))
    mean_h = lambda d: len(d) / reduce(lambda acc, b: acc + 1 / b, d, 0)
    print(apply(mean_a, data))
    print(apply(mean_g, data))
    print(apply(mean_h, data))


if __name__ == "__main__":
    main()
