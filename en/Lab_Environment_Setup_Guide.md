# 🛠️ Lab Environment Setup Guide

> **Course:** Biomaterial Handling & Processing
> **Instructor:** Dongsoo Ryu (Dept. of Biosystems Engineering, JBNU)
> **Last Updated:** 2026-05-17
> **[Korean Version](../ko/실습_환경_설정_가이드.md)**

---

## 📋 Table of Contents

1. [Prerequisites](#1-prerequisites)
2. [Python Installation](#2-python-installation)
3. [VS Code & Google Antigravity Setup](#3-vs-code--google-antigravity-setup)
4. [Git Installation & GitHub Account](#4-git-installation--github-account)
5. [Downloading Lab Materials](#5-downloading-lab-materials)
6. [Python Package Installation](#6-python-package-installation)
7. [Running Lab Codes](#7-running-lab-codes)
8. [Submitting Lab Reports (GitHub Issue)](#8-submitting-lab-reports-github-issue)
9. [Frequently Asked Questions (FAQ)](#9-frequently-asked-questions-faq)

---

## 1. Prerequisites

### Required Software

| Software | Purpose | Download |
|-----------|------|---------|
| **Python 3.11+** | Running lab codes | [python.org](https://www.python.org/downloads/) |
| **VS Code** | Code editor | [code.visualstudio.com](https://code.visualstudio.com/) |
| **Google Antigravity** | AI-based agentic coding assistant | (Refer to class links) |
| **Git** | Version control & downloading materials | [git-scm.com](https://git-scm.com/) |

### Recommended Environment

- **OS**: Windows 10 or Windows 11
- **Internet**: Stable Wi-Fi or wired connection
- **Storage**: At least 5GB of free space

---

## 2. Python Installation

### 2.1 Download

1. Go to [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Click the yellow **"Download Python 3.x.x"** button.

### 2.2 Installation

1. Run the downloaded installer (`python-3.x.x-amd64.exe`).
2. ⚠️ **Check "Add python.exe to PATH"** (Very important!)
3. Click **"Install Now"**.

### 2.3 Verify Installation

- Search for **"cmd"** in Windows and open **Command Prompt**.
- Run the following command:

```bash
python --version
```

- Example output: `Python 3.13.3`

---

## 3. VS Code & Google Antigravity Setup

### 3.1 VS Code Download & Installation

1. Go to [https://code.visualstudio.com/](https://code.visualstudio.com/)
2. Click **"Download for Windows"** and run the installer.
3. Keep default settings, but check `Add "Open with Code" action to Windows Explorer file context menu` and `Add to PATH`.

### 3.2 Install Essential Extensions

- Open VS Code, go to **Extensions** (`Ctrl+Shift+X`).
- Search and **Install**:
  - **Python** (Microsoft)
  - **Korean Language Pack** (Optional for Korean UI)
  - **Jupyter** (Optional)
  - **Markdown Preview Enhanced** (Recommended)

### 3.3 Google Antigravity Agent Setup 🚀

In this course, we go beyond simple chatbot AI assistants by utilizing **Google Antigravity**, an agentic coding assistant capable of planning, executing terminal commands, and modifying files directly.

- **Installation Steps**:
  1. Download the Antigravity setup package provided in class.
  2. Install and launch the application.
  3. Log in with your authorized Google Workspace account.
  4. In the settings, grant workspace access to your lab folder (e.g., `biomaterial-handling`).

- **Usage Example (Agentic Coding)**:
  - You can give complex instructions like:
    - *"Add PCA analysis to the week 12 spectroscopy code, install necessary packages, and plot the results."*
    - *"Update the README format and scan the current folder to refresh the index."*
  - **Note**: Since the agent can run terminal commands and modify files, always **approve** suggested actions before they execute.

### 3.4 Markdown Preview Mode

- To preview Markdown (`.md`) files:
  - Click the **📖 Preview Icon** in the top right.
  - Or use `Ctrl+Shift+V` (Full-screen preview).
  - Or use `Ctrl+K V` (Side-by-side preview).

---

## 4. Git Installation & GitHub Account

### 4.1 Git Installation

1. Go to [https://git-scm.com/](https://git-scm.com/) → Click **"Download for Windows"**.
2. Run the installer and keep all default settings.
3. Verify installation: `git --version`

### 4.2 GitHub Account & Setup

1. Sign up at [https://github.com/](https://github.com/).
2. Open the VS Code terminal and configure your Git user info:

```bash
git config --global user.name "John Doe"
git config --global user.email "johndoe@example.com"
```

---

## 5. Downloading Lab Materials

### Method A: Git Clone (Recommended ⭐)

Run the following command in the VS Code terminal:

```bash
git clone https://github.com/ryu-dongsoo/biomaterial-handling.git
```

Open the `biomaterial-handling` folder in VS Code.

### Method B: Download ZIP

1. Go to [https://github.com/ryu-dongsoo/biomaterial-handling](https://github.com/ryu-dongsoo/biomaterial-handling).
2. Click the green **"<> Code"** button → **"Download ZIP"**.
3. Extract and open the folder in VS Code.

### Updating Materials (Every Week)

```bash
git pull origin main
```

---

## 6. Python Package Installation

This course relies on several scientific computing and data analysis packages.

### 6.1 Batch Installation

Run the following command in the terminal to install essential packages at once:

```bash
pip install numpy scipy pandas matplotlib scikit-learn opencv-python
```

### 6.2 Verify Installation

```bash
python -c "import numpy, scipy, pandas, matplotlib, sklearn, cv2; print('Success!')"
```

---

## 7. Running Lab Codes

1. Open the weekly folder in VS Code (e.g., `en/week13/`).
2. Open the `.py` script (e.g., `step1_acoustic_fft.py`).
3. Click the `▶` (Run) button on the top right, or run `python step1_acoustic_fft.py` in the terminal.
4. Read the manual, modify parameters, and take screenshots for your report.

---

## 8. Submitting Lab Reports (GitHub Issue)

1. Write your report using the provided `.md` template in the weekly folder.
2. Go to [https://github.com/ryu-dongsoo/biomaterial-handling/issues](https://github.com/ryu-dongsoo/biomaterial-handling/issues).
3. Click **"New issue"** and select the report template.
4. Set the title format: `[Week13] 202412345_JohnDoe_Report`.
5. Paste your Markdown report and drag & drop your screenshots.
6. Select the appropriate week label and click **"Submit new issue"**.

---

## 9. Frequently Asked Questions (FAQ)

### 9.1 'python' is not recognized as an internal or external command

- **Cause**: "Add python.exe to PATH" was not checked during installation.
- **Fix**: Re-run the installer → Click "Modify" → Check the PATH option.

### 9.2 pip install errors

- **Fix**: Run `python -m pip install <package>` or open VS Code as Administrator.

### 9.3 Korean Font Rendering Issue in Matplotlib

- **Fix**: All codes include the following snippet to ensure correct font display. Do not remove it:
```python
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False
```

---

## 📞 Support

| Type | Contact |
|------|---------|
| **Instructor** | Dongsoo Ryu (ryudongsoo@jbnu.ac.kr) |
| **Lab** | Room 311, Bldg 4, College of Agriculture and Life Sciences, JBNU (ASRL) |
| **Repository** | [github.com/ryu-dongsoo/biomaterial-handling](https://github.com/ryu-dongsoo/biomaterial-handling) |

---

[← Back to Main README](../README.md)
