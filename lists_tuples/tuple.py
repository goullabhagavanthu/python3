mytuple = tuple(('Denver', 21, True))

anothertuple = (1, 4, 2  ,8)

print(mytuple)
print(type(mytuple))
print(anothertuple)

newlist = list(mytuple)
newlist.append('Akira')
newtuple = tuple(newlist)
print(newtuple)
