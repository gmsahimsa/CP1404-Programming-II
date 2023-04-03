"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    display_subject_details(data)


def get_data():
    """Read data from subject_data.txt and formats it"""
    input_file = open(FILENAME)
    data = []
    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        parts[2] = int(parts[2])
        data.append(parts)
    input_file.close()
    return data


def display_subject_details(data):
    """Displays subject details for each subject."""
    for subject in data:
        print("{} is taught by {} and has {} students".format(subject[0], subject[1], subject[2]))


main()
