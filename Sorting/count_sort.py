n = 5
array = [8, 5, 4, 7, 2]

''' Counting Sort '''

number = max(array)

count = [0]*(number+1)

for i in range(n):
    count[array[i]] += 1


for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=" ")