from animals import birds, amphibians, fish, mammals, reptiles

while True:
    print("1. Birds")
    print("2. Amphibians")
    print("3. Fish")
    print("4. Mammals")
    print("5. Reptiles")
    print("6. Exit")
    print("Enter your choice")
    ch = int(input("Enter your choice: "))

    if ch == 1:
        birds.examples()
        birds.characteristics()
    elif ch == 2:
        amphibians.examples()
        amphibians.characteristics()
    elif ch == 3:
        fish.examples()
        fish.characteristics()
    elif ch == 4:
        mammals.examples()
        mammals.characteristics()
    elif ch == 5:
        reptiles.examples()
        reptiles.characteristics()
    elif ch == 6:
        print("Goodbye!")
        break
    else:
        print("Wrong input.\n")