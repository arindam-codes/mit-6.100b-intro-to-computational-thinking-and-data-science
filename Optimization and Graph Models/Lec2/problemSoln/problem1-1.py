## problem 1.1

class Items:
    
    """" Model the Item """
    
    def __init__(self, items, values, calories):
        self.items = items
        self.values = values
        self.calories = calories
        
    def get_values(self):
        return self.values
    
    def get_calories(self):
        return self.calories
    
    def get_item(self):
        return self.items
    


        
def greedy(value_list):
    
    totalCapacity = 8
    currentCalories = 0
    selected_item_list = []
    
    
        
    for item in value_list:
        if item.get_calories() + currentCalories <= totalCapacity:
            selected_item_list.append(item)
            
            currentCalories += item.get_calories()
    
    return selected_item_list
            
            
            
    
    
    
def item_builder(items, values, calories):
    item_list = []
    for i in range(len(items)):
        item = Items(items[i], values[i], calories[i])
        item_list.append(item)
        
    return item_list    

def greedy_printer(item_builder):
    item_list = item_builder
    
    value_list = sorted(item_list, key= lambda x: x.get_values(), reverse=True)
    
    final_list = greedy(value_list)
    print("Highest Value")
    for item in final_list:
        print(f"{item.get_item()} value--{item.get_values()} calorie--{item.get_calories()}")
    print("\n")
    
    
    calorie_list = sorted(item_list, key= lambda x: 1 / x.get_calories(), reverse=True)
    final_list = greedy(calorie_list)
    print("Lowest Calorie")
    for item in final_list:
        print(f"{item.get_item()} value--{item.get_values()} calorie--{item.get_calories()}")
    print("\n")
    
    density_list = sorted(item_list, key= lambda x: x.get_values() / x.get_calories(), reverse=True)
    final_list = greedy(density_list)
    print("Density")
    for item in final_list:
        print(f"{item.get_item()} value--{item.get_values()} calorie--{item.get_calories()}")
    print("\n")
    



items = ["A", "B", "C", "D"]
values = [10, 8, 6, 5]
calories = [6, 4, 3, 2]
    
    
item_list = item_builder(items, values, calories)

greedy_printer(item_list)
    
    
    
