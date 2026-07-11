# WS-16: Presentation & Defense (UAS)

> **Bab 16 — Presentasi & Pertahanan Ilmiah**

---

## Ringkasan Materi

### Scientific Defense Model

```
Research Work → Presentation → Questioning → Defense → Evaluation → Acceptance
```

### Presentasi ≠ Ringkasan Paper

| Paper | Presentasi |
|-------|-----------|
| Dibaca (self-paced) | Didengar (presenter-paced) |
| Detail lengkap | Ide kunci + highlight |
| Tabel numerik detail | Grafik visual + angka kunci |
| Pembaca bisa re-read | Audiens dengar sekali |

**Prinsip:** Presentasi membutuhkan **reformulasi**, bukan kompresi. Medium berbeda = pendekatan berbeda.

### Claim-Evidence-Reasoning (CER)

Setiap jawaban defense harus memiliki:
1. **Claim** — Pernyataan yang dijawab
2. **Evidence** — Data/fakta pendukung
3. **Reasoning** — Logika yang menghubungkan evidence ke claim

**Contoh:**
| Pertanyaan | Bad Answer | Good Answer (CER) |
|-----------|-----------|-------------------|
| "Kenapa hanya 3 dataset?" | "Tiga sudah cukup" | "3 dataset mewakili variasi: small-clean, medium-clean, medium-noisy [E]. Generalisasi perlu validasi lanjut — listed as limitation [R]" |
| "Hasil DS-3 menurun?" | "Itu outlier" | "Ya, karena distribusi heavy-tail melanggar asumsi Gaussian [E]. Ini menunjukkan boundary condition metode [R]" |
| "Effect size?" | "p=0.003, jadi signifikan" | "Cohen's d=1.2 (large effect) [E] — bukan hanya signifikan tapi substansial [R]" |

### Slide Design — One Slide, One Message

**Optimal 9-Slide Plan (15 menit):**

| # | Slide | Waktu | Pesan |
|---|-------|-------|-------|
| 1 | Title + context | 1 min | Apa ini tentang apa |
| 2 | Problem + motivation | 2 min | Mengapa penting |
| 3 | Gap + RQ | 1.5 min | Apa yang belum terjawab |
| 4 | Method overview | 2 min | Bagaimana dijawab (diagram) |
| 5 | Key result — tabel | 2 min | Temuan utama |
| 6 | Key result — grafik | 2 min | Pola visual |
| 7 | Interpretation + failure | 2 min | Apa artinya |
| 8 | Limitation + future | 1.5 min | Batasan & arah |
| 9 | Conclusion + contribution | 1 min | Closing message |

### Anticipatory Defense

Prediksi pertanyaan berdasarkan kategori:

| Kategori | Contoh Pertanyaan |
|---------|------------------|
| Problem | "Mengapa masalah ini penting?" |
| Gap | "Bagaimana dengan studi X yang sudah menjawab ini?" |
| Method | "Mengapa metode ini, bukan Y?" |
| Results | "Bagaimana menjelaskan anomali di DS-3?" |
| Generalization | "Apakah bisa diterapkan di domain lain?" |

### Tiga Prinsip Jawaban

1. **Direct** — Jawab dulu, elaborasi kemudian
2. **Data-based** — Tunjuk evidence spesifik
3. **Honest** — Akui limitasi jika memang ada

### Jebakan Kognitif

1. "Presentasi = semua yang ada di paper" → terlalu padat
2. "Slide cantik = presentasi bagus" → konten > estetika
3. "Tidak bisa jawab = gagal" → "I don't know, but..." menunjukkan kejujuran
4. "Tidak perlu latihan — saya paham riset saya" → latihan = menemukan celah

---

## Template A.16 — Defense Preparation Sheet

```
DEFENSE PREPARATION

Slide Deck Plan:
  Total slides   : 9 (target: 10-12 konten + title/closing)
  Time per slide : ~1.5 min
  Total time     : 15 menit

Slide Outline:
| # | Pesan Utama | Visual | Waktu |
|---|-------------|--------|-------|
| 1 | Title: Analisis Algoritma Weighted Probability | Cover Paper | 30s |
| 2 | Problem: Whale vs F2P & Efek Bad Luck | Diagram Pemain | 2min |
| 3 | Gap + RQ: Komparasi Empiris Sistem Pity | Tabel Literatur| 2min |
| 4 | Method: Simulasi 1 Juta Pulls (Monte Carlo) | Flowchart | 2min |
| 5 | Results: Pull rate turun drastis (166 -> 62) | Tabel Hasil | 2min |
| 6 | Visual: Ledakan Probabilitas di Pull ke-50 | Line Chart | 2min |
| 7 | Discussion: Pity cegah frustrasi jangka panjang| Box Plot | 2min |
| 8 | Limitasi & Future Work: Eksplorasi ekonomi real | Teks Ringkas | 1.5min|
| 9 | Conclusion: Weighted lebih stabil & efisien | Pesan Utama | 1min |

Anticipatory Defense Matrix:
| Kategori | Pertanyaan Potensial | Jawaban (CER) |
|----------|---------------------|---------------|
| Problem  | Mengapa efisiensi pity penting diteliti?| Menurunkan churn (C). Tanpa pity = butuh >160 pull (E). Krusial bagi retensi (R). |
| Gap      | Bukankah gacha math sudah umum? | Analisis empiris/komparasi kurang (C). Mayoritas bahas model bisnis (E). Kami fokus efek teknis probabilistik (R). |
| Method   | Kenapa pakai simulasi, bukan data riil? | Simulasi menyingkirkan noise (C). Skenario deterministik sesuai rule asli (E). Jika data campur tangan pemain asli digunakan, efek murni probabilitas susah diisolasi (R). |
| Results  | Mengapa d > 5.0 (jaraknya sangat jauh)?| Sistem memotong batas atas distribusi (C). Peluang mencapai 100% pada pull 70 (E). Menghilangkan sifat eksponensial di 'long-tail' murni acak (R). |
| Generalization | Berlaku untuk lootbox e-sports? | Tidak bisa langsung (C). Lootbox standar tak punya 'memory' persentase masa lalu (E). Weighted prob butuh dependensi hasil (R). |

Latihan:
  Latihan 1: [25 Nov 2026] — [Kurang mulus di bagian Method, terlalu lama jelasin kode Python]
  Latihan 2: [28 Nov 2026] — [Transisi ke tabel hasil sudah bagus, waktu tepat 14 menit]
  Latihan 3: [02 Des 2026] — [Siap Q&A, argumen CER terhafal dengan baik]
```

---

## Latihan 1 — Slide Outline

Rencanakan presentasi 15 menit untuk riset Anda.

| # | Pesan Utama | Visual yang Digunakan | Waktu |
|---|-------------|----------------------|-------|
| 1 | *Judul Riset & Konteks Analisis Gacha Game* | *Cover Paper* | *1 min* |
| 2 | *Masalah: Kesialan berujung churn pemain* | *Diagram Frustrasi & Retensi* | *2 min* |
| 3 | *Gap Literatur & Pertanyaan Riset (RQ)* | *Tabel perbandingan literatur (highlight pity)* | *1.5 min* |
| 4 | *Metode Simulasi (Independent t-test)* | *Flowchart Program Python* | *2 min* |
| 5 | *Tabel Hasil Utama (Rata-rata 166.7 vs 62.4)* | *Tabel Komparasi Statistik (p < 0.001)* | *2 min* |
| 6 | *Visualisasi: Efek Soft-Pity Eksponensial* | *Kurva Line-Chart Probabilitas Kumulatif* | *2 min* |
| 7 | *Interpretasi (Discussion)* | *Box-plot Hilangnya Outlier (Tail Distribution)* | *2 min* |
| 8 | *Batasan Riset & Future Work (Validitas)* | *Bullet Points Singkat* | *1.5 min* |
| 9 | *Kesimpulan Akhir H1 Diterima* | *Quote Jawaban RQ* | *1 min* |

**Total waktu estimasi:** 15 menit

---

## Latihan 2 — Anticipatory Defense

Prediksi 5 pertanyaan yang mungkin diajukan penguji, lalu siapkan jawaban CER.

| # | Kategori | Pertanyaan | Claim | Evidence | Reasoning |
|---|----------|-----------|-------|----------|-----------|
| 1 | *Problem* | *Kenapa pity system perlu dianalisis secara saintifik?* | *Mencegah kepergian (churn) pemain dari game.* | *Fixed rng memakan ~166 pulls yang merugikan. Weighted teruji menyelamatkan investasi mereka (62 pulls).* | *Dengan pembuktian akurat, balance designer bisa menetapkan tarif dengan aman.* |
| 2 | *Method* | *Kenapa repot pakai model simulasi Monte Carlo 1 juta run?* | *Demi memenuhi syarat uji distribusi normal.* | *The Law of Large Numbers (LLN) menghilangkan noise statistik/variansi acak yang sering mengganggu.* | *Tanpa adanya data server rahasia dev, simulasi masif adalah satu-satunya substitusi pembuktian empiris.* |
| 3 | *Results* | *Nilai Effect size d > 5.0 itu sangat besar, apakah datanya cacat?* | *Sistem mendistorsi distribusi secara terprogram, bukan acak.* | *Max tarikan di algoritma weighted dibatasi hard-cut pada pull ke-70 secara absolut.* | *Pemotongan outlier murni mengubah sifat kurva secara tidak linear, terbukti hasilnya besar.* |
| 4 | *Gap* | *Apa beda riset komparasi ini dari perhitungan YouTuber?* | *Pendekatan metodologi ilmiah ketat dan metrik saintifik.* | *Penggunaan t-test, interpretasi Cohen's d, & uji batas limitasi eksternal pada paper.* | *Bukan sekadar probabilitas di excel, tetapi reproduktif layaknya artikel ilmiah.* |
| 5 | *Generalize* | *Bisakah metrik temuan ini dipakai di Gacha Lootbox Barat (CS:GO)?* | *Tidak bisa diaplikasikan langsung ke lootbox tanpa pity.* | *Lootbox reguler 'memoryless' (seperti melempar koin independen).* | *Algoritma yang kita teliti mensyaratkan history player (dependensi komputasi) untuk aktif.* |

---

## Latihan 3 — Simulasi Q&A

Minta teman/kolega mengajukan 3 pertanyaan tentang riset Anda. Catat pertanyaan dan evaluasi jawaban Anda.

| # | Pertanyaan | Jawaban Saya | Evaluasi |
|---|-----------|-------------|---------|
| 1 | "Mengapa tidak membandingkan revenue asli/ekonomi in-game di dunia nyata?" | "Data in-game tersebut bersifat rahasia perusahaan dan tertutup rapat. Kami mencantumkan ini sebagai limitasi penelitian (lack of real economy access)." | [x] Direct [x] Data-based [x] Honest |
| 2 | "Bukannya sudah sangat jelas secara logika kalau pity pasti lebih sedikit jumlah tarikannya (common sense)?" | "Tujuannya bukan sekadar tahu mana yang lebih sedikit, tapi mengukur 'seberapa masif signifikansi efisiensinya' (diperoleh Effect Size > 5.0), yang bisa diacu oleh game developer untuk game balancing." | [x] Direct [x] Data-based [x] Honest |
| 3 | "Jika script simulasi diganti dengan bahasa C++, apakah grafiknya tetap akan sama hasilnya?" | "Ya, logika dasar pseudo-random (RNG) akan tetap menghasilkan distribusi uniform yang memproyeksikan kurva probabilitas yang serupa melintasi platform mana saja." | [x] Direct [x] Data-based [x] Honest |

**Pertanyaan yang paling sulit dijawab:**
> Menjawab pertanyaan sentilan dari penguji nomor 2 ("Bukannya sudah sangat jelas secara common sense?"). Menjawab pandangan skeptis yang meremehkan riset karena dianggap 'logika dasar' membutuhkan kesabaran luar biasa dan sandaran kuat pada argumen "bahwa ilmu pengetahuan wajib *mengkuantifikasi* segala *common sense* secara empiris".

**Apa yang perlu disiapkan lebih baik:**
> Memperbanyak wawasan bacaan tambahan soal literatur 'psikologi dan perilaku pemain' (player psychology and gambler's fallacy) agar bisa langsung menyambungkan interpretasi matematis dengan efek riil emosional manusia di sesi Q&A.

---

## Refleksi

> Dari seluruh proses WS-01 sampai WS-16 — dari paradigma riset hingga presentasi — bagian mana yang paling mengubah cara Anda berpikir tentang riset? Apa satu hal yang akan selalu Anda terapkan di riset berikutnya?

**Insight terbesar:**
> Saya menyadari bahwa "menulis dan mempresentasikan riset" sama sekali bukan tentang memamerkan seberapa jago kita *coding* script Python, melainkan tentang *bagaimana kita bisa merangkai cerita logis*: berangkat dari sebuah *Gap*, mengisinya dengan *Metode* objektif, dan meyakinkan penguji melalui *Hasil* saintifik. Menguasai narasi metodologi jauh lebih tangguh saat pertahanan skripsi/riset ketimbang sekadar memunculkan tabel *output database*.

**Yang akan selalu diterapkan:**
> Kerangka "Anticipatory Defense" alias C-E-R (*Claim-Evidence-Reasoning*). Membiasakan diri memetakan potensi kelemahan riset lalu menyiapkannya dalam tabel CER akan menghentikan kebiasaan menjawab secara panik atau *defensif* saat dikritik penguji. Itu membuat saya selalu berpegang erat pada objektivitas *evidence* setiap kali mempertahankan argumen.
