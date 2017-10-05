from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness
        super().__init__(name, fuel)

    def get_fare(self):
        return self.price_per_km * self.current_fare_distance + self.flagfall

    def __str__(self):
        return "{} plus flagfall of ${:.2f}".format(super().__str__(), self.flagfall)
