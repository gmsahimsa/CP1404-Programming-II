from taxi import Taxi


class SilverServiceTaxi(Taxi):
    FLAGFALL = 4.50

    def __init__(self, name, fuel, price_per_km, fanciness=1.0):
        super().__init__(name, fuel, price_per_km)
        self.fanciness = fanciness
        self.price_per_km *= self.fanciness

    def get_fare(self):
        """Return the price for the taxi trip."""
        return super().get_fare() + self.FLAGFALL

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return "{}, ${:.2f}/km plus flagfall of ${:.2f}".format(
            super().__str__(), self.price_per_km, self.FLAGFALL
        )
