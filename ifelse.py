fruit=[
    "mango",
    "orange",
    "apples",
    "pears",
    "pineapple",
    "lime"
]

presidents=[
    "kennedy",
    "lincoln",
    "trump",
    "obama",
    "biden",
    "bush"
]

animals=[
    "monkey",
    "giraffe",
    "bird",
    "cow",
    "cat",
    "fish"
]

numbers=[
    "one",
    "two",
    "three",
    "four",
    "five",
    "six"
]

countries=[
    "uk",
    "nigeria",
    "morocco",
    "egypt",
    "ethiopia",
    "france"
]

number=input("Choose a number >")
# print(fruit[int(number)])
# print(presidents[int(number)])
# print(animals[int(number)])
# print(numbers[int(number)])
# print(countries[int(number)])

# import random
# list1=random.choice(fruit)
# list2=random.choice(presidents)
# list3=random.choice(animals)
# list4=random.choice(numbers)
# list5=random.choice(countries)

list1=fruit[int(number)]
list2=presidents[int(number)]
list3=animals[int(number)]
list4=numbers[int(number)]
list5=countries[int(number)]

print("Twas", list1 + ", and the", list2,"toves")
print("Did gyre and", list3, "in the wabe:")
print("All", list4, "were the borogoves,")
print("And the", list5,"raths outgrabe.")