#json- javascript object notation
import json
'''person={"name":"Jhon","age":30,"city":"chandigarh","hasChildren":False,"titles":["engineer","prgrammer"]}
personJSON=json.dumps(person,indent=4, separators=(";","="),sort_keys=True)
print(personJSON)

with open("person.json","w") as file:
    json.dump(person,file,indent=4)'''

    #person =json.load(file)
    #print(person)    

class User:
    def __init__(self,name,age):
        self.name=name
        self.age=age
user = User("Max",27)

def encode_user(o):
    if isinstance(o,User):
        return {"name":o.name,"age":o.age,o.__class__.__name__:True}
    else:
        raise TypeError("object of type User is not JSON serializable")
from json import JSONEncoder

userJSON=json.dumps(user,default=encode_user)
print(userJSON)