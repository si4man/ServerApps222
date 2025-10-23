from functools import reduce
import math

def max_strategy(strategies, data):
    results = {name: f(data) for name, f in strategies.items()}
    return max(results.items(), key=lambda kv: kv[1])[0]

def min_strategy(strategies, data):
    results = {name: f(data) for name, f in strategies.items()}
    return min(results.items(), key=lambda kv: kv[1])[0]

mean_arith = lambda d: reduce(lambda a, b: a + b, d, 0) / len(d)
mean_geom = lambda d: math.prod(d) ** (1 / len(d))
mean_harm = lambda d: len(d) / reduce(lambda acc, b: acc + 1 / b, d, 0)
median = lambda d: (lambda s: s[len(s)//2] if len(s) % 2 == 1 else (s[len(s)//2 - 1] + s[len(s)//2]) / 2)(sorted(d))

strategies = {
    "arithmetic": mean_arith,
    "geometric": mean_geom,
    "harmonic": mean_harm,
    "median": median
}

def main():
    data = (1, 2, 3, 4, 5)
    results = {name: f(data) for name, f in strategies.items()}
    print("Data:", data)
    print("\n")
    for k, v in results.items():
        print(k, "=", v)
    print("\nMin strategy:", min_strategy(strategies, data))
    print("Max strategy:", max_strategy(strategies, data))

if __name__ == "__main__":
    main()
