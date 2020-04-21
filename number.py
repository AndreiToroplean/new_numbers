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

    def copy(self):
        return self.__class__(*self.digits, is_reversed=False, is_positive=self.is_positive)

    def opposite(self):
        if self != self.__class__(Digits.zero):
            return self.__class__(*self.digits, is_reversed=False, is_positive=not self.is_positive)
        return self.copy()

    def __abs__(self):
        if self.is_positive:
            return self.copy()
        return self.opposite()

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

    def previous(self):
        rtn = self.opposite()
        rtn = rtn.next()
        return rtn.opposite()

    def __add__(self, other):
        counter = self.__class__(Digits.zero)
        rtn = self.copy()
        while counter != other:
            if other.is_positive:
                rtn = rtn.next()
                counter = counter.next()
            else:
                rtn = rtn.previous()
                counter = counter.previous()
        return rtn

    def __mul__(self, other):
        counter = self.__class__(Digits.zero)
        rtn = self.__class__(Digits.zero)
        if other.is_positive:
            addend = self.copy()
        else:
            addend = self.opposite()
        while counter != abs(other):
            rtn = rtn + addend
            counter = counter.next()
        return rtn

    def __repr__(self):
        rtn = ""
        if not self.is_positive:
            rtn += "negative "

        has_hundreds = False
        has_tens = False
        is_first = True
        for index, digit in reversed(list(enumerate(self.digits))):
            if digit != Digits.zero or is_first:
                if has_hundreds:
                    rtn += " and"
                    has_hundreds = False
                if index % 3 == 1:
                    if not is_first:
                        rtn += " "
                    rtn += digit.tens
                    has_tens = True
                else:
                    if has_tens:
                        rtn += "-"
                        has_tens = False
                    elif not is_first:
                        rtn += " "
                    rtn += repr(digit)
                if index % 3 == 2:
                    rtn += " hundred"
                    has_hundreds = True
                is_first = False
            if index == 0:
                continue
            if index == 3:
                rtn += " thousand"
            elif index == 6:
                rtn += " million"
            elif index == 9:
                rtn += " billion"
            elif index % 3 == 0:
                rtn += " zillion"
        return rtn
