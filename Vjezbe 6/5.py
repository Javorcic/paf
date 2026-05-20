import math
import numpy as np


#podaci
malo_n = [99.8, 100.1, 99.9, 100.2, 100.0]

np.random.seed(42)
veliko_n = np.random.normal(loc=100.0, scale=0.2, size=10000).tolist()


#funkcija
def sve_devijacije(podaci, naziv):
    n = len(podaci)
    x_bar = sum(podaci) / n

    sigma_n = math.sqrt(sum((x - x_bar)**2 for x in podaci) / n)
    s = math.sqrt(sum((x - x_bar)**2 for x in podaci) / (n - 1))
    sigma_xbar = s / math.sqrt(n)

    rel_razlika = abs(sigma_n - s) / s * 100

    print(f"\nSkup: {naziv}  (n = {n})")
    print(f"σ_n = {sigma_n:.6f}   (populacijska std. devijacija)")
    print(f"s = {s:.6f}   (uzoračka std. devijacija)")
    print(f"σ_x̄ = {sigma_xbar:.6f}   (std. pogreška srednje vrijednosti)")
    print(f"Relativna razlika (σ_n vs s) = {rel_razlika:.4f} %")

    return sigma_n, s, sigma_xbar


print("Izračun za oba skupa:")
sigma_n_malo, s_malo, _ = sve_devijacije(malo_n, "malo_n (T vrenja, 5 mjerenja)")
sigma_n_vel, s_vel, _ = sve_devijacije(veliko_n, "veliko_n (simulacija, 10 000 mjer)")

print("\n(a) Komentar:")
print("> s ostaje otprilike ista neovisno o n (procjenjuje σ populacije)")
print("> σ_x̄ se smanjuje s povećanjem n (mjeri preciznost srednje vrijednosti)")


print("\n(b) Relativne razlike (σ_n vs s):")
print(f"> Malo n : {abs(sigma_n_malo - s_malo)/s_malo*100:.4f} %"
      f"(veća razlika jer n={len(malo_n)} je malo)")
print(f"> Veliko n : {abs(sigma_n_vel - s_vel)/s_vel*100:.6f} %"
      f"(zanemariva razlika za n=10 000)")


print("\n(c) np.std() po defaultu dijeli s n, kada je to ispravno koristiti?")
print("> Ispravno samo kada imamo CIJELU populaciju (ne uzorak).")
print("> Za uzorke koristiti s (dijeljenje s n-1) — nepristrana procjena standardne devijacije.")