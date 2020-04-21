from digits import Digits
from number import Number


def main():

    a = Number(Digits.one, Digits.zero, Digits.zero)
    b = Number(Digits.two, Digits.five)
    c = Number(Digits.five, is_positive=False)
    d = Number(Digits.one, is_positive=False)

    # print(b.next())

    print(b + b)


if __name__ == '__main__':
    main()
