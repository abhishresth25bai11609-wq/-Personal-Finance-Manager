finance = []
while True:
    print   ("\n===== Personal Finance Manager =====")
    print ("1. Add Income")
    print ("2. Add Expense")
    print ("3. View All Transactions")
    print ("4. Show Balance")
    print( "5. Exit")
    choice = input ("Enter your choice: ")
    if choice == "1":
        amount = float(input ("Enter income amount: "))
        source = input ("Enter income source: ")
        finance.append (("Income", amount, source))
        print("Income added successfully!")
    elif choice == "2":
        amount = float(input("Enter  expense  amount: "))
        reason = input("Enter expense reason: ")
        finance.append(("Expense", amount, reason))
        print("Expense added successfully!")
    elif choice == "3":
        print("\n--- All Transactions ---")
        if not finance:
            print("No records found.")
        else:
            for entry in finance:
                print(f"{entry[0]}  |  ₹{entry[1]}  |  {entry[2]}")
    elif choice == "4":
        income = sum(x[1] for x in finance  if x[0] == "Income")
        expense = sum(x[1] for x in finance if x[0] == "Expense")
        print("\nTotal Income   :", income)
        print("Total Expense :", expense)
        print("Balance       :", income - expense)
    elif choice == "5":
        print("Thank you for using the Finance Manager!")
        break
    else:
        print("Invalid  choice! Please try again.")
