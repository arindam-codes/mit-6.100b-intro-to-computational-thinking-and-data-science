class Food():
    
    def __init__(self, name, value, calories):
        self.name = name
        self.value = value
        self.calories = calories
        
    def get_name(self):
        return self.name
    
    def get_value(self):
        return self.value
    
    def get_calories(self):
        return self.calories
    
def Food_item_builder(name, value, calories):
    
    foods = []
    for i in range(len(value)):
        food = Food(name[i], value[i], calories[i])  
        foods.append(food)
    
    return foods


def greedy(foods, max_calorie):
    
    sorted_foods = sorted(foods, key=lambda food: food.get_value() / food.get_calories(), reverse=True)
    total_calories = 0
    food_list = []
    
    for food in sorted_foods:
        if food.get_calories() + total_calories <= max_calorie:
            food_list.append(food)
            total_calories += food.get_calories()
    
    return food_list
  
foods = [
    ("wine",	 89, 123),
    ("beer", 90,	154),
    ("pizza",	30,	258),
    ("burger", 	50,	354),
    ("fries",	90,	365),
    ("coke",	79	,150),
    ("apple",	90,	95),
    ("donut",	10,	195)
    ]

name = [food[0] for food in foods]
value = [food[1] for food in foods]
calories = [food[2] for food in foods]

food_item = Food_item_builder(name, value, calories)

# for food in greedy(food_item, 750):
#     print(f"{food.get_name()}: {food.get_calories()} calories")
    
# total_value = sum(food.get_value( )for food in greedy(food_item, 750))
# print(f"\nTotal value: ${total_value}")


def max_val(to_consider, avail):
    
    # Base case
    if avail == 0 or to_consider == []:
        result = (0, ())
    
    # If first item doesnt fit
    elif to_consider[0].get_calories() > avail:
        result = max_val(to_consider[1:], avail)

    # If first item does fit 
    # we need two branches

    else:
        
        ## Possible combinations if i take the current value
        
        # Counting all possible combinations if i take the current value
        take_value, take_item = max_val(to_consider[1:], avail - to_consider[0].get_calories())
       
        # Adding the current value with the combinations
        take_value += to_consider[0].get_value()
        take_item += (to_consider[0],)
        
        ## Possible combinations if i dont take current value
        # 2. Leave the item
        leave_value, leave_item = max_val(to_consider[1:], avail)
        
        if take_value > leave_value:
            result = (take_value, take_item)
        else:
            result = (leave_value, leave_item)
        
    return result
    

best_value, best_items = max_val(food_item, 750)

print("Best value:", best_value)
for item in best_items:
    print(item.get_name(), item.get_calories())
