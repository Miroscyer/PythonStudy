words = {
    'if': 'perhaps',
    'or': 'other',
    'print': '打印',
    'str': 'string',
    'len': 'length',
    }

for key, val in words.items():
    print(key + " = " + val)

words['&&']='and'
words['+']='plus'
words['-']='decrease'
words['*']='multiply'
words['/']='divide'

print('\n')
for key, val in words.items():
    print(key + " = " + val)
