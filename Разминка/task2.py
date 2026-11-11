class Counter:
    def __init__(self, name):
        self.name = name
        self.count = 0

    def add(self, n=1):
        self.count += n

    def reset(self):
        self.count = 0

    def __str__(self):
        return f"{self.name}: {self.count}"

right = Counter("верно")
wrong = Counter("ошибок")
right.add(4)
right.add()
wrong.add(2)
print(right, wrong)
right.reset()
print(right)
