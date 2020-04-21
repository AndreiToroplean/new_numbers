from digits import Digits


class Number:
    def __init__(self, *digits, is_reversed=True):
        if is_reversed:
            self.digits = list(reversed(digits))
        else:
            self.digits = list(digits)

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
        return Number(*self._next_from_digits(self.digits), is_reversed=False)

    def __repr__(self):
        rtn = ""
        for digit in reversed(self.digits[1:]):
            rtn += f"{digit}-"
        rtn += f"{self.digits[0]}"
        return rtn
