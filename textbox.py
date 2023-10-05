class TextBox:
    name: str
    value: str
    min: float
    max: float

    def __init__(self, name, value, min, max):
        self.name = name
        self.value = value
        self.min = min
        self.max = max

    def display_name(self):
        return self.name.replace("_", " ").title()