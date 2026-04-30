#!/bin/bash
echo "Calculating size and cleaning up Manim media folders..."

# Find all 'media' directories, excluding portable_env
MEDIA_FOLDERS=$(find . -path "./portable_env" -prune -o -type d -name "media" -print)

if [ -z "$MEDIA_FOLDERS" ]; then
    echo "No media folders found. Everything is already clean!"
else
    TOTAL_BYTES=$(find $MEDIA_FOLDERS -type f -exec stat -c %s {} + 2>/dev/null | awk '{s+=$1} END {print s}')
    if [ -z "$TOTAL_BYTES" ]; then TOTAL_BYTES=0; fi
    TOTAL_MB=$(echo "scale=2; $TOTAL_BYTES / 1048576" | bc -l)
    
    for folder in $MEDIA_FOLDERS; do
        echo -e "\e[36mCleaning up: $folder\e[0m"
        rm -rf "$folder"
    done
    echo ""
    echo -e "\e[32mCleanup complete! You just saved $TOTAL_MB MB of space.\e[0m"
fi
