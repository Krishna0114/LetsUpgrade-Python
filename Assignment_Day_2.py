
#-----------------LIST-----------------
a=[1,2,3,4]
print(a)
a.append(5)
print(a)

b=[1,2,3,4]
print(b)
b.extend([5,6,7])
print(b)

c=[1,3,4]
print(c)
c.insert(1,2)
print(c)


#-----------------DICTIONARY-----------------
a={1:1,2:4,3:9,4:16}
print(a)
a.clear()
print(a)

b={1:1,2:4,3:9,4:16}
print(b)
print(b.items())

c={1:1,2:4,3:9,4:16}
print(c)
c.popitem()
print(c)

d={1:1,2:4,3:9,4:16}
print(d)
print(d.keys())

e={1:1,2:4,3:9,4:16}
print(e)
print(e.values())


#-----------------Set-----------------
a={1,3,5,7,9}
print(a)
a.add(4)
print(a)

b={1,3,5,7,9}
print(b)
b.clear()
print(b)

c={1,3,5,7,9}
print(c)
print(c.pop())
print(c)



#-----------------TUPLE-----------------
a=(1,2,3,"Krishna",[2,5,8],(4,6,9))
print(a)
print(a[1])
print([3])

b=(1,2,3,4,5,6,7,8,9)
print(b)
print(b[1:])
print(b[:7])
print(b[:])
print(b[1:5])
print(b[-5:-2])

tpl=('a','b','c','d')
print(tpl.count('c'))
print(tpl.index('d'))



