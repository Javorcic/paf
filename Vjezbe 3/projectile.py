import numpy as np
import matplotlib.pyplot as plt

class Projectile:
    def __init__(self, x0, y0, vx0, vy0, m=1.0, k=0.1, g=9.81):
        self.x0 = x0
        self.y0 = y0
        self.vx0 = vx0
        self.vy0 = vy0
        self.m = m
        self.k = k
        self.g = g

    def derivatives(self, state):
        x, y, vx, vy = state
        dxdt = vx
        dydt = vy
        dvxdt = -(self.k / self.m) * vx
        dvydt = -self.g - (self.k / self.m) * vy

        return np.array([dxdt, dydt, dvxdt, dvydt], dtype=float)

    def simulate_euler(self, dt):
        state= np.array([self.x0, self.y0, self.vx0, self.vy0], dtype=float)
    
        x_list=[state[0]]
        y_list=[state[1]]
        vx_list=[state[2]]
        vy_list=[state[3]]
        t_list=[0.0]
        t=0.0

        while state[1] >= 0:
            deriv= self.derivatives(state)
            prev_state= state.copy()
            state = state + deriv * dt
            t += dt

            x_list.append(state[0])
            y_list.append(state[1])
            vx_list.append(state[2])
            vy_list.append(state[3])
            t_list.append(t)

        if state[1] < 0:
            y1= prev_state[1]
            y2= state[1]
            alpha= y1 / (y1 - y2)

            x_hit= prev_state[0] + alpha * (state[0] - prev_state[0])
            t_hit=t_list[-2] + alpha * (t_list[-1] - t_list[-2])

            x_list[-1] = x_hit
            y_list[-1] = 0.0 
            t_list[-1] = t_hit
            

        return np.array(t_list), np.array(x_list), np.array(y_list), np.array(vx_list), np.array(vy_list)

    def simulate_rk4(self, dt):
        state= np.array([self.x0, self.y0, self.vx0, self.vy0], dtype=float)
    
        x_list=[state[0]]
        y_list=[state[1]]
        vx_list=[state[2]]
        vy_list=[state[3]]
        t_list=[0.0]
        t=0.0

        while state[1] >= 0:
            k1= self.derivatives(state)
            k2= self.derivatives(state + 0.5 * dt * k1)
            k3= self.derivatives(state + 0.5 * dt * k2)
            k4= self.derivatives(state + dt * k3)

            prev_state= state.copy()
            state = state + (dt / 6.0) * (k1 + 2*k2 + 2*k3 + k4)
            t += dt

            x_list.append(state[0])
            y_list.append(state[1])
            vx_list.append(state[2])
            vy_list.append(state[3])
            t_list.append(t)

        if state[1] < 0:
            y1 = prev_state[1]
            y2 = state[1]
            alpha = y1 / (y1 - y2)

            x_hit = prev_state[0] + alpha * (state[0] - prev_state[0])
            t_hit = t_list[-2] + alpha * (t_list[-1] - t_list[-2])

            x_list[-1] = x_hit
            y_list[-1] = 0.0
            t_list[-1] = t_hit


        return np.array(t_list), np.array(x_list), np.array(y_list), np.array(vx_list), np.array(vy_list)

    def plot_trajectory_euler(self, dt, labele=None):
        _, x, y, _, _ = self.simulate_euler(dt)
        if labele is None:
            labele = f"Euler (dt={dt})"
        plt.plot(x, y, label=labele)

    def plot_trajectory_rk4(self, dt, labele=None):
        _, x, y, _, _ = self.simulate_rk4(dt)
        if labele is None:
            labele = f"RK4 (dt={dt})"
        plt.plot(x, y, label=labele)