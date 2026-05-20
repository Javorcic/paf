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

mase = {
    "Valjak 1": [138.92, 138.98, 139.20, 138.90, 138.92],
    "Valjak 2": [128.65, 128.60, 128.65, 128.35, 128.50],
    "Valjak 3": [71.89, 71.90, 71.79, 71.85, 71.70],
}

valjci = ["Valjak 1", "Valjak 2", "Valjak 3"]


def sr_vr(mjer):
    n = len(mjer)
    return sum(mjer) / n

def stand_od(mjer):
    n = len(mjer)
    x_bar = sr_vr(mjer)
    return math.sqrt(sum((x - x_bar) ** 2 for x in mjer) / (n * (n - 1)))


def volumen_valjka(R, L):
    return R**2 * math.pi * L

def sigma_volumena(R, sR, L, sL):
    dV_dR = 2 * math.pi * R * L
    dV_dL = math.pi * R**2
    return math.sqrt((dV_dR * sR)**2 + (dV_dL * sL)**2)


def gustoca(m, V): #m u g, v u cm3
    return m / V

def sigma_gustoce(m, sm, V, sV):
    #u slučaju pogreške za ρ = m/V
    drho_dm = 1 / V
    drho_dV = -m / V**2
    return math.sqrt((drho_dm * sm)**2 + (drho_dV * sV)**2)


def najblizi_materijal(rho):
    literaturne_gustoce = {
        "Aluminij":   2.700,
        "Čelik":      7.874,
        "Bakar":      8.960,
        "Mesing":     8.400,
        "Mjed":       8.500,
        "Titan":      4.506,
        "Nylon":      1.150,
        "PVC":        1.380,
        "Drvo (bor)": 0.530,
    }
    najmanji_delta = float("inf")
    materijal = "Nepoznat"
    rho_lit = None
    for mat, r in literaturne_gustoce.items():
        delta = abs(rho - r) / r
        if delta < najmanji_delta:
            najmanji_delta = delta
            materijal = mat
            rho_lit = r
    return materijal, rho_lit, najmanji_delta * 100


for v in valjci:
    R_mj = [d / 2 for d in promjeri[v]]
    R_bar = sr_vr(R_mj)
    sigma_R = stand_od(R_mj)
    L_bar = sr_vr(duljine[v])
    sigma_L = stand_od(duljine[v])
    m_bar = sr_vr(mase[v])
    sigma_m = stand_od(mase[v])

    R_cm = R_bar / 10
    sR_cm = sigma_R / 10
    L_cm = L_bar / 10
    sL_cm = sigma_L / 10

    V = volumen_valjka(R_cm, L_cm)
    sig_V = sigma_volumena(R_cm, sR_cm, L_cm, sL_cm)
    rho = gustoca(m_bar, V)

    mat, rho_lit, delta = najblizi_materijal(rho)

    print(f"\n{v}:")
    print(f"Izmjerena gustoća : {rho:.4f} g/cm³")
    print(f"Najbliži materijal: {mat} (ρ_lit = {rho_lit:.3f} g/cm³)")
    print(f"Relativna pogreška: δρ = {delta:.2f} %")