#loops!!!!!!
"""
for ___ in __ :
    pass

first blank: iterative variable <-- represent each thing that we iterate over
ex: [1,2,3,,4,7] iterative variable will represent each number in turn

second black: sequence to iterate over


"""
for i in range(50,-1,-1):
    if i ==10:
        continue
    if i ==8:
        break
    print(i)
# range (start,stop,step)    
# the start is inclusive and defaulted to 0
#stop is exclusive
#step is the increment

fruits = ['mango', 'banana', 'pears', 'lychee', 'dragon fruit', 'tomato']


# for each_fruit in fruits:
#     print(each_fruit)  #without indices


# for i in range(len(fruits)):
#     print(f"{i}): {fruits[i]}" )  #with indecies

# for i in range(len(fruits)-1,-1,-1):
#     print(f"{i}): {fruits[i]}" )

#for in dicts

dog = {
    'name': 'spot',
    'age': 3,
    'color': 'spotted',  
    'favorite_food': 'cheese'
}

for key in dog:
    print(f"{key}: {dog[key]}")

#when loop over a dict, the iterative var will be the keys

#list of dictionares
dog_list = [
    {
    'name': 'spot',
    'age': 3,
    'color': 'spotted',  
    'favorite_food': 'cheese'
    },
    {
    'name': 'fido',
    'age': 55,
    'color': 'grey/white',
    'favorite_food': 'applesauce and crickets'
    }
]

# for dog in dog_list:
#     print(dog)
#WHILE
#ctrl + c will stop terminal
# i = 0 
# while(i<10):
#     i+=1
#     print(i)