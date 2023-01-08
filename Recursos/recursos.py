#Multiply elements un list

list = [1,2,4,8,3]

mul_list = [2* item for item in list]
print('Multiply list is: ', mul_list)

#Remove negatuve elements from list

list1 = [-1, 2, -4, 8, 3, 6]

new_list = [item for item in list if item>0]
print('Positive item list is: ', new_list)

#Convert two lists into key value pair

_key = ['id', 'border', 'color']
_value = ['para', '2px', 'red']

pair = dict(zip(_key, _value))

print('Presenting key', pair)

