data = {
    "394775875" : {
        "name":"Desmond"
        "dob":"09-09-09",
        "bvn":"1234567890",
        "pin":"1234",
        "bal":"0"
    }
}

print("Welcome To Astroverse App")
print("Enter s to signup or 1 to login:")
choice = input(">").lower()

if choice == '1':
    acc_num = input("Enter your account num:\n>")
    pin = input("Enter your pin:\n>")
    user = data.get(acc_num)
    if user and ['pin'] == pin:
        print(f"Welcome {user['name']}.\nYour account is ${user['bal']}")
        else:
            print("Invalid Login")