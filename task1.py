def get_ingredients(row):
    parts = row.split('|')
    ingredient = {}
    ingredient['ingredient_name'] = parts[0].strip()
    ingredient['quantity'] = int(parts[1].strip())
    ingredient['measure'] = parts[2].strip()
    return ingredient


cook_book = {}

is_name = True
is_quantity = False

with open('recipes.txt') as f:
    for line in f:
        if is_name:
            recipe = line.strip()
            cook_book[recipe] = []
            is_name = False
            is_quantity = True
        elif is_quantity:
            quantity = int(line.strip())
            is_quantity = False
        elif quantity > 0:
            cook_book[recipe].append(get_ingredients(line.strip()))
            quantity -= 1
        else:
            is_name = True

print(cook_book)
