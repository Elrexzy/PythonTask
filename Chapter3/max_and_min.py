value = int(input("Enter a vaule: "))
number = int(input("Enter a number: "))

largest = number
smallest = number

for index in range(1, value):
      number = int(input("Enter a number: "))
      
      if largest < number:
         largest = number
         
      if smallest > number:
         smallest = number
         
print("Largest: ", largest)
print("Smallest: ", smallest)
