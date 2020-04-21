from itertools import zip_longest

from digits import Digits


class Number:
    def __init__(self, *digits, is_reversed=True, is_positive=True):
        if is_reversed:
            self.digits = list(reversed(digits))
        else:
            self.digits = list(digits)
        self.is_positive = is_positive

    def __eq__(self, other):
        if not hasattr(other, "digits") or not hasattr(other, "is_positive"):
            return NotImplemented
        if self.is_positive != other.is_positive:
            return False
        for self_digit, other_digit in zip_longest(self.digits, other.digits, fillvalue=Digits.zero):
            if self_digit != other_digit:
                return False

        return True

    def next(self):
        new_digits = []
        if self == self.__class__(Digits.one, is_positive=False):
            return self.__class__(Digits.zero)

        digits = self.digits
        while True:
            try:
                digit = digits.pop(0)
            except IndexError:  # When a new digit is needed to represent the number.
                digit = Digits.zero

            if self.is_positive:
                new_digit, carry = Digits.next(digit)
            else:
                new_digit, carry = Digits.previous(digit)
            new_digits.append(new_digit)
            if not carry:
                new_digits += digits
                break

        return self.__class__(*new_digits, is_reversed=False, is_positive=self.is_positive)

    def copy(self):
        return self.__class__(*self.digits, is_reversed=False, is_positive=self.is_positive)

    def __add__(self, other):
        counter = self.__class__(Digits.zero)
        rtn = self.copy()
        while counter != other:
            rtn = rtn.next()
            counter = counter.next()
        return rtn

    def __repr__(self):
        rtn = ""
        if not self.is_positive:
            rtn += "negative-"
        for digit in reversed(self.digits[1:]):
            rtn += f"{digit}-"
        rtn += f"{self.digits[0]}"
        return rtn
