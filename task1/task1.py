import sys


n = int(sys.argv[1])
m = int(sys.argv[2])

x = 1
line = ''

while '1' not in line:
    if x + m - 1 > n:
        x += m - n - 1
        line += str(x)
    else:
        x += m - 1
        line += str(x)
print('1' + line[:-1])


