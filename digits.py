from digit import Digit


class Digits:
    zero = Digit("zero", "")
    one = Digit("one", "ten")
    two = Digit("two", "twenty")
    three = Digit("three", "thirty")
    four = Digit("four", "forty")
    five = Digit("five", "fifty")
    six = Digit("six", "sixty")
    seven = Digit("seven", "seventy")
    eight = Digit("eight", "eighty")
    nine = Digit("nine", "ninety")

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

