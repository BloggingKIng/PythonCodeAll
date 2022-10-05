fruits = [
    {'name':'Apple', 'color':'red'},
    {'name':'Orange', 'color':'Orange'},
    {'name':'Mango', 'color':'Yellow'}
]

fruit = fruits[0]
print(fruit)

print(type(fruit))

fruit['Taste'] = 'sweet'

print(fruit)

print(fruit.keys())
print(fruit.values())
print(fruit.items())