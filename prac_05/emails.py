def extract_name_from_email(emailid):
    """Extract the name from the given email"""
    name = " ".join(emailid.split("@")[0].split(".")).title()
    choice = input(f"Is your name {name}? (Y/n) ").lower()
    if choice != "" and choice != "y":
        name = input("Name: ").title()
    return name


def main():
    # Create an empty dictionary to store emails and names
    emails = {}
    while True:
        emailid = input("Email: ")
        if emailid == "":
            break
        name = extract_name_from_email(emailid)
        emails[emailid] = name
    for email, name in emails.items():
        print(f"{name} ({email})")


main()

print ("A")