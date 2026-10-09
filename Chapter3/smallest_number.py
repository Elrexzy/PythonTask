numbers = []

smallest = 0
for index in range(10):
      number = int(input("Enter a number: "))
      numbers.append(number)
      if index < smallest:
            smallest = numbers[index]
print(smallest)
