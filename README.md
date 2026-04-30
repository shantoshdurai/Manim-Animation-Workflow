# Manim Animation Workflow 🎥

![Manim Logo](assets/manim-image.png)

Welcome to the **Manim Portable Studio**! This repository provides a self-contained environment for creating professional math and science animations using the Manim Community library. It works seamlessly across both Windows and Linux without requiring global system installations for dependencies like LaTeX.

---

## 🚀 Quick Start

First, clone this repository to your local machine.

### 🪟 Windows Setup & Usage

1. **Setup:** Double-click **`setup.bat`** (Only needed the first time). This sets up the Python environment, FFmpeg, and TinyTeX locally.
2. **Render:** **Drag and drop** any `.py` file from the `model/` folder onto **`render.bat`** to start rendering.
3. **Clean:** Run **`clean.bat`** to clear the `media/` folder and save disk space.

### 🐧 Linux Setup & Usage

1. **Setup:** Run **`./setup.sh`** from your terminal (Only needed the first time). This will create a Python virtual environment and configure TinyTeX locally. Make sure you have `ffmpeg` installed on your system (e.g. `sudo pacman -S ffmpeg`).
2. **Render:** Run **`./render.sh model/<your_animation_file>.py`** in your terminal. You will be prompted to select a render quality.
3. **Clean:** Run **`./clean.sh`** to wipe the generated `media/` artifacts.

---

## 📁 Repository Structure
*   `assets/`: Media files (images, sounds, etc.)
*   `model/`: Your Python animation scripts.
*   `portable_env/`: (Hidden) The self-contained Python and LaTeX tools.
