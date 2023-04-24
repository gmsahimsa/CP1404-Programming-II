class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        return self.typing == "Dynamic"

    def __str__(self):
        reflection_str = "Reflection=True" if self.reflection else "Reflection=False"
        return f"{self.name}, {self.typing} Typing, {reflection_str}, First appeared in {self.year}"
