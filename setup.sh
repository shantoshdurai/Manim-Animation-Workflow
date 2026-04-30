#!/bin/bash
echo "========================================"
echo "  MANIM PORTABLE STUDIO SETUP (LINUX)"
echo "========================================"

ROOT="$(pwd)"
ENV_DIR="$ROOT/portable_env"

echo "Creating Python virtual environment..."
python3 -m venv "$ENV_DIR"

echo "Installing Manim Community..."
"$ENV_DIR/bin/pip" install manim

echo "Checking for system dependencies..."
if ! command -v ffmpeg &> /dev/null; then
    echo -e "\e[33mWarning: ffmpeg is not installed. Manim requires ffmpeg to render videos.\e[0m"
    echo -e "Please install it using: \e[36msudo pacman -S ffmpeg\e[0m"
fi

if [ ! -d "$ENV_DIR/tinytex" ]; then
    echo "Downloading and installing TinyTeX (LaTeX)..."
    export TINYTEX_DIR="$ENV_DIR/tinytex"
    mkdir -p "$TINYTEX_DIR"
    wget -qO- "https://yihui.org/tinytex/install-bin-unix.sh" | sh
    
    echo "Installing required LaTeX packages..."
    export PATH="$ENV_DIR/tinytex/bin/x86_64-linux:$PATH"
    tlmgr install dvisvgm standalone preview doublestroke geometry amsmath
else
    echo "TinyTeX already installed."
fi

echo "========================================"
echo "  SETUP COMPLETE!"
echo "========================================"
echo "You can now use render.sh and clean.sh"
