CURRENT_YEAR = 2017
class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost
        self.age = CURRENT_YEAR - year

    def __str__(self):
        return "{:<15} ({}) : ${:,.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        return self.age

    def is_vintage(self):
        if self.age >= 50:
            return True
        else:
            return False
