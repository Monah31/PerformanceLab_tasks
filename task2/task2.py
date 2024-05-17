# Задание 2
import math
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        f = open(sys.argv[1], 'r')
        koordinats = open(sys.argv[2], 'r')
    else:
        f = open('circle.txt', 'r')
        koordinats = open('dot.txt', 'r')

    x, y = map(int, f.readline().split())
    r = int(f.readline())

    for line in koordinats:
        x1, y1 = map(int, line.split())
        ans = math.sqrt(((x1 - x) ** 2) + ((y1 - y) ** 2))
        if ans == r:
            print(0)
        elif ans < r:
            print(1)
        else:
            print(2)
