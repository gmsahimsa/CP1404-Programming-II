from car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180, "Mazda")
    my_car.drive(30)
    print(f"{my_car}\n")

    limo = Car(100, "Limousine")
    limo.add_fuel(20)
    print(f"{limo}")
    limo.drive(115)
    print(f"After driving 115km: {limo}\n")


main()
