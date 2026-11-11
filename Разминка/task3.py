class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def fahrenheit(self):
        return self.celsius * 9 / 5 + 32

    def __str__(self):
        return f"{self.celsius:.1f} C = {self.fahrenheit:.1f} F"

    def __lt__(self, other):
        return self.celsius < other.celsius

temperatures = [Temperature(19), Temperature(-7), Temperature(28.5)]
for temp in sorted(temperatures):
    print(temp)
print("Самая высокая:", max(temperatures))
