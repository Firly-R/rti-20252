# WS-15: Scientific Writing

> **Bab 15 — Penulisan Ilmiah**

---

## Ringkasan Materi

### Scientific Argument Flow

```
Problem → Gap → RQ → Method → Result → Analysis → Conclusion → Contribution
```

Paper ilmiah adalah **satu argumen utuh** dari masalah ke kontribusi. Setiap node harus terhubung logis ke node sebelum dan sesudahnya.

### Struktur IMRAD

| Section | Peran | Pertanyaan Kunci |
|---------|-------|-----------------|
| **Introduction** | Motivasi + frame | Why is this needed? |
| **Method** | Deskripsi (reproducible) | How was it done? |
| **Results** | Laporan objektif | What was found? |
| **Discussion** | Interpretasi + refleksi | What does it mean? |
| **Conclusion** | Ringkasan + kontribusi | So what? |

### Logical Flow — "Red Thread"

Setiap paragraf menjawab satu pertanyaan dan memicu pertanyaan berikutnya. Alur logis ini harus terasa di tiga level:
1. **Antar-kalimat** dalam paragraf
2. **Antar-paragraf** dalam section
3. **Antar-section** dalam paper

### Internal Consistency

Setiap elemen yang dijanjikan di Introduction harus hadir di Discussion/Conclusion.

**Consistency Matrix:**
```
           Intro  Method  Result  Discuss  Conclude
RQ1          ✓      ✓       ✓       ✓        ✓
RQ2          ✓      ✓       ✓       ✗ ←      ✓
Metrik-X     ✗      ✗       ✓ ←     ✗        ✗
```
**Masalah:** RQ2 dibahas di semua bagian kecuali Discussion. Metrik-X muncul di Result tapi tidak diperkenalkan di Method.

### Writing Quality Triad

| Kualitas | Deskripsi | Contoh Buruk → Baik |
|----------|----------|---------------------|
| **Clarity** | Dipahami sekali baca | "Performa meningkat" → "Accuracy meningkat dari 85.3% ke 89.7%" |
| **Precision** | Istilah eksak, tanpa ambiguitas | "signifikan" → "signifikan secara statistik (p=0.003, d=1.2)" |
| **Conciseness** | Setiap kata menambah informasi | Hapus kalimat redundan, filler words |

### Urutan Penulisan yang Disarankan

1. **Method & Results** — paling stabil, tulis pertama
2. **Discussion** — interpretasi berdasarkan hasil
3. **Introduction** — frame sesuai temuan aktual
4. **Abstract & Conclusion** — terakhir

### Target Jumlah Kata

| Section | Target |
|---------|--------|
| Introduction | 500–700 |
| Related Work | 700–1000 |
| Method | 800–1200 |
| Results | 500–800 |
| Discussion | 600–900 |
| Conclusion | 200–400 |

### Jebakan Kognitif

1. "Lebih panjang = lebih lengkap" → conciseness lebih berharga
2. "Introduction harus ditulis pertama" → justru ditulis terakhir
3. "Jargon teknis = lebih ilmiah" → clarity lebih penting
4. "Discussion = ringkasan Results" → Discussion = interpretasi + konteks

---

## Template A.15 — Paper Structure Checklist

```
PAPER STRUCTURE CHECKLIST

Title   : Analisis Algoritma Weighted Probability pada Sistem Gacha Game
Target  : [x] Jurnal  [ ] Konferensi  [ ] Laporan

Section Check:
  [x] Abstract — masalah, metode, hasil utama, kontribusi (max 250 kata)
  [x] Introduction — konteks → gap → RQ → kontribusi → struktur paper
  [x] Related Work — concept-centric, gap positioning
  [x] Method — reproducible: desain, variabel, metrik, setup, prosedur
  [x] Results — tabel + grafik + observasi (tanpa interpretasi)
  [x] Discussion — interpretasi, perbandingan, implikasi, limitation
  [x] Conclusion — jawaban RQ, kontribusi, future work

Consistency Matrix:
  [x] RQ di Introduction = RQ di Method = RQ di Conclusion
  [x] Variabel di Method = variabel di Results
  [x] Klaim di Discussion didukung data di Results
  [x] Limitasi di Discussion di-address di Conclusion/Future Work

Writing Quality:
  [x] Clarity — mudah dipahami tanpa re-read
  [x] Precision — tidak ada istilah ambigu
  [x] Conciseness — tidak ada kalimat redundan
```

---

## Latihan 1 — Paper Outline

Buat outline paper untuk riset Anda menggunakan struktur IMRAD.

| Section | Konten Utama (2-3 kalimat) | Target Kata |
|---------|---------------------------|------------|
| Abstract | *Studi ini mengevaluasi gap efisiensi dari sistem gacha. Simulasi membandingkan sistem probabilitas terbobot (weighted) dengan sistem probabilitas tetap (fixed). Hasilnya menunjukkan peningkatan efisiensi perolehan dari 166 ke 62 tarikan rata-rata.* | 200-250 |
| Introduction | *Konteks gacha modern menggunakan pity system. Gap: kurangnya analisis kuantitatif tentang signifikansi efisiensinya terhadap peluang perolehan. RQ: Apakah weighted probability memberikan expected pull rate yang lebih efisien?* | 500-700 |
| Related Work | *Kajian pada literatur ekonomi gacha dan perilaku probabilistik. Membahas paper sebelumnya yang menyinggung pity rate secara teoretis, untuk memperkuat posisi perbandingan empiris di studi ini.* | 700-1000 |
| Method | *Desain simulasi eksperimen. Penjelasan dua kondisi independen (fixed dan weighted). Mendefinisikan IV (Jenis Algoritma), DV (Efisiensi Peluang), serta metrik (Average Pulls dan Cumulative Probability).* | 800-1200 |
| Results | *Menyajikan tabel perbedaan mean average pulls (166.7 vs 62.4). Menampilkan line chart akumulasi probabilitas untuk memperlihatkan lonjakan peluang saat soft pity dimulai pada algoritma weighted.* | 500-800 |
| Discussion | *Interpretasi dari penurunan tajam jumlah tarikan (Cohen's d > 5.0) yang memvalidasi efektivitas soft pity. Mengaitkannya dengan pengalaman pengguna untuk mencegah frustasi jangka panjang dari outlier bad luck.* | 600-900 |
| Conclusion | *H1 diterima. Mekanisme weighted probability terbukti lebih efisien dan menjamin kepastian bagi pemain gacha pada rentang simulasi yang terukur. Menyebutkan batasan eksperimen tunggal dan implikasi pengembangan gacha di masa depan.* | 200-400 |

---

## Latihan 2 — Consistency Matrix

Buat consistency matrix untuk memverifikasi internal consistency paper Anda.

|  | Intro | Method | Result | Discussion | Conclusion |
|--|-------|--------|--------|-----------|-----------|
| RQ1 | *✓* | *✓* | *✓* | *✓* | *✓* |
| RQ2 (N/A) | *N/A* | *N/A* | *N/A* | *N/A* | *N/A* |
| Metrik utama | *✓* | *✓* | *✓* | *✓* | *✓* |
| Variabel IV | *✓* | *✓* | *✓* | *✓* | *✓* |
| Variabel DV | *✓* | *✓* | *✓* | *✓* | *✓* |
| Klaim/kontribusi | *✓* | *✓* | *✓* | *✓* | *✓* |

**Inkonsistensi yang ditemukan:**
> Secara konsep sudah konsisten, namun dalam praktiknya sering ditemukan metrik evaluasi tambahan (seperti Cumulative Probability Curve) dimunculkan di bagian Result, padahal tidak pernah didefinisikan cara penghitungannya pada bagian Method.

**Tindakan perbaikan:**
> Meninjau ulang draf bagian Method, dan pastikan setiap metrik yang akan disajikan grafiknya (seperti sumbu X dan Y pada grafik akumulasi persentase) harus sudah tertulis secara rinci definisi variabelnya di dalam *Method section*.

---

## Latihan 3 — Writing Quality Check

Ambil satu paragraf dari tulisan Anda (atau tulis paragraf baru) dan evaluasi kualitasnya.

**Paragraf asli:**
> "Sistem gacha yang pakai pity ini sangat bagus sekali hasilnya. Performa tarikannya lebih cepat dan player jadi lebih gampang menang rare item. Rata-ratanya turun dari 166 jadi 62 saja. Pokoknya sistem weighted probability ini lebih efisien dibanding sistem yang fix probability."

| Kriteria | Evaluasi | Perbaikan |
|----------|---------|-----------|
| Clarity | *Penggunaan "sangat bagus sekali" subjektif, dan "gampang menang" bukan istilah akademis (informal).* | *Ganti menjadi deskripsi objektif tentang peningkatan efisiensi peluang.* |
| Precision | *"Performa tarikan lebih cepat" ambigu (apakah komputasi lebih cepat atau jumlah tarikan lebih sedikit?).* | *Eksplisit menggunakan istilah metrik: "expected pull rate berkurang (d > 5.0)".* |
| Conciseness | *Kalimat terakhir "Pokoknya sistem weighted..." adalah filler yang tidak memiliki bobot akademis.* | *Hapus kata pengulangan dan satukan klaim argumen dengan data pendukung.* |

**Paragraf setelah perbaikan:**
> "Mekanisme *weighted probability* (pity system) terbukti mengurangi *expected pull rate* secara empiris dan signifikan (p < 0.001). Rata-rata tarikan yang dibutuhkan untuk memperoleh *rare item* menurun drastis dari 166.7 menjadi 62.4 tarikan. Hal ini memvalidasi hipotesis bahwa sistem probabilitas terbobot terukur lebih efisien dibandingkan *fixed probability*."

---

## Refleksi

> Apa perbedaan antara menulis "tentang" riset dan menulis sebagai "argumen" riset? Bagaimana urutan penulisan (Method → Discussion → Introduction) mengubah kualitas tulisan?

> Menulis "tentang" riset ibarat melaporkan kronologi (pasif, seperti buku harian). Menulis sebagai "argumen riset" adalah membangun narasi logis di mana setiap data berfungsi menyokong kesimpulan, dan setiap paragraf memicu paragraf selanjutnya untuk memvalidasi posisi penelitian kita di antara literatur lain. Urutan penulisan mulai dari Results/Method lalu menuju Discussion dan bermuara ke Intro memastikan kita mem-*framing* argumen secara jujur sesuai dengan apa yang benar-benar ditemukan di eksperimen, menghindarkan penulis dari janji manis (*overpromising*) yang meleset dari fakta.
