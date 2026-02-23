class Item():
    
    def __init__(self, name, value, weight):
        self.name = name
        self.value = value
        self.weight = weight
        
    def get_value(self):
        return self.value
    
    def get_weight(self):
        return self.weight
    
    def get_value_per_weight(self):
        return self.value / self.weight
    
    
    def __str__(self):
        return f"{self.name}: <{self.value}, {self.weight}>"
    
def build_items(names, values, weights):
    items = []
    for i in range(len(values)):
        items.append(Item(names[i], values[i], weights[i]))
    return items
    

def greedy(items, maxWeight, keyFunction):
    
    ## until it doesnt overs the weight capacity of bag put the best item avaliable
    totalWeight = 0
    totalCost = 0
    totalItems = []
    
    sortedItems = sorted(items, key = keyFunction, reverse = True)
    
    for i in range(len(items)):
        
        if sortedItems[i].get_weight() + totalWeight <= maxWeight:
            totalItems.append(sortedItems[i].name)
            totalWeight += sortedItems[i].get_weight()
            totalCost += sortedItems[i].get_value()
            
    return totalItems, totalCost
            
def test_greedy(items, maxWeight):
    
    # test case 1 by value
    itemsInBag, totalCost = greedy(items, maxWeight, Item.get_value)
    print(f"The items in the bag are: {itemsInBag}\
          \nThe total cost of the items is {totalCost}")
    
    # test case 2 by smallest weight
    itemsInBag, totalCost = greedy(items, maxWeight, lambda item: 1/ Item.get_weight(item))
    print(f"\nThe items in the bag are: {itemsInBag}\
          \nThe total cost of the items is {totalCost}")
    
    # test case 3 by value per weight
    itemsInBag, totalCost = greedy(items, maxWeight, Item.get_value_per_weight)
    print(f"\nThe items in the bag are: {itemsInBag}\
          \nThe total cost of the items is {totalCost}")
    



names = ['wine', 'beer', 'pizza', 'burger', 'fries',
'cola', 'apple', 'donut', 'cake']
values = [89,90,95,100,90,79,50,10]
calories = [123,154,258,354,365,150,95,195]

foods = build_items(names, values, calories)
test_greedy(foods, 750)
