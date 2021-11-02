from prettytable import PrettyTable

is_on = True
global contact
contact = [['A', '1', 'a', 'F']]
table = PrettyTable()
table2 = PrettyTable()
action = ["Add","Delete","See","Update", "Exit"]
priorities = ["F","Fr","P"]
table.add_column("Action", action)

# function
def add():
    this_contact = []
    name = input("Enter a contact name. ")
    number = input("Enter a contact number. ")
    email = input("Enter a contact email. ")
    priority = input("Enter a contact priority. (F: Familly, Fr: Friend, P: professionnal)")
    while priority not in priorities:
        priority = input("Enter a contact priority. (F: Familly, Fr: Friend, P: professionnal). ")
        print("please enter the valid priority")
    
    this_contact.append(name)
    this_contact.append(number)
    this_contact.append(email)
    this_contact.append(priority)
    print(this_contact)
    contact.append(this_contact)
    print(contact)

def delete():
    name = input("Enter a contact name. ")
    find = False
    i = 0
    for j in contact:
        if j[i].lower() == name.lower():
            del contact[i]
            find = True
            break
        else:
            find = False
        i += 1
    if find == False:
        print("This name don't exist with contact book")
    else:
        print("Delete successfully")

def see():
    table2.field_names = ["Name", "Number", "Email", "Priority"]
    for i in contact:
        table2.add_row(i)
    print(table2)
    
while is_on:
    print("Contact Book")
    print(table)
    choose = input("What you like to do? : ").lower()
    if choose == "add":
        add()
    elif choose == "delete":
        delete()
    elif choose == "see":
        see()
    elif choose == "update":
        print("update")
    elif choose == "exit":
        is_on = False
    else:
        print("This choose a valid choose")