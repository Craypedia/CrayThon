my_dict = {'key':"This is the value", "key2": "Another value"}

#You can change values of a dictionary and create new key value pairs using the following methods

my_dict["key3"] =  "Latest value"

my_dict["key"] =  "Edited value"

print(my_dict)

p = {"key4": "4th value", "key5":"5th value"}

my_dict.update(p)
print(my_dict.items())

#Methods of finding keys 

print(my_dict.get("key", "Anything"))
print(my_dict.get("xyz", "Not found"))


data = {"Name": "Chuks", "Location":"Aba", "Job":"Senior Frontend", "Salary": "$50,000"}
data["City"] = data.pop("Location")
print(data)



if "ada" == "john":
    print('True')
else:
    print("False")




user_data = { }
userEmail = input("Enter Email")
userName = input("Enter Name")

if user_data == userEmail:
    print("You already have an account")
else:
    ask = input("Would you like to create an account?:\nYes or No:")
    if ask.lower() == "Yes":
        new = {userEmail: userName}
        user_data.update(new)
    else:
        ("Thank you for registering")
print(user_data)