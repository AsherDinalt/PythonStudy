class Cars:
    wheels_number = 4
    doors_number : int
    chairs_number : int
    def __init__(self, name =""):
        self.name = name

mazda_car = Cars("Mazda CZ7")
bmw_car = Cars("BMW")
bmw_car.doors_number=4
mazda_car.wheels_number = 6
mazda_car.doors_number = 2
print(mazda_car.wheels_number)
print(mazda_car.doors_number)
print("==============")
print(bmw_car.wheels_number)
print(bmw_car.doors_number)


