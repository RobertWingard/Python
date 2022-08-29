print('hello peeps')

#variables
x = 7

name_of_variable = 'in snake case'
# class names will be capitalized
GLOBAL_VAR = 'this is a global variable'

#data types

#primitive
#num
num = 7
num = 9.3

#string
string = 'this is my string'
string2 = "this is my string"


#boolean
# true or false value
bool = True
bool2 = False


#composite / complex

#lists (known as arrays in JS)
list = [1,2,3,4,5,6]
list2 = ['bob', 'kyle', 'suzy']

# zero - indexed
name = list2[1]
#elements accessed by index



# list[3] = 7
#print(list)
# first_three = [list[0:3]]
# last_letter = [list[-2:]]
#print(first_three)
#print(last_letter)
#list functions:
#len()
#print(len(list))
#max() min()
# print(max(list))
# .sort() .pop()
# list.sort() sorts my lowest to highest
# list2.pop()
# print(list2)


#dictionaries (known as objects in JS)
dog = {
    'name': 'spot',
    'age': 3,
    'color': 'spotted',  
    'favorite_food': 'cheese'
}

# print(dog['name'])

# dog['name'] = 'Tiger'
# print(dog)
# # dog['favorite_food'] breaks code, key error
# print(dog.get('favorite_food', 'not found'))

# del 

# if 'favorite_food' in dog:
#     print('he has a fav')
# else:
#     print('he does not')

# del dog['favorite_food']
# fav_food = dog.pop('favorite_food')
# print(fav_food)
# dog.clear()
# print(dog)

#tuples immutable list
tuple = (1,2,3,4,5,6)
#tuple[3] = 8 (cant do this)


#if
#else
#elif
# < > <= >= == !=(not ==) or and

if 'age' not in dog:
    print("Dog doesn't have an age")
elif dog['age'] > 4:
    print('Dog is older than 4')
else:
    print('dog is less than 4')


