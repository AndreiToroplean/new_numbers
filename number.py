from digits import Digits


class Number:
    def __init__(self, *digits):
        self.digits = list(reversed(digits))

    @classmethod
    def _next_from_digits(cls, digits):
        new_digits = []
        if digits[0] == Digits.nine:
            new_digits.append(Digits.zero)
            new_digits += cls._next_from_digits(digits[1:])
        else:
            new_digits.append(Digits.digits[Digits.digits.index(digits[0]) + 1])
            new_digits += digits[1:]
        return new_digits

    def next(self):
        return self.__init__(self._next_from_digits(self.digits))

    def __str__(self):
        rtn = ""
        for digit in self.digits:
            rtn += digit + " "
        return rtn
