# N개의 자연수 중 3가지를 골라서 순서대로 정렬할 수 있는지 묻는 문제

import numpy as np
N = int(input())
problems = list(map(int, input().split(" ")))

if N < 3:
    print("NO")
else:
    if len(np.unique(sorted(problems))) >= 3:
        print("YES")
    else:
        print("NO")