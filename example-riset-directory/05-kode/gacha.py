import random
import csv
from collections import Counter

# ==========================================================
# KONFIGURASI PARAMETER PENELITIAN (BISA KAMU UBAH DI SINI)
# ==========================================================
TOTAL_SAMPEL = 100000      # Jumlah responden/pemain virtual
BASE_PROBABILITY = 0.006   # Probabilitas dasar 0.6%
SOFT_PITY = 50             # Pull tempat probabilitas mulai berbobot/naik
HARD_PITY = 70             # Batas maksimal jaminan dapat rare item (Pity Threshold)

RANDOM_SEED = 42           
random.seed(RANDOM_SEED)   
# ==========================================================

def simulasikan_satu_rare_item(mode):
    """
    Simulasi proses pull menggunakan parameter global di atas.
    """
    jumlah_pull = 0
    
    while True:
        jumlah_pull += 1
        
        if mode == "fixed":
            probabilitas_saat_ini = BASE_PROBABILITY
            
        elif mode == "weighted":
            if jumlah_pull < SOFT_PITY:
                probabilitas_saat_ini = BASE_PROBABILITY
            elif SOFT_PITY <= jumlah_pull < HARD_PITY:
                sisa_pull = HARD_PITY - SOFT_PITY
                probabilitas_saat_ini = BASE_PROBABILITY + (jumlah_pull - (SOFT_PITY - 1)) * (1.0 / sisa_pull)
            else:
                probabilitas_saat_ini = 1.0
                
        if random.random() < probabilitas_saat_ini:
            return jumlah_pull

def jalankan_eksperimen(total_responden):
    kondisi_eksperimen = ["fixed", "weighted"]
    semua_data = {}
    
    print("=" * 60)
    print(f"MEMULAI SIMULASI GACHA ({total_responden} RESPONDEN VIRTUAL)")
    print("=" * 60)
    
    for mode in kondisi_eksperimen:
        print(f"-> Menghitung log data untuk kondisi: {mode.upper()}...")
        data_pull = [simulasikan_satu_rare_item(mode) for _ in range(total_responden)]
        semua_data[mode] = data_pull
        
    return semua_data

def analisis_dan_ekspor_csv(data, total_responden, nama_file="hasil_simulasi_gacha.csv"):
    rata_fixed = sum(data["fixed"]) / total_responden
    rata_weighted = sum(data["weighted"]) / total_responden
    
    hitung_fixed = Counter(data["fixed"])
    hitung_weighted = Counter(data["weighted"])
    
    kumulatif_fixed_persen = 0.0
    kumulatif_weighted_persen = 0.0
    
    baris_csv = []
    
    print("\n" + "=" * 60)
    print("HASIL ANALISIS STATISTIK DESKRIPTIF")
    print("=" * 60)
    print(f"Rata-rata Pull Kondisi A (Fixed)   : {rata_fixed:.2f} pull")
    print(f"Rata-rata Pull Kondisi B (Weighted): {rata_weighted:.2f} pull")
    print("-" * 60)
    print(f"{'Pull Ke-':<10}{'Cum. Prob Fixed':<22}{'Cum. Prob Weighted':<22}")
    print("-" * 60)
    
    for pull in range(1, HARD_PITY + 1):
        kumulatif_fixed_persen += (hitung_fixed[pull] / total_responden) * 100
        kumulatif_weighted_persen += (hitung_weighted[pull] / total_responden) * 100
        
        milestone = [1, 10, 30, 50, SOFT_PITY, (SOFT_PITY + HARD_PITY)//2, HARD_PITY]
        if pull in milestone:
            print(f"{pull:<10}{kumulatif_fixed_persen:.2f}%{'' : <12}{kumulatif_weighted_persen:.2f}%")
            
        baris_csv.append([
            pull, 
            round(kumulatif_fixed_persen, 4), 
            round(kumulatif_weighted_persen, 4)
        ])
        
    with open(nama_file, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Pull_Ke", "Cumulative_Probability_Fixed", "Cumulative_Probability_Weighted"])
        writer.writerows(baris_csv)
        
    print("-" * 60)
    print(f"SUKSES: Data penelitian berhasil diekspor ke '{nama_file}'")
    print("=" * 60)

if __name__ == "__main__":
    data_mentah = jalankan_eksperimen(TOTAL_SAMPEL)
    analisis_dan_ekspor_csv(data_mentah, TOTAL_SAMPEL)