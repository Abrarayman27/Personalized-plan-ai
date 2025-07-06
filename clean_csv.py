import pandas as pd
import csv
import os

input_file = 'wellbeing_data.csv'
output_file = 'wellbeing_data_cleaned.csv'

# Define expected columns
columns = ['gad7', 'who5', 'cesdr10', 'loc', 'swls', 'scs', 'recommended_plan']

# Read CSV with error handling
try:
    data = []
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)  # Skip header
        for row in reader:
            # Handle rows with incorrect column counts
            if len(row) >= 7:
                # Take first 6 fields as numbers, combine rest as plan
                cleaned_row = row[:6] + [','.join(row[6:]).strip()]
                data.append(cleaned_row)
            else:
                print(f"Skipping invalid row: {row}")
    
    # Write cleaned data
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(columns)
        writer.writerows(data)
    
    print(f"Cleaned CSV saved as {output_file}")
    
    # Verify
    df = pd.read_csv(output_file)
    print("Cleaned data preview:")
    print(df.head())
    print(f"Number of rows: {len(df)}")
    print(f"Columns: {df.columns.tolist()}")

except Exception as e:
    print(f"Error: {e}")