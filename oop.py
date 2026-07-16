class Vehicle:
    wheels = 4

    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} is starting...")

    @classmethod
    def wheel_count(cls):
        print(f"Vehicles usually have {cls.wheels} wheels.")

    @staticmethod
    def honk():
        print("Beep Beep!")

class Car(Vehicle):

    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def start(self):
        print(f"{self.brand} {self.model} starts with a button.")

car = Car("Toyota", "Corolla")

car.start()          # Overridden method
Car.wheel_count()    # Class method
Car.honk()           # Static method