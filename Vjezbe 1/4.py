def pravac(x1, y1, x2, y2):
    k = (y2 - y1) / (x2 - x1)
    l = y1 - k * x1
    print(f"Jednadžba pravca: y = {k}x + {l}")

x1 = float(input("x1: "))
y1 = float(input("y1: "))
x2 = float(input("x2: "))
y2 = float(input("y2: "))

pravac(x1, y1, x2, y2)