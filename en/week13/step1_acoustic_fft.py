import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from scipy.signal import find_peaks
import pandas as pd
import os

# ============================================================
# Week 13 Lab: Acoustic Properties — FFT-Based Firmness Analysis
# ============================================================


def generate_impact_signal(f_resonance, damping, mass, sr=44100, duration=0.3):
    """Generate a virtual impact response signal (damped sinusoid)"""
    t = np.linspace(0, duration, int(sr * duration), endpoint=False)
    envelope = np.exp(-damping * t)
    main_tone = envelope * np.sin(2 * np.pi * f_resonance * t)
    harmonic = 0.15 * envelope * np.sin(2 * np.pi * f_resonance * 2.1 * t)
    noise = 0.02 * np.random.randn(len(t))
    signal = main_tone + harmonic + noise
    return t, signal


def compute_fft(signal, sr):
    """FFT transform — extract positive frequency domain"""
    N = len(signal)
    fft_vals = np.fft.rfft(signal)
    magnitude = np.abs(fft_vals) * 2.0 / N
    freqs = np.fft.rfftfreq(N, d=1.0 / sr)
    return freqs, magnitude


def detect_peak(freqs, magnitude, min_freq=50, max_freq=5000, height_ratio=0.3):
    """Automatic resonance peak detection using scipy.signal.find_peaks"""
    mask = (freqs >= min_freq) & (freqs <= max_freq)
    freqs_crop = freqs[mask]
    mag_crop = magnitude[mask]
    threshold = height_ratio * np.max(mag_crop)
    peaks, _ = find_peaks(mag_crop, height=threshold, distance=20)
    if len(peaks) == 0:
        idx = np.argmax(mag_crop)
        return freqs_crop[idx], mag_crop[idx]
    dominant = peaks[np.argmax(mag_crop[peaks])]
    return freqs_crop[dominant], mag_crop[dominant]


def calc_stiffness(f_hz, mass_g):
    """Stiffness coefficient: S = f^2 * m^(2/3), mass in kg"""
    mass_kg = mass_g / 1000.0
    return (f_hz ** 2) * (mass_kg ** (2 / 3))


def classify_firmness(S):
    """Grade classification: Firm / Medium / Soft"""
    if S > 2e5:
        return 'Firm'
    elif S > 8e4:
        return 'Medium'
    else:
        return 'Soft'


def main():
    np.random.seed(42)
    sr = 44100
    num_samples = 30

    # Resonance frequency distribution by maturity
    f_resonances = np.concatenate([
        np.random.uniform(600, 900, 10),   # Firm
        np.random.uniform(400, 600, 10),   # Medium
        np.random.uniform(200, 400, 10),   # Soft
    ])
    dampings = np.random.uniform(15, 40, num_samples)
    masses = np.random.uniform(150, 350, num_samples)

    # FFT analysis for all samples
    results = []
    for i in range(num_samples):
        t, sig = generate_impact_signal(f_resonances[i], dampings[i], masses[i], sr=sr)
        freqs, mag = compute_fft(sig, sr)
        peak_f, peak_m = detect_peak(freqs, mag)
        S = calc_stiffness(peak_f, masses[i])
        grade = classify_firmness(S)
        results.append({
            'Sample': i + 1, 'Mass_g': round(masses[i], 1),
            'True_f_Hz': round(f_resonances[i], 1),
            'Detected_f_Hz': round(peak_f, 1),
            'Stiffness': round(S, 0), 'Grade': grade
        })

    df = pd.DataFrame(results)
    print("=" * 70)
    print("  Week 13 Lab: Acoustic FFT-Based Firmness Analysis Results")
    print("=" * 70)
    print(df.to_string(index=False))
    print(f"\nAnalysis complete for {num_samples} samples\n")

    # Save CSV
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(base_dir, 'data')
    os.makedirs(data_dir, exist_ok=True)
    csv_path = os.path.join(data_dir, 'acoustic_results.csv')
    df.to_csv(csv_path, index=False, encoding='utf-8-sig')
    print(f"Results saved to: {csv_path}\n")

    # Visualization: 4-panel grid
    sample_indices = [0, 10, 20]
    sample_labels = ['Firm', 'Medium', 'Soft']
    sample_colors = ['#2196F3', '#FF9800', '#F44336']

    fig, axes = plt.subplots(2, 2, figsize=(16, 10))
    plt.subplots_adjust(bottom=0.18, hspace=0.35, wspace=0.3)

    # (0,0) Time domain waveform
    ax_wave = axes[0, 0]
    for idx, label, color in zip(sample_indices, sample_labels, sample_colors):
        t, sig = generate_impact_signal(f_resonances[idx], dampings[idx], masses[idx], sr=sr)
        ax_wave.plot(t * 1000, sig, alpha=0.8, label=label, color=color, linewidth=0.8)
    ax_wave.set_title('Time Domain — Impact Response Waveform')
    ax_wave.set_xlabel('Time (ms)')
    ax_wave.set_ylabel('Amplitude')
    ax_wave.legend(loc='upper right', fontsize=9)
    ax_wave.grid(True, linestyle=':', alpha=0.5)

    # (0,1) FFT spectrum
    ax_fft = axes[0, 1]
    for idx, label, color in zip(sample_indices, sample_labels, sample_colors):
        t, sig = generate_impact_signal(f_resonances[idx], dampings[idx], masses[idx], sr=sr)
        freqs, mag = compute_fft(sig, sr)
        mask = freqs <= 2000
        ax_fft.plot(freqs[mask], mag[mask], alpha=0.8, label=label, color=color, linewidth=1.0)
        pf, pm = detect_peak(freqs, mag)
        ax_fft.annotate(f'{pf:.0f} Hz', xy=(pf, pm), fontsize=8,
                        arrowprops=dict(arrowstyle='->', color=color, lw=1.2),
                        xytext=(pf + 100, pm + 0.01), color=color, fontweight='bold')
    ax_fft.set_title('Frequency Domain — FFT Power Spectrum')
    ax_fft.set_xlabel('Frequency (Hz)')
    ax_fft.set_ylabel('Magnitude')
    ax_fft.legend(loc='upper right', fontsize=9)
    ax_fft.grid(True, linestyle=':', alpha=0.5)

    # (1,0) Stiffness scatter plot
    ax_scatter = axes[1, 0]
    grade_colors = {'Firm': '#2196F3', 'Medium': '#FF9800', 'Soft': '#F44336'}
    for grade, color in grade_colors.items():
        subset = df[df['Grade'] == grade]
        ax_scatter.scatter(subset['Detected_f_Hz'], subset['Stiffness'],
                           c=color, label=grade, alpha=0.7, edgecolors='k', linewidth=0.5, s=60)
    ax_scatter.set_title('Stiffness Coefficient vs Resonance Frequency')
    ax_scatter.set_xlabel('Detected Resonance Frequency (Hz)')
    ax_scatter.set_ylabel('Stiffness Index  S = f² × m^(2/3)')
    ax_scatter.legend(loc='upper left', fontsize=9)
    ax_scatter.grid(True, linestyle=':', alpha=0.5)
    ax_scatter.axhline(y=2e5, color='#2196F3', linestyle='--', alpha=0.4)
    ax_scatter.axhline(y=8e4, color='#FF9800', linestyle='--', alpha=0.4)

    # (1,1) Mass vs stiffness
    ax_mass = axes[1, 1]
    for grade, color in grade_colors.items():
        subset = df[df['Grade'] == grade]
        ax_mass.scatter(subset['Mass_g'], subset['Stiffness'],
                        c=color, label=grade, alpha=0.7, edgecolors='k', linewidth=0.5, s=60)
    ax_mass.set_title('Stiffness Index vs Fruit Mass')
    ax_mass.set_xlabel('Mass (g)')
    ax_mass.set_ylabel('Stiffness Index  S = f² × m^(2/3)')
    ax_mass.legend(loc='upper left', fontsize=9)
    ax_mass.grid(True, linestyle=':', alpha=0.5)

    # Slider: mass override
    ax_slider = plt.axes([0.2, 0.05, 0.6, 0.03], facecolor='lightgoldenrodyellow')
    mass_slider = Slider(ax=ax_slider, label='Mass Override (g)',
                         valmin=100, valmax=500, valinit=250, valstep=10)

    def update(val):
        m_override = mass_slider.val
        detected_fs = df['Detected_f_Hz'].values
        new_s = np.array([calc_stiffness(f, m_override) for f in detected_fs])
        colors_arr = np.where(new_s > 2e5, '#2196F3',
                              np.where(new_s > 8e4, '#FF9800', '#F44336'))
        ax_scatter.clear()
        ax_scatter.set_title(f'Stiffness (mass={m_override:.0f}g)')
        ax_scatter.set_xlabel('Detected Resonance Frequency (Hz)')
        ax_scatter.set_ylabel('Stiffness Index  S = f² × m^(2/3)')
        ax_scatter.grid(True, linestyle=':', alpha=0.5)
        ax_scatter.scatter(detected_fs, new_s, c=colors_arr, alpha=0.7,
                           edgecolors='k', linewidth=0.5, s=60)
        ax_scatter.axhline(y=2e5, color='#2196F3', linestyle='--', alpha=0.4)
        ax_scatter.axhline(y=8e4, color='#FF9800', linestyle='--', alpha=0.4)
        fig.canvas.draw_idle()

    mass_slider.on_changed(update)
    plt.suptitle('Week 13 Lab: Acoustic FFT-Based Firmness Analysis', fontsize=14, fontweight='bold', y=0.98)
    print("Check the plot window. Use the slider at the bottom to adjust mass and observe stiffness recalculation.")
    plt.show()


if __name__ == '__main__':
    main()
