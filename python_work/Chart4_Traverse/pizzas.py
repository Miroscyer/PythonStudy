pizzas=['beef', 'cheeze', 'tomato']
for pizza in pizzas:
	print('I like ' + pizza + ' pizza')
print('I really love pizza!')
print("\n")

friend_pizzas = pizzas[:]
pizzas.append('apple')
friend_pizzas.append('berries')

print("My favorite pizzas are:")
for pizza in pizzas:
	print(pizza)

print("\n")

print("My friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
	print(friend_pizza)
