import numpy as np
import matplotlib.pyplot as plt

# --- konstante
q_e = -1
q_p = 1
m = 1

# polja
E = np.array([0.0, 0.0, 0.0])
B = np.array([0.0, 0.0, 1.0])

# početni uvjeti
r0 = np.array([0.0, 0.0, 0.0])
v0 = np.array([1.0, 1.0, 1.0])

dt = 0.05
steps = 4000

def borisov_korak(q):
    r = np.zeros((steps, 3))
    v = np.zeros((steps, 3))

    r[0] = r0
    v[0] = v0

    for i in range(steps - 1):
        # prva polovica ubrzanja zbog E
        v_minus = v[i] + (q * E / m) * (dt / 2)

        # rotacija zbog B
        t = (q * B / m) * (dt / 2)
        t_kvadrat = np.dot(t, t)
        s = 2 * t / (1 + t_kvadrat)

        v_prim = v_minus + np.cross(v_minus, t)
        v_plus = v_minus + np.cross(v_prim, s)

        # druga polovica ubrzanja zbog E
        v[i+1] = v_plus + (q * E / m) * (dt / 2)

        # novi položaj
        r[i+1] = r[i] + v[i+1] * dt

    return r

# simulacije
putanja_e = borisov_korak(q_e)
putanja_p = borisov_korak(q_p)

# --- crtanje
fig = plt.figure(figsize=(10, 5))

ax = fig.add_subplot(121, projection='3d')
ax.plot(putanja_e[:,0],
        putanja_e[:,1],
        putanja_e[:,2])
ax.set_box_aspect([1,1,1])
ax.set_title("Elektron")

ax = fig.add_subplot(122, projection='3d')
ax.plot(putanja_p[:,0],
        putanja_p[:,1],
        putanja_p[:,2])
ax.set_box_aspect([1,1,1])
ax.set_title("Pozitron")

plt.show()