##To do list
#Samantha
#Stefan

#Initialize

myshoppinglist = ["milk", "eggs", "apples", "bread"]

def add():    
    add= input("What do vou want to add to the list?: ")
    myshoppinglist.append(add)
    print(myshoppinglist)

def view():
    print(myshoppinglist)

def markascomplete():
    ans = input("Select an item from the list to mark as complete: ")
    print(ans)
    i = myshoppinglist.index(ans)
    print(i)
    myshoppinglist(i) == "ans" + "x"
    print(myshoppinglist) 

def remove():
    remove= input("What do vou want to remove from the list?: ")
    myshoppinglist.remove(remove)
    print(myshoppinglist)

def exit():
    exit = input("Do you want to exit the shopping list?: ")
    if exit == "Yes":
        print("You are exiting the shopping list.")
    else:
        shoppinglist()

def removeall():
    myshoppinglist.clear()
    print(myshoppinglist)

def sort(): 
    print(sorted(myshoppinglist))

def count():
    print (len(myshoppinglist))

    
def shoppinglist():
    print("Welcome to your shopping list!")
    print("Please select an option.")
    option = int(input("Option: "))
    if option == 1:
        add()
    if option == 2:
        view()
    if option == 3:
        markascomplete()
    if option == 4:
        remove()
    if option == 5:
        exit()
    if option == 6:
        removeall()
    if option == 7:
        sort()
    if option == 8: 
        count()


   

    
#Main
shoppinglist()