numbers = list(range(1, 1000001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

odd_numbers = list(range(1,20,2))
for odd_number in odd_numbers:
	print(odd_number)
	
divid_numbers = list(range(3,30,3))
for divid_number in divid_numbers:
	print(divid_number)
	
cube_numbers = []
for cube_number in range(1,11):
	cube_numbers.append(cube_number**3)
	print(cube_number**3)

cube_numbers2 = [cube_number**3 for cube_number in range(1,11)]
print(cube_numbers2)
