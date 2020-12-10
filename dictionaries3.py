# We updated and replaced a key within a Dictionary
# Also deleted an item. Point Blank.

meal = {

  "drink": "beer",
  "appetizer": "nachos",
  "entree": "tacos",
  "dessert": "cake"
}

print(meal)

meal["drink"] = "green tea"

if "water" in meal:
  del meal["dessert"] #this alone would delete just fine.

print(meal)