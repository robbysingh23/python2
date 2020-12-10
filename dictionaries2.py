# Added a new meal to our dictionary

meal = {
  "drink": "beer",
  "appetizer": "nachos",
  "entree": "tacos",
  "dessert": "cake"
}

meal['water'] = "fizzy"
meal['pizza'] = False

print(meal)

if "pizza" in meal and "pizza" == True:
  print("Robby has a pizza")
else:
  print("Robby did NOT have a pizza")