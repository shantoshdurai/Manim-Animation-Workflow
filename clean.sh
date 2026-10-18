#!/bin/bash
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"

echo "Calculating size and cleaning up Manim rendered media folders..."

# Find all 'media' and 'rendered_animations' directories, excluding portable_env
MEDIA_FOLDERS=$(find . -path "./portable_env" -prune -o -type d \( -name "media" -o -name "rendered_animations" \) -print)

if [ -z "$MEDIA_FOLDERS" ]; then
    echo "No media or rendered animation folders found. Everything is already clean!"
else
    TOTAL_BYTES=$(find $MEDIA_FOLDERS -type f -exec stat -c %s {} + 2>/dev/null | awk '{s+=$1} END {print s}')
    if [ -z "$TOTAL_BYTES" ]; then TOTAL_BYTES=0; fi
    TOTAL_MB=$(awk -v b="$TOTAL_BYTES" 'BEGIN {printf "%.2f", b / 1048576}')
    
    for folder in $MEDIA_FOLDERS; do
        echo -e "\e[36mCleaning up: $folder\e[0m"
        rm -rf "$folder"
    done
    echo ""
    echo -e "\e[32mCleanup complete! You just saved $TOTAL_MB MB of space.\e[0m"
fi
