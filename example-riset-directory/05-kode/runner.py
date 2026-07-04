import os
import random
import gacha

def run_all_experiments():
    seeds = [42, 123, 999, 2026, 8888, 111, 2222, 3333, 4444, 5555]
    output_dir = r"d:\rti\rti-20252\example-riset-directory\04-data"
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for i, seed in enumerate(seeds, 1):
        print(f"=== RUN {i}: SEED {seed} ===")
        random.seed(seed)
        
        # Override the RANDOM_SEED variable just in case, though random.seed is what matters
        gacha.RANDOM_SEED = seed
        
        data_mentah = gacha.jalankan_eksperimen(gacha.TOTAL_SAMPEL)
        nama_file = os.path.join(output_dir, f"hasil_simulasi_gacha_{i}.csv")
        gacha.analisis_dan_ekspor_csv(data_mentah, gacha.TOTAL_SAMPEL, nama_file=nama_file)
        print(f"Saved to {nama_file}\n")

if __name__ == "__main__":
    run_all_experiments()
