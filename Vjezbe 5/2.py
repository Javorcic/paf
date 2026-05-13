def inacice(N):
    x=5
    for _ in range(N):
        x+=1/3
    for _ in range(N):
        x-=1/3
    return x

for N in [200, 2000, 20000]:
    print(f"N={N}: {inacice(N)}")