def solve()->None:
    n = int(input())
    x = list(map(int, input().split()))
    x.sort()
    cost = 0
    for i in range(n//2):
        cost += x[n-i-1]-x[i]
    print(cost) 

if __name__=='__main__':
    t = int(input())
    for _ in range(t):
        solve()


