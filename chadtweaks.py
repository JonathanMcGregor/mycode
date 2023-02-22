answer="placeholder"
i= 0
gin= ["Gimlet", "Negroni", "Ramos Gin Fizz"]
vodka= ["Lemon Drop", "Martini", "Blackberry-Thyme Mule"]
whiskey= ["Whiskey Smash", "Old Fashioned", "New York Sour"]
tequilla= ["Tequila Sunrise", "Paloma", "Mango-Habanero Margarita"]
rum= ["Rum Punch", "Mai Tai", "Pineapple Caipirinha"]
brandy= ["Sidecar", "Brandy Alexander", "Vieux Carre"]

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
