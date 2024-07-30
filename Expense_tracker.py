import json

travel,grocery,entertainment,medicines,rent,books = 0,0,0,0,0,0

amt = 0

"""while(True):
    print("1. Adding a new expense")
    print("2. Save to a file")
    print("3. Load from a file")
    print("4. Display expense")
    print("5. Exit")
    dic = {"Travel:", travel,"Groceries:", grocery,"Entertainment:", entertainment,"Medicine", medicines,"Rent:", rent,"Book:", books}

    choice = int(input("Enter your choice[1-5]: "))
    #travel,grocery,entertainment,medicines,rent,books = 0

    if choice == 1:
        while(1):
            print("1. Travel")
            print("2. Groceries")
            print("3. Entertainment")
            print("4. Medicines")
            print("5. Rent")
            print("6. Books")
            print("7. Exit")
           
           #travel,grocery,entertainment,medicines,rent,books = 0
            ch = int(input("Enter choice:"))
            count = 0

            if choice == 1:
                amt = int(input("Enter your amount:"))
                travel += amt
                
            elif choice == 2:
                amt = int(input("Enter your amount:"))
                grocery += amt
               
            elif choice == 3:
                amt = int(input("Enter your amount:"))
                entertainment += amt
               
            elif choice == 4:
                amt = int(input("Enter your amount:"))
                medicines += amt
                
            elif choice == 5:
                amt = int(input("Enter your amount:"))
                rent += amt 
                       
            elif choice == 6:
                amt = int(input("Enter your amoun:"))
                books += amt
           
                
            elif choice == 7:
                print("Exit!")
                break
        
   


    elif choice == 2:
        filename = input("Enter filename")
        fileobj = open("filename.json", "w")
        json.dump(dic , fileobj)

    elif choice == 3:
        filename = input("Enter filename")
        fileobj = open("filename.json", "r")
        data = json.load(fileobj)
        print(data)

    elif choice == 4:
      
        for k, v in dic:
            print(k, ":", v)
        break
    elif choice == 5:
        break

    else:
        print("Invalid choice!")"""
        

''' print("Total expenses:")
        #if(travel != 0):
        print(travel, " on travel. ")
        #elif (grocery != 0):
        print( grocery, " on groceries.")
        #elif (entertainment != 0):
        print(entertainment, " on entertainment.")
        #elif (medicines != 0):
        print(medicines, " on medicines.")
        #elif (rent != 0):
        print(rent, " on rent.")
        #elif (books != 0):
        print(books, " on books.")'''

class Expense:
    def __init__(self, amount, category):
        self.amount = int(amount)
        self.category = input("category")
        self.filename = input("ENter filename")
        self.__dict__ = {"self.category": self.amount}

    def save(self):
        fileobj = open("self.filename.json", "w")
        json.dump(self.__dict__, fileobj)

    def load(self):
        fileobj = open("self.filename.json", "r")
        data = json.load(fileobj)
        self.__dict__ = data

    def display(self):
        for k in self.__dict__:
            print(k, ":", k[1])

ex = Expense(1000, "travel")
ex.save()
ex.load()

ex.display()


    

        
        



           
