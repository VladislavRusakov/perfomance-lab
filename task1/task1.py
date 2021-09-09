import sys


n = int(sys.argv[1])
m = int(sys.argv[2])

x = 1
line = []

while '1' not in line:
    if x + m - 1 > n:
        x += m - n - 1
        line.append(str(x))
    else:
        x += m - 1
        line.append(str(x))


print('1', end='')
for index in line[:-1]:
    print(index, end='')


