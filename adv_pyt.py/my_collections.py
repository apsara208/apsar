from collections import Counter
a="aaaaaabbbbbbccccc"
my_counter= Counter(a)
print(my_counter)
print(my_counter.most_common(2)[0][0])#a
print(list(my_counter.elements())) #have to define the datatype of output


from collections import namedtuple
point=namedtuple("point","x,y")
pt=point(1,-4)
print(pt)#point(x=1, y=-4)
print(pt.x,pt.y)#1 -4


from collections import OrderedDict #remember the order in which items were inserted
ordered_dict= OrderedDict()
ordered_dict["b"]=3
ordered_dict["d"]=2
ordered_dict["a"]=1
ordered_dict["c"]=5
print(ordered_dict)#OrderedDict({'b': 3, 'd': 2, 'a': 1, 'c': 5})


from collections import defaultdict
d=defaultdict(int) #int- default type
d['a']=1
d["b"]=2
print(d["c"])#0
# float default =0.0


from collections import deque
# deque- double ended queue
q=deque()
q.append(1)
q.append(2)
q.appendleft(3)
print(q)
q.pop()
print(q)
q.popleft()
print(q)
q.extend([4,5,6])# aslo extendleft
print(q)
q.rotate(1)#rotates right , if negative no. given it rotates the deque to n places left
print(q)
q.clear()
print(q)
