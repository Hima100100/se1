x = {
    "name":["ali","omar","hima"],
    "phone":["123","456","789"]
}
y = input("enter name : ")
if y in x ["name"]:
    index=x["name"].index (y)
    phone = x ["phone"][index]
    print (f"{y}'s phone number {phone}")
else:
    print("not found")

