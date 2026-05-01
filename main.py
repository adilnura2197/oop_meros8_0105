class Vehicla:
    def __init__(self, speed, weight, fuel_type):
        self.speed = speed
        self.weight = weight
        self.fuel_type = fuel_type

    def drive(self):
        print("tezlik bn harakat")


class Bike(Vehicla):
    def __init__(self, speed, weight, fuel_type, bike_type, gear):
        super().__init__(speed, weight, fuel_type)
        self.bike_type = bike_type
        self.gear = gear

    def drive(self):
        super().drive()
        print(f"Bike_type: {self.bike_type}")


b1 = Bike(234, 12, "benzin", "bike", "stol")
b1.drive()
