import random
countries = ['col', 'mex', 'bol', 'pe']
population_v2 = {country: random.randint(1, 100) for country in countries}
print(population_v2)

result = {country: population for (country, population) in population_v2.items() if population > 30}
print(result)

text = 'Hola, soy Nicolas'
unique = {c: text.count(c) for c in text if c in 'aeiou'}
print(unique)