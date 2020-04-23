from itertools import zip_longest

from digits import Digits


class Number:
    def __init__(self, *digits, is_reversed=True, is_positive=True):
        if is_reversed:
            self.digits = list(reversed(digits))
        else:
            self.digits = list(digits)
        self.is_positive = is_positive

    @classmethod
    def from_int(cls, int_):
        digit_conversion = {
            '0': Digits.zero,
            '1': Digits.one,
            '2': Digits.two,
            '3': Digits.three,
            '4': Digits.four,
            '5': Digits.five,
            '6': Digits.six,
            '7': Digits.seven,
            '8': Digits.eight,
            '9': Digits.nine
            }
        digits = []
        is_positive = True
        for digit in str(int_):
            if digit == '-':
                is_positive = False
                continue
            if digit == " ":
                continue
            digits.append(digit_conversion[digit])

        return cls(*digits, is_positive=is_positive)

    def to_int(self):
        rtn = 0
        for index, digit in enumerate(self.digits):
            rtn += digit.int_value * 10**index
        if not self.is_positive:
            rtn *= -1
        return rtn

    def __eq__(self, other):
        if not hasattr(other, "digits") or not hasattr(other, "is_positive"):
            return NotImplemented
        if self.is_positive != other.is_positive:
            return False
        for self_digit, other_digit in zip_longest(self.digits, other.digits, fillvalue=Digits.zero):
            if self_digit is not other_digit:
                return False

        return True

    def copy(self, in_place=False):
        if in_place:
            return self
        else:
            return self.__class__(*self.digits, is_reversed=False, is_positive=self.is_positive)

    def opposite(self, in_place=False):
        if self == self.__class__(Digits.zero):
            is_positive = True
        else:
            is_positive = not self.is_positive

        if in_place:
            self.is_positive = is_positive
            return self
        else:
            return self.__class__(*self.digits, is_reversed=False, is_positive=is_positive)

    def __abs__(self, in_place=False):
        if self.is_positive:
            return self.copy(in_place=in_place)
        return self.opposite(in_place=in_place)

    def next(self, in_place=False):
        new_digits = []
        if self == self.__class__(Digits.one, is_positive=False):
            new_digits.append(Digits.zero)
            is_positive = True
        else:
            abs_next = Digits.next if self.is_positive else Digits.previous
            digits = self.digits
            carry = True
            if digits[-1] == Digits.nine:
                digits.append(Digits.zero)
            while carry:
                digit = digits.pop(0)
                new_digit, carry = abs_next(digit)
                new_digits.append(new_digit)

            new_digits += digits
            is_positive = self.is_positive

        if in_place:
            self.digits = new_digits
            self.is_positive = is_positive
            return self
        else:
            return self.__class__(*new_digits, is_reversed=False, is_positive=is_positive)

    def previous(self, in_place=False):
        rtn = self.opposite(in_place=in_place)
        rtn = rtn.next(in_place=in_place)
        return rtn.opposite(in_place=in_place)

    def __add__(self, other, in_place=False):
        rtn = self.copy(in_place=in_place)
        counter = self.__class__(Digits.zero)
        rtn_abs_next = rtn.next if other.is_positive else rtn.previous
        counter_abs_next = counter.next if other.is_positive else counter.previous
        while counter != other:
            rtn = rtn_abs_next(in_place=True)
            counter = counter_abs_next(in_place=True)
        return rtn

    def __iadd__(self, other):
        return self.__add__(other, in_place=True)

    def __sub__(self, other, in_place=False):
        return self.__add__(other.opposite(), in_place=in_place)

    def __isub__(self, other):
        return self.__sub__(other, in_place=True)

    def __mul__(self, other, in_place=False):
        counter = self.__class__(Digits.one)
        if other.is_positive:
            rtn = self.copy(in_place=in_place)
            addend = rtn.copy()
        else:
            rtn = self.opposite(in_place=in_place)
            addend = rtn.copy()
        while counter != other.__abs__():
            rtn = rtn.__add__(addend, in_place=True)
            counter = counter.next(in_place=True)
        return rtn

    def __imul__(self, other):
        return self.__mul__(other, in_place=True)

    def __pow__(self, power, in_place=False):
        counter = self.__class__(Digits.one)
        if power.is_positive:
            rtn = self.copy(in_place=in_place)
            multiplier = rtn.copy()
        else:
            return NotImplemented
        while counter != power:
            rtn = rtn.__mul__(multiplier, in_place=True)
            counter = counter.next(in_place=True)
        return rtn

    def __ipow__(self, other):
        return self.__pow__(other, in_place=True)

    def __str__(self):
        rtn = ""
        if not self.is_positive:
            rtn += "negative "

        has_hundreds = False
        has_tens = False
        is_first = True
        is_teen = False
        for index, digit in reversed(list(enumerate(self.digits))):
            if digit != Digits.zero or is_first or is_teen:
                if has_hundreds:
                    rtn += " and"
                    has_hundreds = False
                if index % 3 == 1:
                    if not is_first:
                        rtn += " "
                    if digit != Digits.one:
                        rtn += digit.tens
                        has_tens = True
                    else:
                        is_teen = True
                else:
                    if has_tens:
                        rtn += "-"
                        has_tens = False
                    elif not is_first and not is_teen:
                        rtn += " "
                    if not is_teen:
                        rtn += str(digit)
                    else:
                        rtn += digit.teen
                        is_teen = False
                if index % 3 == 2:
                    rtn += " hundred"
                    has_hundreds = True
                is_first = False
            if index == 0:
                continue
            if index == 3:
                rtn += " thousand,"
            elif index == 6:
                rtn += " million,"
            elif index == 9:
                rtn += " billion,"
            elif index % 3 == 0:
                rtn += " zillion,"
        return rtn

    def __repr__(self):
        return f"Number({', '.join(f'Digits.{x}' for x in self.digits)}{', is_positive=False' if not self.is_positive else ''})"
        # Huge cheat, I don't like it.
