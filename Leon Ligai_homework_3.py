data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')
letters = []
numbers = []

for i in data_tuple:
    if type(i) == str:
        letters.append(i)
    else:
        numbers.append(i)

numbers.remove(6.13)
numbers.pop(True)
letters.append(True)
# letters.insert(8,True)
numbers.insert(2,2)

numbers.sort()
letters.reverse()

letters.insert(1,"G")
letters.insert(5,"T")
letters.remove("T")
letters.insert(8,"c")
letters.remove("C")
letters.remove('g')


letters = tuple(letters)
numbers = tuple(numbers)


print(numbers)
print(letters)