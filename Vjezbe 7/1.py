import numpy as np
import matplotlib.pyplot as plt

# Generiranje podataka
np.random.seed(42)
mase_ciste = np.random.normal(loc=2.06, scale=0.05, size=57).tolist()

def hist(podaci, k):
    xmin = min(podaci)
    xmax = max(podaci)
    h = (xmax-xmin) / k

    rub = [xmin + i * h for i in range(k + 1)]
    f = [0] * k

    for x in podaci:
        for i in range(k):
            l = rub[i]
            d = rub[i + 1]
            #zdnji razred ukljucuje i maksimalnu vrijednost
            if i == k - 1:
                if l <= x <= d:
                    f[i] += 1
            else:
                if l <= x < d:
                    f[i] += 1

    print("Tekstualni histogram")
    for i in range(k):
        print(f"[{rub[i]:.2f}, {rub[i+1]:.2f}): {f[i]}")

    return rub, f

rub, f = hist(mase_ciste, k=10)

sirine = [rub[i+1] - rub[i] for i in range(len(rub)-1)]
plt.figure(figsize=(8, 5))
plt.bar(rub[:-1], f, width=sirine, align='edge', color='slategray', edgecolor='white')
plt.xlabel("Masa")
plt.ylabel("Frekvencija")
plt.title("Ručni histogram")
plt.tight_layout()
plt.savefig("1.png", dpi=150)
plt.show()
