# WS-10: Experiment Execution & Data Collection

> **Bab 10 — Eksekusi Eksperimen & Pengumpulan Data**

---

## Ringkasan Materi

### Experiment Execution Pipeline

```
Design → Execution Plan → Controlled Execution → Data Collection → Data Logging → Dataset for Analysis
```

### Multiple Run = Non-Negotiable

Single run **tidak pernah cukup** untuk klaim ilmiah. Minimum 5-10 run per skenario dengan seed berbeda. Multiple run menghasilkan:
- Mean, std, confidence interval
- Distribusi hasil → uji statistik
- Variabilitas → error bar di grafik

### Execution Plan

Setiap eksperimen harus memiliki plan sebelum eksekusi:
- Daftar skenario
- Jumlah run per skenario
- Random seed per run (pre-determined!)
- Urutan eksekusi (randomisasi/counterbalancing)
- Pre-execution checklist

### Data Logging Komprehensif

Setiap run menghasilkan log terstruktur:
1. **Identitas** — Run ID, timestamp, skenario
2. **Konfigurasi** — Semua parameter, seed, code version
3. **Hasil** — Semua metrik, output detail
4. **Metadata** — Waktu eksekusi, resource usage, warning/error

Format: CSV/JSON/database — **bukan stdout yang di-copy-paste**.

### Engineering vs Research Execution

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Run | Sekali (deploy) | Multiple (min 5-10, seed berbeda) |
| Logging | Error log, access log | Semua parameter, metrik, metadata |
| Anomali | Bug → fix → redeploy | Investigasi → dokumentasi → analisis |
| Urutan | Tidak penting | Bisa bias — perlu randomisasi |

### Anomali = Dokumentasi, Bukan Hapus

Run gagal/anomali tidak boleh dihapus tanpa dokumentasi. Bisa jadi:
- **Bug** → fix & re-run (dokumentasikan!)
- **Batas kemampuan metode** → DNF = temuan
- **Data yang bias** jika hanya simpan run "berhasil"

### Jebakan Kognitif

1. "Satu angka cukup" → tanpa distribusi, tidak bisa diuji
2. "Seed tidak penting" → bahkan algoritma deterministik bisa dipengaruhi library stokastik
3. "Run gagal langsung hapus" → kehilangan temuan potensial
4. "Semua run harus hari ini" → thermal throttling, fatigue

---

## Latihan 1 — Execution Plan

Susun execution plan untuk eksperimen Anda. Tentukan skenario, jumlah run, dan seed sebelum eksekusi.

| Run # | Skenario | Seed | Parameter | Status | Waktu | Output File |
|-------|----------|------|-----------|--------|-------|-------------|
| 1 | Fixed vs Weighted | 42 | N=100.000, BP=0.6%, SP=50, HP=70 | Planned | TBD | hasil_simulasi_gacha_1.csv |
| 2 | Fixed vs Weighted | 123 | N=100.000, BP=0.6%, SP=50, HP=70 | Planned | TBD | hasil_simulasi_gacha_2.csv |
| 3 | Fixed vs Weighted | 999 | N=100.000, BP=0.6%, SP=50, HP=70 | Planned | TBD | hasil_simulasi_gacha_3.csv |
| 4 | Fixed vs Weighted | 2026 | N=100.000, BP=0.6%, SP=50, HP=70 | Planned | TBD | hasil_simulasi_gacha_4.csv |
| 5 | Fixed vs Weighted | 8888 | N=100.000, BP=0.6%, SP=50, HP=70 | Planned | TBD | hasil_simulasi_gacha_5.csv |
| 6 | Fixed vs Weighted | 111 | N=100.000, BP=0.6%, SP=50, HP=70 | Planned | TBD | hasil_simulasi_gacha_6.csv |
| 7 | Fixed vs Weighted | 2222 | N=100.000, BP=0.6%, SP=50, HP=70 | Planned | TBD | hasil_simulasi_gacha_7.csv |
| 8 | Fixed vs Weighted | 3333 | N=100.000, BP=0.6%, SP=50, HP=70 | Planned | TBD | hasil_simulasi_gacha_8.csv |
| 9 | Fixed vs Weighted | 4444 | N=100.000, BP=0.6%, SP=50, HP=70 | Planned | TBD | hasil_simulasi_gacha_9.csv |
| 10 | Fixed vs Weighted | 5555 | N=100.000, BP=0.6%, SP=50, HP=70 | Planned | TBD | hasil_simulasi_gacha_10.csv |

**Total skenario:** 2(kondisi A : Fixed Probability, Kondisi B : Weighted Probability
**Run per skenario:** 10
**Total run keseluruhan:** 10 (Mengeksekusi total 1.000.000 responden virtual per kondisi)

---

## Latihan 2 — Data Log Terstruktur

Desain format data log untuk eksperimen Anda. Tentukan field apa saja yang akan dicatat.

**Identitas:**
| Field | Contoh |
|-------|--------|
| Run ID | run-sim-001 |
| Timestamp | 2026-07-03T22:57:30 |
| Skenario | Komparasi Algoritma Gacha: Fixed vs Weighted |

**Konfigurasi:**
| Field | Contoh |
|-------|--------|
| Seed | 42 |
| Total sampel | 100000 |
| Base probability | 0.006 |
| Pity threshold | Soft pity = 50, Hard pity = 70
| Code version | v1.0-sim-prototype |

**Hasil:**
| Metrik | Tipe Data | Range Valid |
|--------|----------|-------------|
| Average Pulls to Rare (Fixed & Weighted) | Float | 1.0 – Tidak Terhingga (Fixed) / 1.0 - 70.0 (Weighted) |
| Cumulative Probability per Pull | Float | 0.0-100.0 |

**Format output:** [x] CSV / [ ] JSON / [ ] Database / [ ] Lainnya: ____
> (Data akan diekspor sebagai hasil_simulasi_gacha.csv yang memuat baris Pull_Ke, Cumulative_Probability_Fixed, dan Cumulative_Probability_Weighted).
---

## Latihan 3 — Anomaly Protocol

Rencanakan bagaimana menangani anomali. Untuk setiap jenis, tentukan langkah yang diambil.

| Jenis Anomali | Contoh | Tindakan |
|---------------|--------|----------|
| Run gagal (crash) | Memory Error (OOM) akibat list semua_data menampung >200.000 entri secara bersamaan dalam RAM. | Dokumentasi error. Lakukan optimasi kode (misal menggunakan generator atau memproses data langsung ke disk tanpa menyimpan raw array) dan ulangi run. |
| Hasil ekstrem | Sistem Weighted membutuhkan pull > 70 (Hard Pity) padahal probabilitas seharusnya 100%. | Hentikan eksperimen sementara. Lakukan debugging pada fungsi simulasikan_satu_rare_item untuk memverifikasi logika probabilitas_saat_ini = 1.0. Catat perubahan kode. |
| Waktu eksekusi anomali | Mesin pull simulator macet (infinite loop) pada kondisi fixed karena gagal acak RNG yang terus menerus. | Batasi limit iterasi (misal max pull = 1000 per orang untuk fixed), catat sebagai outlier, dan evaluasi fungsi random.random(). |
| Inkonsistensi dengan run lain | Kumulatif Fixed tiba-tiba lebih besar dari Weighted setelah Soft Pity. | Verifikasi persamaan matematika perhitungan bobot: BASE_PROBABILITY + (jumlah_pull - (SOFT_PITY - 1)) * (1.0 / sisa_pull). Lakukan re-run. |

**Prinsip:** Detect → Investigate → Document → Decide

---

## Refleksi

> Pernahkah Anda melaporkan hasil riset/tugas dari single run? Apa risikonya? Bagaimana multiple run mengubah kepercayaan terhadap hasil?

**Pengalaman sebelumnya:**
> Pada eksperimen simulasi atau pembuatan sistem terdahulu, pengujian sering kali hanya dilakukan satu kali (single run) asalkan program tidak error dan sudah menghasilkan satu output atau persentase keberhasilan.

**Yang akan dilakukan berbeda:**
> Simulasi probabilitas (gacha) sangat dipengaruhi oleh RNG (Random Number Generator). Mengandalkan single run sangat berisiko memunculkan bias kebetulan—bisa saja seed tertentu secara kebetulan memberikan rata-rata pull yang terlalu rendah atau terlalu tinggi. Ke depannya, saya akan selalu mengeksekusi minimal 5-10 run dengan seed yang berbeda, lalu mengambil nilai rata-rata dari seluruh komputasi tersebut untuk memastikan bahwa temuan terkait cumulative probability dapat dipertanggungjawabkan secara statistik.
