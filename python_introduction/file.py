num1 = 42 #stating an int
num2 = 2.3  #stating a float
boolean = True  #stating a boolean
string = 'Hello World' #stating a string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #stating a list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}  #stating a dictionary
fruit = ('blueberry', 'strawberry', 'banana')  #stating a tuple
print(type(fruit)) #output class tuple
print(pizza_toppings[1])  #output Sausage
pizza_toppings.append('Mushrooms')  # add mushrooms to the end
print(person['name']) #output person name = John
person['name'] = 'George' # changing name to George
person['eye_color'] = 'blue' #adds eye_color to the dictionary
print(fruit[2]) #output banana

if num1 > 45: #if statment
    print("It's greater") # passes by since the number is 42
else: #else statement
    print("It's lower") #output It's lower

if len(string) < 5: #if statement 
    print("It's a short word!") # passes by since the string is greater then 5 characters long
elif len(string) > 15: #elif statement
    print("It's a long word!") # passes by since the string is less then 15 characters  long
else: #else statement
    print("Just right!") #output Just right! since it doesnt fall between the other parameters

for x in range(5): #
    print(x) #output prints out 0-4 NOT including 5
for x in range(2,5):
    print(x) #output 2,3,4 NOT including 5
for x in range(2,10,3):
    print(x) #output 2,5,8 up to 10 and skipping by 3 each time
x = 0 #stating a variable
while(x < 5):
    print(x) #output 1,2,3,4 STOPS at 5 and does NOT include
    x += 1 #increments by 1 each time

pizza_toppings.pop() #removes the whole list
pizza_toppings.pop(1) #removes the index of 1 item (sausage)

print(person) #output prints the whole dictionary
person.pop('eye_color') #removes eye_color from person dictionary
print(person) #output prints the whole updated dictionary (without eye_color this time)

for topping in pizza_toppings: #for loop
    if topping == 'Pepperoni': #
        continue #continue
    print('After 1st if statement') #output will print this
    if topping == 'Olives':
        break #stops here

def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)