# Arbaz Khan
# 11/15/2022
# Problem 6 modifying the following code with the Python Class car

class car:
    def __init__(self, model, year, color, type, manufacturer):
        self.model = model
        self.year = year
        self.color = color
        self.type = type
        self.manufacturer = manufacturer
    def get_model(self):
        return self.model
    def get_year(self):
        return self.year
    def get_color(self):
        return self.color
    def get_type(self):
        return self.type
    def get_manufacturer(self):
        return self.manufacturer
    def fullspecs(self):
        return self.model + ' ' + str(self.year) + ' ' + self.color + self.type + self.manufacturer

car1 = car("Sports", 2022, "White"," coupe"," BMW")
car2 = car("SUV", 2022, "Black", "Model Y", " Tesla")

print(car1.get_color())
print(car1.get_model())
print(car2.get_color())
print(car1.fullspecs())
print(car2.fullspecs())