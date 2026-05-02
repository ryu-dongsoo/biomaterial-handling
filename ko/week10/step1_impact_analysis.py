"""
10주차 실습 Step 1: 과일 낙하 충격 특성 및 반발 계수 분석
- 가상의 Tracker 속도 데이터를 활용하여 충돌 직전/직후 속도 기반 반발 계수 산출
- 완충재 유무에 따른 최대 충격력(Impact Force) 비교 및 손상 한계치 시뮬레이션
"""

import numpy as np

# 1. 생물자원 기본 파라미터
mass = 0.25          # 사과 질량 (kg)
drop_height = 1.0    # 낙하 높이 (m)
g = 9.81             # 중력 가속도 (m/s^2)

# 이론적 충돌 직전 속도 연산 (자유낙하 수식)
v1_theoretical = -np.sqrt(2 * g * drop_height)

# 2. 가상의 Tracker 비디오 분석 데이터 (충돌 전후 y축 속도)
# Case A: 맨바닥 충돌 (Hard surface)
v1_hard = -4.40  # 충돌 직전 속도 (m/s)
v2_hard = 1.50   # 튕겨오른 직후 속도 (m/s)
dt_hard = 0.005  # 충돌 지속 시간 (s)

# Case B: 완충재 적용 (Cushioning material)
v1_soft = -4.40  # 충돌 직전 속도 (m/s)
v2_soft = 0.80   # 튕겨오른 직후 속도 (m/s)
dt_soft = 0.020  # 충돌 지속 시간 (s)

# 3. 반발 계수(Coefficient of Restitution, e) 산출
e_hard = abs(v2_hard / v1_hard)
e_soft = abs(v2_soft / v1_soft)

# 4. 최대 충격력(Impact Force) 산출: F = m * dv / dt
dv_hard = v2_hard - v1_hard
dv_soft = v2_soft - v1_soft

force_hard = mass * dv_hard / dt_hard
force_soft = mass * dv_soft / dt_soft

# 5. 분석 결과 출력
print("--- 🍎 낙하 충격 특성 분석 결과 ---")
print(f"사과 질량: {mass} kg, 낙하 높이: {drop_height} m")
print(f"이론적 충돌 속도: {v1_theoretical:.2f} m/s\n")

print("[맨바닥 충돌 분석]")
print(f"- 반발 계수 (e): {e_hard:.3f}")
print(f"- 충돌 지속 시간: {dt_hard} s")
print(f"- 발생 최대 충격력: {force_hard:.2f} N")

print("\n[완충재 충돌 분석]")
print(f"- 반발 계수 (e): {e_soft:.3f}")
print(f"- 충돌 지속 시간: {dt_soft} s")
print(f"- 발생 최대 충격력: {force_soft:.2f} N")

print("\n--- 📊 멍(Bruise) 손상 예측 모델 ---")
bruise_threshold = 150.0  # 과일 내부 조직 파괴 한계 하중 (N)
print(f"적용 손상 임계치: {bruise_threshold} N")
print(f"맨바닥 적재: {'손상 발생 위험 ❌' if force_hard > bruise_threshold else '안전 ✅'}")
print(f"완충재 적재: {'손상 발생 위험 ❌' if force_soft > bruise_threshold else '안전 ✅'}")
