


def discount(isMember, age, isResident):
    if (age < 12 or age >= 65):
        if (isResident == True or isMember == True):
            print("yes discount")
    else:
        print("no discount boohoo")

discount(True, 21, False)