symbol = "*"

for index in range(1, 20, 2):

      for space in range(9, (index + 1) // 2 - 1, -1):
            print(" ", end ="")
            
      for count in range(1, index + 1):
            print(symbol, end ="")
            
      print()
      
for index in range(17, 0, -2):

      for space in range(9, (index + 1) // 2 - 1, -1):
            print(" ", end ="")
            
      for count in range(index, 0, -1):
            print(symbol, end ="")
            
      print()
