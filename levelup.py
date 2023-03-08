# Create 5 lists. Each list will contain 6 words.
# Create a program which allows a user to pick a word from
# each list by choosing a number. The user shouldn’t see the lists
# before they chose



# Create 5 lists with 6 words each
list1 = ["apple", "banana", "cherry", "date", "elderberry", "fig"]
list2 = ["grape", "honeydew", "kiwi", "lemon", "mango", "nectarine"]
list3 = ["orange", "peach", "quince", "raspberry", "strawberry", "tangerine"]
list4 = ["ugli", "violet", "watermelon", "xigua", "yellow plum", "zucchini"]
list5 = ["almond", "blueberry", "coconut", "durian", "elderberry", "fig"]

# Combine all lists into one list of lists
lists = [list1, list2, list3, list4, list5]

# Prompt user to pick a number from 1 to 6 for each list
for i in range(5):
    # The expression "for i in range(5):" is a for loop in Python. 
    # It iterates over a sequence of numbers (0, 1, 2, 3, 4) and assigns each number to the variable "i" in each iteration. 
    # The loop will run 5 times. In other words, the code inside the loop will be executed 5 times with i taking on the values 0, 1, 2, 3, and 4.
    print("Choose a number from 1 to 6 for list", i + 1)
    choice = int(input("Enter your choice: "))
    # Validate user input
    while choice < 1 or choice > 6:
        print("Invalid choice. Please enter a number from 1 to 6.")
        choice = int(input("Enter your choice: "))
    # Print the word corresponding to the chosen number
    print("You chose:", lists[i][choice - 1])