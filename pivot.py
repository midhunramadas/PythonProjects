def find_smallest(numbers):
    i = 0
    smallest = numbers[i]
    while i < len(numbers):
        if numbers[i] < smallest:
            smallest = numbers[i]
        i = i + 1
    return smallest


def find_nearest(numbers, pivot):
    if pivot <= find_smallest(numbers):
        print
        'No number found smaller than ', pivot
        return None
    i = 0
    nearest = find_smallest(numbers)
    while i < len(numbers):
        if numbers[i] < pivot and numbers[i] >= nearest:
            print
            numbers[i]
            nearest = numbers[i]
            index = i
        i = i + 1
    return nearest, index


numbers = [6, 10, 3, -1, -2, -5, 0, 4, 1, 2, 3, 4, 5, 6]
pivot = -5

print ('Numbers list is ', numbers, ' and pivot is ', pivot)


print (find_nearest(numbers, pivot))