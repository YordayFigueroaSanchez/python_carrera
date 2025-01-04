def sum_with_range(min, max):
  print(min,max)
  sum = 0
  for x in range(min, max):
    sum += x
  return sum

#ejecutar la funcion
result = sum_with_range(4, 10)
print(result)
result = sum_with_range(4, 40)
print(result)
result = sum_with_range(1, 2)
print(result)