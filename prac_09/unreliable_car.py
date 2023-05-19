import random
from car import Car


class UnreliableCar(Car):
    """A class of Car that represents an unreliable car."""

    def __init__(self, name, fuel, reliability):
        """Initialize an UnreliableCar."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car only if the condition is met."""
        if random.randint(0, 100) < self.reliability:
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0
        return distance_driven
