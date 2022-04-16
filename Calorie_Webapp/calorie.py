class Calorie:
    """Represent amount of calories calculated with
    BMR = 10 * weight + 6.25 * height - 5 * age + 5 - 10 * temperature
    """

    def __init__(self, weight, height, age, temperature):
        self.temperature = temperature
        self.age = age
        self.weight = weight
        self.height = height

    def calculate(self):
        pass
