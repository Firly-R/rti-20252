import os
import glob
import pandas as pd
import matplotlib.pyplot as plt

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, '04-data')
OUT_DIR = os.path.join(BASE_DIR, '06-output')
TABLES_DIR = os.path.join(OUT_DIR, 'tables')
FIGURES_DIR = os.path.join(OUT_DIR, 'figures')

os.makedirs(TABLES_DIR, exist_ok=True)
os.makedirs(FIGURES_DIR, exist_ok=True)

# Find all CSV files
csv_files = glob.glob(os.path.join(DATA_DIR, 'hasil_simulasi_gacha_*.csv'))

# Read and aggregate
all_data = []
for file in csv_files:
    df = pd.read_csv(file)
    all_data.append(df)

if not all_data:
    print("No data found!")
    exit(1)

# Concatenate all dataframes and calculate mean
concat_df = pd.concat(all_data)
agg_df = concat_df.groupby('Pull_Ke').mean().reset_index()

# Save aggregated stats to CSV
out_csv = os.path.join(TABLES_DIR, 'aggregated_stats.csv')
agg_df.to_csv(out_csv, index=False)
print(f"Saved aggregated stats to {out_csv}")

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(agg_df['Pull_Ke'], agg_df['Cumulative_Probability_Fixed'], label='Fixed Probability', marker='o', markersize=3)
plt.plot(agg_df['Pull_Ke'], agg_df['Cumulative_Probability_Weighted'], label='Weighted Probability (Pity System)', marker='s', markersize=3)
plt.axvline(x=50, color='r', linestyle='--', alpha=0.5, label='Soft Pity (50)')
plt.axvline(x=70, color='g', linestyle='--', alpha=0.5, label='Hard Pity (70)')
plt.title('Cumulative Probability to Get Rare Item: Fixed vs Weighted')
plt.xlabel('Number of Pulls')
plt.ylabel('Cumulative Probability (%)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()

out_fig = os.path.join(FIGURES_DIR, 'fig_cumulative_probability.png')
plt.savefig(out_fig, dpi=300)
print(f"Saved figure to {out_fig}")
