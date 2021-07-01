def mysum(numbers, start=0):
    sum = start
    for number in numbers:
        sum += number

    return sum

print(mysum([1, 2, 3], 4))