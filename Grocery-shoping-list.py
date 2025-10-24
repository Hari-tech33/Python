grocery_list = ["milk", "bread", "eggs"]

def add_item(item):
    grocery_list.append("sugar")

add_item("sugar")
print(grocery_list)

def remove_last_item():
    grocery_list.pop()

remove_last_item()
print(grocery_list)

def item():
    return [print(f"item: {i}") for i in grocery_list]

item()

def count_char(items):
    if not items:
        return 0
    else:
        return len(items[0]) + count_char(items[1:])
   
print("total characters =", count_char(grocery_list))