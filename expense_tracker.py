# Project_2 - Expense Tracker : DecodeLabs

print("-" * 40)
print("       Personal Expense Tracker")
print("-" * 40)

print("Welcome! Track your Expenses.")
print("Enter an Expense Amount.")
print("Type 'quit' to finish!\n")

# Initilization 
total = 0
transaction_count= 0

# Storing each expense in the list
expenses = []

# Countinue Expense Entry 

while True :
    user_input = input("Enter Expense :").strip()

    # kill Switch
    if user_input.lower() == "quit":
        break

    # Validate Process Input
    try:
        new_expense = float (user_input)

        if new_expense <= 0 :
            print ("Please Enter a Positive Amount.")
            continue

        # Accumulator

        total = total + new_expense
        transaction_count += 1

        # Storing Indiviual Expense 
        expenses.append(new_expense)

        # Success Message

        print("Expense Added Successfully!")
        print(f"Current Total : ${total:.2f}\n")

    except ValueError:
        print("Invalid Input ! Please enter the number input")

# Displaying All Enteries 
print("-" * 40)
print("       All Expenses Today")
print("-" * 40)

for index , expense in enumerate(expenses , start=1):
    print (f"Transaction {index}. ${expense:.2f}")

# Total Summary 
print("-" * 40)
print (" Total Summary of Today's Expenses")
print("-" * 40)

print(f"Total Transactions :{transaction_count}")
print(f"Total Expense : ${total:.2f}")
print("-" * 40)
print("Thanks for using Expense Tracker\n Goodbye!!!")

