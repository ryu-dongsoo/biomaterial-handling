# Week 13 Lab: Acoustic Properties — FFT-Based Firmness Analysis

## 🎯 Lab Objectives

- **Understanding Acoustic Non-Destructive Testing Principles**: Analysis of correlation between resonance frequency from impact excitation and fruit firmness
- **Acquisition of FFT (Fast Fourier Transform) Techniques**: Conversion of time-domain impact response signals to frequency domain for resonance peak extraction
- **Execution of Stiffness Coefficient Modeling**: Coding implementation of $S = f^2 \times m^{2/3}$ formula for mass-corrected non-destructive firmness index calculation and grade classification

---

## 📊 1. Overview of Lab Data

- **Data Generation Method**: Virtual damped sinusoid-based impact response signals (30 samples)
- **Sample Composition**:
  - Firm fruit group: Resonance frequency 600–900 Hz (10 samples)
  - Medium fruit group: Resonance frequency 400–600 Hz (10 samples)
  - Soft fruit group: Resonance frequency 200–400 Hz (10 samples)
- **Additional Variables**: Individual fruit mass randomly assigned between 150–350g
- **Output**: Automatically saved to `data/acoustic_results.csv`

---

## 🛠️ 2. FFT (Fast Fourier Transform) Spectrum Analysis

- Time-domain impact sound signals are complex waveforms containing multiple frequency components
- **FFT Transform** (`np.fft.rfft`):
  - Conversion of time-domain array to frequency-domain magnitude spectrum
  - Extraction of only positive frequency range for analytical efficiency
- **Power Spectrum Visualization**: Intuitive identification of resonance peak positions on X-axis (Hz) vs Y-axis (Magnitude) graph

---

## 🔍 3. Automatic Resonance Peak Detection

- **Detection Tool**: `scipy.signal.find_peaks` function
- **Parameter Settings**:
  - `height`: Selection of only peaks exceeding 30% of maximum amplitude as valid candidates
  - `distance`: Minimum spacing between adjacent peaks to exclude noise peaks
- **Dominant Frequency**: Extraction of frequency value of the peak with highest amplitude among detected peaks

---

## 💻 4. Stiffness Coefficient Calculation and Grade Classification

- **Formula**: $S = f^2 \times m^{2/3}$
  - $f$: Detected resonance frequency (Hz)
  - $m$: Fruit mass (converted to kg)
- **Significance of Mass Correction**: Application of mass weighting for fair firmness comparison between fruits of different sizes
- **Classification Criteria**:

| Grade | Stiffness Range | Interpretation |
|-------|----------------|----------------|
| Firm | S > 200,000 | Freshly harvested or unripe stage |
| Medium | 80,000 < S ≤ 200,000 | Optimal ripeness range |
| Soft | S ≤ 80,000 | Over-ripe or tissue softening stage |

---

## 📈 5. Visualization and Interactive Analysis

- **4-Panel Grid Layout**:
  1. Time-domain waveform comparison (representative samples: Firm/Medium/Soft)
  2. FFT power spectrum comparison with peak frequency annotations
  3. Stiffness index vs resonance frequency scatter plot (color-coded by grade)
  4. Stiffness index vs fruit mass scatter plot
- **Interactive Slider**:
  - Slider at bottom for batch mass (m) parameter adjustment with real-time stiffness recalculation
  - Intuitive observation of how mass correction affects grade classification results
- **Code Execution Method**:
  - Execute `python step1_acoustic_fft.py` in terminal, then review console analysis results and popup plot window
