# Manim Portable Animation Studio 🎥

![Manim Logo](assets/manim-image.png)

A cross-platform, self-contained environment for creating professional mathematical and scientific animations using the **Manim Community** library. Works out-of-the-box on both **Linux** and **Windows** without requiring global system installations for dependencies like LaTeX.

---

## 🚀 Quick Start

Clone this repository:
```bash
git clone https://github.com/shantoshdurai/Manim-Animation-Workflow.git
cd Manim-Animation-Workflow
```

### 🐧 Linux (Arch / Omarchy / Ubuntu / Debian / Fedora)

1. **Prerequisite:** Ensure `ffmpeg` is installed:
   ```bash
   sudo pacman -S ffmpeg      # Arch / Omarchy
   sudo apt install ffmpeg    # Ubuntu / Debian
   ```
2. **First-time Setup:**
   ```bash
   ./setup.sh
   ```
   *Creates a local virtual environment in `portable_env/`, installs Manim Community, and configures self-contained TinyTeX for LaTeX formulas.*
3. **Render Animation:**
   ```bash
   # Interactive quality selection:
   ./render.sh model/scene_01_basics.py

   # Direct scene and quality selection:
   ./render.sh model/scene_01_basics.py HelloWorld -ql
   ./render.sh model/scene_02_math.py EquationScene -qh

   # Optional GPU offload on hybrid NVIDIA laptops:
   USE_GPU=1 ./render.sh model/scene_01_basics.py
   ```
4. **Clean Media Artifacts:**
   ```bash
   ./clean.sh
   ```

---

### 🪟 Windows 10 / 11

1. **First-time Setup:**
   * Double-click **`setup.bat`** (or run `setup.bat` in CMD/PowerShell).
   * This automatically downloads and configures embedded Python 3.12, portable FFmpeg, portable TinyTeX, and Manim into `portable_env\`.
2. **Render Animation:**
   * **Drag and drop** any `.py` animation file onto **`render.bat`**, or run:
     ```cmd
     render.bat model\scene_01_basics.py
     ```
   * Select your render quality from the prompt (1-4).
3. **Clean Media Artifacts:**
   * Double-click **`clean.bat`** to purge generated video cache and reclaim disk space.

---

## 🎬 Render Quality Presets

| Choice | Flag | Resolution | Frame Rate | Intended Use |
| :---: | :---: | :---: | :---: | :--- |
| **1** | `-pql` | 480p (854×480) | 15 fps | Rapid prototyping & preview |
| **2** | `-pqm` | 720p (1280×720) | 30 fps | Balanced review & testing |
| **3** | `-pqh` | 1080p (1920×1080) | 60 fps | High-definition YouTube export |
| **4** | `-pqk` | 4K (3840×2160) | 60 fps | Ultra-HD production export |

---

## 📁 Repository Structure

```text
Manim-Animation-Workflow/
├── assets/                # Images, audio, and branding assets
│   └── manim-image.png
├── model/                 # Animation scripts
│   ├── scene_01_basics.py     # Intro text, shapes, morphing transforms
│   ├── scene_02_math.py       # LaTeX formulas (Euler's identity, graphs)
│   ├── scene_03_animation.py  # Movement, updaters, camera zoom
│   ├── scene_04_comparison.py # Comparative animations
│   ├── scene_05_image.py      # Image placement & animations
│   ├── scene_06_loop.py       # Continuous loops
│   └── run.md                 # Detailed scene guide
├── setup.sh / setup.bat   # Automated environment setup (Linux / Windows)
├── render.sh / render.bat # One-click renderers (Linux / Windows)
├── clean.sh / clean.bat   # Disk cleanup scripts (Linux / Windows)
└── portable_env/          # Self-contained Python and LaTeX environment (git-ignored)
```

---

## 🧪 Included Scenes

- `scene_01_basics.py`: `HelloWorld`, `ShapesDemo`, `TransformDemo`
- `scene_02_math.py`: `EquationScene`, `GraphScene`, `NumberLineScene`
- `scene_03_animation.py`: `MovementDemo`, `ColorAndOpacity`, `Updaters`, `CameraZoom`
- `scene_04_comparison.py`: Comparative algorithms & visualizations
- `scene_05_image.py`: External assets & SVGs
- `scene_06_loop.py`: Seamless looping animations
