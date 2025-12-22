# Loops
#iteration/iterative
""" using Loop in python is different from other programming languages so we use for loop like this:
for and a variable to store the name and in and that actual variable name
for age in my_age:
  print(age)
"""


name_list=["Elon", "Jeff", "Mark", "Trump","Max"]
greetings="Hello, have a good day"

#for loops
for name in name_list:
    print(name)

# Loops in string
for word in greetings:  # so this prints the word only, if we use loop in just string it prints single letter only like 
    """
    h
    e 
    l 
    l 
    o
    """
    print(word)  # it prints the letter 

#Search
# we can search whether the element exist in that particular variable or not.
for name in name_list: 
    if name=="Trump":
        print("Yes, Trump exist on the name list ")