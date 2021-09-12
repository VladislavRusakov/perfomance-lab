import sys


n = int(sys.argv[1])
m = int(sys.argv[2])

number = 1
line = []

while '1' not in line:
    if number + m - 1 > n:
        number += m - n - 1
        line.append(str(number))
    else:
        number += m - 1
        line.append(str(number))


print('1', end='')
for index in line[:-1]:
    print(index, end='')


