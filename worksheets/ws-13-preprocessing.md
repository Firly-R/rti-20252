# WS-13: Data Preprocessing

> **Bab 13 — Preprocessing & Persiapan Data untuk Analisis**

---

## Ringkasan Materi

### Data Refinement Pipeline

```
Raw Data → Cleaning → Transformation → Normalization → Processed Data → Analysis Ready
```

Setiap tahap memiliki tujuan berbeda. **Preprocessing bukan langkah teknis biasa** — setiap keputusan preprocessing adalah keputusan riset yang bisa mengubah kesimpulan.

### Empat Prinsip Preprocessing

| Prinsip | Deskripsi |
|---------|----------|
| **Consistency** | Metode sama untuk data yang sama |
| **Transparency** | Setiap langkah terdokumentasi |
| **Reproducibility** | Orang lain bisa mengulang dengan hasil sama |
| **Minimal Distortion** | Ubah sesedikit mungkin; jika normalisasi tidak perlu, jangan lakukan |

### Cleaning Triad

| Masalah | Strategi | Risiko |
|---------|---------|--------|
| **Missing values** | | |
| — Listwise deletion | Missing < 5%, random | Data loss |
| — Mean/median imputation | Sedikit missing, dist. normal | Mengurangi variabilitas |
| — Model-based imputation | Banyak missing, pola sistematis | Introduces dependency |
| — Flag & separate | Missing karena alasan substantif | Kompleksitas analisis |
| **Duplikat** | Identifikasi → verifikasi → hapus | False positive (data mirip ≠ duplikat) |
| **Error format** | Standardisasi tipe, encoding | Kehilangan informasi saat konversi |

### Normalisasi — Kapan & Metode Mana

| Metode | Formula | Output | Sensitif Outlier? |
|--------|---------|--------|-------------------|
| Min-max | (x-min)/(max-min) | [0, 1] | Ya |
| Z-score | (x-mean)/std | Unbounded | Lebih robust |
| Robust scaling | (x-median)/IQR | Unbounded | Paling robust |

**Kunci:** Parameter normalisasi harus dihitung dari **training set saja** — bukan seluruh data. Pelanggaran = **data leakage**.

### Data Leakage Prevention

Data leakage terjadi ketika informasi dari test set "bocor" ke preprocessing:
- Normalisasi parameter dari seluruh dataset ← **SALAH**
- Cross-validation dilakukan sebelum split ← **SALAH**
- Feature selection menggunakan label test set ← **SALAH**

### Jebakan Kognitif

1. "Preprocessing cuma teknis — tidak perlu detail" → bisa ubah kesimpulan
2. "Lebih banyak preprocessing = lebih bersih = lebih baik" → over-processing distorsi data
3. "Normalisasi selalu diperlukan" → belum tentu, tergantung metode analisis
4. "Imputation sama untuk semua situasi" → strategi harus sesuai konteks

---

## Template A.13 — Preprocessing Documentation Log

```
PREPROCESSING LOG

Dataset           : hasil_simulasi_gacha.csv
Jumlah data awal  : 70 baris x 3 kolom (Mewakili milestone pull 1 hingga 70 dari 100.000 iterasi)

Cleaning:
| Masalah | Jumlah Kasus | Penanganan | Justifikasi |
|---------|-------------|------------|-------------|
| Missing | 0           | Tidak ada  | Data dihasilkan secara deterministik oleh engine Python RNG. |
| Duplikat| 0           | Tidak ada  | Iterasi `Pull_Ke` dieksekusi secara sekuensial (1-70) tanpa pengulangan loop log. |
| Error   | 0           | Tidak ada  | Tipe data telah dipaksa menjadi `integer` dan `float` sejak kompilasi script[cite: 3]. |

Transformation:
| Transformasi | Variabel | Detail | Alasan |
|-------------|----------|--------|--------|
| Pembulatan  | Cumulative_Probability | Dibulatkan ke 4 angka di belakang koma (round(val, 4))[cite: 3] | Memudahkan visualisasi grafik analisis tanpa mengorbankan tingkat presisi yang signifikan[cite: 3]. |

Normalization:
  Metode    : Tidak diterapkan
  Alasan    : Eksperimen ini mengukur metrik probabilitas murni (0% - 100%) dan perhitungan frekuensi absolut (pull 1-70), bukan melatih model Machine Learning berbasis jarak (distance-based).
  Parameter : N/A

Leakage Check:
  [X] Parameter normalisasi dari training set saja (N/A - Bukan riset ML prediktif)
  [X] Tidak ada informasi test set dalam preprocessing (N/A)
  [X] Cross-validation dilakukan setelah split (N/A)

Jumlah data akhir : 70 baris[cite: 3]
Script tersedia   : [X] Ya → path: gacha.py | [ ] Belum
```

---

## Latihan 1 — Cleaning Plan

Periksa dataset Anda (atau dataset contoh) dan dokumentasikan masalah yang ditemukan.

| Masalah | Jumlah Kasus | Penanganan | Justifikasi |
|---------|-------------|------------|-------------|
| Missing values (NaN/Null) | 0 dari 70 (0%) | Tidak ada tindakan | Data sintetis 100.000 sampel digenerasi sempurna oleh perulangan komputasi tertutup. |
| Outlier ekstrem | 0 kasus | Tidak ada tindakan | Sistem diikat oleh parameter HARD_PITY = 70, sehingga tidak ada nilai penarikan yang melebihi batas ini. |
| Kesalahan format tipe data | 0 kasus | Standardisasi otomatis | Library csv di Python menangani konversi tipe data memori menjadi teks secara seragam. |

**Jumlah data sebelum cleaning:** 70 Baris
**Jumlah data setelah cleaning:** 70 Baris
**Persentase data yang hilang/berubah:** 0%

---

## Latihan 2 — Normalisasi Decision

Tentukan apakah data Anda perlu normalisasi, dan jika ya, metode apa yang tepat.

| Variabel | Range Asli | Distribusi | Outlier? | Metode Normalisasi | Alasan |
|----------|-----------|-----------|----------|-------------------|--------|
| *Pull_Ke* | 1-70 | *Sekuensial / Linear* | *Tidak* | *Tidak perlu* | *Merupakan variabel urutan (indeks) absolut penarikan ke-n, mengubah skalanya akan menghilangkan konteks iterasi.* |
| *Cumulative_Probability_Fixed* | *0.0-100.0* | *Monotonik Naik* | *Tidak* | *Tidak perlu* | *Sudah berada dalam bentuk persentase probabilitas kumulatif bawaan (sudah terikat di skala 0-100).* || | | | | | |
| *Cumulative_Probability_Weighted* | *0.0-100.0* | *Eksponensial Terakselerasi* | *Tidak* | *Tidak perlu* | *Mencapai 100% tepat pada pull ke-70; tidak perlu diubah karena metrik ini adalah output inti eksperimen.* |

**Apakah normalisasi diperlukan?** [ ] Ya / [x] Tidak
**Justifikasi:**
> Seluruh variabel yang direkam (sekuens pull dan persentase keberhasilan kumulatif) memiliki makna interpretatif langsung[cite: 3]. Melakukan Z-score atau Min-Max scaling justru akan mendistorsi (over-processing) informasi probabilitas gacha menjadi angka arbitrer yang tidak bisa dibaca oleh pengamat.

**Leakage check:**
- [x] Parameter dihitung dari training set saja
- [x] Normalisasi diterapkan setelah train-test split

---

## Latihan 3 — Preprocessing Report

Buat ringkasan preprocessing lengkap — dokumentasi yang cukup bagi orang lain untuk mereplikasi.

```
PREPROCESSING SUMMARY

1. Dataset: hasil_simulasi_gacha.csv (Log hasil simulasi 100.000 agen virtual)
2. Data awal: 70 records, 3 features (Pull_Ke, Cum. Prob Fixed, Cum. Prob Weighted)
3. Cleaning:
   - Missing values: 0 kasus, metode: Bypass (Data komputasional bebas degradasi)
   - Duplikat: 0 kasus, tindakan: Bypass
   - Error: 0 kasus, tindakan: Bypass
4. Transformation: Pembulatan (rounding) float probabilitas hingga 4 desimal di level script Python sebelum ekspor
5. Normalisasi: Tidak diterapkan (metode), parameter dari N/A
6. Data akhir: 70 records, 3 features
7. Leakage check: [X] Lulus / [ ] Ada masalah
```

---

## Refleksi

> Apakah Anda pernah melakukan normalisasi "karena biasa dilakukan" tanpa mempertimbangkan apakah benar-benar diperlukan? Apa risiko over-preprocessing?

> Banyak literatur yang menyarankan normalisasi data secara membabi buta. Risiko terbesar dari over-preprocessing adalah hilangnya interpretabilitas metrik. Dalam kasus simulasi ini, jika persentase peluang keberhasilan (0% - 100%) diubah menjadi skala Z-score (misalnya -1.5 hingga 2.3), kita tidak bisa lagi menyimpulkan secara gamblang "pada pull ke-50, peluang pemain mendapatkan item adalah sekian persen. Keputusan untuk membiarkan data dalam bentuk naturalnya adalah langkah untuk mematuhi prinsip Minimal Distortion.
