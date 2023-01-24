

N= int(input())
arr= list(map(int,input().split()))
print(arr)

maxV= arr[0] #첫 원소를 최대값으로 가정
for i in range(1, N): #나머지 모든 원소에 대해 
    if arr[i] > maxV:
        maxV = arr[i]
print(maxV)


N= int(input())
arr= list(map(int,input().split()))


maxIdx = 0 #가정
for i in range(1, N):
    if arr[maxIdx] <= arr[i]:
        maxIdx = i
print(maxIdx)


#거품정렬
for i in range(N-1, 0 , -1): #구간의 맨 끝 인덱스
    for j in range(i): # 인접원소 중 왼쪽 원소 인덱스
        if arr[j] > arr[j+1]: # 오름차순, 더 큰 수를 오른쪽으로
            arr[j], arr[j+1] = arr[j+1], arr[j]
print(arr)

#카운트정렬
tmp = [0] * N
c=[0]*101 #0부터 100까지 숫자 개수, 인덱스가 100까지 있어야함
for i in range(N): #카운트
    c[arr[i]] += 1
for j in range(1, 101): #개수 누적
    c[j] += c[j+1] # 오름차순, 더 큰수를 오른쪽으로

for i in range(N-1, -1, -1): 