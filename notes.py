# Day 1 
# ============================================================================================================
# 
# We looked at data types and methods.
# We’ve been using 4 data types – we’ve had strings, which represent characters. We use these with quote marks
print("This is a string")
# We’ve used integers which are whole numbers. This is the mathmatical value one hundred and twenty three
print(123)
# If you’ve got a decimal though, it’s a floating point
print(123.5)
# We’ve also had Boolean values – true and false. These are binary data types, on and off, 0 or 1. It is true, it is false, it cannot be both. For python to recognise us using a boolean, the words true or false need to start with a capital letter.
print(True)
print(False)
# We briefly touched upon none, a placeholder value that will allow our code to run without data
print(None)

# Properties are bits of information about our data. Data about the data! For example, how long is a string? 
# Rather than count it (which we might not be able to do!) we can use the len() function to find out!

print(len("Hello"))

# print the length of the string "hello" - and our terminal should show 5!

# we can use index position to pinpoint a particular character in the string

#when we use index, we need to remember that it starts at 0

print("hello"[0])  #will show "h" - even through WE see it as the first character, in this case it has an index of 0
print("hello"[1])
print("hello"[2])
print("hello"[3])
print("hello"[4])

# Methods are functions we can use on specific objects. Data types have assosiated methods - things we can do to them specifically. Methods usually let us modify or add data. 

print("Hello".upper()) #makes the whole string uppercase
print("HELLO".lower()) #makes the whole string lowercase
print("                 hello    ".strip()) #removes trailing spaces
print("hello".strip("h")) # or specified terms from the START and END of the string

#there are other methods - like replace, count and find

print("the quick brown fox".upper()) #upper() makes all lowercase characters uppercase within the specified string. It does not need parameters
print("THE QUICK brown fox".lower()) #lower() makes all uppercase characters lowercase within the specified string. It does not need parameters
print("the quick bROWn fox.".capitalize()) #capitalize() will capitalise the first letter of the string, and make any other character lowercase. It only works per string, sentences mean nothing. It does not need parameters

print("the quick brown fox fox fox".count("fox")) #count needs one parameter. It counts all instances of the parameter, and displays the amount in the terminal. This example would return "3".
print("the quick brown foxfoxfox".count("fox")) #this example would still return 3, because our parameter is the word fox with no spaces either side
print("the quick brown fox fox fox".count("fox ")) #this example would return 2, because our paramter has a space at the end, and only two examples of the word fox do
print("the quick brown fox fox fox".count("Fox ")) #this example would return 0. There are no instances of fox with a capital F in our string. The paramters are EXACT MATCHES

print("the quick brown fox".find("quick")) #find() will give the index value of the first occurrence of the specified term in a string. Here, it will show us the index of the start of quick, which is q. Because it is index, it starts the count from 0. The output is 4, even though q is the 5th character. 

print("the quick brown fox".replace("fox","frog")) #replace() will replace a term with another term in a specified string. This will output as "the quick brown frog". It needs two parameters to work as intended

print("the quick brown fox          ".strip()) #strip() removes characters from the beginning or the end of a string - depending on the parameter. If no character is specified, it will remove spaces

print("the quick brown fox".strip("the")) #strip() would remove the word "the"
print("the quick brown fox".strip("brown")) #strip() would not remove anything - it only looks at the start and the end

#these methods are built in to python, we can access more using libraries
#--------------------------------------------------------------------------------------------------------------------------------------------#

#Day 2 - Variables

#variables are like boxes we can store out data in. It's easier for use to carry round everything we need in a box, rather than the individual items!
# we give out variables unique names, so we know what's inside them, and so we can refer to them within our code
# we don't have to declare a data type for a variable - python already knows

my_name = "Klong"       #is a string
my_age = 30             #is an integer
happy = False           #is a boolean

#when we name a variable - we use snake case! things are written in lower case, joined by underscores. 
# we can then just call our variable by name to use it!

print(my_name)    #will print Klong to the terminal!

# you can update the value of a variable by just defining it again
my_name="Katherine"
print(my_name)   #will print Katherine to the terminal - but any use of my_name before line 59 is still Klong! We haven't changed the value - we've updated it

# we can put our variables into strings to give them more context

print("My name is", my_name)
print("My name is " + my_name)
print("My name is {}".format(my_name))
print(f"MY name is {my_name}")

# All of these will print "My name is Katherine" to the terminal - they're just different ways of doing it!
# the last one (print(f"MY name is {my_name}")) is called an f string - and is the most recent. Not all versions of python support it, though!

# python can do maths for us!
# These are called arithmetic operators
# + is addition
# - is subtraction
# * is multiplication
# ** is to the power of
# % is modulo - it divides two numbers - but it only returns the remainder (the modulous)

# sometimes it's as simple as writing
print(1+2)     #this will print 3

# but we can also use variables for this!

num1 = 1
num2 = 2
print(num1+num2)

#this is very overcomplicated in this situation - but having using variables means you can update them!

num1 = 7
num2 = 2
num1 = 12
print(num1+num2)

#on line 84 - num1 = 7, but we update it on line 86. By the time it gets to the sum on line 87, num1=12, so 14 will be printed to the terminal
# when we use variable_name="bit of data", we are using equals to assign a value. = is an assignment operator
# we can use of arithmetic operators with our assignment operators to update the value of variables!

num1=7 # gives our variable num1 the value of 7

num1 +=1 # now updates the value of num1 to one more than it was
print(num1)   #so num 1 now equals 8

# This can be really useful - because when other people use your programs, you won't be able to update the variables yourself!
# For example, if you get your pin number wrong three times in a cash machine, what happens?
# it kicks you out - but how does it know?

# the bank might have a variable called "attempts" which starts at 0 - but each time you enter your pin, attempts +=1
# so if it gets to three, you're stuck!

# another kind of operator is a comparison operator
# == is equal to
# != is not equal to
# > greater than
# >= greater than or equal to
# < less than
# <= less than or equal to

# we can use these to compare two values - but what can we do with that information?

#variables are very handy for us to work types of data, without knowing what that data is! Because sometimes, we might be waiting for a user to give us data! 

#input("What is your name      >")

#a variable let's us save that data, and work with it elsewhere!

#name=input("What is your name?")
#print(f"Hello, {name}!")

#--------------------------------------------------------------------------------------------------------------------------------------------#

# Day 3 - if else

# We can write situations into our code using "if"
# we write it like this:
#if condition:
    #do this
#elif condition:
    #do this
#else:
    #do this

# if is our first statement - if it is true, python will run the next section (the indented bit)
# if if isn't true, python goes down to the elif (else if...) and sees if it can run that
# else is out last statement - it's a cover-all. If nothing matches, else will run. That's why it doesn't need a condition
# ALWAYS be aware of your orders in if statements. Python reads top down, and as soon as it hits a statement that's true, it will run it, even if there's a more true statement after!

#if statements are a good place for our comparison operators

num1 = 20
num2 = 40

if num1 < num2:                                   # if the number assigned to our variable num1 is smaller than the number assigned to our variable num2
    print("Num1 is smaller")                      # do this action
elif num1 > num2:                                 # else if the num1 is bigger than num2
    print("num1 is bigger")                       # do this
elif num1 == num2:                                # if the values we've assigned num1 and num2 are exactly equal
    print("The are the same")                     # do this
else:                                             # if none of the above statements are true
    print("Well how did that happen?")            # do this

# that's not a very efficient code! You can make that smaller - it's just to show you different operators!
# let's have another look at a cash machine

pin=1234

if pin!=1234:
    print("Your pin is incorrect")
else:
    print("correct pin")

# line 160 is saying "if the value we gave the variable 'pin' does not equal 1234"
# we can see that pin is 1234, so the if statement isn't true, and will run to the else instead

# we can use and in our statements!

#let's see if the user is using the right pin for the card!

pin=1234
card="mastercard"

if pin==1234 and card=="visa":
    print("card and pin accepted")
elif pin!=1234 and card=="visa":
    print("This is not the correct pin for this card")
elif pin==1234 and card!="visa":
    print("please try your visa card")
else:
    print("Both your pin and your card are wrong")

# when we use and, BOTH statements have to be true for the condition to run. As soon as one is false, the whole line is false, and it will move on

# unlike or, which we can also use. When we use or, only one statement has to be true for it to run

pin=1234
card="mastercard"

if pin==1234 or card=="visa":
    print("Close enough!")
else:
    print("Both your pin and your card are wrong")

# we can get our if/elif/else to do anything we want! Remember when we said about pin tries?

tries=0

pin=1234

if pin==1234 and tries <4:
    print("Success")
elif pin!=1234 and tries <4:
    print("Oh no, try again")
    tries +=1
    print("you have tried {} times".format(tries))
elif tries >=4:
    print("oops")

# Lists!

# Lists are nice!

# Lists are ways that can store lots of items in one variable 
# we use square brackets for lists!

fav_songs=["Buddy Holly - Weezer",
    "Sleep - My Chemical Romance",
    "15 Step - Radiohead"
]

# When we make items in a list, we seperate them by commas. Also, depending on our data type, we might need quotes!
# look at our list - each of those items is in their own set of quotes, seperated by commas 

#we can then just call the list by calling it by its variable name

print(fav_songs)

# you can access specific items in the list using its index position. So in this case, I want to target
# the MCR song

#Remember, on strings and lists, python uses index!

#I can write print(fav_songs[1])
print(fav_songs[1])

# so we are asking it to print the index 1 of fav_songs
# we can also use index to update a value in the list

print(fav_songs)

#I want to swap Weezer for Blink-182, so I can use the index position to do that
# I can do it in a similar way to how I would update any other variable - but I need to target
# the specific position! Otherwise I would replace the whole list!

fav_songs[0]="I Miss You - Blink-182"
print(fav_songs)

# In your terminal, you should see how that's updated!
#We can use other methods on our list! Like len

print(len(fav_songs))
#len will print out the number of items in the list though, not how many characters there are!
# you can use index to target a specific item in the list and use len on that

print(len(fav_songs[0]))
# that will show us how many characters are in that item
# We can add things to our list with append

fav_songs.append("Army of Me - Bjork")

# this updates the list
print(fav_songs)
# the new item, by default, goes at the end of the list
# append will only add one item as it only takes one parameter
# you can add a list to a list with append - but that's going to make a list IN a list. 
# There are other methods you can use!
# you can also remove items from a list using pop (like a balloon)
# pop can take no parameters and remove the last item on the list

fav_songs.pop()
#that will now print the list without Bjork - or you can give it an idex position to target a specific item
# this would be written as:
#fav_songs.pop(1)
# pop can't take a string - you couldn't write:
#fav_songs.pop("Army of Me - Bjork")
# it only takes integers!

#there are methods we can use on lists - just like strings!

# remove removes an specific item from the list using its value rather than an index position. Remove only takes one arguement - it will only remove one thing at a time
fav_websites=[
    "Reddit",
    "Neopets",
    "Wowhead",
    "GrowRPG"
]

fav_websites.remove("GrowRPG")
print(fav_websites)

#remove updates the list - from now on, the list will now have GrowRPG in

print(len(fav_websites)) # we can see that by printing it, but also, len is only three!

#reverse reverses the order of the list

fav_websites.reverse()

print(fav_websites)

#this updates the list - from now on, it is in this order. if we use pop, it will remove reddit - even though that's first when we wrote it!

fav_websites.pop()
print(fav_websites)

#I'm just going to make a new list now =p

fav_websites=[
    "Reddit",
    "Neopets",
    "Wowhead",
    "GrowRPG"
]

#sort will sort the list alphabetically - but can sort it by reverse alphabetically, or by a function

fav_websites.sort()
print(fav_websites)

#this updates the list - from now on, it is in this order. if we use pop, it will remove wowhhead!

fav_websites.pop()
print(fav_websites)

#loops are ways yo make our code repeat actions - it automates things for us!

# If I asked you to make a list of your favourite drinks, and then print those items out one at a time, you'd probably write:

fav_drinks=["juice", "tea", "water"]

print(fav_drinks[0])
print(fav_drinks[1])
print(fav_drinks[2])

#and that's a fine way of doing it! But what if you had a list of 1000 items....?

#for loops can make this job easier for us!

# we use for loops when we know how many times we want the loop to run. In this case, we want the loop to run for as many items as there are in the list

# we define a for loop using "for" and they're written as:

for drink in fav_drinks:
    print(drink)

# for is the loop, we need that as a keyword!

# drink is a variable. Each time the loop runs, it takes the value of the next item in the thing we are looping through. 
# in lets the code know what the thing we want to loop through is - in this case, it's the list "fav drinks"
# we use a colon and in an indent - like in our functions and our if statements, we can ask the for loop to do whatever we want
# in this case - we just want it to print the item. 

# so that code sort-of translates to:

#"for every item in the list fav_drinks":
# print out that item

# you might see it written as:

for i in fav_drinks:
    print(i)

# it does the same thing. The second word is just a variable that represents each item =]

# so the first time that code runs, i / drink = "juice"
# the second time it runs, i / drink = "tea"
#the third time it runs, i / drink = "water"
# there are no more items for it to iterate through now, so the loop stops

# there are many things we can ask a for loop to work with - one is "range"

for i in range(10):
    print(i)

# this will print out the values 0-9 (which is 10 values)

# using range means we can ask out code do something a certain number of times! If I wanted an action to occur 10 times, I could use range

# range takes three parameters, but only NEEDS one

# the first one is the start value. By default, this is zero. The second number is our dtop value - in our example, this is 10
# Range stops short of the value you put in as the stop value. I googled why, and stack overflow said:
# "This is just how python's range works."

#The final value is the step - how we get from one value to another. By default it is 1. 

#so our example:

for i in range(10):
    print(i)

# is the same as writing:


for i in range(0,10,1):
    print(i)

# if we wanted the step to be two we would write:

for i in range(0,10,2):
    print(i)

# and this would print out the numbers 0,2,4,6,8

# or if we wanted to start our count at 2, we could write:

for i in range(2,10,2):
    print(i)

# and this would print 2,4,6,8

# Remember on,line 53 when I said if I wanted an action to occur 10 times, I could use range?

# remeber, we can ask our for loop to do anything! So far, we've been asking it to print the item at each loop - but we don't have to!

# if I wanted to print the sentence "Here's an ice cream" 20 times, I could write:

for i in range (20):
    print("Here's an ice cream")

# or I could mix it up!

class_names=["Ash","Anthony","Elmi","Graham","Kat","Markus","Michal D","Michael S","Tom"]

for name in class_names:
    print(f"Thanks for all your hard work in week one, {name}!")
    print("Hope you enjoyed it!")

# there are MANY things you can ask a for loop to do - check on W3 schools for more info!

# There is another kind of loop!

# While loops!

# We use for loops when we know how many times the loop will run. (Even if we don't know the EXACT number. If we have a list with hundreds of items in, the loop can only run at its max for as many items as there are in that list. We might not have an exact figure - but we have a limit!)

# while loops run until a condition is met. We can define this condition!

num = 0                                              #our variable - num. It current equals 0

while num < 10:                                      # while our variable num is less than ten, we want our while loop to:
    num += 1                                         # add one to whatever num is, and update the variable to have that value
    print(num)                                       # and then print this new, updated value of 10

# eventually, the loop will run enough times that num < 10, so it will stop. This code prints out the numbers 1 - 10. Check the order of the code to see why!

#we see as the output:                              Why we see this output:

# 1                                                 # num = 0, which is less than 10. The loops adds 1, prints the new value (1) and goes again
# 2                                                 # num = 1, which is less than 10. The loops adds 1, prints the new value (2) and goes again
# 3                                                 # num = 2, which is less than 10. The loops adds 1, prints the new value (3) and goes again
# 4                                                 # num = 3, which is less than 10. The loops adds 1, prints the new value (4) and goes again
# 5                                                 # num = 4, which is less than 10. The loops adds 1, prints the new value (5) and goes again
# 6                                                 # num = 5, which is less than 10. The loops adds 1, prints the new value (6) and goes again
# 7                                                 # num = 6, which is less than 10. The loops adds 1, prints the new value (7) and goes again
# 8                                                 # num = 7, which is less than 10. The loops adds 1, prints the new value (8) and goes again
# 9                                                 # num = 8, which is less than 10. The loops adds 1, prints the new value (9) and goes again
# 10                                                # num = 9, which is less than 10. The loops adds 1, prints the new value (10) and STOPS. Because

# num now equals 10. Our condition has been met- so the loop doesn't need to go again.

# in this case - because we're just adding one, we kind of know how many times this loop will run. But the situation and conditions won't always be so neat!

# what if I want to generate a random number, and have it match my number? 
# Remember to generate random numbers, we need the random library

import random

my_chosen_num = 13                                  # the number I want the code to find

random_number = random.randint(1,50)                # a random number

while my_chosen_num != random_number:               # while my chosen number (13) doesn't match whatever the random number is:
    print(random_number)                            # print the random number
    random_number = random.randint(1,50)            # and generate a new random number under the same name - otherwise we'd get stuck in the loop forever!

print(f"My number, {my_chosen_num}, matched the random number {random_number}!")  #notice the indents above? Now we're out of the loop, you can tell because it's not indented!
# this line will only run once the lop is broken - in this case, once my_chosen_num == random_number

# run this a few times - you'll see a different amount of attempts each time!

