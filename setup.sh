#!/bin/bash
set -e

echo "========================================"
echo "  MANIM PORTABLE STUDIO SETUP (LINUX)"
echo "========================================"

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ENV_DIR="$ROOT/portable_env"

echo "Project root: $ROOT"
echo "Environment directory: $ENV_DIR"

# Check system dependencies
echo "Checking system dependencies..."
if ! command -v ffmpeg &> /dev/null; then
    echo -e "\e[33mWarning: ffmpeg is not installed. Manim requires ffmpeg to render videos.\e[0m"
    echo -e "Please install it using: \e[36msudo pacman -S ffmpeg\e[0m"
else
    echo "✓ ffmpeg is available."
fi

# Create virtual environment
if [ ! -d "$ENV_DIR" ]; then
    echo "Creating Python virtual environment in portable_env..."
    python3 -m venv "$ENV_DIR"
else
    echo "Python virtual environment already exists in portable_env."
fi

echo "Upgrading pip, setuptools, and wheel..."
"$ENV_DIR/bin/pip" install --upgrade pip setuptools wheel

echo "Installing Manim Community library..."
"$ENV_DIR/bin/pip" install manim

# TinyTeX setup for LaTeX formulas (MathTex)
if [ ! -d "$ENV_DIR/tinytex" ]; then
    echo "Downloading and installing self-contained TinyTeX (LaTeX)..."
    export TINYTEX_DIR="$ENV_DIR/tinytex"
    mkdir -p "$TINYTEX_DIR"
    curl -sL "https://tinytex.yihui.org/install-bin-unix.sh" | sh
else
    echo "TinyTeX directory already present."
fi

# Locate TinyTeX binaries dynamically
TLMGR_PATH=$(find "$ENV_DIR" -type f -name tlmgr 2>/dev/null | head -n 1)
if [ -n "$TLMGR_PATH" ]; then
    TLMGR_BIN_DIR="$(dirname "$TLMGR_PATH")"
    export PATH="$TLMGR_BIN_DIR:$PATH"
    echo "TinyTeX binaries located at: $TLMGR_BIN_DIR"
    echo "Installing required LaTeX packages for Manim (standalone, preview, etc.)..."
    "$TLMGR_PATH" install dvisvgm standalone preview doublestroke geometry amsmath fundus-calligra wasysym microtype || true
else
    echo "Warning: TinyTeX bin directory could not be located."
fi

echo ""
echo "========================================"
echo "  SETUP COMPLETE!"
echo "========================================"
echo "You can now run:"
echo "  ./render.sh model/scene_01_basics.py"
echo "  ./clean.sh"
echo "========================================"
