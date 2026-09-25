print("Welcome to the tip calculator!")
bill = float(input("What was the total bill in # ?"))
print(f"{bill}")
tip = int(input("How much tip will you like to give? 10%,12%,15%?"))
# if you want to enter the tip pls type the integer value not the percentage else the code will have error and stop half way.
print(f"{tip}")
number = int(input("How many people will split the bill?"))
# enter integer value 
print(f"{number}")
amount = (bill + (bill * tip / 100)) / number
amount_1 = round(amount,2)
print(f"Each person should pay: #{amount_1}")