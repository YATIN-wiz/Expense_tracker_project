import json

class Expense:
    category = ["Travel", "Groceries", "Medicines", "Rent"]
    def __init__(self, amount, cat):
        self.data = {
            "amount": amount,
            "cat": cat
        }
    def getdata(self):
        return self.data

  
        
    def display(self):
       print(f'{self.data["amount"]} on {self.category[self.data["cat"]]}')


def save_all(data):
    l = []
    fileobj = open("expense.json", "w")
    for expense in data:
        l.append(expense.getdata())
    print(l)
    json.dump(l, fileobj)
   

def load(expenses):
    fileobj = open("expense.json", "r")
    data = json.load(fileobj)
    expenses.append(data)
    #for datum in data:
       # print(datum)

expenses = []


while(True):
    print("1. Add a new expense")
    print("2. Save to a file")
    print("3. Load from a file")
    print("4. Display expense")
    print("5. Exit")
    choice = int(input("Enter your choice[1-5]: "))
    
    if choice == 1:
        amount = input("Enter amount: ")
        for i, cat in enumerate(Expense.category):
            print(i, cat)
        
        cat = int(input("Enter category: "))
        expenses.append(Expense(amount, cat))
       
        #ex = Expense(1000, "travel" , "expense", {})
    
    elif choice == 2:
        save_all(expenses)
        
    #    save(expenses)

    elif choice == 3:
        load(expenses)

    elif choice == 4:
       #print(expenses)

       for expense in expenses:
           print(expense)  #.display()

    elif choice == 5:
        break

    

        
        



           
