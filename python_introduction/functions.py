#functions WHY??
#return something
#can be called
#save space
#repeatable code

def function_name(parameter_one, parameter_two):
    pass

a = 59
b = 65
c = a+b
print(c)

def determine_speed(miles, hours):
    print(f'Calculating speed when we travel {miles} in {hours}')
    print(miles/hours)
    return miles/hours


determine_speed(300,2)