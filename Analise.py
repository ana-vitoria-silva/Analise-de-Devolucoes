# Programming Logic

# Step 0 - Understand the challenge you want to solve

# Step 1 - Iterate through all files in the base data folder (Sales Folder)

import os
import pandas as pd
import plotly.express as px

files_list = os.listdir("Curso Básico de Python\Vendas")
for file in files_list:
    print(file)

# Step 2 - Import the sales databases

# Create empty table for consolidated

table_df_consolidated = pd.DataFrame()

for file in files_list:

    # Have a if it has "Vendas" in the file name, then:

    if "Vendas" in file:

        # Import file

        table_df = pd.read_csv(f"Curso Básico de Python/Vendas/{file}")

        # Table df consolidated

        table_df_consolidated = table_df_consolidated._append(table_df)

# Step 3 - Process/Compile the databases

print(table_df_consolidated)

# Step 4 - Calculate the best-selling product (in quantity)

table_df_product = table_df_consolidated.groupby("Produto").sum()
table_df_product = table_df_product[["Quantidade Vendida"]].sort_values(by="Quantidade Vendida", ascending=False)
print(table_df_product)

# Step 5 - Calculate the highest-grossing product (in revenue)

table_df_consolidated["Faturamento"] = table_df_consolidated["Quantidade Vendida"] * \
                                       table_df_consolidated["Preco Unitario"]
table_df_revenue = table_df_consolidated.groupby("Produto").sum()
table_df_revenue = table_df_revenue[["Faturamento"]].sort_values(by="Faturamento", ascending=False)
print(table_df_revenue)

# Step 6 - Calculate the store/city that generated the most sales (in revenue) - create a chart/dashboard

table_df_store = table_df_consolidated.groupby("Loja").sum()
table_df_store = table_df_store[["Faturamento"]].sort_values(by="Faturamento", ascending=False)
print(table_df_store)

chart = px.bar(table_df_store, x=table_df_store.index, y="Faturamento")
chart.show()