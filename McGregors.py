#!/usr/bin/final
import requests

answer="placeholder"
i= 0
gin= ["Gimlet.", "Negroni.", "Ramos Gin Fizz."]
vodka= ["Lemon Drop.", "Martini.", "Blackberry-Thyme Mule."]
whiskey= ["Whiskey Smash.", "Old Fashioned.", "New York Sour."]
tequila= ["Tequila Sunrise.", "Paloma.", "Mango-Habanero Margarita."]
rum= ["Rum Punch.", "Mai Tai.", "Pineapple Caipirinha."]
brandy= ["Sidecar.", "Brandy Alexander.", "Vieux Carre."]

print("Welcome to the TLG Bar & Grill!")
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

food= {
    "poultry": {
    "chicken": {
      "fried": "https://www.themealdb.com/api/json/v1/1/search.php?s=fried%20chicken",
      "baked": "https://www.themealdb.com/api/json/v1/1/search.php?s=Chicken%20Enchilada%20Casserole",
      "grilled": "https://www.themealdb.com/api/json/v1/1/search.php?s=Tandoori%20chicken",
      "pan-seared": "https://www.themealdb.com/api/json/v1/1/search.php?s=Chicken%20Couscous"
    },
    "turkey": {
      "fried": "https://www.foodandwine.com/recipes/deep-fried-turkey-brined-in-cayenne-and-brown-sugar",
      "baked": "https://www.foodandwine.com/recipes/spatchcocked-sheet-pan-turkey",
      "grilled": "https://www.foodandwine.com/recipes/turkey-kibbe-kebabs-two-sauces",
      "stew": "https://www.foodandwine.com/recipes/thai-inspired-turkey-green-curry"
    },
    "duck": {
      "fried": "https://www.foodandwine.com/recipes/peking-duck",
      "baked": "https://www.foodandwine.com/recipes/slow-cooked-duck-green-olives-and-herbes-de-provence",
      "grilled": "https://www.foodandwine.com/recipes/jerk-smoked-duck-peach-barbecue-sauce",
      "pan-seared": "https://www.foodandwine.com/recipes/crisped-sous-vide-duck-breast-port-juniper-berries-and-oranges"
    }
  },
  "seafood": {
"octopus": {
      "fried": "https://www.foodandwine.com/recipes/extra-crunchy-calamari",
      "baked": "https://www.foodandwine.com/recipes/octopus-turnovers-spicy-creole-mayonnaise",
      "grilled": "https://www.foodandwine.com/recipes/grilled-octopus-ancho-chile-sauce",
      "pan-seared": "https://www.foodandwine.com/recipes/pan-seared-octopus-italian-vegetable-salad"
    },
    "fish": {
      "fried": "https://www.foodandwine.com/recipes/extra-crispy-fried-fish",
      "baked": "https://www.foodandwine.com/recipes/whole-roast-fish-lemon-and-herbs",
      "grilled": "https://www.foodandwine.com/recipes/grilled-snapper-in-coconut-sauce",
      "pan-seared": "https://www.onceuponachef.com/recipes/restaurant-style-pan-seared-salmon.html"
    },
    "lobster": {
        "fried": "https://www.cookedbyjulie.com/fried-lobster-tails/",
      "baked": "https://tasty.co/recipe/baked-lobster-tails",
      "grilled": "https://www.saveur.com/grilled-lobster-with-garlic-parsley-butter-recipe/",
      "pan-seared": "https://cafedelites.com/butter-seared-lobster-tails/"
    }
  },
  "meat": {
    "beef": {
      "fried": "https://www.beyondkimchee.com/crispy-beef/",
      "baked": "https://www.simplyrecipes.com/recipes/roast_beef/",
      "grilled": "https://keviniscooking.com/perfect-rib-eye-steak/",
      "pan-seared": "https://natashaskitchen.com/pan-seared-steak/"
    },
    "lamb": {
      "roasted": "https://www.foodandwine.com/recipes/garlic-crusted-roast-rack-lamb",
      "baked":"https://feelgoodfoodie.net/recipe/baked-lamb-chops/",
      "grilled": "https://www.delishdlites.com/type/gluten-free-recipes/perfect-grilled-lamb-loin-chops-recipe/",
      "pan-seared": "https://gimmedelicious.com/pan-seared-lamb-chops/"
    },
    "pork": {
      "fried": "https://spaceshipsandlaserbeams.com/fried-pork-chops/",
      "baked": "https://www.theendlessmeal.com/juicy-baked-pork-chops/",
      "grilled": "https://kristineskitchenblog.com/grilled-pork-chops/",
      "pan-seared": "https://whatsinthepan.com/easy-pan-seared-pork-chops/"
  }
  },
  "vegetarian": {
    "cauliflower": {
      "fried": "https://thehiddenveggies.com/fried-cauliflower/",
      "baked": "https://www.loveandlemons.com/cauliflower-recipes/",
      "grilled": "https://www.alphafoodie.com/grilled-cauliflower-steaks/",
      "pan-seared": "https://cookieandkate.com/creamy-roasted-cauliflower-soup-recipe/"
    },
    "chickpeas": {
      "fried": "https://www.appetizeraddiction.com/pan-fried-chickpeas/",
      "baked": "https://www.gimmesomeoven.com/roasted-chickpeas/",
      "salad": "https://www.loveandlemons.com/chickpea-recipes/",
      "cold app": "https://www.inspiredtaste.net/15938/easy-and-smooth-hummus-recipe/"
    },
    "leafy-greens": {
      "sauteed": "https://www.plantbasedcooking.com/recipe/sauteed-greens/",
      "soup": "https://greenletes.com/veggie-barley-soup/",
      "salad": "https://www.eastewart.com/recipes-and-nutrition/easy-lentil-salad-low-fodmap/",
      "pan-seared": "https://greenletes.com/sweet-potato-quesadilla/"
    }
  }
  }
print("Feeling hungry?")
print("Are you looking for a poultry, seafood, meat or vegetarian option?")
answer= input(">").lower()

if answer in "poultry":
    while True:
        print("Would you prefer chicken, turkey, or duck?")
        poultry_choice= input(">").lower()
        print("Check out these amazing recipes!")
        url= food["poultry"][poultry_choice]
        recipe= requests.get(url).json()
        print(recipe[0][strInstructions])

if answer in "seafood":
    while True:
        print("Would you prefer octopus, fish, or lobster?")
 seafood_choice= input(">").lower()
        print("Check out these amazing recipes!")
        url= food["seafood"][seafood_choice]
        recipe= requests.get(url).json()
        print(recipe[0][strInstructions])

if answer in "meat":
    while True:
        print("Would you prefer beef, lamb, or pork?")
        meat_choice= input(">").lower()
        print("Check out these amazing recipes!")
        url= food["meat"][meat_choice]
        recipe= requests.get(url).json()
        print(recipe[0][strInstructions])

if answer in "vegetarian":
    while True:
        print("Would you prefer cauliflower, chickpeas, or leafy-greens?")
        vegetarian_choice= input(">").lower()
        print("Check out these amazing recipes!")
        url= food["vegetarian"][vegetarian_choice]
        recipe= requests.get(url).json()
        print(recipe[0][strInstructions])
