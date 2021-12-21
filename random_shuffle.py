# 셔플 알고리즘
# random.shuffle없이 list 섞기 (출처: https://crystalcube.co.kr/87)
import random

n = int(input('숫자를 입력해주세요:'))

num_list = list(range(n))

while n > 0:
    l = random.randint(0, n - 1)
    num_list[l], num_list[n - 1] = num_list[n - 1], num_list[l]
    n -= 1

print(num_list)
