print("Welcome to the Tip Calculator")

Total = float(input("What is the total amount of the bill?\n"))
Split_Between = float(input("How many people will be splitting the bill?\n"))
Tip = float(input("What % tip do you wish to leave? EX: 10, 12, 15 or 20%\n"))

Adapted_Tip = Tip / 100 

Final_Product = ((Total * Adapted_Tip) / Split_Between)
Converted_Final_Product = str(Final_Product)
print("Each person shall pay " + Converted_Final_Product + " dollars")