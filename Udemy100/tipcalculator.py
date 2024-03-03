print("Welcome to the Tip Calculator")

Total = float(input("What is the total amount of the bill?\n"))
Split_Between = int(input("How many people will be splitting the bill?\n"))
Tip = float(input("What % tip do you wish to leave? EX: 10, 12, 15 or 20\n"))

Adapted_Tip = Tip / 100 


Final_Product = float(((Total * Adapted_Tip) + Total) / Split_Between)


print(f"Each person shall pay {round(Final_Product, 2)} dollars")