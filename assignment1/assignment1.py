import pandas as pd

# Read the CSV file
df = pd.read_csv('train.csv')

# Display the first 5 rows
print(df.head().to_markdown(index=False, numalign='left', stralign='left'))
