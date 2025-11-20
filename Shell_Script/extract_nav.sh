#!/bin/bash

URL="https://portal.amfiindia.com/spages/NAVAll.txt"
OUTPUT="nav_data.tsv"

echo -e "Scheme_Name\tAsset_Value" > "$OUTPUT"

echo "Downloading NAV data..."

CONTENT=$(curl -s "$URL")

if [ -z "$CONTENT" ]; then
    echo "Failed to fetch data. Empty response."
    exit 1
fi

# Detect delimiter
SAMPLE_LINE=$(echo "$CONTENT" | grep -v '^#' | sed '/^\s*$/d' | head -n 1)

if [[ "$SAMPLE_LINE" == *"|"* ]]; then
    SEP="|"
elif [[ "$SAMPLE_LINE" == *";"* ]]; then
    SEP=";"
else
    echo "Unknown separator in NAV file"
    exit 1
fi

echo "Detected delimiter: '$SEP'"

# Extract Scheme Name (col 4) and NAV (col 5)
echo "$CONTENT" | awk -F"$SEP" '
    NF >= 5 && $0 !~ /^#/ {
        scheme=$4;
        nav=$5;
        gsub(/^[ \t]+|[ \t]+$/, "", scheme);
        gsub(/^[ \t]+|[ \t]+$/, "", nav);
        print scheme "\t" nav;
    }
' >> "$OUTPUT"

echo "Saved to $OUTPUT"
