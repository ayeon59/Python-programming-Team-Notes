n = 5
array = [8, 5, 4, 7, 2]

''' Insertion Sort '''

for i in range(1,n):
    for j in range(i,0,-1):
        if array[j] < array[j-1] :
            array[j],array[j-1] = array[j-1],array[j]
        else :
            break

for x in array:
    print(x, end=" ")