from digit import Digit


class Digits:
    zero = Digit("zero")
    one = Digit("one")
    two = Digit("two")
    three = Digit("three")
    four = Digit("four")
    five = Digit("five")
    six = Digit("six")
    seven = Digit("seven")
    eight = Digit("eight")
    nine = Digit("nine")

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

