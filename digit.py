class Digit:
    def __init__(self, value, tens, teen):
        self.value = value
        self.tens = tens
        self.teen = teen

    def __repr__(self):
        return self.value

    def __eq__(self, other):
        return self.value == other.value
