import math

# Write your code below this line 👇
def paint_calc(height, width, cover):
    amount = math.ceil(height * width / cover)
    print(f"You'll need {amount} cans of paint.")

# Write your code above this line 👆
# Define a function called paint_calc() so the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input()) # Height of wall (m)
test_w = int(input()) # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)














# def greeting():
#     print("Hello, world!")
#     print("How are you doing")
#     print("YOU BETTER ANSWER ME")
    
    
# def greet_with(name, location):
#     print(f"Hello, {name}")
#     print(f"What is it like in {location}?")

# greet_with("Tim", "London")


