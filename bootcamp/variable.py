#variable s and data types
# In python (hash #) is used to write comment
"""
This is how we write multi line comment in python (""" """)
"""

name ='John'
age=24
pie=3.14


print("The name is", name)
print("The age is", age)
print("The value of pie is", pie)


#*** List ****
"""List is same as array and do same work as array"""

names=["Pawan", "Sundar", "Bhuwan", 14, name, pie] # we can use different data types in list and can use variables too 
print(names)
print(names[1]) # we can access the elements by using index which starts from zero 
print(names[5])

#dictionary

#Key, value

userDetail={
    "name": "Harry", # name is key and harry is value
    "age":"28",
    "address":"Birendranagar, Surkhet"
}
print(userDetail)

userName=userDetail.get("name") # we can access the key by using get , we need to store that in a new variable
print(userName)

userAddress=userDetail.get("address")
print(userAddress)

userAge=userDetail.get("age")
print(userAge)