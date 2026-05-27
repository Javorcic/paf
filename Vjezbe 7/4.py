import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
mase_ciste = np.random.normal(loc=2.06, scale=0.05, size=57).tolist()
mase = mase_ciste + [6.0, 1.2, 3.2, 4.5, 8.5, 7.8, 0.08, 0.02]

def med(podaci):
    sort = sorted(podaci)
    n = len(sort)
    if n % 2 == 1:
        return sort[(n - 1) // 2]
    else:
        return (sort[n // 2 - 1] + sort[n // 2]) / 2

#sa greškama
srednja_svih = np.mean(mase)
med_svih = med(mase)

#granica za znacajna odstupanja
mase_ociscene = [x for x in mase if 1.5 < x < 3.0]

#bez
srednja_ociscena = np.mean(mase_ociscene)
med_ociscen = med(mase_ociscene)

print(f"Sa pogreškama - srednja: {srednja_svih:.4f}, medijan: {med_svih:.4f}")
print(f"Bez pogrešaka - srednja: {srednja_ociscena:.4f}, medijan: {med_ociscen:.4f}")
print(f"\nPromjena srednje vrijednosti: {abs(srednja_svih - srednja_ociscena):.4f}")
print(f"Promjena medijana: {abs(med_svih - med_ociscen):.4f}")
print("\nZaključak: Medijan se gotovo nije promijenio.")

# Graf
plt.figure(figsize=(10, 6))
plt.hist(mase, bins=15, color='slategray', edgecolor='white', alpha=0.7, label='Sva mjerenja')
plt.axvline(srednja_svih, color='palevioletred', linewidth=2, label=f'Srednja (sve) = {srednja_svih:.3f}')
plt.axvline(med_svih, color='pink', linewidth=2, linestyle='--', label=f'Medijan (sve) = {med_svih:.3f}')
plt.axvline(srednja_ociscena, color='mediumvioletred', linewidth=2, label=f'Srednja (bez outliera) = {srednja_ociscena:.3f}')
plt.axvline(med_ociscen, color='plum', linewidth=2, linestyle='--', label=f'Medijan (bez outliera) = {med_ociscen:.3f}')
plt.xlabel("Masa")
plt.ylabel("Frekvencija")
plt.title("Usporedba sa i bez pogrešnih mjerenja")
plt.legend(fontsize=9)
plt.tight_layout()
plt.savefig("4.png", dpi=150)
plt.show()
