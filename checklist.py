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
        print(str(index) + ". " + listItem)
        index += 1

def exit():
    running = false

def markComplete(index):
    original = str(checklist[int(index)])
    update(int(index), "√" + original)

def test():
    running = True
    while running:
        selection = input("Press C to add to list, R to Read from list, D to mark done, Q to quit, and P to display list \n")
        select(selection)

def select(function_code):
    # Create item
    if function_code == "C" or function_code == "c":
        input_item = input("Input item: ")
        create(input_item)

    if function_code == "Q" or function_code == "q":
        quit()
    # Read item
    elif function_code == "R" or function_code == "r":
        item_index = input("Index Number: ")

        # Remember that item_index must actually exist or our program will crash.
        print(read(int(item_index)))

    # Print all items
    elif function_code == "P" or function_code == "p":
        listAllItems()

    elif function_code == "D" or function_code =="d":
        markComplete(input("Index Number: "))

    # Catch all
    else:
        print("Unknown Option")

test()
