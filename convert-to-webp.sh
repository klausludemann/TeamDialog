#!/bin/bash

# WebP Image Conversion Script for TeamDialog
echo "=========================================="
echo "TeamDialog - WebP Image Converter"
echo "=========================================="
echo ""

cd /Users/klausludemann/Documents/GitHub/TeamDialog/docs

echo "Converting images to WebP format..."
echo ""

converted=0

# Convert JPG images
for img in $(find wp-content/uploads -name "*.jpg" -o -name "*.jpeg"); do
    webp_name="${img%.*}.webp"
    if [ -f "$webp_name" ]; then
        continue
    fi
    
    cwebp -q 85 "$img" -o "$webp_name" &> /dev/null
    echo "✓ Converted: $(basename "$img")"
    ((converted++))
done

# Convert PNG images
for img in $(find wp-content/uploads -name "*.png"); do
    webp_name="${img%.*}.webp"
    if [ -f "$webp_name" ]; then
        continue
    fi
    
    cwebp -q 85 "$img" -o "$webp_name" &> /dev/null
    echo "✓ Converted: $(basename "$img")"
    ((converted++))
done

echo ""
echo "=========================================="
echo "✅ Conversion complete!"
echo "Converted: $converted images"
echo "=========================================="
