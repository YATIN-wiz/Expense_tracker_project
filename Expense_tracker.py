import json

class Expense:
    
    def __init__(self, amount, cat):
        self.amount = int(amount)
        
        print(category)
        self.cat = int(cat)
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
       # for i in expense:
           # print(i)
        for k, v in self.dic.items():
            print(k, ":", v )
expense = []
while(True):
    print("1. Adding a new expense")
    print("2. Save to a file")
    print("3. Load from a file")
    print("4. Display expense")
    print("5. Exit")
    choice = int(input("Enter your choice[1-5]: "))
    
    if choice == 1:
        amount = input("Enter amount: ")
        category = ["0. Travel", "1. Groceries", "2. Medicines", "3. Rent"]
        print(category)
        cat = int(input("Enter category: "))
        expense.append(Expense(amount, cat ))
        #ex = Expense(1000, "travel" , "expense", {})
    
    elif choice == 2:
        expense.save()

    elif choice == 3:
        expense.load()

    elif choice == 4:
       
        expense.display()

    elif choice == 5:
        break



    

        
        



           
