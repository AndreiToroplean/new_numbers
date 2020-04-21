from digits import Digits
from number import Number


def main():

    one_hundred = Number(Digits.one, Digits.zero, Digits.zero)
    # ten = Number(one, zero)

    # print(one_hundred + ten)

    print(Number.next(one_hundred))


if __name__ == '__main__':
    main()
