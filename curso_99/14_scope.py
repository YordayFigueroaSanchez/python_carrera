price = 100 # global

def increment():
  price = 205
  price = price + 10
  print(price)
  return price
  
print(price)

price_2 = increment()
print(price_2)