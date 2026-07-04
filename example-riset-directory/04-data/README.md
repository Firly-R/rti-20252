# 04-data

Data mentah hasil pengujian (simulasi probabilitas) — output dari **Tahap 3**, input untuk **Tahap 4**.

## Isi yang diharapkan

- Hasil simulasi komparasi *Fixed Probability* vs *Weighted Probability* dalam format CSV, untuk 10 kali run (masing-masing 100.000 responden) menggunakan *seed* yang berbeda.
- Metadata eksekusi tiap run (skenario, parameter dasar, seed, status, dan penamaan file keluaran).

## Berkas

- `hasil_simulasi_gacha_1.csv` sampai `hasil_simulasi_gacha_10.csv` — Raw dataset simulasi (1 juta iterasi).
- `metadata-eksekusi.md` — Log metadata dan konfigurasi eksprimen per run.

## Catatan

Data di folder ini bersifat mentah (raw) dan belum diolah. Hasil olahan (statistik agregat, grafik) disimpan di [../06-output/](../06-output/).
