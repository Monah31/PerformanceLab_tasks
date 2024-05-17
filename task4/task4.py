# Задание 4
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        f = open(sys.argv[1], 'r')

    else:
        f = open('numbers.txt', 'r')

    sum_nums = 0
    list_i = []
    ans = 0

    for i in f:
        sum_nums += int(i)
        list_i.append(int(i))

    middle = sum_nums // len(list_i)

    for i in list_i:
        ans += abs(middle - i)
    print(ans)
