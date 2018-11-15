def smallest(numbers):
    i = 0
    small = numbers[0]
    while i < len (numbers):
        if numbers[i] < small:
            small = numbers[i]
        i = i + 1
    return small



numbers = [6,10,3,-1,-2,-5,0,4,1,2,3,4,5,6]
pivot = 0

i = 0
nearest = smallest(numbers)
while i < len (numbers):
    if numbers[i] < pivot:

        if nearest <= numbers[i]:
            nearest = numbers[i]
            index = i
    i = i + 1
print "Nearest is ",nearest, " and index is ", index