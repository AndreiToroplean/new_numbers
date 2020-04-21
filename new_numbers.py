from digits import Digits
from number import Number


def main():
    num = Number(Digits.zero)

    while num != Number(Digits.one, Digits.zero, Digits.one):
        print(num)
        num = num.next()

    print(Number(Digits.one, Digits.one, Digits.one, Digits.one, Digits.one, Digits.one, Digits.one, Digits.one, Digits.one, Digits.one, ))


if __name__ == '__main__':
    main()
