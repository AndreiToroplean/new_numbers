from enum import Enum

from digit import Digit


class Digits():
    zero = Digit("zero", "", "ten", 0)
    one = Digit("one", "ten", "eleven", 1)
    two = Digit("two", "twenty", "twelve", 2)
    three = Digit("three", "thirty", "thirteen", 3)
    four = Digit("four", "forty", "fourteen", 4)
    five = Digit("five", "fifty", "fifteen", 5)
    six = Digit("six", "sixty", "sixteen", 6)
    seven = Digit("seven", "seventy", "seventeen", 7)
    eight = Digit("eight", "eighty", "eighteen", 8)
    nine = Digit("nine", "ninety", "nineteen", 9)

    digits = zero, one, two, three, four, five, six, seven, eight, nine

    @classmethod
    def next(cls, digit):
        if digit == cls.nine:
            return cls.zero, True
        return cls.digits[cls.digits.index(digit) + 1], False

    @classmethod
    def previous(cls, digit):
        if digit == cls.zero:
            return cls.nine, True
        return cls.digits[cls.digits.index(digit) - 1], False
