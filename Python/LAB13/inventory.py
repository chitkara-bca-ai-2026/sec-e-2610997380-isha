#Inventory Control System
print("====================================================================")
print("     INVENTORY CONTROL SYSTEM   ")
print("====================================================================")
inventory=["pen","eraser","pencil","scale","highlighter","stapler","stapler pins","sticky notepads"]
x=5
while x<10:
    Number=int(input("Select an Operation\n1.View\n2.Add\n3.Remove\n4.Sort\n5.Exit\nENTER NUMBER:"))
    if Number==1:
        #for r in inventory:
         #print(r)
        for i in range(len(inventory)):
             print(f"{i+1}.{inventory[i]}")      
    elif Number==2:
        item=input("what to add:")
        inventory.append(item)
        print(f"{item} has been successfully added to the inventory")
        print(inventory)
    elif Number==3:
        item=input("what to remove:")
        inventory.remove(item)
        print(f"{item} has been successfully removed from the inventory")
        print(inventory)
    elif Number==4:
        inventory.sort()
        print(f"Inventory has been successfully ordered")
        print(inventory)
    elif Number==5:
            print("Thank you,Good bye!")
            break
    else:
         print("Invalid Input")