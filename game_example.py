
# This is an example code showing how blocking code into functions can give the user
# the freedom to move around the program, as opposed to it being linear

# This is a flag variable - flag variables are typically booleans, and they are used to mark if 
# something has already been done or accessed.

#We're using this one to see if the user has already been to the forest. 

# forest_done = False

# the definition for a forest level. When the user has "been here", it will flip the flag from # False to True. Because forest_done is a global variable, we have to use the global keyword to
# change it's value locally (inside the function)

# def forest_level():
#     global forest_done
#     print("You have gone to the forest")
#     print("You have finished at the forest")
#     forest_done = True    <- flip the flag variable
#     where_go()    <- at the end of the process, return the user to the where_go function

# the definition for a forest level.

# def beach_level():
#     print("you have gone to the beach")
#     print("you have finished at the beach")
#     where_go()      <- at the end of the process, return the user to the where_go function

# the where_go function is the central "hub" where users can make choices from. Their input is what controls where they go
# def where_go():

#     print("where do you want to go?")
#     answer = input("    >  ")

#     if answer=="forest" and forest_done !=True:   <- checks the flag variable too
#         print("You have chosen the forest")
#         forest_level()
#     elif answer=="forest" and forest_done ==True: <- checks the flag variable too
#         print("You have been there, pick again")
#         where_go()
#     elif answer=="beach":
#         print("you have chosen the beach")
#         beach_level()
#     else:
#         print("that's not a level")
#         print("You can type forest or beach to select your answer")
#         where_go()    <- if the user types an unexpected option, this else statement makes the where_go() function call itself. This is called recursion. It has good and bad points, so maybe a while loop could do this job, too!

# Everything up until this point is definitions, nothing will run until we press our big start button below

# where_go()  <- calling the where_go() function triggers the proccess

# print("hello world" .upper())

# print ("Hello world"[::-1])

# print("134".isdigit())

# Math="211120000"

# MM = Math.isdigit()

# print(MM)

# Trainer developmental feedback

# The grid you've submitted shows a good understanding of strings. You've used the print function and strings to great effect, showing how the string data type displays characters (including punctuation and spaces.)


# This is a great first step in seeing how information is transformed into output between the text-editor (VSC) and the terminal! 

print("             bananas         apples       kiwis".strip())
#The strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters (space is the default leading character to remove)