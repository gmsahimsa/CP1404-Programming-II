COLOR_CODES = {"ABSOLUTE ZERO": "#0048ba", "ACID GREEN": "#b0bf1a", 'ALICE BLUE': "#f0f8ff", "ALIZARIN crimson": "#e32636", "AMARANTH": "#e52b50",
               "AMBER": "#ffbf00", "AMETHYST": "#9966cc", "ANTIQUEWHITE": "#faebd7", "ANTIQUEWHITE1": "#ffefdb", "ANTIQUEWHITE2": "#eedfcc"}

print(COLOR_CODES)
colour_name = input("Enter a colour name: ").upper()
while colour_name != "":
    if colour_name in COLOR_CODES:
        print(colour_name, "is", COLOR_CODES[colour_name])
    elif colour_name == "":
        break
    else:
        print("Invalid colour name")
    state_code = input("Enter a colour name: ").upper()

print ("A")