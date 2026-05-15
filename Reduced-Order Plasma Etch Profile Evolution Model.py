import numpy as np
import matplotlib.pyplot as plt

# =====================================================
# INITIAL PARAMETERS
# =====================================================

# Process knobs
pressure = 20          # mTorr
source_power = 800     # W
bias_power = 100       # W
gas_ratio = 0.6

# Initial conditions
DOE_v = 0              # Vertical etch depth (nm)
DOE_l = 0              # Lateral etch depth (nm)

Ei0 = 120              # Initial ion energy (eV)

theta_max = 75         # Maximum angular spread (deg)

passivation = 0.25

# Geometry
W0 = 50                # Initial trench width (nm)

# Time
dt = 1
total_time = 60

# =====================================================
# CONSTANTS
# =====================================================

kB = 1.38e-23          # Boltzmann constant
mi = 6.63e-26          # Ion mass

# Electron temperature
Te0 = 5
Pc = 25

# Plasma density
ni_max = 5e17
Ps_c = 400

# Energy attenuation
k_energy = 0.02

# Flux attenuation
k_flux = 0.05

# Angular spread
k_theta = 1.5

# Bias-energy coupling
q = 0.08

# =====================================================
# STORAGE ARRAYS
# =====================================================

time_list = []

Te_list = []
ni_list = []
cs_list = []

Ei_list = []
theta_list = []

vertical_list = []
lateral_list = []

anisotropy_list = []

# =====================================================
# TIME LOOP
# =====================================================

for t in range(total_time):

    # -------------------------------------------------
    # 1. ELECTRON TEMPERATURE
    # Te = Te0 exp(-p/Pc)
    # -------------------------------------------------

    Te = Te0 * np.exp(-pressure / Pc)

    # -------------------------------------------------
    # 2. PLASMA DENSITY
    # ni = nimax(1-exp(-Ps/Psc))
    # -------------------------------------------------

    ni = ni_max * (
        1 - np.exp(-source_power / Ps_c)
    )

    # -------------------------------------------------
    # 3. BOHM VELOCITY
    # cs = sqrt(kTe/mi)
    # -------------------------------------------------

    cs = np.sqrt((kB * Te * 11600) / mi)

    # -------------------------------------------------
    # 4. ION FLUX
    # Gamma0 = ni * cs
    # -------------------------------------------------

    Gamma0 = ni * cs

    # Normalize for plotting stability
    Gamma0 = Gamma0 / 1e21

    # -------------------------------------------------
    # 5. ASPECT RATIO
    # AR = DOEv/(W0 + DOEl)
    # -------------------------------------------------

    trench_width = W0 + DOE_l

    if trench_width == 0:
        AR = 0
    else:
        AR = DOE_v / trench_width

    # -------------------------------------------------
    # 6. ION ENERGY
    # Ei = Ei0 exp(-(p/Ei0)AR)
    #      + q*bias_power
    # -------------------------------------------------

    Ei = (
        Ei0
        * np.exp(-(pressure / Ei0) * AR)
    ) + (q * bias_power)

    # -------------------------------------------------
    # 7. ANGULAR SPREAD
    # theta = theta_max(1-exp(-p/Ei))
    # -------------------------------------------------

    theta = theta_max * (
        1 - np.exp(-(k_theta * pressure) / Ei)
    )

    theta_rad = np.radians(theta)

    # -------------------------------------------------
    # 8. VERTICAL ETCH RATE
    # -------------------------------------------------

    ER_v = (
        Gamma0
        * np.cos(theta_rad)
        * np.exp(-(k_flux * pressure * AR) / Ei)
    )

    # -------------------------------------------------
    # 9. LATERAL ETCH RATE
    # -------------------------------------------------

    ER_l = (
        Gamma0
        * np.sin(theta_rad)
        * (
            1
            - np.exp(-(k_flux * pressure * AR) / Ei)
        )
        * (1 - passivation)
    )

    # Scale etch rates
    ER_v = ER_v * 0.5
    ER_l = ER_l * 0.2

    # -------------------------------------------------
    # 10. GEOMETRY UPDATE
    # -------------------------------------------------

    DOE_v = DOE_v + ER_v * dt

    DOE_l = DOE_l + 2 * ER_l * dt

    # -------------------------------------------------
    # 11. ANISOTROPY
    # -------------------------------------------------

    if (DOE_v + DOE_l) == 0:
        A = 0
    else:
        A = DOE_v / (DOE_v + DOE_l)

    # -------------------------------------------------
    # STORE VALUES
    # -------------------------------------------------

    time_list.append(t)

    Te_list.append(Te)
    ni_list.append(ni)

    cs_list.append(cs)

    Ei_list.append(Ei)

    theta_list.append(theta)

    vertical_list.append(DOE_v)
    lateral_list.append(DOE_l)

    anisotropy_list.append(A)

# =====================================================
# PLOTS
# =====================================================

plt.figure(figsize=(14,12))

# -----------------------------------------------------
# Depth Evolution
# -----------------------------------------------------

plt.subplot(3,2,1)

plt.plot(time_list, vertical_list,
         label='Vertical Depth')

plt.plot(time_list, lateral_list,
         label='Lateral Depth')

plt.xlabel("Time Step")
plt.ylabel("Depth (nm)")

plt.title("Etch Depth Evolution")

plt.legend()
plt.grid()

# -----------------------------------------------------
# Anisotropy
# -----------------------------------------------------

plt.subplot(3,2,2)

plt.plot(time_list, anisotropy_list)

plt.xlabel("Time Step")
plt.ylabel("Anisotropy")

plt.title("Anisotropy Evolution")

plt.grid()

# -----------------------------------------------------
# Electron Temperature
# -----------------------------------------------------

plt.subplot(3,2,3)

plt.plot(time_list, Te_list)

plt.xlabel("Time Step")
plt.ylabel("Te")

plt.title("Electron Temperature")

plt.grid()

# -----------------------------------------------------
# Ion Energy
# -----------------------------------------------------

plt.subplot(3,2,4)

plt.plot(time_list, Ei_list)

plt.xlabel("Time Step")
plt.ylabel("Ion Energy (eV)")

plt.title("Ion Energy Evolution")

plt.grid()

# -----------------------------------------------------
# Angular Spread
# -----------------------------------------------------

plt.subplot(3,2,5)

plt.plot(time_list, theta_list)

plt.xlabel("Time Step")
plt.ylabel("Theta (deg)")

plt.title("Angular Spread")

plt.grid()

# -----------------------------------------------------
# Bohm Velocity
# -----------------------------------------------------

plt.subplot(3,2,6)

plt.plot(time_list, cs_list)

plt.xlabel("Time Step")
plt.ylabel("cs")

plt.title("Bohm Velocity")

plt.grid()

plt.tight_layout()
plt.show()

# =====================================================
# FINAL RESULTS
# =====================================================

print("\n========== FINAL RESULTS ==========")

print(f"Final Vertical Depth : {DOE_v:.3f} nm")
print(f"Final Lateral Depth  : {DOE_l:.3f} nm")
print(f"Final Anisotropy     : {A:.3f}")

print(f"Final Ion Energy     : {Ei:.3f} eV")
print(f"Final Angular Spread : {theta:.3f} deg")