#!/bin/bash
VENV_PATH="$(pwd)/portable_env"

if [ ! -d "$VENV_PATH" ]; then
    echo "Error: portable_env not found. Please run ./setup.sh first."
    exit 1
fi

export PATH="$VENV_PATH/bin:$VENV_PATH/tinytex/bin/x86_64-linux:$PATH"

if [ -z "$1" ]; then
    echo "Usage: ./render.sh <path_to_py_file>"
    exit 1
fi

echo ""
echo "========================================"
echo "  MANIM PORTABLE RENDERER (LINUX)"
echo "========================================"
echo " [1] Low Quality    (480p,  15 fps) - Fast"
echo " [2] Medium Quality (720p,  30 fps) - Balanced"
echo " [3] High Quality   (1080p, 60 fps) - YouTube"
echo " [4] 4K Quality     (2160p, 60 fps) - Best"
echo "========================================"
echo ""

read -p "Choose quality (1-4) [Default is 1]: " choice

case "$choice" in
    2) flag="-pqm" ;;
    3) flag="-pqh" ;;
    4) flag="-pqk" ;;
    *) flag="-pql" ;;
esac

echo ""
echo "Rendering $1 with $flag..."
python -m manim $flag "$1"
echo ""
echo "Done!"
