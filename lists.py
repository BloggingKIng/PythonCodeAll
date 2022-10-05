fruits = ['apple','banana','mangoes','oranges'] # declaring a list

fruits.append('strawberries')  # adds element at the end of the list
print(fruits)

print(fruits[0])  # accessing the element at index 0

fruits.insert(0,'grapes')  # inserts grapes in list at index 0

print(fruits)

fruits.remove('apple')  # removing apple from list

print(fruits)

print(fruits[-1]) # accessing the last element of the list

fruits.pop(3) # removes element at index 3 and will also print out the removed element 

print(fruits)

moreFruits = ['blueberries','cherries']

fruits.extend(moreFruits)
print(fruits)