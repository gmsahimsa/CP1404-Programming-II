import csv


def read_csv(filename):
    """Read the csv file's data"""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        next(reader)
        data = []
        for row in reader:
            data.append(row)
    return data


def get_champions(data):
    """Get the list of champions"""
    champions = {}
    for row in data:
        player = row[4]
        year = row[1]
        if player in champions:
            champions[player].append(year)
        else:
            champions[player] = [year]
    return champions


def get_countries(data):
    """Get the list of countries"""
    countries = set()
    for row in data:
        country = row[1]
        countries.add(country)
    return sorted(countries)


def display_champions(champions):
    """Prints the name's of the Wimbledon Champions"""
    print("Wimbledon Champions: ")
    for player in sorted(champions):
        num_wins = len(champions[player])
        print(f"{player} {num_wins}")


def display_countries(countries):
    """Prints the list's of who have won Wimbledon"""
    print("\nThese {} countries have won Wimbledon: ".format(len(countries)))
    print(", ".join(countries))


def main():
    data = read_csv("wimbledon.csv")
    champions = get_champions(data)
    winning_countries = get_countries(data)
    display_champions(champions)
    display_countries(winning_countries)


main()
