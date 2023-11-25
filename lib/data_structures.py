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
    names = [food['name'] for food in spicy_foods]
    return names
    
def get_spiciest_foods(spicy_foods):
    spiciest_foods = [food for food in spicy_foods if food.get('heat_level', 0) > 5]
    return spiciest_foods

    

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food.get('name', 'Unknown Food')
        cuisine = food.get('cuisine', 'Unknown Cuisine')
        heat_level = food.get('heat_level', 0)
        
        heat_level_symbols = '🌶' * heat_level

        print(f"{name} ({cuisine}) | Heat Level: {heat_level_symbols}")
def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food.get('cuisine', '').lower() == cuisine.lower():
            return food
    

def print_spiciest_foods(spicy_foods):
     for food in spicy_foods:
        name = food.get('name', 'Unknown Food')
        cuisine = food.get('cuisine', 'Unknown Cuisine')
        heat_level = food.get('heat_level', 0)

        if heat_level > 5:
            heat_level_symbols = '🌶' * heat_level
            print(f"{name} ({cuisine}) | Heat Level: {heat_level_symbols}")
     

def get_average_heat_level(spicy_foods):
    total_heat_level = 0
    num_foods = len(spicy_foods)

    if num_foods == 0:
        return 0  

    for food in spicy_foods:
        total_heat_level += food.get('heat_level', 0)

    return total_heat_level // num_foods
    
    

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods

    