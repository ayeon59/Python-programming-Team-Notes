n = 5
array = [8, 5, 4, 7, 2]

''' Selection Sort '''


for i in range(n):
    min_index = i
    for j in range(i+1,n):
        if array[j] < array[min_index]:
            min_index = j
        
        array[i],array[min_index]=array[min_index],array[i]



for x in array:
    print(x, end=" ")