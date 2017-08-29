names=['Huang Dan', 'Dai Xu', 'Zhang Yang']
print(names[0] + ", hello")
print(names[1] + ", hello")
print(names[2] + ", hello")
names.append('Omina')
names.insert(0, 'zeng')
print(names)
del names[4]
print(names)
poped_name=names.pop()
print(names)
print(poped_name)
first_friend=names.pop(1)
print("My first friend is " + first_friend.title())

names.remove('zeng')
print(names)
