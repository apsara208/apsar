mylist=["banana","cherry","apple"]
print(mylist)

mylist2=[5,True,"apple","apple"] #different datatypes and duplicate items allowed
item=mylist2[0]
print(item)
if "apple" in mylist2:
    print("yes")
else:
    print("no")
print(len(mylist2))

#append
mylist2.append("lemon")
print(mylist2)
#insert
mylist2.insert(1,"bluberry") #inser(index,item)

#pop
iten=mylist2.pop()
print(mylist2)

#remove
mylist2.remove(5)
print(mylist2)

#reverse
mylist2.reverse()

#sort
mylist.sort() #in string sort works on first letters a,b,c... order
print(mylist)

#sort reverse
mylist.sort(reverse=True)
print(mylist)

#adding
newlist=mylist2+mylist
print(newlist)

#slicing slicing uses ":"
mylist3=[1,2,3,4,5,6,7,8,9]
a=mylist3[1:5]
print(a)


#equating list
list_org=["a","b","c"]
list_copy=list_org
list_copy.append("d")
print(list_copy)
print(list_org) #change in copy also brings change to the origional one

#copy
#can make actual copy of list via .copy
listy=mylist3.copy()

#relating lists
sq_list=[x*x for x in mylist3]
print(sq_list)