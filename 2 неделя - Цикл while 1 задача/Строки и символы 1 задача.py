# GC-состав является важной характеристикой геномных последовательностей и определяется как процентное соотношение суммы всех гуанинов и цитозинов к общему числу нуклеиновых оснований в геномной последовательности.
# Напишите программу, которая вычисляет процентное содержание символов G (гуанин) и C (цитозин) в введенной строке (программа не должна зависеть от регистра вводимых символов).
# Например, в строке "acggtgttat" процентное содержание символов G и C равно 4/10 * 100=40.0, где 4 -- это количество символов G и C,  а 10 -- это длина строки.

a = input()
res1 = a.upper()
k = res1.count('C')
k2 = res1.count('G')
k3 = int(k) + int(k2)
k4 = res1.count('')
result = (k3 / (k4 - 1)) * 100
print(result)