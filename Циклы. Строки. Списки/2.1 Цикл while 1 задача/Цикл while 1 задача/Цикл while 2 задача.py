# В Институте биоинформатики между информатиками и биологами устраивается соревнование. Победителям соревнования достанется большой и вкусный пирог. В команде биологов aa человек, а в команде информатиков — bb человек.

# Нужно заранее разрезать пирог таким образом, чтобы можно было раздать кусочки пирога любой команде, выигравшей соревнование, при этом каждому участнику этой команды должно достаться одинаковое число кусочков пирога. И так как не хочется резать пирог на слишком мелкие кусочки, нужно найти минимальное подходящее число.

# Напишите программу, которая помогает найти это число.
# Программа должна считывать размеры команд (два положительных целых числа aa и bb, каждое число вводится на отдельной строке) и выводить наименьшее число dd, которое делится на оба этих числа без остатка.

a = int (input())
b = int (input())
s = 1
k = 2
while s<k:
  if s % a == 0 and s % b == 0:
    k=s
  else:
    s=s+1
    k=k+1
print(s)
