"""
Menus
"""
name = input("Enter name: ")

while True:
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")
    choice = input(">>> ").upper()
    if choice == "H":
        print("Hello", name)
    elif choice == "G":
        print("Goodbye", name)
    elif choice == "Q":
        break
    else:
        print("Invalid choice")

print("Finished.")
