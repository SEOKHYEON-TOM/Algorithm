# 리스트의 크기 입력 받고, 1~n까지 크기가 무작위 순인 리스트 만들기
import random

n = int(input('숫자를 입력해주세요:'))

list1 = list(range(1, n + 1))
random.shuffle(list1)
print(list1)
