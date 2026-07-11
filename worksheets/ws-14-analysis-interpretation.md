# WS-14: Analysis, Interpretation & Failure Analysis

> **Bab 14 — Analisis Data, Interpretasi & Failure Analysis**

---

## Ringkasan Materi

### Data → Knowledge Model

```
Data → Analysis → Interpretation → Explanation → Knowledge
```

Tiga level yang berbeda:
- **Analysis** — "Apa yang terjadi?" (deskriptif + inferensial)
- **Interpretation** — "Apa artinya?" (konteks RQ + literatur)
- **Failure Analysis** — "Mengapa tidak berhasil?" (boundary conditions)

### Beyond p-value

**Statistical significance ≠ practical significance.** Selalu laporkan:
1. p-value (signifikansi statistik)
2. Effect size (besarnya efek)
3. Confidence interval (rentang ketidakpastian)

| Effect Size (Cohen's d) | Interpretasi |
|-------------------------|-------------|
| < 0.2 | Small |
| 0.2 – 0.8 | Medium |
| > 0.8 | Large |

### Pemilihan Uji Statistik

| Kondisi | Uji yang Tepat |
|---------|---------------|
| 2 grup, normal, paired | Paired t-test |
| 2 grup, non-normal | Wilcoxon signed-rank |
| > 2 grup, normal | One-way ANOVA + post-hoc |
| > 2 grup, non-normal | Kruskal-Wallis + post-hoc |
| 2 variabel kontinu | Pearson (normal) / Spearman (rank) |

### Failure Analysis as Contribution

Hipotesis yang ditolak adalah **temuan yang berharga**:

| Dataset | New (F1) | Baseline (F1) | p-value | Cohen's d |
|---------|---------|--------------|---------|-----------|
| DS-1 (small, clean) | 94.2±1.1 | 89.3±1.5 | <0.001 | **3.7** |
| DS-4 (medium, noisy) | 78.3±3.2 | 82.1±2.8 | 0.008 | **-1.3** |
| DS-5 (large, noisy) | 71.6±4.1 | 80.5±3.0 | <0.001 | **-2.5** |

**Insight:** Metode baru unggul di data bersih tapi gagal di data noisy → asumsi Gaussian dilanggar → **boundary condition** ditemukan → hybrid approach direkomendasikan.

**Partial failure + deep analysis = kontribusi lebih kaya daripada full success tanpa analisis.**

### Limitation Types

| Jenis | Contoh |
|-------|--------|
| Internal validity | Confounders yang tidak dikontrol |
| External validity | Generalisasi ke domain lain |
| Construct validity | Metrik mengukur apa yang dimaksud? |
| Statistical limitation | Sample size, asumsi distribusi |

### Jebakan Kognitif

1. "Signifikan statistik = penting secara praktis" → cek effect size
2. "Hipotesis tidak didukung → cari sudut baru" → p-hacking
3. "Kegagalan tidak perlu dilaporkan detail" → missed insight
4. "Limitasi cukup disebutkan, tidak perlu dianalisis" → kedalaman hilang

---

## Template A.14 — Analysis & Interpretation Report

```
ANALYSIS & INTERPRETATION

1. Statistik Deskriptif:
   | Skenario | Mean (Pulls) | Std | Median | Min | Max | n |
   |----------|--------------|-----|--------|-----|-----|---|
   | Fixed    | 166.7        | 0.6 | 166.7  | 165 | 168 | 10|
   | Weighted | 62.4         | 0.3 | 62.4   | 62  | 63  | 10|

2. Uji Hipotesis:
   Uji yang digunakan  : Independent t-test (Unpaired t-test)
   Justifikasi          : Membandingkan rata-rata dari dua kelompok sampel independen (simulasi yang berbeda) dengan distribusi normal.
   Hasil: p = <0.001, effect size (Cohen's d) = > 5.0
   CI 95%               : [103.8, 104.8] selisih pull

3. Keputusan:
   [x] H₀ ditolak → H₁ diterima
   [ ] H₀ tidak ditolak

4. Interpretasi:
   Hubungan ke RQ       : Membuktikan bahwa mekanisme weighted probability secara signifikan lebih efisien dengan mengurangi expected pull rate.
   Practical significance: Penurunan dari 166 menjadi 62 tarikan merupakan dampak praktikal yang masif pada pemain dan ekonomi game.
   Perbandingan literatur: Sejalan dengan literatur tentang gacha game design, bahwa pity system mendistorsi secara positif peluang perolehan.

5. Limitation:
   | Jenis | Ancaman | Dampak | Mitigasi |
   |-------|---------|--------|----------|
   | External validity | Simulasi di satu set nilai rate (0.6% rate) | Generalisasi terbatas untuk gacha rate/struktur itu | Eksplorasi cross-rule gacha |

6. Failure Analysis (jika H₀ tidak ditolak):
   Penyebab potensial  : N/A (H₀ ditolak)
   Boundary condition   : N/A
   Insight              : N/A
```

---

## Latihan 1 — Pemilihan Uji Statistik

Tentukan uji statistik yang tepat untuk eksperimen Anda.

| Pertanyaan | Jawaban |
|-----------|---------|
| Berapa grup yang dibandingkan? | *2 (Fixed Probability vs Weighted Probability)* |
| Apakah data berpasangan (paired)? | *Tidak (independen run simulasi)* |
| Apakah distribusi normal? (uji normalitas) | *Ya, berdasarkan central limit theorem dari jumlah simulasi besar.* |
| **Uji yang dipilih:** | *Independent t-test* |
| **Justifikasi:** | *Membandingkan dua kondisi eksperimen rata-rata yang independen dan berdistribusi normal.* |

**Effect size yang akan dilaporkan:** [x] Cohen's d / [ ] Eta-squared / [ ] Lainnya: ____

---

## Latihan 2 — Interpretasi Hasil

Gunakan data berikut (atau data riil Anda) untuk berlatih interpretasi.

**Data (Riil - Eksperimen Gacha):**
| Skenario | Average Pulls (mean ± std) | n |
|----------|----------------------|---|
| Fixed Probability | 166.7 ± 0.6 | 10 |
| Weighted Probability | 62.4 ± 0.3 | 10 |

p < 0.001, Cohen's d > 5.0, CI 95% = [103.8, 104.8] (selisih pulls)

| Aspek | Interpretasi |
|-------|-------------|
| Signifikansi statistik | *p < 0.001 → Sangat signifikan secara statistik pada α=0.01.* |
| Effect size | *d > 5.0 → Sangat besar (huge effect). Perbedaan mekanisme ini tidak bisa diabaikan secara komputasi maupun user.* |
| Practical significance | *Sistem weighted menghemat rata-rata 100 pull bagi user, dampak cost/monetisasi yang mengubah behaviour pemain.* |
| Hubungan ke RQ | *Menjawab penuh H1 bahwa efisiensi weighted probability jauh lebih tinggi dari fixed.* |
| Perbandingan literatur | *Sesuai dengan fenomena "pity mechanic" yang mendongkrak player retention.* |

---

## Latihan 3 — Failure Analysis

Latih kemampuan failure analysis: hipotesis TIDAK didukung. Apa yang bisa dipelajari?

**Skenario (Hipotetis Riset Gacha):** Anda membuat varian algoritma "Dynamic Pity" (pity beradaptasi per pemain). Namun perbedaannya dari soft-pity reguler ternyata memiliki p = 0.12 (tidak signifikan).

| Pertanyaan | Jawaban |
|-----------|---------|
| Apakah ini "gagal"? | *Bukan. Membuktikan bahwa menambah komputasi untuk "Dynamic Pity" tidak memberi manfaat tambahan (diminishing returns).* |
| Kemungkinan penyebab? | *Distribusi penarikan sudah cukup dimitigasi oleh sistem soft pity standar; efek noise RNG mendominasi algoritma tambahan.* |
| Boundary condition? | *Mungkin Dynamic Pity hanya ada efeknya di segmen whale spender; bagi kelompok general populasinya efeknya tertutup noise rata-rata.* |
| Insight yang bisa diambil? | *Gunakan sistem Weighted Pity standar. Hindari implementasi Dynamic Pity karena membebani logic backend secara mubazir.* |
| Apakah layak dilaporkan? Mengapa? | *Ya, informasi ini menyelamatkan waktu dan biaya riset industri game dalam bereksperimen dengan dynamic pity.* |

**Limitation terkait:**
| Jenis | Ancaman | Dampak |
|-------|---------|--------|
| *Construct validity* | *Sistem tidak membedakan player segment* | *Efek pity canggih yang spesifik player-base bisa hilang (flattened) dalam rata-rata.* |
| *External validity* | *Base spending behavior dianggap uniform* | *Model simulasi bisa meleset di dunia nyata di mana player punya threshold limit frustrasi.* |
| *Statistical limitation* | *Tail of distribution (outlier)* | *Simulasi standar terkadang memuluskan variance di ekstrem-ekstrem (lack of heavy-tails representation).* |

---

## Refleksi

> Apakah "failure" dalam riset benar-benar gagal, atau justru kontribusi? Bagaimana failure analysis mengubah cara Anda melihat hasil negatif?

> "Failure" yang terdokumentasi adalah temuan ilmiah yang valid. Ia mencegah riset/industri mengulang kesalahan yang sama. Melalui failure analysis, hasil negatif yang awalnya terasa mengecewakan justru berubah menjadi wawasan atas *boundary conditions* (batasan kapan suatu sistem tidak bekerja lagi) dan berkontribusi terhadap landasan state-of-the-art di masa depan.
