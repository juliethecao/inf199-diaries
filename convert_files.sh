#!/bin/bash

# Iterate over the files from p1.csv to p30.csv, excluding p3.csv and p20.csv
for i in $(seq 1 30); do
  # Skip files p3.csv and p20.csv
  if [ "$i" -eq 3 ] || [ "$i" -eq 20 ]; then
    continue
  fi

  # Construct the file name
  filename="p${i}.csv"
  
  # Call the Python function with the file name as an argument
  python3 parse.py "$filename"
  
  # Check if the Python script executed successfully
  if [ $? -ne 0 ]; then
    echo "Error processing file $filename"
  else
    echo "Successfully processed file $filename"
  fi
done