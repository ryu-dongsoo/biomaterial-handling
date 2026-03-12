# 🥑 Week 4: Density & Porosity Lab for Agricultural Materials
**– Computing Physical Properties and Virtual 3D Packing Simulation –**

> 📂 **Navigation**: [← Week 3: Volume & Surface Area](../week3/03주차_실습_체적_표면적.md) · [Main README](../../README.md) · [📝 Quiz Bank](../../QUIZ_BANK.md)

---

## 0. Target Data: Continuation from Week 3

This week's lab utilizes the numerical integration volume data from Week 3, combined with simulated mass and packaging box properties.

| Parameter | Data Value |
|-----------|------------|
| Specimen | Avocado (Hass variety) |
| Individual Volume | 205.4 cm³ (from Week 3 Simpson's integration) |
| Individual Mass | 215.0 g (Assumed scale measurement) |
| Standard Packaging Box | 40cm (W) × 30cm (D) × 15cm (H) (Total Vol: 18,000 cm³) |
| Box Capacity | 45 units per box |

---

## 1. Theoretical Background: Significance of Density and Porosity

### 1-1. True Density & Apparent Density
- **Concept**: Intrinsic density of an individual biological specimen, varying by the presence of internal cellular voids
- **Applications**: Quality grading, aerodynamic sorting (e.g., wind extraction), mass-to-volume estimations
- **Lab Integration**: Defined cohesively as 'Particle Density'

### 1-2. Bulk Density
- **Concept**: Ratio of the total mass of biological materials to the entire volume of their enclosing container
- **Applications**: Designing capacities of silos and logistics warehouses; calculating payload limits for transport trucks
- **Characteristics**: Highly dependent on packing method, compaction cycles, and particle shape

### 1-3. Porosity
- **Concept**: The proportion of void volume relative to the total bulk volume
- **Applications**: Assessing airflow resistance during hot-air drying; predicting gas permeability for fumigation treatments; designing heat dissipation
- **Calculation Methods**:
  - `Density Ratio Strategy` = 1 - (Bulk Density / Particle Density)
  - `Volume Subtraction Strategy` = (Void Volume / Box Volume)

---

## 2. Python Algorithm Lab: Computing Density and Porosity

This module covers a complete Python pipeline scaling from individual properties to population properties, along with 3D visualization.

### 📝 [Mandatory] Environment Setup & Execution Guide
1. **Package Installation**: Install required libraries via terminal
   ```bash
   pip install numpy matplotlib
   ```
2. **File Location**: `week4/step1_density_porosity.py` and `week4/step2_advanced_apple.py`
3. **Execution**: Run the Python script iteratively
   ```bash
   python step1_density_porosity.py    # Baseline Avocado Lab
   python step2_advanced_apple.py      # Advanced Apple Lab (after filling variables)
   ```

---

### 📊 Python Script Key Highlights (Step 1 ~ Step 4)

#### 2-1. [Step 1] Particle Density
- Individual density computation via mass and volume inputs
- Computed value exceeds water density (1.0 g/cm³) → Sink behavior expected during washing processes

#### 2-2. [Step 2] Bulk Density (Packed Cargo)
- Calculation of total mass within the container (Unit mass × Totals)
- Assessment against the total physical volume of the plastic box

#### 2-3. [Step 3] Porosity Cross-validation
- Systematic comparison of two distinct mathematical approaches
- Verification confirming identity between `Density Ratio` formula and `Physical Volume Subtraction` formula

#### 2-4. [Step 4] Unified Data Visualization
- **3D Virtual Packing (Scatter)**: Spatial arrangement of 45 avocados and direct visualization of void spaces
- **Density Gap Analysis (Bar Chart)**: Numerical contrast between Particle vs. Bulk Density
- **Occupancy Analysis (Pie Chart)**: Ratio of actual avocado volume versus porosity allocations

#### 2-5. 🚀 [Advanced] Target Swap Exercise: Applying Apple Data
- **Objective**: Adapt the baseline script to compute physical properties of a different agricultural product
- **Assignment**: Replace the baseline avocado variables with the apple data below, execute the script, and analyze the outcomes
  - Individual Volume (`volume_single_cm3`): **315.0 cm³** (Reference: Week 2 Apple)
  - Individual Mass (`mass_single_g`): **280.0 g**
  - Loaded Object Count (`apple_count`): **24 units**
- **Observation Points**: Shift in Particle Density (flotation vs. sink behavior) and fluctuations in Porosity values based on the morphological difference

---

## 3. 💡 Advanced Discussion Topics

### Topic 1: Correlation Between Shape and Porosity
- **Background**: Perfectly spherical fruits yield vastly different void architectures compared to irregularly shaped produce when packed.
- **Prompt**: If avocados were replaced with highly spherical 'Tomatoes' or elongated 'Bananas' within the identical box dimensions, how would porosity statistics and localized airflow resistance shift?

### Topic 2: Compaction Effects in Logistics Packaging
- **Background**: Vibrations during trucking organically rearrange the payload's geometry.
- **Prompt**: Evaluate the dynamic impact of transportation vibrations on Bulk Density and Porosity. Formulate an engineering strategy utilizing localized buffer materials to mitigate excessive compaction damages.

---

## 4. 📝 Evaluation Quiz Repository

### Q1. [Theory] Application Scopes of Density Metrics
Which metric is primarily used to layout and design the overarching total volume capacity of a large-scale storage facility like a Silo?

- [ ] A. True Density
- [ ] B. Apparent Density
- [x] C. Bulk Density
- [ ] D. Solid Density

### Q2. [Python Functions] 3D Grid Visualization Module
To map avocados repetitively onto virtual X, Y, Z spatial coordinates, which `numpy` function acts as the core mesh generator?

- [x] A. `np.meshgrid`
- [ ] B. `np.linspace`
- [ ] C. `np.dot`
- [ ] D. `np.cross`

---

## 5. Lab Artifacts Version Control & GitHub Submissions

- Assignments follow an accumulative repository model per week
- For step-by-step GitHub integration and `push` directives, consult the comprehensive [Integrated Lab Submission Guide](../../README.md) located in the root directory
