#3. Store user information in a dictionary (name, age, ID)
#and print each key-value pair.

user = {}

user["name"] = input("Enter name: ")
user["age"] = input("Enter age: ")
user["id"] = input("Enter ID: ")

for key in user:
    print(key, ":", user[key])
