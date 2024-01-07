def find_indices(array,min_value, max_value):
    result=[]
    for i in range(len(array)):
        if array[i] in range(min_value,max_value+1):
            result.append(i)
    return result 

min_element = int(input("Введите значение минимума "))
max_element = int(input("Введите значение максимума "))
arr =[int(x) for x in input().split(",")]
indices=find_indices(arr,min_element,max_element)
print(indices)