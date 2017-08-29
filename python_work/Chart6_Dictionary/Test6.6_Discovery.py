favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

test_persons = ['Miros', 'sarah', 'phil']

for person in favorite_languages.keys():
    if person in test_persons:
        print(person + ", Thank you for discoverying!")
    elif person not in test_persons:
        print(person + ", Please join in discoverying~")

