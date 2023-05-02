import csv
from guitar import Guitar


def load_guitars():
    guitars = []
    with open("guitars.csv", "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            name, year, cost = row
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars


def save_guitars(guitars):
    with open("guitars.csv", "w", newline="") as file:
        writer = csv.writer(file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])


def main():
    guitars = load_guitars()
    for guitar in guitars:
        print(guitar)

    guitars.sort()
    print("\n___ Sorted by year ____")
    for guitar in guitars:
        print(guitar)

    print("\nAdd A New Guitar")
    while True:
        name = input("Name: ")
        if not name:
            break
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitars.append(Guitar(name, year, cost))
        print(f"{name} ({year}) : ${cost:,.2f} added.\n")

    save_guitars(guitars)
    print("Guitars saved to guitars.csv")


if __name__ == "__main__":
    main()
