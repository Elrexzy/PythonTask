product_list = ("Laptop", 1200), ("Mouse", 25), ("Keyboard", 45), ("Monitor", 300), ("USB Cable", 10)

def compare_product(product):
      if product[1] >= 100:
            return product
            
result = filter(compare_product, product_list)
print(tuple(result))

     
total = sum(score for name, score in product_list)
print(total)
