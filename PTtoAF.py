#!/usr/bin/env python3

import sys
import pandas as pd

if len(sys.argv) != 3:
    print("Usage: python3 rename_csv_columns.py input.csv output.csv")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

column_renames = {
    "Target": "Affected Asset",
    "Risk level": "Vulnerability Priority",
    "Vulnerability name": "Vulnerability Title",
    "Vulnerability description": "Vulnerability Description",
    "Recommendation": "Vulnerability Remediation Recommendation",
    "How to reproduce": "Vulnerability Proof of Concept"
}

try:
    df = pd.read_csv(input_file)
except Exception as e:
    print(f"Error reading {input_file}: {e}")
    sys.exit(1)

df.rename(columns=column_renames, inplace=True)

if "Vulnerability Proof of Concept" not in df.columns:
    df["Vulnerability Proof of Concept"] = "N/A"
else:
    df["Vulnerability Proof of Concept"] = df["Vulnerability Proof of Concept"].fillna("N/A").replace(r'^\s*$', 'N/A', regex=True)

df["Vulnerability Attack Scenario"] = "N/A"

try:
    df.to_csv(output_file, index=False)
    print(f"CSV processed and saved to: {output_file}")
except Exception as e:
    print(f"Error writing to {output_file}: {e}")
    sys.exit(1)
