from digits import Digits
from number import Number
from timer import timer


@timer
def main():
    a = Number(Digits.eight)
    b = Number(Digits.seven)

    print(f"{a} + {b} = {a + b}")
    print(f"{a} * {b} = {a * b}")
    print(f"{a} ** {b} = {a ** b}")


if __name__ == '__main__':
    main()
