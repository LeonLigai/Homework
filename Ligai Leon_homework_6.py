numbers = [2, 7, 11, 15]
need_summ = int(input('Введите желаемую сумму '))
for result in range(len(numbers)-1):
    if (numbers[result]+(numbers[result+1])) == need_summ:
       print([result,result+1])
