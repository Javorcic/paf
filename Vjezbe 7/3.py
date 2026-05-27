import numpy as np

np.random.seed(42)
mase_ciste = np.random.normal(loc=2.06, scale=0.05, size=57).tolist()
mase = mase_ciste + [6.0, 1.2, 3.2, 4.5, 8.5, 7.8, 0.08, 0.02]

def med(podaci):
    sort = sorted(podaci)
    n = len(sort)
    if n % 2 == 1:  #neparan
        return sort[(n - 1) // 2]
    else:   #paran
        return (sort[n // 2 - 1] + sort[n // 2]) / 2

#testiranje
a = [3, 1, 4, 1, 5, 9, 2, 6]
b = [3, 1, 4, 1, 5, 9, 2, 6, 5]

print(f"Medijan liste a (paran n=8): {med(a)} numpy: {np.median(a)}")
print(f"Medijan liste b (neparan n=9): {med(b)} numpy: {np.median(b)}")

med_mase = med(mase)
print(f"Medijan skupa 'mase': {med_mase:.4f}")
print(f"Provjera numpy: {np.median(mase):.4f}")
