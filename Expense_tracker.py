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
    
    def __init__(self, amount, cat, file, dic):
        self.amount = int(amount)
        category = ["Travel", "Groceries", "Medicines", "Rent"]
        print(category)
        self.cat = int(cat)
        self.file = file
        self.dic = {category[self.cat]: self.amount}
     

    def save(self):
        name = self.file
        fileobj = open("expense1.json", "w")
        json.dump(self.dic, fileobj)

    def load(self):
        fileobj = open("expense1.json", "r")
        data = json.load(fileobj)
        print(data)
        #self.dic = data

    def display(self):
        for k, v in self.dic.items():
            print(k, ":", v )

while(True):
    print("1. Adding a new expense")
    print("2. Save to a file")
    print("3. Load from a file")
    print("4. Display expense")
    print("5. Exit")
    choice = int(input("Enter your choice[1-5]: "))
    
    if choice == 1:
        amount = input("Enter amount: ")
        cat = int(input("Enter category: "))
        ex = Expense(amount, cat , "expense", {})
        #ex = Expense(1000, "travel" , "expense", {})
    
    elif choice == 2:
        ex.save()

    elif choice == 3:
        ex.load()

    elif choice == 4:
        ex.display()

    elif choice == 5:
        break



    

        
        



           
