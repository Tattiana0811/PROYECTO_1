import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Clase Padre: Circuito LC
class CircuitoLC:
    def __init__(self, L, C, V_in, dt=0.01, t_max=10):
        self.L = L  # Inductancia
        self.C = C  # Capacitancia
        self.V_in = V_in  # Voltaje de entrada
        self.dt = dt  # Paso de tiempo
        self.t = np.arange(0, t_max, dt)  # Vector de tiempo

    @property
    def omega_0(self):
        """Frecuencia natural del circuito LC."""
        return 1 / np.sqrt(self.L * self.C)

    def calcular_oscilaciones(self):
        """Simulación de las oscilaciones de un circuito LC ideal."""
        I = np.zeros_like(self.t)  # Corriente inicial
        dI_dt = np.zeros_like(self.t)  # Derivada de la corriente
        # Método de Euler para resolver la EDO
        for i in range(1, len(self.t)):
            V = self.V_in
            d2I_dt2 = (V - I[i-1] / self.C) / self.L  # Ecuación diferencial de segundo orden
            dI_dt[i] = dI_dt[i-1] + d2I_dt2 * self.dt
            I[i] = I[i-1] + dI_dt[i] * self.dt
        return I

# Clase Hija: Circuito RLC
class CircuitoRLC(CircuitoLC):
    def __init__(self, L, C, R, V_in, dt=0.01, t_max=10):
        super().__init__(L, C, V_in, dt, t_max)
        self.R = R  # Resistencia

    def calcular_oscilaciones(self):
        """Simulación de las oscilaciones en un circuito RLC (amortiguadas)."""
        I = np.zeros_like(self.t)  # Corriente inicial
        dI_dt = np.zeros_like(self.t)  # Derivada de la corriente
        # Método de Euler para resolver la EDO
        for i in range(1, len(self.t)):
            V = self.V_in
            # Ecuación diferencial con resistencia (amortiguamiento)
            d2I_dt2 = (V - self.R * dI_dt[i-1] - I[i-1] / self.C) / self.L
            dI_dt[i] = dI_dt[i-1] + d2I_dt2 * self.dt
            I[i] = I[i-1] + dI_dt[i] * self.dt
        return I

    def graficar_oscilaciones(self, I):
        """Genera una gráfica de las oscilaciones en función del tiempo."""
        plt.plot(self.t, I, label=f'R={self.R}')
        plt.title('Oscilaciones en un Circuito RLC Amortiguado')
        plt.xlabel('Tiempo [s]')
        plt.ylabel('Corriente [A]')
        plt.legend()
        plt.grid(True)
        plt.show()

    def animar_oscilaciones(self, I):
        """Genera una animación de las oscilaciones en función del tiempo."""
        fig, ax = plt.subplots()
        ax.set_xlim(0, self.t[-1])
        ax.set_ylim(min(I), max(I))
        line, = ax.plot([], [], lw=2)

        def init():
            line.set_data([], [])
            return line,

        def update(frame):
            line.set_data(self.t[:frame], I[:frame])
            return line,

        anim = FuncAnimation(fig, update, frames=len(self.t), init_func=init, blit=True, interval=50)
        plt.title('Animación de las Oscilaciones Amortiguadas en un Circuito RLC')
        plt.xlabel('Tiempo [s]')
        plt.ylabel('Corriente [A]')
        plt.show()

# Parámetros para un circuito subamortiguado
L = 0.5 # Henrys
C = 0.02# Faradios
R = 1 # Ohmios
V_in = 1 # Voltios

# Parámetros para un circuito criticamente amortiguado

#L = 0.5 # Henrys
#C = 0.02# Faradios
#R = 10 # Ohmios
#V_in = 1 # Voltios

# Parámetros para un circuito sobreamortiguado

#L = 0.5 # Henrys
#C = 0.02# Faradios
#R = 20 # Ohmios
#V_in = 1 # Voltios

# Crear objeto del CircuitoRLC
circuito_rlc = CircuitoRLC(L, C, R, V_in)

# Calcular y graficar las oscilaciones
T = circuito_rlc.calcular_oscilaciones()
circuito_rlc.graficar_oscilaciones(T)
circuito_rlc.animar_oscilaciones(T)


