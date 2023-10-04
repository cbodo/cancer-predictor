class TextBox:
    name: str
    value: str
    disabled: bool

    def __init__(self, name, value, disabled):
        self.name = name
        self.value = value
        self.disabled = disabled

    def display_name(self):
        return self.name.replace("_", " ").title()