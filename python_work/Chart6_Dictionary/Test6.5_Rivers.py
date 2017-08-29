rivers = {
    'nile': 'Egypt',
    'yangzi river': 'China',
    'huang river': 'China',
    }
    
for river, country in rivers.items():
    print("The " + river + " runs through " + country + ".")

print('\n')
for river in rivers.keys():
    print(river)
    
print('\n')
for country in set(rivers.values()):
    print(country)
