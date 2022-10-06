import random


x = random.randint(1,150)

# generate a random integer between 1 and 15

print(x)


choices = [
    'Ben',
    'Alax',
    'John',
    'Starc',
    'Buttler',
    'Mitchael'
]

places = [
    'hotel',
    'bar',
    'stadium',
    'watch movie',
    'eat ice cream'
]

people = random.choices(choices, k=2)  # choose 2 random people from choices list

print(people)

place = random.choice(places) # chose a random place from places list

print(place)

print("{} went to {} with {}".format(people[0], place, people[1]))

random.shuffle(places) # shuffles the list
print(places)
