spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
        names = []
        for item in spicy_foods:
            [names.append(item[key]) for key in item if key == 'name']
        return names

def get_spiciest_foods(spicy_foods):
        spicy_item = []
        for item in spicy_foods:
            if item['heat_level'] >5:
                spicy_item.append(item)
        return(spicy_item)

def print_spicy_foods(spicy_foods):
    for item in spicy_foods:
         print(item['name'] + ' (' + item['cuisine']+ ') ' + "| " + 'Heat Level: ' + int(item['heat_level'])*"🌶")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for item in spicy_foods:
         if item['cuisine'] == cuisine:
              return item

def print_spiciest_foods(spicy_foods):
    for item in spicy_foods:
         if item['heat_level'] > 5:
            print(item['name'] + ' (' + item['cuisine']+ ') ' + "| " + 'Heat Level: ' + int(item['heat_level'])*"🌶")

def get_average_heat_level(spicy_foods):
    sum = 0
    count = 0
    for item in spicy_foods:
        sum += item['heat_level']
        count +=  1
    average = sum/count
    return average




def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
