# Week 14 Lab: Thermal Properties — Cooling Simulation and Energy Engineering

## 🎯 Lab Objectives

- **Understanding Thermal Property Parameters of Biomaterials**: Comprehension of mathematical definitions and physical meanings of specific heat ($C_p$), thermal conductivity ($k$), and thermal diffusivity ($\alpha$)
- **Acquisition of 1D Spherical Heat Conduction PDE Numerical Solution**: Cooling curve simulation based on partial differential equations using SciPy `solve_ivp`
- **Cooling Process Design Parameter Analysis**: Calculation of half-cooling time, Biot Number, and simulation under varying convective coefficients

---

## 📊 1. Thermal Property Parameter Definitions

| Parameter | Symbol | Unit | Apple Default | Meaning |
|-----------|--------|------|---------------|---------|
| Specific Heat | $C_p$ | J/kg·°C | 3,800 | Heat required to change 1kg by 1°C |
| Thermal Conductivity | $k$ | W/m·°C | 0.42 | Ease of internal heat transfer |
| Density | $\rho$ | kg/m³ | 840 | Mass per unit volume |
| Thermal Diffusivity | $\alpha$ | m²/s | $k / (\rho C_p)$ | Heat transfer vs heat storage ratio |
| Convective Coefficient | $h$ | W/m²·°C | 20 | Surface-fluid heat exchange intensity |

---

## 🛠️ 2. Heat Transfer Equations and Numerical Method

- **1D Spherical Coordinate Heat Conduction Equation (PDE)**:
  $$\frac{\partial T}{\partial t} = \alpha \left( \frac{\partial^2 T}{\partial r^2} + \frac{2}{r} \frac{\partial T}{\partial r} \right)$$
- **Boundary Conditions**:
  - Center ($r=0$): Symmetry condition — $\partial T / \partial r = 0$ (L'Hôpital's rule applied)
  - Surface ($r=R$): Conduction-convection balance — $-k \frac{\partial T}{\partial r}\big|_R = h(T_R - T_\infty)$
- **Initial Condition**: $T(r, 0) = T_{init}$ (uniform temperature at all nodes)
- **Numerical Method**: Spatial finite difference (FDM) + SciPy `solve_ivp` (RK45 time integration)

---

## 💻 3. Simulation Parameters and Code Structure

- **Spatial Discretization**: 50 nodes from center ($r=0$) to surface ($r=R$)
- **Time Range**: 0 to 7,200 seconds (2 hours), 500 evaluation points
- **Core Functions**:
  - `build_ode_system()`: PDE → ODE system conversion (finite difference)
  - `run_simulation()`: `solve_ivp` execution → center/surface temperature time series + half-cooling time
- **Biot Number**: $Bi = hR/k$
  - $Bi < 0.1$: Lumped capacitance model applicable
  - $Bi > 0.1$: 1D PDE simulation required (most fruits)

---

## 📈 4. Visualization and Interactive Analysis

- **2-Panel Layout**:
  1. **Temperature vs Time**: Center temperature (solid line) + surface temperature (dashed line), half-cooling time vertical marker
  2. **Dimensionless Temperature θ**: $\theta = (T - T_\infty)/(T_i - T_\infty)$ transform, half-cooling (θ=0.5) and 7/8 cooling (θ=0.125) reference lines
- **3 Interactive Sliders**:
  - `h` (Convective coefficient): 5 – 100 W/m²·°C — forced air blowing intensity simulation
  - `R` (Radius): 2 – 8 cm — cooling delay observation with fruit size variation
  - `T_init` (Initial temperature): 15 – 40 °C — pre-packaging field heat scenario
- **Info Box**: Real-time display of Biot number, half-cooling time, and current parameters
- **Code Execution Method**:
  - Execute `python step1_cooling_simulation.py` in terminal, then review console output and plot window
