# Calculate values of oreo cookies (portion/3)
print("Values for 1 oreo cookie")

oreo_calories = 53.33
print (str(oreo_calories) + "kcal")

oreo_sodium = 63.33
print(str(oreo_sodium) + "mg sodium")

oreo_carbohydrate = 8.33
print(str(oreo_carbohydrate) + "g carbohydrate")

oreo_fat = 2.33
print(str(oreo_fat) + "g fat")

# Maximum of calories
max_calories = 2000

# How much oreo cookies did you eat?
oreos_consumed = input("How much oreo cookies did you eat?")
oreos_consumed = int(oreos_consumed)
print("You eat " + str(oreos_consumed) + " cookies")

# Calculate consumed values 
print("That means, you've consumed...")
oreo_calories_consumed = oreos_consumed * oreo_calories
print(str(oreo_calories_consumed) + "kcal calories")

oreo_sodium_consumed=oreos_consumed * oreo_sodium
print(str(oreo_sodium_consumed) + "mg sodium")

oreo_carbohydrate_consumed=oreos_consumed * oreo_carbohydrate
print(str(oreo_carbohydrate_consumed) + "g carbohydrates")

oreo_fat_consumed=oreos_consumed * oreo_fat
print(str(oreo_fat_consumed) + "g fat")

# Oreo cookies you can still eat 
oreos_left = (max_calories - oreo_calories_consumed) / (oreo_calories)
oreos_left = round(oreos_left, 0)

# Can you still eat oreo cookies? 
if (oreo_calories_consumed >= max_calories):
    message = "O no..." + " WARNING: you've consumed more than 2000 calories!"
    print(message)

else:
    message = "YES!" + " You can still eat " + str(oreos_left) + " oreo cookies"
    print(message)





