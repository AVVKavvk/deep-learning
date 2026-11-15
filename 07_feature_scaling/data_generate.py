import argparse
import pandas as pd
import numpy as np

# Set up the argument parser to take N from the command line
parser = argparse.ArgumentParser(description="Generate synthetic CSV data.")
parser.add_argument("N", type=int, help="Number of data rows to generate")
args = parser.parse_args()

# Extract N from the parsed arguments
N = args.N

# Generate random data for each column
ages = np.random.randint(18, 101, size=N)
salaries = np.random.randint(5000, 10000001, size=N)
purchased = np.random.choice([0, 1], size=N)

# Create a DataFrame
df = pd.DataFrame({
    'Age': ages,
    'EstimatedSalary': salaries,
    'Purchased': purchased
})

# Save the DataFrame to a CSV file
df.to_csv('synthetic_data.csv', index=False)

print(f"Successfully generated {N} rows and saved to 'synthetic_data.csv'.")
