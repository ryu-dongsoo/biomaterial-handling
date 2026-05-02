"""
Week 10 Lab Step 1: Fruit Free-Fall Impact Characteristics & Restitution Analysis
- Calculate the coefficient of restitution using pre- and post-impact velocities based on mock Tracker data.
- Compare maximum impact forces with and without cushioning material, simulating the damage threshold.
"""

import numpy as np

# 1. Biomaterial basic parameters
mass = 0.25          # Mass of apple (kg)
drop_height = 1.0    # Free-fall height (m)
g = 9.81             # Gravitational acceleration (m/s^2)

# Theoretical velocity right before impact
v1_theoretical = -np.sqrt(2 * g * drop_height)

# 2. Mock Tracker video analysis data (Y-axis velocity pre/post impact)
# Case A: Hard surface impact
v1_hard = -4.40  # Velocity just before impact (m/s)
v2_hard = 1.50   # Velocity immediately after rebound (m/s)
dt_hard = 0.005  # Collision duration time (s)

# Case B: Soft cushioning material
v1_soft = -4.40  # Velocity just before impact (m/s)
v2_soft = 0.80   # Velocity immediately after rebound (m/s)
dt_soft = 0.020  # Collision duration time (s)

# 3. Calculate Coefficient of Restitution (e)
e_hard = abs(v2_hard / v1_hard)
e_soft = abs(v2_soft / v1_soft)

# 4. Calculate Maximum Impact Force: F = m * dv / dt
dv_hard = v2_hard - v1_hard
dv_soft = v2_soft - v1_soft

force_hard = mass * dv_hard / dt_hard
force_soft = mass * dv_soft / dt_soft

# 5. Output analysis results
print("--- 🍎 Impact Characteristics Analysis ---")
print(f"Apple Mass: {mass} kg, Drop Height: {drop_height} m")
print(f"Theoretical Impact Velocity: {v1_theoretical:.2f} m/s\n")

print("[Hard Surface Impact]")
print(f"- Coefficient of Restitution (e): {e_hard:.3f}")
print(f"- Collision Duration: {dt_hard} s")
print(f"- Maximum Impact Force: {force_hard:.2f} N")

print("\n[Cushioned Surface Impact]")
print(f"- Coefficient of Restitution (e): {e_soft:.3f}")
print(f"- Collision Duration: {dt_soft} s")
print(f"- Maximum Impact Force: {force_soft:.2f} N")

print("\n--- 📊 Bruise Damage Prediction Model ---")
bruise_threshold = 150.0  # Critical force threshold for internal tissue damage (N)
print(f"Applied Damage Threshold: {bruise_threshold} N")
print(f"Hard Surface: {'Damage Risk ❌' if force_hard > bruise_threshold else 'Safe ✅'}")
print(f"Cushioned Surface: {'Damage Risk ❌' if force_soft > bruise_threshold else 'Safe ✅'}")
