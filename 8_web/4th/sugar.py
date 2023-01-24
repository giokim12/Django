
# a=int(input())
a= 4999

if a <8:
    print(-1)
elif a%5==0:
    print(a//5)
elif a%5==1:
    print((a//5) +1)
elif a%5==2:
    print((a//5) +2)
elif a%5==3:
    print((a//5) +1)
else:
    print((a//5) +2)