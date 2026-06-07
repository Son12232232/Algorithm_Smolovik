n = int(input())
lst = list(map(int, input().split()))
m = int(input())
q = list(map(int, input().split()))

s = set(lst)

for x in q:
    if x in s:
        print("YES")
    else:
        print("NO")
