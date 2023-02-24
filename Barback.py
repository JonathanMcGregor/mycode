answer="placeholder"
i= 0
gin= ["Gimlet.", "Negroni.", "Ramos Gin Fizz."]
vodka= ["Lemon Drop.", "Martini.", "Blackberry-Thyme Mule."]
whiskey= ["Whiskey Smash.", "Old Fashioned.", "New York Sour."]
tequila= ["Tequila Sunrise.", "Paloma.", "Mango-Habanero Margarita."]
rum= ["Rum Punch.", "Mai Tai.", "Pineapple Caipirinha."]
brandy= ["Sidecar.", "Brandy Alexander.", "Vieux Carre."]

print("Welcome to the best bar in town!")
print("What is your liquor of choice?")
answer= input(">")

if  answer == "gin":
    print("Do you prefer sweet, spirit forward, or complex cocktails?")

    while True:
        answer = input(">>")
        if answer == "sweet":
             print("You should order a "+ gin[0])
             break
        if answer == "spirit forward":
             print("You should order a "+ gin[1])
             break
        if answer == "complex":
             print("You should order a "+ gin[2])
             break
        else:
             print("That was not one of the available answers. Try again.")

if  answer == "vodka":
    print("Do you prefer sweet, spirit forward, or complex cocktails?")

    while True:
        answer = input(">>")
        if answer == "sweet":
             print("You should order a "+ vodka[0])
             break
        if answer == "spirit forward":
             print("You should order a "+ vodka[1])
             break
        if answer == "complex":
             print("You should order a "+ vodka[2])
             break
        else:
             print("That was not one of the available answers. Try again.")

if  answer == "whiskey":
    print("Do you prefer sweet, spirit forward, or complex cocktails?")

    while True:
        answer = input(">>")
        if answer == "sweet":
             print("You should order a "+ whiskey[0])
             break
        if answer == "spirit forward":
             print("You should order an "+ whiskey[1])
             break
        if answer == "complex":
             print("You should order a "+ whiskey[2])
             break
        else:
             print("That was not one of the available answers. Try again.")

if  answer == "brandy":
    print("Do you prefer sweet, spirit forward, or complex cocktails?")

    while True:
        answer = input(">>")
        if answer == "sweet":
             print("You should order a "+ brandy[0])
             break
        if answer == "spirit forward":
             print("You should order a "+ brandy[1])
             break
        if answer == "complex":
             print("You should order a "+ brandy[2])
             break
        else:
             print("That was not one of the available answers. Try again.")

if  answer == "tequila":
    print("Do you prefer sweet, spirit forward, or complex cocktails?")

    while True:
        answer = input(">>")
        if answer == "sweet":
             print("You should order a "+ tequila[0])
             break
        if answer == "spirit forward":
             print("You should order a "+ tequila[1])
             break
        if answer == "complex":
             print("You should order a "+ tequila[2])
             break
        else:
             print("That was not one of the available answers. Try again.")

if  answer == "rum":
    print("Do you prefer sweet, spirit forward, or complex cocktails?")

    while True:
        answer = input(">>")
        if answer == "sweet":
             print("You should order a "+ rum[0])
             break
        if answer == "spirit forward":
             print("You should order a "+ rum[1])
             break
        if answer == "complex":
             print("You should order a "+ rum[2])
             break
        else:
             print("That was not one of the available answers. Try again.")
