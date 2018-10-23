checklist = list()

def create(item):
    checklist.append(item)

def read(index):
    item = checklist[index]
    return item

def update(index, item):
    checklist[index] = item

def destroy(index):
    checklist.pop(index)

def listAllItems():
    index = 0
    for listItem in checklist:
        print(str(index) + listItem)
        index += 1

def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")
    destroy(1)

    print(read(0))

def select(function_code):
    # Create item
    if function_code == "C":
        input_item = input("Input item: ")
        create(input_item)

    # Read item
    elif function_code == "R":
        item_index = input("Index Number: ")

        # Remember that item_index must actually exist or our program will crash.
        print(read(int(item_index)))

    # Print all items
    elif function_code == "P":
        listAllItems()

    elif function_code == "D":
        index = input("Index Number: ")
        checklist[index] = "√" + checklist[index]

    # Catch all
    else:
        print("Unknown Option")

running = True
while running:
    selection = input(
        "Press C to add to list, R to Read from list, D to mark done, and P to display list \n")
    select(selection)
