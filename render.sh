#!/bin/bash
set -e

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_PATH="$ROOT/portable_env"
MEDIA_OUTPUT_DIR="$ROOT/rendered_animations"

if [ ! -d "$VENV_PATH" ]; then
    echo "Error: portable_env not found. Please run ./setup.sh first."
    exit 1
fi

# Locate TinyTeX binaries dynamically if installed
TINYTEX_BIN=""
TLMGR_PATH=$(find "$VENV_PATH" -type f -name tlmgr 2>/dev/null | head -n 1)
if [ -n "$TLMGR_PATH" ]; then
    TINYTEX_BIN="$(dirname "$TLMGR_PATH")"
    export PATH="$VENV_PATH/bin:$TINYTEX_BIN:$PATH"
else
    export PATH="$VENV_PATH/bin:$PATH"
fi

if [ -z "$1" ]; then
    echo "Usage: ./render.sh <path_to_py_file> [SceneName] [quality_flag]"
    echo "Example: ./render.sh model/scene_01_basics.py HelloWorld"
    exit 1
fi

FILE="$1"
shift

# Check if quality flag was provided as an option (-ql, -qm, -qh, -q2k, -qk)
flag=""
PASSED_ARGS=()
for arg in "$@"; do
    case "$arg" in
        -ql|-pql) flag="-pql" ;;
        -qm|-pqm) flag="-pqm" ;;
        -qh|-pqh) flag="-pqh" ;;
        -q2k|-pq2k) flag="-r 2560,1440 --fps 60 -p" ;;
        -qk|-pqk) flag="-pqk" ;;
        *) PASSED_ARGS+=("$arg") ;;
    esac
done

if [ -z "$flag" ]; then
    echo ""
    echo "========================================"
    echo "  MANIM STUDIO RENDERER (LINUX + NVIDIA)"
    echo "========================================"
    echo " [1] Low Quality       (480p,  15 fps) - Fast preview"
    echo " [2] Medium Quality    (720p,  30 fps) - Draft"
    echo " [3] High Quality      (1080p, 60 fps) - Standard HD"
    echo " [4] 2K Quality [DEF]  (1440p, 60 fps) - Recommended / High Detail"
    echo " [5] 4K Quality        (2160p, 60 fps) - Production / UHD"
    echo "========================================"
    echo ""

    read -p "Choose quality (1-5) [Default is 4 (1440p 60fps)]: " choice
    case "$choice" in
        1) flag="-pql" ;;
        2) flag="-pqm" ;;
        3) flag="-pqh" ;;
        5) flag="-pqk" ;;
        *) flag="-r 2560,1440 --fps 60 -p" ;;
    esac
fi

# NVIDIA GPU Acceleration via prime-run
RUNNER=""
if command -v prime-run &> /dev/null; then
    RUNNER="prime-run"
    echo "⚡ NVIDIA GPU Acceleration active (via prime-run on RTX 2050)"
fi

mkdir -p "$MEDIA_OUTPUT_DIR"

echo ""
echo "Rendering $FILE with flag $flag ${PASSED_ARGS[*]}..."
echo "Media output directory: $MEDIA_OUTPUT_DIR"
echo ""

$RUNNER "$VENV_PATH/bin/python" -m manim $flag --media_dir "$MEDIA_OUTPUT_DIR" "$FILE" "${PASSED_ARGS[@]}"

echo ""
echo "Done! Render saved in $MEDIA_OUTPUT_DIR"
