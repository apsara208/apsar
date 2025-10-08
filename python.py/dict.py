#dictionary=collection of key value pairs
#ordered,mutable,no duplicates
rolls={"as":1,
       "bs":2,
       "cs":3,
       "ds":4}
print(rolls.get("as")) #1 - works on keys

#update
rolls.update({"es":5})
rolls.update({"as":10})
print(rolls)

#pop
rolls.pop("es")
print(rolls)
rolls.popitem()
print(rolls)

#clear
'''
rolls.clear()
print(rolls)'''

print(rolls.keys()) #iterable
#can be used in loops
for key in rolls.keys():
    print(key)

#same with values: rolls.values()
#also keys,values together
for key,value in rolls.items():
    print(f"{key} is of value {value}")