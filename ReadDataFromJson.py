import json
myjsonfile=open('jsonFiles/employee.json','r')
jsondata=myjsonfile.read()

obj=json.loads(jsondata)
print(str(obj['firstName']))
print(str(obj['lastName']))
list=obj['address']
print(list)
print(len(list))
for i in range(len(list)):
    print("address of",i,"is ....")
    print("street:", list[i].get("street"))
    print("city:", list[i].get("city"))
    print("state:", list[i].get("state"))