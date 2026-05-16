import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from scipy.integrate import solve_ivp
import os

# ============================================================
# Week 14 Lab: Thermal Properties — 1D Spherical Cooling Simulation
# ============================================================

# Default thermal properties for apple
DEFAULT_PARAMS = {
    'k': 0.42,           # Thermal conductivity (W/m·°C)
    'rho': 840.0,        # Density (kg/m³)
    'cp': 3800.0,        # Specific heat (J/kg·°C)
    'R': 0.04,           # Radius (m) — approx. 8cm diameter
    'h': 20.0,           # Convective heat transfer coefficient (W/m²·°C)
    'T_init': 25.0,      # Initial product temperature (°C)
    'T_inf': 2.0,        # Cooling fluid temperature (°C)
    'N': 50,             # Number of spatial grid nodes
    't_end': 7200,       # Simulation end time (seconds, 2 hours)
}


def build_ode_system(params):
    """
    Build 1D spherical heat conduction ODE system

    PDE: dT/dt = alpha * (1/r²) * d/dr(r² * dT/dr)
    Finite difference spatial discretization → ODE system dT/dt = f(T)
    """
    k = params['k']
    rho = params['rho']
    cp = params['cp']
    R = params['R']
    h = params['h']
    T_inf = params['T_inf']
    N = params['N']

    alpha = k / (rho * cp)  # Thermal diffusivity (m²/s)
    dr = R / N              # Spatial grid spacing

    r = np.linspace(0, R, N + 1)

    def dTdt(t, T):
        dT = np.zeros_like(T)

        # Interior nodes (i = 1 to N-1): spherical finite difference
        for i in range(1, N):
            d2T_dr2 = (T[i + 1] - 2 * T[i] + T[i - 1]) / dr**2
            dT_dr = (T[i + 1] - T[i - 1]) / (2 * dr)
            dT[i] = alpha * (d2T_dr2 + (2 / r[i]) * dT_dr)

        # Center boundary (r=0): symmetry via L'Hôpital's rule
        d2T_center = (T[1] - T[0]) / dr**2
        dT[0] = alpha * 3 * d2T_center

        # Surface boundary (r=R): conduction = convection balance
        T_surface = (k * T[N - 1] + h * dr * T_inf) / (k + h * dr)
        T[N] = T_surface
        d2T_surf = (T[N - 1] - 2 * T[N] + T[N]) / dr**2
        dT_dr_surf = (T[N] - T[N - 1]) / dr
        if r[N] > 0:
            dT[N] = alpha * (d2T_surf + (2 / r[N]) * dT_dr_surf)
        else:
            dT[N] = 0

        return dT

    return r, dTdt


def run_simulation(params):
    """Run simulation and return results"""
    N = params['N']
    T_init = params['T_init']
    T_inf = params['T_inf']
    t_end = params['t_end']

    r, dTdt = build_ode_system(params)

    T0 = np.full(N + 1, T_init)
    t_eval = np.linspace(0, t_end, 500)

    sol = solve_ivp(dTdt, [0, t_end], T0, t_eval=t_eval,
                    method='RK45', max_step=10.0)

    T_center = sol.y[0, :]
    T_surface = sol.y[N, :]

    # Half-cooling time calculation
    theta = (T_center - T_inf) / (T_init - T_inf)
    half_idx = np.where(theta <= 0.5)[0]
    half_cool_time = t_eval[half_idx[0]] if len(half_idx) > 0 else t_end

    return t_eval, T_center, T_surface, half_cool_time


def main():
    params = DEFAULT_PARAMS.copy()

    t_eval, T_center, T_surface, hct = run_simulation(params)

    print("=" * 60)
    print("  Week 14 Lab: 1D Spherical Cooling Simulation Results")
    print("=" * 60)
    print(f"  Thermal diffusivity α = {params['k']/(params['rho']*params['cp']):.2e} m²/s")
    print(f"  Biot number Bi = {params['h']*params['R']/params['k']:.3f}")
    print(f"  Half-cooling time = {hct:.0f} sec ({hct/60:.1f} min)")
    print(f"  Final center temperature = {T_center[-1]:.2f} °C")
    print(f"  Final surface temperature = {T_surface[-1]:.2f} °C")
    print("=" * 60)

    # Visualization
    fig, axes = plt.subplots(1, 2, figsize=(16, 7))
    plt.subplots_adjust(bottom=0.30, wspace=0.3)

    # Left: Temperature time series
    ax_temp = axes[0]
    line_center, = ax_temp.plot(t_eval / 60, T_center, 'b-', linewidth=2, label='Center Temp')
    line_surface, = ax_temp.plot(t_eval / 60, T_surface, 'r--', linewidth=2, label='Surface Temp')
    ax_temp.axhline(y=params['T_inf'], color='gray', linestyle=':', alpha=0.7, label=f'Fluid {params["T_inf"]}°C')
    line_half = ax_temp.axvline(x=hct / 60, color='green', linestyle='--', alpha=0.6, label=f'Half-cool {hct/60:.1f} min')
    ax_temp.set_title('Temperature vs Time — Spherical Cooling')
    ax_temp.set_xlabel('Time (min)')
    ax_temp.set_ylabel('Temperature (°C)')
    ax_temp.legend(loc='upper right', fontsize=9)
    ax_temp.grid(True, linestyle=':', alpha=0.5)
    ax_temp.set_ylim(0, params['T_init'] + 2)

    # Right: Dimensionless temperature
    ax_theta = axes[1]
    theta_center = (T_center - params['T_inf']) / (params['T_init'] - params['T_inf'])
    theta_surface = (T_surface - params['T_inf']) / (params['T_init'] - params['T_inf'])
    line_tc, = ax_theta.plot(t_eval / 60, theta_center, 'b-', linewidth=2, label='Center θ')
    line_ts, = ax_theta.plot(t_eval / 60, theta_surface, 'r--', linewidth=2, label='Surface θ')
    ax_theta.axhline(y=0.5, color='green', linestyle='--', alpha=0.5, label='θ = 0.5 (Half-cooling)')
    ax_theta.axhline(y=0.125, color='orange', linestyle='--', alpha=0.5, label='θ = 0.125 (7/8 cooling)')
    ax_theta.set_title('Dimensionless Temperature θ')
    ax_theta.set_xlabel('Time (min)')
    ax_theta.set_ylabel('θ = (T - T∞) / (Ti - T∞)')
    ax_theta.legend(loc='upper right', fontsize=9)
    ax_theta.grid(True, linestyle=':', alpha=0.5)
    ax_theta.set_ylim(-0.05, 1.05)

    # Info text box
    info_text = ax_temp.text(0.05, 0.35, '', transform=ax_temp.transAxes, fontsize=10,
                             verticalalignment='top',
                             bbox=dict(boxstyle='round,pad=0.5', facecolor='lightyellow', alpha=0.9))

    def format_info(p, hct_val):
        bi = p['h'] * p['R'] / p['k']
        return (f"Bi = {bi:.3f}\n"
                f"R = {p['R']*100:.1f} cm\n"
                f"h = {p['h']:.0f} W/m²·°C\n"
                f"T₀ = {p['T_init']:.0f} °C\n"
                f"Half-cool = {hct_val/60:.1f} min")

    info_text.set_text(format_info(params, hct))

    # 3 Sliders
    ax_h = plt.axes([0.15, 0.15, 0.7, 0.03], facecolor='lightgoldenrodyellow')
    ax_r = plt.axes([0.15, 0.10, 0.7, 0.03], facecolor='lightgoldenrodyellow')
    ax_t = plt.axes([0.15, 0.05, 0.7, 0.03], facecolor='lightgoldenrodyellow')

    slider_h = Slider(ax_h, 'h (W/m²·°C)', 5, 100, valinit=params['h'], valstep=5)
    slider_r = Slider(ax_r, 'Radius (cm)', 2, 8, valinit=params['R'] * 100, valstep=0.5)
    slider_t = Slider(ax_t, 'T_init (°C)', 15, 40, valinit=params['T_init'], valstep=1)

    def update(val):
        p = params.copy()
        p['h'] = slider_h.val
        p['R'] = slider_r.val / 100.0
        p['T_init'] = slider_t.val

        t_ev, Tc, Ts, hct_new = run_simulation(p)

        line_center.set_data(t_ev / 60, Tc)
        line_surface.set_data(t_ev / 60, Ts)
        line_half.set_xdata([hct_new / 60])
        ax_temp.set_ylim(0, p['T_init'] + 2)

        tc = (Tc - p['T_inf']) / (p['T_init'] - p['T_inf'])
        ts = (Ts - p['T_inf']) / (p['T_init'] - p['T_inf'])
        line_tc.set_data(t_ev / 60, tc)
        line_ts.set_data(t_ev / 60, ts)

        info_text.set_text(format_info(p, hct_new))
        fig.canvas.draw_idle()

    slider_h.on_changed(update)
    slider_r.on_changed(update)
    slider_t.on_changed(update)

    plt.suptitle('Week 14 Lab: 1D Spherical Cooling Simulation', fontsize=14, fontweight='bold', y=0.98)
    print("\nCheck the plot window. Use sliders to adjust h, R, T_init for real-time recalculation.")
    plt.show()


if __name__ == '__main__':
    main()
