def find_volume(length=1, width=1, depth=1):
  return length * width * depth

result = find_volume(width=10)
print(result)

result = find_volume()
print(result)

result = find_volume(2,5,7)
print(result)

def find_volume_2(length=1, width=1, depth=1):
  return length * width * depth, length, 'hola'
result = find_volume_2()
print(result)

result_1,result_2,result_3 = find_volume_2()
print(result_1)
print(result_2)
print(result_3)