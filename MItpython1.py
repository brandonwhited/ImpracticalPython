x = int(input("Enter a number an integer greater than 2:")
smallest_factor =  None
for guess in range(2,x):
  if x % guess == 0:
    smallest_factor = guess
    break
if smallest_factor != None:
  print(f"Smallest factor other than 1 is {smallest_factor}")
else:
  print(x, "is prime")
  
x = int(input("Enter a number an integer greater than 2: "))
largest_divisor = None
for guess in range(x - 1, 1, -1):
    if x % guess == 0:
        largest_divisor = guess
        break
if largest_divisor != None:
    print("Largest divisor other than", x, "is", largest_divisor)
else:
    print(x, "is prime")
    
    