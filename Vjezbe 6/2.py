import math


promjeri = {
    "Valjak 1": [19.98, 20.18, 20.10, 20.08, 19.74],
    "Valjak 2": [19.92, 19.82, 19.96, 19.98, 19.88],
    "Valjak 3": [24.96, 24.98, 24.98, 24.92, 24.94],
}

duljine = {
    "Valjak 1": [49.80, 49.00, 50.48, 49.80, 49.96],
    "Valjak 2": [52.56, 52.50, 52.62, 52.58, 52.54],
    "Valjak 3": [55.34, 55.40, 55.30, 55.44, 55.48],
}

valjci = ["Valjak 1", "Valjak 2", "Valjak 3"]


def sr_vr(mjer):
    n = len(mjer)
    return sum(mjer) / n

def stand_od(mjer):
    n = len(mjer)
    x_bar = sr_vr(mjer)
    return math.sqrt(sum((x - x_bar) ** 2 for x in mjer) / (n * (n - 1)))


def volumen_valjka(R, L): #R i L u cm
    return R**2 * math.pi * L

def sigma_volumena(R, sR, L, sL):
    #u slučaju pogreške za V = π R² L
    dV_dR = 2 * math.pi * R * L
    dV_dL = math.pi * R**2
    return math.sqrt((dV_dR * sR)**2 + (dV_dL * sL)**2)


for v in valjci:
    R_mj = [d / 2 for d in promjeri[v]]
    R_bar = sr_vr(R_mj)
    sigma_R = stand_od(R_mj)
    L_bar = sr_vr(duljine[v])
    sigma_L = stand_od(duljine[v])

    #mm u cm
    R_cm = R_bar   / 10
    sR_cm = sigma_R / 10
    L_cm = L_bar   / 10
    sL_cm = sigma_L / 10

    V = volumen_valjka(R_cm, L_cm)
    sig_V = sigma_volumena(R_cm, sR_cm, L_cm, sL_cm)

    print(f"\n{v}:")
    print(f"V = {V:.4e} ± {sig_V:.4e} cm³")
