from digits import Digits
from number import Number


def main():

    a = Number(Digits.one, Digits.zero, Digits.zero)
    b = Number(Digits.two, Digits.five)
    c = Number(Digits.five, is_positive=False)
    d = Number(Digits.one, is_positive=False)
    e = Number(Digits.three)
    f = Number(Digits.five)

    print(b*e)


if __name__ == '__main__':
    main()
