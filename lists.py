shopping_list = ["Milk", "Banana", "Eggs", "Bread", "Apples", "Cheese"]

shopping_list.append("Kip")
shopping_list.append("Coсa Cola")

shopping_list.remove("Cheese")
#print aantal en volledige lijst
print(len(shopping_list))
print(shopping_list)

#bonus controleren of een product op de lijst staat
if "Milk" in shopping_list: 
    print ("Milk is on the shopping list")