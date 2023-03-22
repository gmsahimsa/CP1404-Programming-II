def main():
    temperature = float(input("Enter temperature: "))
    unit = input("Enter unit Celcius (C) or Fahrenheit (F): ")

    if unit == "C":
        converted_temp = celsius_to_fahrenheit(temperature)
        print(f"{temperature}'C is {converted_temp}'F")
    elif unit == "F":
        converted_temp = fahrenheit_to_celsius(temperature)
        print(f"{temperature}'F is {converted_temp}'C")
    else:
        print("Invalid unit")


def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

main()