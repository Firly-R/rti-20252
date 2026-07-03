# WS-01: Distorsi & Paradigma

> **Bab 1 — Research Mindset in IT**

---

## Ringkasan Materi

### Research Trust Model

Pengetahuan ilmiah tidak muncul langsung dari kenyataan. Ia melewati **6 tahap transformasi** yang masing-masing rawan distorsi:

```
Reality → Data → Processing → Analysis → Inference → Knowledge
```

Etika mencegah distorsi yang disengaja (fabrikasi, cherry-picking). Validitas mendeteksi distorsi yang tidak disengaja (confounding variable, sampling bias).

### Tiga Jenis Validitas

| Jenis | Pertanyaan | Contoh Ancaman |
|-------|-----------|----------------|
| **Internal Validity** | Apakah hubungan kausal benar ada? | Confounding variable |
| **External Validity** | Apakah bisa digeneralisasi? | Dataset terlalu homogen |
| **Construct Validity** | Apakah mengukur hal yang benar? | Metrik tidak sesuai klaim |

### Paradigma Riset

Mata kuliah ini menggunakan pendekatan **Positivist** (fenomena TI bisa diukur objektif melalui eksperimen terkontrol) diperkuat **Design Science Research** (DSR). Penting untuk membedakan keduanya:

| Paradigma | Cara Kerja | Contoh di TI |
|-----------|-----------|---------------|
| **Positivis** | Uji hipotesis dengan eksperimen terkontrol | Apakah CNN lebih akurat dari RF pada dataset X? |
| **Design Science Research** | Bangun artefak (sistem/model/framework) untuk menguji proposisi | Dapatkah arsitektur hybrid CNN+LSTM membuktikan peningkatan recall ≥5%? |
| **Interpretivis** | Pahami makna melalui konteks & kualitatif | Bagaimana peneliti manafsirkan anomali data sensor IoT? |

Dalam DSR, artefak **bukan tujuan akhir** — ia adalah instrumen untuk menghasilkan pengetahuan. Pertanyaan riset tetap harus difalsifikasi.

### Mode Berpikir Peneliti

**Curious** (mempertanyakan fenomena) → **Critical** (mengevaluasi klaim berdasarkan bukti) → **Systematic** (merancang investigasi terstruktur dan reproducible).

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan | Membuat sistem yang bekerja | Menghasilkan pengetahuan yang valid |
| Pertanyaan khas | "Bagaimana membuatnya jalan?" | "Apakah klaim ini benar?" |
| Ukuran sukses | Sistem berfungsi, client puas | Hipotesis terjawab, temuan tervalidasi |
| Kegagalan | Harus dihindari | Harus dilaporkan (negative result = kontribusi) |

### Istilah Penting

- **Research Mindset** — Pola pikir yang menuntut bukti dan mempertanyakan asumsi
- **Research Ethics** — Prinsip perilaku: kejujuran, objektivitas, keterbukaan, akuntabilitas
- **HARKing** — Hypothesizing After Results are Known — merumuskan hipotesis setelah melihat data
- **Falsifiability** — Hipotesis harus bisa dibuktikan salah

---

## Template A.1 — Research Mindset Self-Assessment

```
Nama Peneliti    : Muhammad Firly Ramadhan
Tanggal          : 24 April 2026

1. Ketika membaca klaim "metode X 95% akurat":
   - Pertanyaan pertama saya: Bagaimana metrik "efisiensi" didefinisikan secara matematis, dan apakah angka 95% tersebut merupakan peluang kumulatif pada batas hard pity atau nilai rata-rata (mean)?
   - Data yang dibutuhkan untuk verifikasi: Log mentah (raw logs) hasil pengundian RNG sebanyak minimal 100.000 sampel beserta dokumentasi parameter dasar (base rate) yang digunakan.

2. Posisi paradigma:
   - Pendekatan: [ ] Positivis  [ ] Interpretivis  [X] Design Science  [ ] Mixed
   - Alasan: Penelitian ini membangun sebuah artefak digital (prototype gacha simulator) yang digunakan sebagai instrumen ilmiah untuk menguji proposisi matematika dan hipotesis komparatif.

3. Identifikasi distorsi:
   - Asumsi tersembunyi: Mengasumsikan bahwa fungsi library pengacak angka (Random Number Generator) di komputer bekerja secara uniform sempurna tanpa adanya bias periodik.
   - Sumber bias potensial: Sampling bias jika jumlah iterasi simulasi terlalu kecil (misal hanya 100 pull), yang menyebabkan deviasi ekstrem akibat faktor keberuntungan acak.
   - Langkah mitigasi: Meningkatkan ukuran sampel eksperimen hingga 100.000 responden virtual untuk mencapai konvergensi statistik (Law of Large Numbers).

4. Komitmen etika:
   - Data yang tidak akan dimanipulasi: Angka mentah dari counter urutan pull sukses yang dicatat langsung oleh engine simulasi.
   - Batasan yang diakui sejak awal: Model simulasi ini disederhanakan dan tidak merepresentasikan faktor psikologis pemain asli atau intervensi dinamis sisi server (seperti algoritma anti-cheat/cookie tracker).
```

---

## Latihan 1 — Identifikasi Distorsi

Pilih satu paper riset di bidang TI yang mengklaim "metode X meningkatkan performa." Telusuri setiap tahap Research Trust Model.

> **Panduan pencarian paper:** Gunakan [IEEE Xplore](https://ieeexplore.ieee.org), [ACM Digital Library](https://dl.acm.org), atau Google Scholar. Pilih paper **tahun 2020 ke atas**, di topik yang Anda minati: deteksi anomali, klasifikasi citra, NLP, keamanan siber, IoT, dsb.
>
> **Contoh domain TI:** "Deteksi anomali lalu-lintas jaringan menggunakan CNN — akurasi meningkat 94% vs baseline SVM 87%." Distorsi potensial: apakah dataset normal/anomali seimbang? Apakah hanya diuji pada satu vendor traffic?

**Paper yang dipilih:**
> Judul: Gacha Game Analysis and Design
> Penulis (Tahun): C. Chen & Z. Fang (2023)
> Sumber/Link DOI: https://doi.org/10.1145/3579312

| Tahap | Apa yang Dilakukan | Potensi Distorsi |
|-------|-------------------|-----------------|
| Reality → Data | Mengamati mekanisme pengundian item pada game komersial (contoh: Genshin Impact) untuk dijadikan acuan data awal. | Sampling Bias: Hanya mengambil sampel model dari game besar yang populer, sehingga mengabaikan variasi algoritma gacha pada game indie atau kasual. |
| Data → Processing | Menyusun kode logika pemrograman bertingkat (soft pity dan hard pity) berdasarkan dokumentasi game nyata. | Penyederhanaan Ekstrem: Mengasumsikan kenaikan probabilitas di fase soft pity bersifat linear murni, padahal di game aslinya bisa jadi kurva eksponensial. |
| Processing → Analysis | Menghitung persentase cumulative probability di setiap urutan pull menggunakan counter loop. | Flawed Metric: Mengabaikan sisa data pull yang hangus jika simulasi tidak memisahkan sistem single-pull dengan multi-pull (10x sekaligus). |
| Analysis → Inference | Menyimpulkan bahwa sistem weighted probability jauh lebih menguntungkan pemain daripada fixed rate. | Survival Bias: Hanya berfokus pada jaminan pasti dapat di akhir (hard pity), tanpa menganalisis tingkat frustrasi/atrisi pemain di fase transisi. |
| Inference → Knowledge | Mengklaim bahwa formula pity system ini adalah standar paling optimal untuk menjaga keseimbangan ekonomi game gacha modern. | Overgeneralization: Menganggap satu formula probabilitas cocok untuk semua genre game, tanpa menguji dampaknya pada game non-RPG. |

**Distorsi paling besar di tahap:** Data → Processing

**Dua distorsi spesifik yang teridentifikasi:**
1. Construct Validity Distortion: Pemodelan matematika pada prototype terlalu ideal dan steril (bebas kendala network latency atau concurrency pool), sehingga ada jarak validitas dengan performa algoritma di server game asli.
2. Sampling Bias: Keterbatasan variasi parameter (jika hanya menguji satu pasang nilai pity) membuat kesimpulan rentan bias terhadap variasi desain game gacha lainnya.

---

## Latihan 2 — Analisis Kasus Etika

Skenario: Seorang peneliti menemukan bahwa jika 3 data point outlier dihapus, hasil eksperimennya menjadi signifikan. Dengan outlier, hasilnya tidak signifikan.

| Perspektif | Analisis |
|------------|---------|
| Kejujuran ilmiah | Penghapusan data point secara sengaja hanya demi mendapatkan status "signifikan" (p-value rendah) tanpa alasan teknis yang valid merupakan bentuk Data Cooking / Cherry-picking yang melanggar integritas ilmiah. |
| Transparansi | Peneliti wajib menyajikan keseluruhan data asli. Jika memang ada data yang dibuang, peneliti harus secara transparan menjelaskan di bab metodologi mengapa data itu dianulir (misal: karena sistem crash atau error RNG). |
| Peer review | Penjaga gawang ilmiah (reviewer) akan mendeteksi manipulasi ini lewat kejanggalan sebaran data. Menyembunyikan outlier akan merusak reputasi akademik peneliti saat paper ditolak (rejected). |

**Keputusan akhir dan justifikasi:**
> Peneliti harus tetap menyertakan 3 data point outlier tersebut di dalam analisis akhir. Di dalam dunia probabilitas dan simulasi stochastic (seperti sistem gacha), kemunculan anomali ekstrem—seperti responden virtual yang mendapatkan rare item 3 kali berturut-turut pada pull awal (keberuntungan ekstrem) atau tidak mendapatkannya sama sekali hingga batas akhir—bukanlah error, melainkan variansi murni dari hukum peluang yang justru membuktikan keaslian dari fungsi Random Number Generator (RNG) yang diuji.

---

## Latihan 3 — Posisi Paradigma

**Topik riset:** Analisis Evaluatif Algoritma Weighted Probability terhadap Cumulative Probability pada Sistem Gacha Game melalui Eksperimen Simulasi Komparatif.

> **Skala 1–5:** 1 = tidak sesuai sama sekali dengan topik ini, 5 = sangat sesuai dan dominan digunakan pada riset bertopik serupa.

| Kriteria | Positivis | Interpretivis | Design Science |
|----------|-----------|---------------|----------------|
| Kesesuaian dengan topik (1–5) | 4 — Sangat sesuai karena riset ini menguji hipotesis kuantitatif, bebas nilai, dan mengukur metrik angka secara objektif. | 1 — Tidak sesuai karena riset ini sama sekali tidak meneliti makna sosial, budaya, atau persepsi kualitatif dari pemain game. | 5 — Paling sesuai karena riset ini menuntut pembangunan sebuah komponen sistem (prototype gacha engine) sebagai instrumen utama penelitian. |
| Jenis data yang dikumpulkan | Metrik numerik, nilai rata-rata jumlah pull, persentase cumulative probability di setiap titik percobaan. | Transkrip wawancara dengan pemain gacha, catatan observasi perilaku kecanduan lootbox. | Kode program (source code), arsitektur sistem simulator, skema database log, dan file konfigurasinya. |
| Limitasi paradigma | Cenderung kaku dan hanya melihat angka, tidak bisa menjelaskan mengapa developer memilih angka pity tertentu secara bisnis. | Hasilnya subjektif, tidak bisa dipakai untuk membuktikan keakuratan performa algoritma matematika secara eksak. | Terlalu fokus pada "apakah sistemnya berfungsi", sehingga memerlukan bantuan metode Positivis untuk menganalisis data keluaran sistem secara statistik. |

**Paradigma yang dipilih:** Design Science Research (DSR) dengan penguatan Positivisme.
**Alasan:** Riset ini berfokus pada perancangan dan pembuatan sebuah artefak teknologi berupa Prototype Gacha Simulator (DSR). Perangkat lunak ini kemudian dioperasikan dalam lingkungan terkontrol untuk menghasilkan data log yang dianalisis menggunakan statistik deskriptif demi membuktikan kebenaran hipotesis secara empiris dan objektif (Positivis).

---

## Refleksi

> Sebelum membaca materi ini, apakah pernah mempertanyakan klaim "95% akurat"? Setelah memahami rantai distorsi, pertanyaan apa yang sekarang akan diajukan saat membaca paper?

**Jawaban:**
> Sebelum membaca materi ini, saya cenderung menerima klaim persentase akurasi atau performa tinggi di sebuah paper secara mentah-mentah. Namun, setelah memahami rantai Research Trust Model, saya menyadari bahwa angka akhir yang indah bisa saja menyembunyikan distorsi di tengah jalan.[cite: 2]
> 
> Sekarang, saat membaca paper TI, pertanyaan kritis yang akan saya ajukan adalah:[cite: 2]
> 1. *"Bagaimana data tersebut ditransformasikan dari realitas ke bentuk digital, dan apakah ada sampling bias di sana?"*[cite: 2]
> 2. *"Apakah metrik yang dipilih penulis benar-benar mengukur hakikat masalah (Construct Validity) atau hanya dipilih karena metrik itu yang paling menguntungkan klaim mereka?"*[cite: 2]
> 3. *"Apakah eksperimen ini dirancang secara systematic sehingga jika saya menduplikasi kodingannya, hasilnya akan tetap sama (reproducible)?"*[cite: 2]

