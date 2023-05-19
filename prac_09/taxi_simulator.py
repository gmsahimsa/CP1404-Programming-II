from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def main():
    price_per_km = 1.23
    taxis = [Taxi("Prius", 100, price_per_km), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    total_cost = 0
    current_taxi = None

    print("Let's drive!")
    user_choice = get_menu_choice()

    while user_choice != 'q':
        if user_choice == 'c':
            display_taxis(taxis)
            current_taxi = get_taxi_choice(taxis)
        elif user_choice == 'd':
            if current_taxi:
                total_cost += drive_taxi(current_taxi)
            else:
                print("You need to choose a taxi before you can drive")
        print("Bill to date: ${:.2f}".format(total_cost))
        user_choice = get_menu_choice()

    print("Total trip cost: ${:.2f}".format(total_cost))
    print("Taxis are now:")
    display_taxis(taxis)


def get_menu_choice():
    print("q)uit, c)hoose taxi, d)rive")
    return input(">>> ").lower()


def display_taxis(taxis):
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))


def get_taxi_choice(taxis):
    taxi_choice = int(input("Choose taxi: "))
    if taxi_choice < 0 or taxi_choice >= len(taxis):
        print("Invalid taxi choice")
        return None
    return taxis[taxi_choice]


def drive_taxi(taxi):
    distance = float(input("Drive how far? "))
    taxi.drive(distance)
    cost = taxi.get_fare()
    print("Your {} trip cost you ${:.2f}".format(taxi.name, cost))
    return cost


main()
