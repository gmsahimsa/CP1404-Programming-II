"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def print_report(monthly_incomes):
    """Prints report of monthly incomes and their cumulative total."""
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, len(monthly_incomes) + 1):
        income = monthly_incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


def main():
    """Displays income report for incomes over a given number of months."""
    monthly_incomes = []
    num_months = int(input("How many months? "))
    for month in range(1, num_months + 1):
        income = float(input("Enter income for month {}: ".format(str(month))))
        monthly_incomes.append(income)
    print_report(monthly_incomes)


main()
