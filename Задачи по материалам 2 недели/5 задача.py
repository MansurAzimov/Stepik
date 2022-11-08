# Выведите таблицу размером n x n, заполненную числами от 1 до n по спирали, 
# выходящей из левого верхнего угла и закрученной по часовой стрелке, как показано в примере (здесь n=5):

n = int(input())

x = 0
y = 0
dx = 1
dy = 0

# Инициализация квадратной матрицы nxn с элементами типа None
matrix = [[None] * n for _ in range(n)]

for i in range(1, n**2+1):
    matrix[x][y] = i
    nx = x + dx
    ny = y + dy
    # Проверяем, не вышла ли позиция за границы и не занята ли уже ячейка
    if (0 <= nx < n) and (0 <= ny < n) and (not matrix[nx][ny]):
        x = nx
        y = ny
    else:
        #dx, dy = -dy, dx
        # Если позиция за границей и ячейка не пуста, разворачиваем матрицу на 90 градусов
        swap = -dy
        dy = dx
        dx = swap
        x = x + dx
        y = y + dy

# Выводим заполненную матрицу        
for y in range(n):
    for x in range(n):
        print(matrix[x][y], end = ' ')
    print()