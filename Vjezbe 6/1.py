import math


#funkcije iz v5
def sr_vr(mjer):
    n = len(mjer)
    return sum(mjer) / n
 
def stand_od(mjer):
    #Formula: sqrt( Σ(xi - x̄)**2 / (n·(n-1)) )
    n = len(mjer)
    x_bar = sr_vr(mjer)
    return math.sqrt(sum((x - x_bar) ** 2 for x in mjer) / (n * (n - 1)))


#iz tablica
#2R [mm]
promjeri = {
    "Valjak 1": [19.98, 20.18, 20.10, 20.08, 19.74],
    "Valjak 2": [19.92, 19.82, 19.96, 19.98, 19.88],
    "Valjak 3": [24.96, 24.98, 24.98, 24.92, 24.94],
}
 
#L [mm]
duljine = {
    "Valjak 1": [49.80, 49.00, 50.48, 49.80, 49.96],
    "Valjak 2": [52.56, 52.50, 52.62, 52.58, 52.54],
    "Valjak 3": [55.34, 55.40, 55.30, 55.44, 55.48],
}
 
#m [g]
mase = {
    "Valjak 1": [138.92, 138.98, 139.20, 138.90, 138.92],
    "Valjak 2": [128.65, 128.60, 128.65, 128.35, 128.50],
    "Valjak 3": [71.89, 71.90, 71.79, 71.85, 71.70],
}
 
valjci = ["Valjak 1", "Valjak 2", "Valjak 3"]

 
R_bar = {}
sigma_R = {}
L_bar = {}
sigma_L = {}
m_bar = {}
sigma_m = {}
 
for v in valjci:
    R_mj = [d / 2 for d in promjeri[v]]
    R_bar[v] = sr_vr(R_mj)
    sigma_R[v] = stand_od(R_mj)
 
    L_bar[v] = sr_vr(duljine[v])
    sigma_L[v] = stand_od(duljine[v])
 
    m_bar[v] = sr_vr(mase[v])
    sigma_m[v] = stand_od(mase[v])
 
    print(f"\n{v}:")
    print(f"R̄ = {R_bar[v]:.4f} ± {sigma_R[v]:.4f}mm")
    print(f"L̄ = {L_bar[v]:.4f} ± {sigma_L[v]:.4f} mm")
    print(f"m̄ = {m_bar[v]:.4f} ± {sigma_m[v]:.4f} g")