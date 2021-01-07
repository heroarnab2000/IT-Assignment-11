from pattern import patterns
while True:
    print("1. Pattern 1")
    print("2. Pattern 2")
    print("3. Pattern 3")
    print("4. Pattern 4")
    print("5. Pattern 5")
    print("6. Exit")
    print("Enter your choice")
    ch = int(input("Enter your choice: "))

    if ch == 1:
        patterns.pat1()

    elif ch == 2:
        patterns.pat2()
        
    elif ch == 3:
        patterns.pat3()
        
    elif ch == 4:
        patterns.pat4()

    elif ch == 5:
        patterns.pat5()
        
    elif ch == 6:
        print("Goodbye!")
        break
    else:
        print("Wrong input.\n")