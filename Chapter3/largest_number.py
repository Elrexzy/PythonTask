numbers = []

largest = 0
for index in range(10):
      number = int(input("Enter a number: "))
      numbers.append(number)
      if numbers[index] > largest:
            largest = numbers[index]
print(largest)
