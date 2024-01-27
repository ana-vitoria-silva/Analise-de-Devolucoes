# Programming Logic

# Step 0 - Understand the challenge you want to solve

# Step 1 - Iterate through all files in the base data folder (Sales Folder)

import os
import pandas as pd

files_list = os.listdir("Curso Básico de Python\Vendas")
for file in files_list:
    print(file)

# Step 2 - Import the sales databases

for file in files_list:
    if "Vendas" in file:
        print(f"Curso Básico de Python/Vendas/{file}")

# Step 3 - Process/Compile the databases

# Step 4 - Calculate the best-selling product (in quantity)

# Step 5 - Calculate the highest-grossing product (in revenue)

# Step 6 - Calculate the store/city that generated the most sales (in revenue) - create a chart/dashboard
