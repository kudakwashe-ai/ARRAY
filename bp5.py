shopping_list = []
for i in range(5):
    item = input(f"Enter item {i+1}: ")
    shopping_list.append(item)

print("Your Shopping List:", shopping_list)
purchased_item = input("Enter the name of the item you bought: ")

if purchased_item in shopping_list:
    shopping_list.remove(purchased_item)
    print("Updated Shopping List:", shopping_list)
else:
    print("Item not found in the shopping list.")











