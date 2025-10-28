inventory = []

def add_item():
    inventory.append("Dog chain")
    
add_item()
print(inventory)

def main():

    add_item("dog food")
    add_item("cat toy")
    add_item("bird cage")
    add_item("fish tank")

def count_item(items):
    if not items:
        return  0
    else:
        return 1 + count_item(items [1:])
    
total = count_item(inventory) 
print("no. of items in the list", total)

show_item = lambda item: print(f"Item in Stock: {item}")

for item in inventory:
    show_item(item)

main()
    







