string = input('Enter string, please')
# first_2 = string[0]+string[1]
# if first_2 == 'Is':
#     print('The string is {}'.format(string))
# else:
#     print('The string is {}'.format('Is' + ' ' + string))
if string[:2] == 'Is':
    print(string)
else:
    print('Is ' + string)
