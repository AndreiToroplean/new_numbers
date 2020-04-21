from digit import Digit


class Digits:
    zero = Digit("zero", "", "ten")
    one = Digit("one", "ten", "eleven")
    two = Digit("two", "twenty", "twelve")
    three = Digit("three", "thirty", "thirteen")
    four = Digit("four", "forty", "fourteen")
    five = Digit("five", "fifty", "fifteen")
    six = Digit("six", "sixty", "sixteen")
    seven = Digit("seven", "seventy", "seventeen")
    eight = Digit("eight", "eighty", "eighteen")
    nine = Digit("nine", "ninety", "nineteen")

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

