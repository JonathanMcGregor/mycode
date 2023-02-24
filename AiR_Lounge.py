import requests

food= {
    "poultry": {
    "chicken": {
      "fried": "https://www.themealdb.com/api/json/v1/1/search.php?s=fried%20chicken",
      "baked": "https//www.themealdb.com/api/json/v1/1/search.php?s=Chicken%20Enchilada%20Casserole",
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
      "grilled": "",
      "pan-seared": ""
    },
    "lamb": {
      "fried": "",
      "baked": "",
      "grilled": "",
      "pan-seared": ""
    },
    "pork": {
      "fried": "URL GOES HERE",
      "baked": "URL GOES HERE",
      "grilled": "URL GOES HERE",
      "pan-seared": "URL GOES HERE"
    }
  },
  "vegetarian": {
    "cauliflower": {
      "fried": "",
      "baked": "",
      "grilled": "",
      "pan-seared": ""
    },
    "chickpeas": {
      "fried": "",
      "baked": "",
      "grilled": "",
      "pan-seared": "URL GOES HERE"
    },
    "leafy-greens": {
      "fried": "URL GOES HERE",
      "baked": "URL GOES HERE",
      "grilled": "URL GOES HERE",
      "pan-seared": "URL GOES HERE"
    }
  },
  "vegan": {
    "tofu": {
      "fried": "URL GOES HERE",
      "baked": "URL GOES HERE",
      "grilled": "URL GOES HERE",
      "pan-seared": "URL GOES HERE"
    },
    "lentils": {
      "fried": "URL GOES HERE",
      "baked": "URL GOES HERE",
      "grilled": "URL GOES HERE",
      "pan-seared": "URL GOES HERE"
    },
    "seitan": {
      "fried": "URL GOES HERE",
      "baked": "URL GOES HERE",
      "grilled": "URL GOES HERE",
      "pan-seared": "URL GOES HERE"
    }
   }
  }
#}
#}

print("Welcome to the AiR Lounge, the first Artificial Intelligence Lounge!")
print("Are you looking for a poultry, seafood, meat, vegetarian, or vegan dish?")
answer= input(">").lower()

if answer in food:
    while True:
        print("Would you prefer chicken, turkey, or duck?")
        poultry_choice= input(">").lower()
        if poultry_choice in food["poultry"]:
            print("Would you like that fried, baked, grilled, or in a stew?")
            prep_preference= input(">").lower()
            if prep_preference in food["poultry"][poultry_choice]:
                url= food["poultry"][poultry_choice]
                recipe= requests.get(url).json()
                print(recipe[0][strInstructions])

if answer in food:
    while True:
        print("Would you prefer octopus, fish, or lobster?")
        seafood_choice= input(">").lower()
        if seafood_choice in food["seafood"]:
            print("Would you like that fried, baked, grilled, or pan-seared?")
            prep_preference= input(">").lower()
            if prep_preference in food["seafood"][seafood_choice]:
                url= food["seafood"][seafood_choice]
                recipe= requests.get(url).json()
                print(recipe[0][strInstructions])

if answer in food:
    while True:
        print("Would you prefer beef, lamb, or pork?")
        meat_choice= input(">").lower()
        if meat_choice in food["meat"]:
            print("Would you like that fried, baked, grilled, or pan-seared?")
            prep_preference= input(">").lower()
            if prep_preference in food["meat"][meat_choice]:
                url= food["meat"][meat_choice]
                recipe= requests.get(url).json()
                print(recipe[0][strInstructions])

if answer in food:
    while True:
        print("Would you prefer cauliflower, chickpeas, or leafy-greens?")
        vegetarian_choice= input(">").lower()
        if vegetarian_choice in food["vegetarian"]:
            print("Would you like that fried, baked, grilled, or in a stew?")
            prep_preference= input(">").lower()
            if prep_preference in food["vegetarian"][vegetarian_choice]:
                url= food["vegetarian"][vegetarian_choice]
                recipe= requests.get(url).json()
                print(recipe[0][strInstructions])

if answer in food:
    while True:
        print("Would you prefer seitan, tofu, or lentils?")
        vegan_choice= input(">").lower()
        if vegan_choice in food["vegan"]:
            print("Would you like that fried, baked, grilled, or in a stew?")
            prep_preference= input(">").lower()
            if prep_preference in food["vegan"][vegan_choice]:
                url= food["vegan"][vegan_choice]
                recipe= requests.get(url).json()
                print(recipe[0][strInstructions])
