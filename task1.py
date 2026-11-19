with open("demo.txt") as f:
    result = f.read()
    print(result)

obj = {"UpperCase": {}, "LowerCase": {}, "Numbers": {}, "Special Characters": {}}
# abc#$234ABC
for i in result:
    if i.isupper():
        category = "UpperCase"
        # print(category, i)
    elif i.islower():
        category = "LowerCase"
        # print(category)
    elif i.isdigit():
        category = "Numbers"
        # print(category)
    else:
        category = "Special Characters"
        # print(category)

    if i in obj[category]:
        obj[category][i] += 1

    else:
        obj[category][i] = 1

print(obj)
