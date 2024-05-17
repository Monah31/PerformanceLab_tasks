# Задание 1
import sys

if __name__ == "__main__":
    if len (sys.argv) > 1:
        n, m = int(sys.argv[1]), int(sys.argv[2])
    else:
        n, m = map(int, input().split())

    nums = [i for i in range(1, n + 1)]
    if n == 1:
        print(1)
    else:
        i = 0
        j = -1
        interval = []
        ans = '1'
        while j != 0:
            if len(interval) != m:
                interval.append(nums[i])
                i += 1
                if i == n:
                    i = 0
            else:
                interval = []
                interval.append(nums[i - 1])
                j = i - 1
                ans = ans + str(nums[j])

        print(ans[:-1])