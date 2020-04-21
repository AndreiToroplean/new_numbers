from digits import Digits
from number import Number


def main():

    a = Number(Digits.one, Digits.zero, Digits.zero)
    b = Number(Digits.two, Digits.five)

    print(b.next())

    # print(a + b)


if __name__ == '__main__':
    main()
