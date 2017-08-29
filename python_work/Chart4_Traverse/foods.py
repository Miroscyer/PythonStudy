my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
my_foods.append('chicken')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

print("\nThe first three items in the list are: ")
print(my_foods[:3])

print("\nThree items from the middle of the list are: ")
print(my_foods[1:4])

print("\nThe last three items in the list are: ")
print(my_foods[2:])
print("\n")

for my_food in my_foods:
	print(my_food)

print("\n")

for friend_food in friend_foods:
	print(friend_food)
