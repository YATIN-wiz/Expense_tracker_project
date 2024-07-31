import json

class Expense:
    category = ["Travel", "Groceries", "Medicines", "Rent"]
    def __init__(self, amount, cat):
        self.data = {
            "amount": amount,
            "cat": cat
        }

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
       print(f'{self.data["amount"]} on {self.category[self.data["cat"]]}')

#main starts here
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
        expenses.save()

    elif choice == 3:
        expenses.load()

    elif choice == 4:
       for expense in expenses:
            expense.display()

    elif choice == 5:
        break



    

        
        



           
