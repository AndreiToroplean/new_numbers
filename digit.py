class Digit:
    def __init__(self, value, tens, teen, int_value):
        self.value = value
        self.tens = tens
        self.teen = teen
        self.int_value = int_value

    def __str__(self):
        return self.value
