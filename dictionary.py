data = {
    'name':'Alex',
    'age' : 12,
    'isTall': True,
    }

# declaring a dictionary in python

data['isStudent'] = True # adding a key value pair to dictionary 



print(data)

print(data['name']) # accessing value of a key in dictionary

data.pop('age') # removing key "age" from the dictionary
print(data)

data['Recent Scores'] = [85,79,40] # you can also use a list as a value in dict

print(data)

print(data['Recent Scores'][0]) # accessing the value of index 0 of key "Recent scores"

data['Recent Scores'].append(12)  # appending a value to list in dict
 
print(data['Recent Scores']) 