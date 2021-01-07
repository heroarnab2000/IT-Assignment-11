def pat1():
    r = int(input("Enter no. of rows: "))
    for i in range(r + 1):
        for j in range(i):
            print("*", end = '')
        print("")

def pat2():
    r = int(input("Enter no. of rows: "))
    for i in range(1, r+1):
        for sp in range(1, r-i+1):
            print(" ", end = '')
        for j in range(1,2*i):
            print("*", end = '')
        print("")

def pat3():
    r=int(input("Enter no. of rows: "))
    for i in range(1,r+1):
        for sp in range(r-i,0,-1):
            print(" ",end='')
        for j in range(1,i+1):
            print("*",end='')
        print("\n")
def pat4():
    r=int(input("Enter no. of rows: "))
    for i in range(1,r+1):
        for j in range(1,i+1):
            print(j,end='')
        print("\n")

def pat5():
    c=1
    r=int(input("Enter no. of rows: "))
    for i in range(1,r+1):
        for j in range(1,i+1):
            print(c," ",end='')
            c+=1
        print("\n")