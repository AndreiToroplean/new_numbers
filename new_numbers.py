from digits import Digits
from number import Number
from utilities import timer


@timer
def main():
    a = Number(Digits.eight)
    b = Number(Digits.seven)

    print(f"{a} + {b} = {a + b}")
    print(f"{a} * {b} = {a * b}")
    print(f"{a} ** {b} = {a ** b}")

    print()


if __name__ == '__main__':
    main()
