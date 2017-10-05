"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from prac_07.car import Car


def main():
    """Demo test code to show how to use car class."""
    limo = Car(100)
    my_car = Car(180)
    limo.drive(115)
    limo.add_fuel(20)
    print("fuel =", limo.fuel)
    print("odo =", limo.odometer)
    print(limo)

    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))


main()