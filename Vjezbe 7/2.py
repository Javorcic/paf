import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
mase_ciste = np.random.normal(loc=2.06, scale=0.05, size=57).tolist()

sred = np.mean(mase_ciste)
med = np.median(mase_ciste)

print(f"Aritmetička sredina: {sred:.4f}")
print(f"Medijan: {med:.4f}")

plt.figure(figsize=(8, 5))
plt.hist(mase_ciste, bins=10, color='slategray', edgecolor='white', label='Frekvencija')
plt.axvline(sred, color='palevioletred', linewidth=2, label=f'Srednja = {sred:.3f}')
plt.axvline(sred, color='pink', linewidth=2, linestyle='--', label=f'Medijan = {med:.3f}')
plt.xlabel("Masa")
plt.ylabel("Frekvencija")
plt.title("Histogram s numpy")
plt.legend()
plt.tight_layout()
plt.savefig("2.png", dpi=150)
plt.show()
