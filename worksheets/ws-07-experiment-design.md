# WS-07: Experimental Design & Validity

> **Bab 7 — Experimental Design & Validity**

---

## Ringkasan Materi

### Correlation ≠ Causality

Kausalitas membutuhkan 3 syarat:
1. **Covariance** — X dan Y bergerak bersama
2. **Temporal precedence** — X berubah sebelum Y
3. **Elimination of alternatives** — Tidak ada faktor lain yang menjelaskan Y

Controlled experiment adalah satu-satunya metode yang bisa membuktikan kausalitas.

### Empat Jenis Validitas

| Jenis | Pertanyaan | Ancaman Umum |
|-------|-----------|-------------|
| **Internal** | Apakah hubungan IV→DV nyata? | Confounding variable, selection bias |
| **External** | Apakah bisa digeneralisasi? | Dataset terlalu spesifik |
| **Construct** | Apakah mengukur konsep yang benar? | Metrik tidak sesuai |
| **Conclusion** | Apakah kesimpulan statistik valid? | Sample size kecil, uji salah |

Internal dan external validity sering berkonflik: semakin terkontrol (internal kuat) → semakin artificial (external lemah).

### Tiga Tipe Eksperimen dalam Riset TI

| Tipe | Deskripsi | Kapan Digunakan |
|------|----------|----------------|
| **Comparison Study** | Metode A vs B pada kondisi identik | Membandingkan pendekatan berbeda |
| **Ablation Study** | Full system → lepas komponen satu per satu | Mengukur kontribusi tiap komponen |
| **Parameter Study** | Variasikan satu parameter, amati dampak | Uji sensitifitas/robustness |

### Fairness dalam Perbandingan

Perbandingan yang adil = **kondisi identik** untuk semua metode: dataset sama, preprocessing sama, tuning effort sebanding, environment sama, metrik sama.

Contoh tidak adil: Transformer (30 fitur tambahan + Bayesian optimization) vs RF (default params) → hasilnya misleading.

### Threats to Validity = Diidentifikasi Sebelum Eksperimen

Ancaman validitas harus diidentifikasi **sebelum** eksperimen dan mitigasinya dirancang sebagai bagian dari desain — bukan ditulis sebagai boilerplate setelah selesai.

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan testing | Memastikan sistem memenuhi requirement | Membuktikan hubungan kausal antar variabel |
| Baseline | Versi sebelumnya (last release) | Metode tervalidasi dari literatur |
| Kegagalan | Bug → fix → release | H₀ tidak ditolak → tetap kontribusi ilmiah |
| Sukses | 100% test pass | Evidence valid — mendukung atau menolak hipotesis |

### Istilah Penting

- **Causality** — Hubungan sebab-akibat (covariance + temporal + elimination)
- **Controlled Experiment** — Ubah satu variabel, kontrol sisanya, amati efek
- **Fairness** — Semua metode diuji pada kondisi yang benar-benar identik
- **Threats to Validity** — Faktor yang bisa melemahkan kesimpulan jika tidak dimitigasi
- **Conclusion Validity** — Validitas statistik: power, sample size, uji yang tepat

---

## A.7 — Desain Eksperimen Lengkap

## EXPERIMENT DESIGN

**Research Question** : Bagaimana algoritma Weighted Probability memengaruhi peluang memperoleh item rare pada sistem gacha game?

**Hypothesis**        : Algoritma Weighted Probability meningkatkan cumulative probability memperoleh item rare dibandingkan fixed probability.

**Tipe Eksperimen**   : 
- [ ] Comparison
- [x] Ablation
- [ ] Parameter

**Kondisi Eksperimen**:
| Kondisi | Deskripsi | IV Value | CV Settings |
|---------|-----------|----------|-------------|
| Control | Sistem fixed probability | Fixed Probability | Base probability 0.6%, pity threshold 90 |
| Treatment | Sistem weighted probability | Weighted Probability | Base probability 0.6%, pity threshold 90 |

**Fairness Checklist**:
  - [x] Dataset identik untuk semua kondisi
  - [x] Preprocessing setara
  - [x] Tuning effort setara
  - [x] Environment identik
  - [x] Metrik evaluasi sama

**Threat Analysis**:
| Threat Type | Ancaman Spesifik | Mitigasi |
|-------------|-----------------|----------|
| Internal | Perubahan parameter selain weighted probability | Mengunci seluruh control variable |
| External | Sistem simulasi tidak sepenuhnya merepresentasikan game asli | Menggunakan parameter umum pada game gacha modern |
| Construct | Cumulative probability tidak menggambarkan seluruh sistem gacha | Menambahkan jumlah pull sebagai secondary metric |
| Conclusion | Jumlah simulasi terlalu sedikit | Menggunakan banyak iterasi simulasi |

### Statistical Plan
  **Uji statistik**    : Perbandingan rata-rata cumulative probability
  
  **Justifikasi**      : Digunakan untuk melihat perbedaan probabilitas antar kondisi
  
  **Alpha**            : 0.05
  
  **Effect size min**  : 0.1


## Latihan 1 — Desain Eksperimen

Susun desain eksperimen berdasarkan RQ, variabel, dan sistem dari WS-04 sampai WS-06.

**RQ:** Bagaimana algoritma Weighted Probability memengaruhi peluang memperoleh item rare pada sistem gacha game?

**Tipe eksperimen:** 
- [ ] Comparison
- [x] Ablation
- [ ] Parameter

| Kondisi | Deskripsi | IV Value | CV Settings |
|---------|-----------|----------|-------------|
| Control | Sistem probabilitas tetap | Fixed Probability | Base probability 0.6%, pity threshold 90 |
| Treatment | Sistem weighted probability | Weighted Probability | Base probability 0.6%, pity threshold 90 |

---

## Latihan 2 — Fairness Checklist

Evaluasi apakah desain eksperimen di Latihan 1 sudah fair.

| Kriteria | Status | Detail |
|----------|--------|--------|
| Dataset identik | ✅ | Menggunakan simulasi pull yang sama |
| Preprocessing setara | ✅ | Tidak ada perbedaan preprocessing |
| Tuning effort setara | ✅ | Parameter selain IV dibuat sama |
| Environment identik | ✅ | Simulasi dijalankan pada sistem yang sama |
| Metrik evaluasi sama | ✅ | Menggunakan cumulative probability |


**Ada yang tidak fair?** 
- [ ] Ya
- [x] Tidak

---

## Latihan 3 — Threat Analysis

Identifikasi ancaman validitas untuk desain eksperimen ini.

| Threat Type | Ancaman Spesifik | Mitigasi |
|-------------|-----------------|----------|
| Internal | Parameter lain berubah selama eksperimen | Mengunci seluruh control variable |
| External | Simulasi berbeda dengan implementasi game asli | Menggunakan parameter dari sistem gacha modern |
| Construct | Metrik tidak cukup merepresentasikan algoritma | Menggunakan cumulative probability dan jumlah pull |
| Conclusion | Iterasi simulasi terlalu sedikit | Menambah jumlah simulasi |

---

**Ancaman mana yang paling sulit dimitigasi?** 
> External Validity

**Mengapa?**
> Karena sistem simulasi tidak dapat sepenuhnya merepresentasikan seluruh mekanisme pada game gacha asli.

---

## Refleksi

> Sebuah paper melaporkan "metode kami mengalahkan semua baseline." Apa 3 pertanyaan pertama yang harus diajukan untuk mengevaluasi klaim ini?

**Jawaban:**
1. Apakah semua metode diuji pada kondisi yang sama?
2. Apakah baseline yang digunakan relevan dan berasal dari literatur terpercaya?
3. Apakah metrik evaluasi dan jumlah eksperimen sudah valid?
