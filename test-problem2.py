# 중복되지 않는 1~N까지의 숫자중 연속되는 K개를 고르면 최소값으로 변한다고 할 때, 모든 수가 같아지는 최소 횟수를 구하는 문제

N, K = map(int, input().split(" "))
num = list(map(int, input().split(" ")))
        
for i, n in enumerate(num):
    if n == 1:
        one = i

n_iter = 1

if one < K:
    box = K-1
    while True:
        if box >= N-K:
            n_iter += 1
            break
        else:
            box += K-1
            n_iter += 1
elif one >= N-K:
    box = N-K
    while True:
        if box < K:
            n_iter += 1
            break
        else:
            box -= K-1
            n_iter += 1        

else:
    n_iter1 = 2
    box_back = one
    box_for = one + K - 1
    while True:
        if box_back < K:
            break
        else:
            box_back -= K-1
            n_iter1 += 1
    while True:
        if box_for >= N-K:
            n_iter1 += 1
            break
        else:
            box_for += K-1
            n_iter1 += 1
    
    n_iter2 = 1
    box_back = one + K//2
    box_for = one + K//2
    while True:
        if box_back < K:
            break
        else:
            box_back -= K-1
            n_iter2 += 1
    while True:
        if box_for >= N-K:
            n_iter2 += 1
            break
        else:
            box_for += K-1
            n_iter2 += 1
            
    n_iter = min(n_iter1, n_iter2)
            
print(n_iter)