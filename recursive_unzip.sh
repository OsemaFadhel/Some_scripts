#!/usr/bin/env bash

# Unzip files in sequence until no more zip files remain
while ls *.zip 1> /dev/null 2>&1; do
  for file in *.zip; do
    echo "Extracting ${file}…"
    unzip -q "$file"
    rm "$file" # Remove the zip file after extraction
  done
done

#concatenates all strings
#ls chunk_*.txt | sort -V | xargs cat > full_base64.txt
ls {fileextracted_}*.txt | sort -V | xargs cat > {filename}.txt

echo "Extraction completed."

