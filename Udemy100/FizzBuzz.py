# Write your code here 👇

for numbers in range(1, 101):
  if numbers % 5 == 0 and numbers % 3 == 0:
    print("FizzBuzz")
  elif numbers % 5 == 0:
    print("Buzz")
  elif numbers % 3 == 0:
    print("Fizz")
  else:
    print(numbers)
