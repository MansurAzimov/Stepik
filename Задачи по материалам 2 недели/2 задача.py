# Напишите программу, которая выводит часть последовательности 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ... (число повторяется столько раз, чему равно). 
# На вход программе передаётся неотрицательное целое число n — столько элементов последовательности должна отобразить программа. 
# На выходе ожидается последовательность чисел, записанных через пробел в одну строку.
# Например, если n = 7, то программа должна вывести 1 2 2 3 3 3 4.

n = int(input())
lst = []
i = 1
while True:
    lst += [i] * i
    if len(lst) >= n:
        print(*lst[0:n])
        break
    i += 1
