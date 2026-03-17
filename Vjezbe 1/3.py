while True:
    try:
        x1 = float(input("Unesi x1: "))
        y1 = float(input("Unesi y1: "))
        x2 = float(input("Unesi x2: "))
        y2 = float(input("Unesi y2: "))
        break
    except:
        print("Pogrešan unos! Pokušaj ponovno.")

k = (y2 - y1) / (x2 - x1)
l = y1 - k * x1

print(f"Jednadžba pravca: y = {k}x + {l}")