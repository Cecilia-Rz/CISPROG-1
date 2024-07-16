print("--------------------------------------------------------------------------------")
print("---------------------------Welcome To Chaffey Airlines--------------------------")
print("--------------------------------------------------------------------------------")
print("-----------------CA Travel System by Final Project Group 3----------------------")
print("-----------(By Cecilia Rodriguez, Joshua Schumperli, Adam Schumperli)-----------")
print("--------------------------------------------------------------------------------")
#Determines change left from user payment
def money(change):
    oneHundred = int(0)
    twenty = int(0)
    ten = int(0)
    five = int(0)
    one = int(0)
    quarter = int(0)
    dime = int(0)
    nickel = int(0)
    penny = int(0)
    while round(float(change), 2) != float(0):
        if change >= 100:
            oneHundred += 1
            change -= 100
        elif change >= 20:
            twenty += 1
            change -= 20
        elif change >= 10:
            ten += 1
            change -= 10
        elif change >= 5:
            five += 1
            change -= 5
        elif change >= 1:
            one += 1
            change -= 1
        elif change >= 0.25:
            quarter += 1
            change -= 0.25
        elif change >= 0.10:
            dime += 1
            change -= 0.10
        elif change >= 0.05:
            nickel += 1
            change -= 0.05
        elif change >= 0.01:
            penny += 1
            change -= 0.01
    print("$100 bills: " + str(oneHundred))
    print("$20 bills: " + str(twenty))
    print("$10 bills: " + str(ten))
    print("$5 bills " + str(five))
    print("$1 bills: " + str(one))
    print("Quarters: " + str(quarter))
    print("Dimes: " + str(dime))
    print("Nickels: " + str(nickel))
    print("Pennies: " + str(penny))


print("What would you like to do? ")
print("a) Make a new first class reservation. ")
print("b) Make a new coach class reservation. ")
print("c) Change an existing reservation. ")
print("d) Print seat listing. ")
print("e) Quit")
#seats available for both fist class and coach class
fClass = 8
cClass = 40
pColumnA = ["Open", "Open", "Open", "Open"]
pColumnB = ["Open", "Open", "Open", "Open"]
cColumnA = ["Open", "Open", "Open", "Open", "Open", "Open", "Open", "Open", "Open","Open"]
cColumnB = ["Open", "Open", "Open", "Open", "Open", "Open", "Open", "Open", "Open","Open"]
cColumnC = ["Open", "Open", "Open", "Open", "Open", "Open", "Open", "Open", "Open","Open"]
cColumnD = ["Open", "Open", "Open", "Open", "Open", "Open", "Open", "Open", "Open","Open"]
Name = ""
while True:
    choice = input("Enter choice(a,b,c,d,e): ")
    number = 0

    def PcheckA():
        Name = input("What is your name?: ")
        Age = input("What is your age?: ")
        cost = 545
        if int(Age) <= 7 or int(Age) >= 65:
            cost = 436
            print("You get a 20% discount")
        payment = input("This seat will be $" + str(cost) + " (9% tax) Please input amount given: ")
        if int(payment) >= cost:
            change = float(payment) - float(cost)
            print("Your change will be $" + str(round(change, 2)) + " and your seat has been reserved")
            money(change)
            print("Thank you for your purchase. Have a nice day.")
            count = len(Name)
            if count > 12:
                pColumnA[number] = Name[0:12]
            else:
                pColumnA[number] = Name
        else:
            print("Sorry, that isn't enough.")

    def PcheckB():
        Name = input("What is your name?: ")
        Age = input("What is your age?: ")
        cost = 545
        if int(Age) <= 7 or int(Age) >= 65:
            cost = 436
            print("You get a 20% discount")
        payment = input("This seat will be $" + str(cost) + " (9% tax) Please input amount given: ")
        if int(payment) >= cost:
            change = float(payment) - float(cost)
            print("Your change will be $" + str(round(change, 2)) + " and your seat has been reserved")
            money(change)
            print("Thank you for your purchase. Have a nice day.")
            count = len(Name)
            if count > 12:
                pColumnB[number] = Name[0:12]
            else:
                pColumnB[number] = Name
        else:
            print("Sorry, that isn't enough.")

    def CcheckA():
        Name = input("What is your name?: ")
        Age = input("What is your age?: ")
        cost = 216.91
        if int(Age) <= 7 or int(Age) >= 65:
            cost = 159
            print("You get a 20% discount")
        payment = input("This seat will be $" + str(cost) + " (9% tax) Please input amount given: ")
        if int(payment) >= cost:
            change = float(payment) - float(cost)
            print("Your change will be $" + str(round(change, 2)) + " and your seat has been reserved")
            money(change)
            print("Thank you for your purchase. Have a nice day.")
            count = len(Name)
            if count > 12:
                cColumnA[number] = Name[0:12]
            else:
                cColumnA[number] = Name
        else:
            print("Sorry, that isn't enough.")

    def CcheckB():
        Name = input("What is your name?: ")
        Age = input("What is your age?: ")
        cost = 545
        if int(Age) <= 7 or int(Age) >= 65:
            cost = 436
            print("You get a 20% discount")
        payment = input("This seat will be $" + str(cost) + " (9% tax) Please input amount given: ")
        if int(payment) >= cost:
            change = float(payment) - float(cost)
            print("Your change will be $" + str(round(change, 2)) + " and your seat has been reserved")
            money(change)
            print("Thank you for your purchase. Have a nice day.")
            count = len(Name)
            if count > 12:
                cColumnB[number] = Name[0:12]
            else:
                cColumnB[number] = Name
        else:
            print("Sorry that isn't enough.")

    def CcheckC():
        Name = input("What is your name?: ")
        Age = input("What is your age?: ")
        cost = 545
        if int(Age) <= 7 or int(Age) >= 65:
            cost = 436
            print("You get a 20% discount")
        payment = input("This seat will be $" + str(cost) +
                        " (9% tax) Please input amount given: ")
        if int(payment) >= cost:
            change = float(payment) - float(cost)
            print("Your change will be $" + str(round(change, 2)) +
                  " and your seat has been reserved")
            money(change)
            print("Thank you for your purchase. Have a nice day.")
            count = len(Name)
            if count > 12:
                cColumnC[number] = Name[0:12]
            else:
                cColumnC[number] = Name
        else:
            print("Sorry, that isn't enough.")

    def CcheckD():
        Name = input("What is your name?: ")
        Age = input("What is your age?: ")
        cost = 545
        if int(Age) <= 7 or int(Age) >= 65:
            cost = 436
            print("You get a 20% discount")
        payment = input("This seat will be $" + str(cost) + " (9% tax) Please input amount given: ")
        if int(payment) >= cost:
            change = float(payment) - float(cost)
            print("Your change will be $" + str(round(change, 2)) + " and your seat has been reserved")
            money(change)
            print("Thank you for your purchase. Have a nice day.")
            count = len(Name)
            if count > 12:
                cColumnD[number] = Name[0:12]
            else:
                cColumnD[number] = Name
        else:
            print("Sorry, that isn't enough.")

    def ChangeReservation(Name):
        if Change == "A1" and pColumnA[0] == "Open":
            count = len(Name)
            if count > 12:
                pColumnA[0] = Name[0:12]
            else:
                pColumnA[0] = Name
        elif Change == "A1" and pColumnA[0] != "Open":
            print("sorry that seat is taken")
        if Change == "A2" and pColumnA[1] == "Open":
            count = len(Name)
            if count > 12:
                pColumnA[1] = Name[0:12]
            else:
                pColumnA[1] = Name
        elif Change == "A2" and pColumnA[1] != "Open":
            print("sorry that seat is taken")
        if Change == "A3" and pColumnA[2] == "Open":
            count = len(Name)
            if count > 12:
                pColumnA[2] = Name[0:12]
            else:
                pColumnA[2] = Name
        elif Change == "A3" and pColumnA[2] != "Open":
            print("sorry that seat is taken")
        if Change == "A4" and pColumnA[3] == "Open":
            count = len(Name)
            if count > 12:
                pColumnA[3] = Name[0:12]
            else:
                pColumnA[3] = Name
        elif Change == "A4" and pColumnA[3] != "Open":
            print("sorry that seat is taken")
        if Change == "B1" and pColumnB[0] == "Open":
            count = len(Name)
            if count > 12:
                pColumnB[0] = Name[0:12]
            else:
                pColumnB[0] = Name
        elif Change == "B1" and pColumnB[0] != "Open":
            print("sorry that seat is taken")
        if Change == "B2" and pColumnB[1] == "Open":
            count = len(Name)
            if count > 12:
                pColumnB[1] = Name[0:12]
            else:
                pColumnB[1] = Name
        elif Change == "B2" and pColumnB[1] != "Open":
            print("sorry that seat is taken")
        if Change == "B3" and pColumnB[2] == "Open":
            count = len(Name)
            if count > 12:
                pColumnB[2] = Name[0:12]
            else:
                pColumnB[2] = Name
        elif Change == "B3" and pColumnB[2] != "Open":
            print("sorry that seat is taken")
        if Change == "B4" and pColumnB[3] == "Open":
            count = len(Name)
            if count > 12:
                pColumnB[3] = Name[0:12]
            else:
                pColumnB[3] = Name
        elif Change == "B4" and pColumnB[3] != "Open":
            print("sorry that seat is taken")
        if Change == "A1." and cColumnA[
                0] == "Open":  #Starting A Column in Coach Class
            count = len(Name)
            if count > 12:
                cColumnA[0] = Name[0:12]
            else:
                cColumnA[0] = Name
        elif Change == "A1." and cColumnA[0] != "Open":
            print("sorry that seat is taken")
        if Change == "A2." and cColumnA[1] == "Open":
            count = len(Name)
            if count > 12:
                cColumnA[1] = Name[0:12]
            else:
                cColumnA[1] = Name
        elif Change == "A2." and cColumnA[1] != "Open":
            print("sorry that seat is taken")
        if Change == "A3." and cColumnA[2] == "Open":
            count = len(Name)
            if count > 12:
                cColumnA[2] = Name[0:12]
            else:
                cColumnA[2] = Name
        elif Change == "A3." and cColumnA[2] != "Open":
            print("sorry that seat is taken")
        if Change == "A4." and cColumnA[3] == "Open":
            count = len(Name)
            if count > 12:
                cColumnA[3] = Name[0:12]
            else:
                cColumnA[3] = Name
        elif Change == "A4." and cColumnA[3] != "Open":
            print("sorry that seat is taken")
        if Change == "A5." and cColumnA[4] == "Open":
            count = len(Name)
            if count > 12:
                cColumnA[4] = Name[0:12]
            else:
                cColumnA[4] = Name
        elif Change == "A5." and cColumnA[4] != "Open":
            print("sorry that seat is taken")
        if Change == "A6." and cColumnA[5] == "Open":
            count = len(Name)
            if count > 12:
                cColumnA[5] = Name[0:12]
            else:
                cColumnA[5] = Name
        elif Change == "A6." and cColumnA[5] != "Open":
            print("sorry that seat is taken")
        if Change == "A7." and cColumnA[6] == "Open":
            count = len(Name)
            if count > 12:
                cColumnA[6] = Name[0:12]
            else:
                cColumnA[6] = Name
        elif Change == "A7." and cColumnA[6] != "Open":
            print("sorry that seat is taken")
        if Change == "A8." and cColumnA[7] == "Open":
            count = len(Name)
            if count > 12:
                cColumnA[7] = Name[0:12]
            else:
                cColumnA[7] = Name
        elif Change == "A8." and cColumnA[7] != "Open":
            print("sorry that seat is taken")
        if Change == "A9." and cColumnA[8] == "Open":
            count = len(Name)
            if count > 12:
                cColumnA[8] = Name[0:12]
            else:
                cColumnA[8] = Name
        elif Change == "A9." and cColumnA[8] != "Open":
            print("sorry that seat is taken")
        if Change == "A10." and cColumnA[9] == "Open":
            count = len(Name)
            if count > 12:
                cColumnA[9] = Name[0:12]
            else:
                cColumnA[9] = Name
        elif Change == "A10." and cColumnA[9] != "Open":
            print("sorry that seat is taken")
        if Change == "B1." and cColumnB[0] == "Open":  #Starting B Column in Coach Class
            count = len(Name)
            if count > 12:
                cColumnB[0] = Name[0:12]
            else:
                cColumnB[0] = Name
        elif Change == "B1." and cColumnB[0] != "Open":
            print("sorry that seat is taken")
        if Change == "B2." and cColumnB[1] == "Open":
            count = len(Name)
            if count > 12:
                cColumnB[1] = Name[0:12]
            else:
                cColumnB[1] = Name
        elif Change == "B2." and cColumnB[1] != "Open":
            print("sorry that seat is taken")
        if Change == "B3." and cColumnB[2] == "Open":
            count = len(Name)
            if count > 12:
                cColumnC[2] = Name[0:12]
            else:
                cColumnC[2] = Name
        elif Change == "B3." and cColumnB[2] != "Open":
            print("sorry that seat is taken")
        if Change == "B4." and cColumnB[3] == "Open":
            count = len(Name)
            if count > 12:
                cColumnB[3] = Name[0:12]
            else:
                cColumnB[3] = Name
        elif Change == "B4." and cColumnB[3] != "Open":
            print("sorry that seat is taken")
        if Change == "B5." and cColumnB[4] == "Open":
            count = len(Name)
            if count > 12:
                cColumnB[4] = Name[0:12]
            else:
                cColumnB[4] = Name
        elif Change == "B5." and cColumnB[4] != "Open":
            print("sorry that seat is taken")
        if Change == "B6." and cColumnB[5] == "Open":
            count = len(Name)
            if count > 12:
                cColumnB[5] = Name[0:12]
            else:
                cColumnB[5] = Name
        elif Change == "B6." and cColumnB[5] != "Open":
            print("sorry that seat is taken")
        if Change == "B7." and cColumnB[6] == "Open":
            count = len(Name)
            if count > 12:
                cColumnB[6] = Name[0:12]
            else:
                cColumnB[6] = Name
        elif Change == "B7." and cColumnB[6] != "Open":
            print("sorry that seat is taken")
        if Change == "B8." and cColumnB[7] == "Open":
            count = len(Name)
            if count > 12:
                cColumnB[7] = Name[0:12]
            else:
                cColumnB[7] = Name
        elif Change == "B8." and cColumnB[7] != "Open":
            print("sorry that seat is taken")
        if Change == "B9." and cColumnB[8] == "Open":
            count = len(Name)
            if count > 12:
                cColumnB[8] = Name[0:12]
            else:
                cColumnB[8] = Name
        elif Change == "B9." and cColumnB[8] != "Open":
            print("sorry that seat is taken")
        if Change == "B10." and cColumnB[9] == "Open":
            count = len(Name)
            if count > 12:
                cColumnB[9] = Name[0:12]
            else:
                cColumnB[9] = Name
        elif Change == "B10." and cColumnB[9] != "Open":
            print("sorry that seat is taken")
        if Change == "C1." and cColumnC[0] == "Open":  #Starting C Column in Coach Class
            count = len(Name)
            if count > 12:
                cColumnC[0] = Name[0:12]
            else:
                cColumnC[0] = Name
        elif Change == "C1." and cColumnC[0] != "Open":
            print("sorry that seat is taken")
        if Change == "C2." and cColumnC[1] == "Open":
            count = len(Name)
            if count > 12:
                cColumnC[1] = Name[0:12]
            else:
                cColumnC[1] = Name
        elif Change == "C2." and cColumnC[1] != "Open":
            print("sorry that seat is taken")
        if Change == "C3." and cColumnC[2] == "Open":
            count = len(Name)
            if count > 12:
                cColumnC[2] = Name[0:12]
            else:
                cColumnC[2] = Name
        elif Change == "C3." and cColumnC[2] != "Open":
            print("sorry that seat is taken")
        if Change == "C4." and cColumnC[3] == "Open":
            count = len(Name)
            if count > 12:
                cColumnC[3] = Name[0:12]
            else:
                cColumnC[3] = Name
        elif Change == "C4." and cColumnC[3] != "Open":
            print("sorry that seat is taken")
        if Change == "C5." and cColumnC[4] == "Open":
            count = len(Name)
            if count > 12:
                cColumnC[4] = Name[0:12]
            else:
                cColumnC[4] = Name
        elif Change == "C5." and cColumnC[4] != "Open":
            print("sorry that seat is taken")
        if Change == "C6." and cColumnC[5] == "Open":
            count = len(Name)
            if count > 12:
                cColumnC[5] = Name[0:12]
            else:
                cColumnC[5] = Name
        elif Change == "C6." and cColumnC[5] != "Open":
            print("sorry that seat is taken")
        if Change == "C7." and cColumnC[6] == "Open":
            count = len(Name)
            if count > 12:
                cColumnC[6] = Name[0:12]
            else:
                cColumnC[6] = Name
        elif Change == "C7." and cColumnC[6] != "Open":
            print("sorry that seat is taken")
        if Change == "C8." and cColumnC[7] == "Open":
            count = len(Name)
            if count > 12:
                cColumnC[7] = Name[0:12]
            else:
                cColumnC[7] = Name
        elif Change == "C8." and cColumnC[7] != "Open":
            print("sorry that seat is taken")
        if Change == "C9." and cColumnC[8] == "Open":
            count = len(Name)
            if count > 12:
                cColumnC[8] = Name[0:12]
            else:
                cColumnC[8] = Name
        elif Change == "C9." and cColumnC[8] != "Open":
            print("sorry that seat is taken")
        if Change == "C10." and cColumnC[9] == "Open":
            count = len(Name)
            if count > 12:
                cColumnC[9] = Name[0:12]
            else:
                cColumnC[9] = Name
        elif Change == "C10." and cColumnC[9] != "Open":
            print("sorry that seat is taken")
        if Change == "D1." and cColumnD[0] == "Open":#Starting D Column in Coach Class
            count = len(Name)
            if count > 12:
                cColumnD[0] = Name[0:12]
            else:
                cColumnD[0] = Name
        elif Change == "D1." and cColumnD[0] != "Open":  
            print("sorry that seat is taken")
        if Change == "D2." and cColumnD[1] == "Open":
            count = len(Name)
            if count > 12:
                cColumnD[1] = Name[0:12]
            else:
                cColumnD[1] = Name
        elif Change == "D2." and cColumnD[1] != "Open":
            print("sorry that seat is taken")
        if Change == "D3." and cColumnD[2] == "Open":
            count = len(Name)
            if count > 12:
                cColumnD[2] = Name[0:12]
            else:
                cColumnD[2] = Name
        elif Change == "D3." and cColumnD[2] != "Open":
            print("sorry that seat is taken")
        if Change == "D4." and cColumnD[3] == "Open":
            count = len(Name)
            if count > 12:
                cColumnD[3] = Name[0:12]
            else:
                cColumnD[3] = Name
        elif Change == "D4." and cColumnD[3] != "Open":
            print("sorry that seat is taken")
        if Change == "D5." and cColumnD[4] == "Open":
            count = len(Name)
            if count > 12:
                cColumnD[4] = Name[0:12] 
            else:
                cColumnD[4] = Name
        elif Change == "D5." and cColumnD[4] != "Open":
            print("sorry that seat is taken")
        if Change == "D6." and cColumnD[5] == "Open":
            count = len(Name)
            if count > 12:
                cColumnD[5] = Name[0:12]
            else:
                cColumnD[5] = Name
        elif Change == "D6." and cColumnD[5] != "Open":
            print("sorry that seat is taken")
        if Change == "D7." and cColumnD[6] == "Open":
            count = len(Name)
            if count > 12:
                cColumnD[6] = Name[0:12]
            else:
                cColumnD[6] = Name
        elif Change == "D7." and cColumnD[6] != "Open":
            print("sorry that seat is taken")
        if Change == "D8." and cColumnD[7] == "Open":
            count = len(Name)
            if count > 12:
                cColumnD[7] = Name[0:12]
            else:
                cColumnD[7] = Name
        elif Change == "D8." and cColumnD[7] != "Open":
            print("sorry that seat is taken")
        if Change == "D9." and cColumnD[8] == "Open":
            count = len(Name)
            if count > 12:
                cColumnD[8] = Name[0:12]
            else:
                cColumnD[8] = Name
        elif Change == "D9." and cColumnD[8] != "Open":
            print("sorry that seat is taken")
        if Change == "D10." and cColumnD[9] == "Open":
            count = len(Name)
            if count > 12:
                cColumnD[9] = Name[0:12]
            else:
                cColumnD[9] = Name
        elif Change == "D10." and cColumnD[9] != "Open":
            print("sorry that seat is taken")

# a will be the choice to enter 1st class

    if choice == "a":
        print(
            "The price for a first class seat is $500, 20% off if you are 7 or younger or if you are 65 or older and their are only "
            + str(fClass) + " seats left.")
        answer = input("Are you sure you want to continue? yes/no: ")
        if answer == "yes":
            PremuimSeat = input("Which seat would you like? (A1-4 and B1-4): ")
            if PremuimSeat == "A1" and pColumnA[0] == "Open":
                PcheckA()
            elif PremuimSeat == "A1" and pColumnA[0] != "Open":
                print("sorry that seat is taken")
            if PremuimSeat == "A2" and pColumnA[1] == "Open":
                number = 1
                PcheckA()
            elif PremuimSeat == "A2" and pColumnA[1] != "Open":
                print("sorry that seat is taken")
            if PremuimSeat == "A3" and pColumnA[2] == "Open":
                number = 2
                PcheckA()
            elif PremuimSeat == "A3" and pColumnA[2] != "Open":
                print("sorry that seat is taken")
            if PremuimSeat == "A4" and pColumnA[3] == "Open":
                number = 3
                PcheckA()
            elif PremuimSeat == "A4" and pColumnA[3] != "Open":
                print("sorry that seat is taken")
            if PremuimSeat == "B1" and pColumnB[0] == "Open":
                PcheckB()
            elif PremuimSeat == "B1" and pColumnB[0] != "Open":
                print("sorry that seat is taken")
            if PremuimSeat == "B2" and pColumnB[1] == "Open":
                number = 1
                PcheckB()
            elif PremuimSeat == "B2" and pColumnB[1] != "Open":
                print("sorry that seat is taken")
            if PremuimSeat == "B3" and pColumnB[2] == "Open":
                number = 2
                PcheckB()
            elif PremuimSeat == "B3" and pColumnA[2] != "Open":
                print("sorry that seat is taken")
            if PremuimSeat == "B4" and pColumnB[3] == "Open":
                number = 3
                PcheckB()
            elif PremuimSeat == "B4" and pColumnA[3] != "Open":
                print("sorry that seat is taken")

        else:
            print("What would you like to do? ")
            print("a) make a new first class reservation. ")
            print("b) make a new coach class reservation. ")
            print("c) change an existing reservation. ")
            print("d) print seat listing. ")
            print("e) quit")

# b will be the choice to enter coach class
    if choice == "b":
        print(
            "The price for a coach seat is $199, 20% off if you are 7 or younger or if you are 65 or older and their are only "
            + str(cClass) + " seats left.")
        answer = input("Are you sure you want to continue? yes/no: ")
        if answer == "yes":
            CoachSeat = input(
                "Which seat would you like? (A1. - A10., B1. - B10., C1. - C10., or D1. - D10. , The dot is important: )"
            )
            if CoachSeat == "A1." and cColumnA[0] == "Open":
                CcheckA()
            elif CoachSeat == "A1." and cColumnA[0] != "Open":
                print("sorry that seat is taken")
            if CoachSeat == "A2." and cColumnA[1] == "Open":
                number = 1
                CcheckA()
            elif CoachSeat == "A2." and cColumnA[1] != "Open":
                print("sorry that seat is taken")
            if CoachSeat == "A3." and cColumnA[2] == "Open":
                number = 2
                CcheckA()
            elif CoachSeat == "A3." and cColumnA[2] != "Open":
                print("sorry that seat is taken")
            if CoachSeat == "A4." and cColumnA[3] == "Open":
                number = 3
                CcheckA()
            elif CoachSeat == "A4." and cColumnA[3] != "Open":
                print("sorry that seat is taken")
            if CoachSeat == "A5." and cColumnA[4] == "Open":
                number = 4
                CcheckA()
            elif CoachSeat == "A5." and cColumnA[4] != "Open":
                print("sorry that seat is taken")
            if CoachSeat == "A6." and cColumnA[5] == "Open":
                number = 5
                CcheckA()
            elif CoachSeat == "A6." and cColumnA[5] != "Open":
                print("sorry that seat is taken")
            if CoachSeat == "A7." and cColumnA[6] == "Open":
                number = 6
                CcheckA()
            elif CoachSeat == "A7." and cColumnA[6] != "Open":
                print("sorry that seat is taken")
            if CoachSeat == "A8." and cColumnA[7] == "Open":
                number = 7
                CcheckA()
            elif CoachSeat == "A8." and cColumnA[7] != "Open":
                print("sorry that seat is taken")
            if CoachSeat == "A9." and cColumnA[8] == "Open":
                number = 8
                CcheckA()
            elif CoachSeat == "A9." and cColumnA[8] != "Open":
                print("sorry that seat is taken")
            if CoachSeat == "A10." and cColumnA[9] == "Open":
                number = 9
                CcheckA()
            elif CoachSeat == "A10." and cColumnA[9] != "Open":
                print("sorry that seat is taken")
            if CoachSeat == "B1." and cColumnB[0] == "Open":
                CcheckB()
            elif CoachSeat == "B1." and cColumnB[0] != "Open":
                print("sorry that seat is taken")
            if CoachSeat == "B2." and cColumnB[1] == "Open":
                number = 1
                CcheckB()
            elif CoachSeat == "B2." and cColumnB[1] != "Open":
                print("sorry that seat is taken")
            if CoachSeat == "B3." and cColumnB[2] == "Open":
                number = 2
                CcheckB()
            elif CoachSeat == "B3." and cColumnB[2] != "Open":
                print("sorry that seat is taken")
            if CoachSeat == "B4." and cColumnB[3] == "Open":
                number = 3
                CcheckB()
            elif CoachSeat == "B4." and cColumnB[3] != "Open":
                print("sorry that seat is taken")
            if CoachSeat == "B5." and cColumnB[4] == "Open":
                number = 4
                CcheckB()
            elif CoachSeat == "B5." and cColumnB[4] != "Open":
                print("sorry that seat is taken")
            if CoachSeat == "B6." and cColumnB[5] == "Open":
                number = 5
                CcheckB()
            elif CoachSeat == "B6." and cColumnB[5] != "Open":
                print("sorry that seat is taken")
            if CoachSeat == "B7." and cColumnB[6] == "Open":
                number = 6
                CcheckB()
            elif CoachSeat == "B7." and cColumnB[6] != "Open":
                print("sorry that seat is taken")
            if CoachSeat == "B8." and cColumnB[7] == "Open":
                number = 7
                CcheckB()
            elif CoachSeat == "B8." and cColumnB[7] != "Open":
                print("sorry that seat is taken")
            if CoachSeat == "B9." and cColumnB[8] == "Open":
                number = 8
                CcheckB()
            elif CoachSeat == "B9." and cColumnB[8] != "Open":
                print("sorry that seat is taken")
            if CoachSeat == "B10." and cColumnB[9] == "Open":
                number = 9
                CcheckB()
            elif CoachSeat == "B10." and cColumnB[9] != "Open":
                print("sorry that seat is taken")
            if CoachSeat == "C1." and cColumnC[0] == "Open":
                CcheckC()
            elif CoachSeat == "C1." and cColumnC[0] != "Open":
                print("sorry that seat is taken")
            if CoachSeat == "C2." and cColumnC[1] == "Open":
                number = 1
                CcheckC()
            elif CoachSeat == "C2." and cColumnC[1] != "Open":
                print("sorry that seat is taken")
            if CoachSeat == "C3." and cColumnC[2] == "Open":
                number = 2
                CcheckC()
            elif CoachSeat == "C3." and cColumnC[2] != "Open":
                print("sorry that seat is taken")
            if CoachSeat == "C4." and cColumnC[3] == "Open":
                number = 3
                CcheckC()
            elif CoachSeat == "C4." and cColumnC[3] != "Open":
                print("sorry that seat is taken")
            if CoachSeat == "C5." and cColumnC[4] == "Open":
                number = 4
                CcheckC()
            elif CoachSeat == "C5." and cColumnC[4] != "Open":
                print("sorry that seat is taken")
            if CoachSeat == "C6." and cColumnC[5] == "Open":
                number = 5
                CcheckC()
            elif CoachSeat == "C6." and cColumnC[5] != "Open":
                print("sorry that seat is taken")
            if CoachSeat == "C7." and cColumnC[6] == "Open":
                number = 6
                CcheckC()
            elif CoachSeat == "C7." and cColumnC[6] != "Open":
                print("sorry that seat is taken")
            if CoachSeat == "C8." and cColumnC[7] == "Open":
                number = 7
                CcheckC()
            elif CoachSeat == "C8." and cColumnC[7] != "Open":
                print("sorry that seat is taken")
            if CoachSeat == "C9." and cColumnC[8] == "Open":
                number = 8
                CcheckC()
            elif CoachSeat == "C9." and cColumnC[8] != "Open":
                print("sorry that seat is taken")
            if CoachSeat == "C10." and cColumnC[9] == "Open":
                number = 9
                CcheckC()
            elif CoachSeat == "C10." and cColumnC[9] != "Open":
                print("sorry that seat is taken")
            if CoachSeat == "D1." and cColumnD[0] == "Open":
                CcheckD()
            elif CoachSeat == "D1." and cColumnD[0] != "Open":
                print("sorry that seat is taken")
            if CoachSeat == "D2." and cColumnD[1] == "Open":
                number = 1
                CcheckD()
            elif CoachSeat == "D2." and cColumnD[1] != "Open":
                print("sorry that seat is taken")
            if CoachSeat == "D3." and cColumnD[2] == "Open":
                number = 2
                CcheckD()
            elif CoachSeat == "D3." and cColumnA[2] != "Open":
                print("sorry that seat is taken")
            if CoachSeat == "D4." and cColumnD[3] == "Open":
                number = 3
                CcheckD()
            elif CoachSeat == "D4." and cColumnD[3] != "Open":
                print("sorry that seat is taken")
            if CoachSeat == "D5." and cColumnD[4] == "Open":
                number = 4
                CcheckD()
            elif CoachSeat == "D5." and cColumnD[4] != "Open":
                print("sorry that seat is taken")
            if CoachSeat == "D6." and cColumnD[5] == "Open":
                number = 5
                CcheckD()
            elif CoachSeat == "D6." and cColumnD[5] != "Open":
                print("sorry that seat is taken")
            if CoachSeat == "D7." and cColumnD[6] == "Open":
                number = 6
                CcheckD()
            elif CoachSeat == "D7." and cColumnD[6] != "Open":
                print("sorry that seat is taken")
            if CoachSeat == "D8." and cColumnD[7] == "Open":
                number = 7
                CcheckD()
            elif CoachSeat == "D8." and cColumnD[7] != "Open":
                print("sorry that seat is taken")
            if CoachSeat == "D9." and cColumnD[8] == "Open":
                number = 8
                CcheckD()
            elif CoachSeat == "D9." and cColumnD[8] != "Open":
                print("sorry that seat is taken")
            if CoachSeat == "D10." and cColumnD[9] == "Open":
                number = 9
                CcheckD()
            elif CoachSeat == "D10." and cColumnD[9] != "Open":
                print("sorry that seat is taken")
        else:
            print("What would you like to do? ")
            print("a) make a new first class reservation. ")
            print("b) make a new coach class reservation. ")
            print("c) change an existing reservation. ")
            print("d) print seat listing. ")
            print("e) quit")

# c will be the option to change reservations
    if choice == "c":
        CurrentReservation = input("What is your current reservation?")
        Change = input("What seat would you like to change to?")
        Name = input("What is your name?: ")
        if CurrentReservation == "A1":
            ChangeReservation(Name)
            pColumnA[0] = "Open"
        if CurrentReservation == "A2":
            ChangeReservation(Name)
            pColumnA[1] = "Open"
        if CurrentReservation == "A3":
            ChangeReservation(Name)
            pColumnA[2] = "Open"
        if CurrentReservation == "A4":
            ChangeReservation(Name)
            pColumnA[3] = "Open"
        if CurrentReservation == "B1":
            ChangeReservation(Name)
            pColumnB[0] = "Open"
        if CurrentReservation == "B2":
            ChangeReservation(Name)
            pColumnB[1] = "Open"
        if CurrentReservation == "B3":
            ChangeReservation(Name)
            pColumnB[2] = "Open"
        if CurrentReservation == "B4":
            ChangeReservation(Name)
            pColumnB[3] = "Open"
        if CurrentReservation == "A1.":
            ChangeReservation(Name)
            cColumnA[0] = "Open"
        if CurrentReservation == "A2.":
            ChangeReservation(Name)
            cColumnA[1] = "Open"
        if CurrentReservation == "A3.":
            ChangeReservation(Name)
            cColumnA[2] = "Open"
        if CurrentReservation == "A4.":
            ChangeReservation(Name)
            cColumnA[3] = "Open"
        if CurrentReservation == "A5.":
            ChangeReservation(Name)
            cColumnA[4] = "Open"
        if CurrentReservation == "A6.":
            ChangeReservation(Name)
            cColumnA[5] = "Open"
        if CurrentReservation == "A7.":
            ChangeReservation(Name)
            cColumnA[6] = "Open"
        if CurrentReservation == "A8.":
            ChangeReservation(Name)
            cColumnA[7] = "Open"
        if CurrentReservation == "A9.":
            ChangeReservation(Name)
            cColumnA[8] = "Open"
        if CurrentReservation == "A10.":
            ChangeReservation(Name)
            cColumnA[9] = "Open"
        if CurrentReservation == "B1.":
            ChangeReservation(Name)
            cColumnB[0] = "Open"
        if CurrentReservation == "B2.":
            ChangeReservation(Name)
            cColumnB[1] = "Open"
        if CurrentReservation == "B3.":
            ChangeReservation(Name)
            cColumnB[2] = "Open"
        if CurrentReservation == "B4.":
            ChangeReservation(Name)
            cColumnB[3] = "Open"
        if CurrentReservation == "B5.":
            ChangeReservation(Name)
            cColumnB[4] = "Open"
        if CurrentReservation == "B6.":
            ChangeReservation(Name)
            cColumnB[5] = "Open"
        if CurrentReservation == "B7.":
            ChangeReservation(Name)
            cColumnB[6] = "Open"
        if CurrentReservation == "B8.":
            ChangeReservation(Name)
            cColumnB[7] = "Open"
        if CurrentReservation == "B9.":
            ChangeReservation(Name)
            cColumnB[8] = "Open"
        if CurrentReservation == "B10.":
            ChangeReservation(Name)
            cColumnB[9] = "Open"
        if CurrentReservation == "C1.":
            ChangeReservation(Name)
            cColumnC[0] = "Open"
        if CurrentReservation == "C2.":
            ChangeReservation(Name)
            cColumnC[1] = "Open"
        if CurrentReservation == "C3.":
            ChangeReservation(Name)
            cColumnC[2] = "Open"
        if CurrentReservation == "C4.":
            ChangeReservation(Name)
            cColumnC[3] = "Open"
        if CurrentReservation == "C5.":
            ChangeReservation(Name)
            cColumnC[4] = "Open"
        if CurrentReservation == "C6.":
            ChangeReservation(Name)
            cColumnC[5] = "Open"
        if CurrentReservation == "C7.":
            ChangeReservation(Name)
            cColumnC[6] = "Open"
        if CurrentReservation == "C8.":
            ChangeReservation(Name)
            cColumnC[7] = "Open"
        if CurrentReservation == "C9.":
            ChangeReservation(Name)
            cColumnC[8] = "Open"
        if CurrentReservation == "C10.":
            ChangeReservation(Name)
            cColumnC[9] = "Open"
        if CurrentReservation == "D1.":
            ChangeReservation(Name)
            cColumnD[0] = "Open"
        if CurrentReservation == "D2.":
            ChangeReservation(Name)
            cColumnD[1] = "Open"
        if CurrentReservation == "D3.":
            ChangeReservation(Name)
            cColumnD[2] = "Open"
        if CurrentReservation == "D4.":
            ChangeReservation(Name)
            cColumnD[3] = "Open"
        if CurrentReservation == "D5.":
            ChangeReservation(Name)
            cColumnD[4] = "Open"
        if CurrentReservation == "D6.":
            ChangeReservation(Name)
            cColumnD[5] = "Open"
        if CurrentReservation == "D7.":
            ChangeReservation(Name)
            cColumnD[6] = "Open"
        if CurrentReservation == "D8.":
            ChangeReservation(Name)
            cColumnD[7] = "Open"
        if CurrentReservation == "D9.":
            ChangeReservation(Name)
            cColumnD[8] = "Open"
        if CurrentReservation == "D10.":
            ChangeReservation(Name)
            cColumnD[9] = "Open"

# d will be the option to see all existing reservations
    if choice == "d":
        print("==========FIRST CLASS==========")
        print("   =====A=====   =====B=====")
        print("1  |   " + pColumnA[0] + "   |  |   " + pColumnB[0] + "   |")
        print("2  |   " + pColumnA[1] + "   |  |   " + pColumnB[1] + "   |")
        print("3  |   " + pColumnA[2] + "   |  |   " + pColumnB[2] + "   |")
        print("4  |   " + pColumnA[3] + "   |  |   " + pColumnB[3] + "   |")
        print("==========COACH CLASS==========")
        print("     =====A=====   =====B=====   =====C=====   =====D=====")
        print("1   |   " + cColumnA[0] + "   |  |   " + cColumnB[0] +
              "   |  |   " + cColumnC[0] + "   |  |   " + cColumnD[0] + "   |")
        print("2   |   " + cColumnA[1] + "   |  |   " + cColumnB[1] +
              "   |  |   " + cColumnC[1] + "   |  |   " + cColumnD[1] + "   |")
        print("3   |   " + cColumnA[2] + "   |  |   " + cColumnB[2] +
              "   |  |   " + cColumnC[2] + "   |  |   " + cColumnD[2] + "   |")
        print("4   |   " + cColumnA[3] + "   |  |   " + cColumnB[3] +
              "   |  |   " + cColumnC[3] + "   |  |   " + cColumnD[3] + "   |")
        print("5   |   " + cColumnA[4] + "   |  |   " + cColumnB[4] +
              "   |  |   " + cColumnC[4] + "   |  |   " + cColumnD[4] + "   |")
        print("6   |   " + cColumnA[5] + "   |  |   " + cColumnB[5] +
              "   |  |   " + cColumnC[5] + "   |  |   " + cColumnD[5] + "   |")
        print("7   |   " + cColumnA[6] + "   |  |   " + cColumnB[6] +
              "   |  |   " + cColumnC[6] + "   |  |   " + cColumnD[6] + "   |")
        print("8   |   " + cColumnA[7] + "   |  |   " + cColumnB[7] +
              "   |  |   " + cColumnC[7] + "   |  |   " + cColumnD[7] + "   |")
        print("9   |   " + cColumnA[8] + "   |  |   " + cColumnB[8] +
              "   |  |   " + cColumnC[8] + "   |  |   " + cColumnD[8] + "   |")
        print("10  |   " + cColumnA[9] + "   |  |   " + cColumnB[9] +
              "   |  |   " + cColumnC[9] + "   |  |   " + cColumnD[9] + "   |")
    #Quit option
# e is the choice to quit
    if choice == "e":
        print("Exit!")
        break

    next_choice = input("Would you like to do anything else? (yes/no): ")
    #To stop the program
    if next_choice == "no":
        print("Exit!")
        break
