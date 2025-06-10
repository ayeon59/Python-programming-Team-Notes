n = 5
array = [8, 5, 4, 7, 2]

''' Quick Sort '''

def quick_sort(array):
    if len(array)<=1:
        return array
    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x<= pivot]
    right_side = [x for x in tail if x> pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

array=quick_sort(array)

for x in array:
    print(x , end= " ")