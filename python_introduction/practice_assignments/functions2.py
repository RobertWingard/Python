def count_down(n):
    result = []
    for i in range(n, -1, -1):
        result.append(i)    
    return result

my_list = count_down(5)
print(my_list)





def print_and_return(l):
    print(l[0])
    return l[1]
print(print_and_return([1,2]))




def new_list(l):
    return l[0] + len(l)

print(new_list([1,2,3,4,5]))

# Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)



def values_greater_than_second(arr):
    new_arr = []
    if len(arr) < 2:
        return False

    for i in range(0,len(arr)):
        if arr[i]>arr[1]:
            new_arr.append(arr[i])
    print(len(new_arr))
    return new_arr
    

print(values_greater_than_second([5,2,3,2,1,4]))
# Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
# Example: values_greater_than_second([3]) should return False


def length_and_value(size,value):
    arr = []
    for i in range(0, size):
        arr.append(value)
    return arr



print(length_and_value(4,7))
print(length_and_value(6,2))



