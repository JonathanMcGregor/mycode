import requests

answer= "placeholder"

print("Welcome to the Ai-R Lounge, the first Artificial Intelligence Lounge!")
print("Are you looking for a poultry, seafood, meat, vegetarian, or vegan dish?")
answer= input(">").lower()

if answer == "poultry":
    while True:
        print("Would you prefer chicken, turkey, or duck?")
        poultry_choice= input(">").lower()
        if poultry_choice == "chicken":
            print("Would you like your chicken fried, baked, grilled, or pan-seared?")
            prep_preference= input(">").lower()
            if prep_preference == "fried":
                recipe= requests.get("https://www.themealdb.com/api/json/v1/1/search.php?s=fried%20chicken").json()
                print(recipe["meals"][0]["strInstructions"])
                break
            elif prep_preference == "baked":
                recipe= requests.get("https://www.themealdb.com/api/json/v1/1/search.php?s=Chicken%20Enchilada%20Casserole").json()                
                print(recipe["meals"][0]["strInstructions"])
                break
            elif prep_preference == "grilled":
                recipe= requests.get("https://www.themealdb.com/api/json/v1/1/search.php?s=Tandoori%20chicken").json()                
                print(recipe["meals"][0]["strInstructions"])
                break
            elif prep_preference == "pan-seared":
                recipe= requests.get("https://www.themealdb.com/api/json/v1/1/search.php?s=Chicken%20Couscous").json()                
                print(recipe["meals"][0]["strInstructions"])
                break
            
