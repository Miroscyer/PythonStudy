guests=['xiao ming', 'li lei', 'tom cruid']
print("sorry "+guests[0] + ' can not come here')
guests[0]='alex geriod'

print('Hey, I find a larger table!')

guests.insert(0,'Miros Klose')
guests.insert(2,'Bruklin frances')
guests.append('West Jack')

print("Welcome "+guests[0])
print("Welcome "+guests[1])
print("Welcome "+guests[2])
print("Welcome "+guests[3])
print("Welcome "+guests[4])
print("Welcome "+guests[5])

print('Sorry it can be only two guys')
poped_guest=guests.pop()
print('so sorry for ' + poped_guest)
poped_guest=guests.pop()
print('so sorry for ' + poped_guest)
poped_guest=guests.pop()
print('so sorry for ' + poped_guest)
poped_guest=guests.pop()
print('so sorry for ' + poped_guest)

print('Lucky, '+ guests[0] + '. You will stay here!')
print('Lucky, '+ guests[1] + '. You will stay here!')

print('You invited ' + str(len(guests)) + ' guests')

print(guests)
del guests[0]
del guests[0]
print(guests)

