import json


def loadData():
    with open("data.json") as f:
        return json.load(f)


def create():
    print("Performing Create Operation")
    name = input("Enter the username")
    email = input("Enter the user email")
    role = input("Enter the user Role")
    data = loadData()
    if data:
        unique_id = max(eachData["id"] for eachData in data) + 1
    else:
        unique_id = 1
    userData = {"id": unique_id, "name": name, "email": email, "role": role}
    data = loadData()
    data.append(userData)
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)


def read():
    print("Performing Read Operation")
    read = input("Do you want to \n 1. See All Records \n OR \n 2.Specific Person ID\n")
    if read == "1":
        data = loadData()
        print(data)
    elif read == "2":
        choseId = int(input("Enter the UserId\n"))
        data = loadData()
        for eachData in data:
            if choseId == eachData["id"]:
                print(eachData)
                break
        else:
            print("Invalid")


def delete():
    print("Performing Delete Operation")
    choseId = int(input("Enter the UserId\n"))
    data = loadData()
    for eachData in data:
        if choseId == eachData["id"]:
            data.remove(eachData)
            with open("data.json", "w") as file:
                json.dump(data, file, indent=2)
                print(data)
                break

    else:
        print("You have selected an invalid Id")


def update():
    print("Performing Update Operation")
    choseId = int(input("Which Id you want to edit \n"))

    data = loadData()
    print(data)
    for eachData in data:
        # print(eachData)
        if eachData["id"] == choseId:
            eachData["name"] = input("Enter the username")
            eachData["email"] = input("Enter the user email")
            eachData["role"] = input("Enter the user Role")
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)


print("----CRUD----")
print("1. Create")
print("2. Read")
print("3. Update")
print("4. Delete")
print("5. Exit")


while True:
    choose = int(input("Enter Your Choice (1-5) \n"))

    if choose == 1:
        create()

    elif choose == 2:
        read()

    elif choose == 3:
        update()

    elif choose == 4:
        delete()

    elif choose == 5:
        break
    else:
        print("Invalid Operation")
