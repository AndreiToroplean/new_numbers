class Digit:
    def __init__(self, value, tens):
        self.value = value
        self.tens = tens

    def __repr__(self):
        return self.value

    def __eq__(self, other):
        return self.value == other.value
