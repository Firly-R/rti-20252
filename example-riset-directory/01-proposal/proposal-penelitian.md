# PROPOSAL PENELITIAN
**Analisis Algoritma Weighted Probability pada Sistem Gacha Game**

**Oleh:**  
Muhammad Firly Ramadhan  
240202872

PROGRAM STUDI ILMU KOMPUTER  
FAKULTAS SAINS DAN TEKNOLOGI  
UNIVERSITAS PUTRA BANGSA  
2026

---

## RINGKASAN

Sistem gacha game merupakan mekanisme probabilitas yang banyak digunakan pada game modern untuk menentukan peluang pemain memperoleh item tertentu, terutama item rare. Pada implementasi modern, banyak game menggunakan weighted probability yang memungkinkan peluang rare item berubah secara dinamis berdasarkan jumlah pull pemain dan mekanisme pity system. Sistem ini membuat peluang rare item meningkat secara bertahap hingga mencapai batas tertentu.

Penelitian ini bertujuan menganalisis pengaruh algoritma weighted probability terhadap cumulative probability memperoleh item rare pada sistem gacha game. Penelitian menggunakan metode eksperimen komparatif berbasis simulasi antara sistem fixed probability dan weighted probability dengan parameter yang sama. Variabel independen utama penelitian adalah mekanisme weighted probability, sedangkan variabel dependennya adalah cumulative probability rare item.

Data penelitian diperoleh dari hasil simulasi pull menggunakan prototype sistem gacha yang terdiri atas probability engine, pull simulator, pity system, dan cumulative probability calculator. Hasil eksperimen dianalisis melalui perbandingan cumulative probability dan jumlah pull rata-rata hingga rare item diperoleh.

Penelitian ini diharapkan menghasilkan analisis evaluatif mengenai pengaruh weighted probability terhadap peluang rare item serta menghasilkan prototype simulasi sistem gacha yang dapat digunakan untuk penelitian lanjutan mengenai algoritma probabilitas pada game modern.

**KATA KUNCI:** *weighted probability; gacha game; cumulative probability; pity system; eksperimen simulasi.*

---

## PENDAHULUAN

### A. LATAR BELAKANG DAN RUMUSAN MASALAH

Game modern saat ini banyak menggunakan sistem gacha sebagai mekanisme distribusi item virtual kepada pemain. Sistem ini menggunakan probabilitas tertentu untuk menentukan peluang pemain memperoleh item rare melalui proses pull. Pada implementasi modern, sistem gacha tidak hanya menggunakan fixed probability, tetapi juga weighted probability yang memungkinkan peluang rare item berubah secara dinamis berdasarkan jumlah pull yang dilakukan pemain.

Mekanisme weighted probability biasanya dipadukan dengan pity system untuk meningkatkan peluang rare item setelah pemain gagal memperoleh item dalam sejumlah pull tertentu. Namun, perubahan probabilitas tersebut sering dianggap sulit dipahami karena peluang rare item tidak bersifat tetap sepanjang proses gacha berlangsung.

Jurnal *Gacha Game Analysis and Design* menjelaskan bahwa weighted probability menjadi salah satu mekanisme utama dalam desain sistem gacha modern karena mampu mengatur distribusi probabilitas rare item secara dinamis. Namun, sebagian besar penelitian masih berfokus pada monetisasi game dan perilaku pemain dibanding analisis algoritma probabilitas itu sendiri.

Berdasarkan kondisi tersebut, rumusan masalah penelitian ini adalah bagaimana algoritma weighted probability memengaruhi cumulative probability memperoleh item rare pada sistem gacha game.

### B. PENDEKATAN PEMECAHAN MASALAH

Tujuan penelitian ini adalah menganalisis pengaruh algoritma weighted probability terhadap peluang memperoleh rare item pada sistem gacha game. Research question (RQ) yang diajukan adalah: "Seberapa besar signifikansi perbedaan cumulative probability dan jumlah rata-rata pull dalam memperoleh rare item antara sistem weighted probability dibandingkan sistem fixed probability?"

Terdapat peningkatan cumulative probability yang signifikan dan penurunan rata-rata jumlah pull pada penerapan intervensi weighted probability dibandingkan baseline fixed probability saat jumlah percobaan mendekati batas pity threshold.

Pendekatan penelitian dilakukan menggunakan eksperimen komparatif berbasis simulasi. Penelitian membandingkan sistem fixed probability sebagai baseline (Kondisi A) dengan weighted probability sebagai intervention (Kondisi B) menggunakan parameter dasar dan jumlah pull yang identik agar hasil eksperimen valid dan obyektif.

### C. STATE OF THE ART DAN KEBARUAN

Penelitian mengenai sistem gacha game telah banyak membahas monetisasi, perilaku pemain, loot box design, dan gambling effect. Penelitian *Gacha Game Analysis and Design* membahas desain probabilitas pada sistem gacha modern, termasuk weighted probability dan pity system sebagai mekanisme utama pengaturan rare item.

Penelitian lain juga membahas transparency probability dan pity timer pada sistem gacha modern. Namun, sebagian besar penelitian masih menitikberatkan pada perilaku pemain dan dampak psikologis dibanding analisis algoritma probabilitas rare item.

Gap penelitian muncul karena masih sedikit penelitian yang secara spesifik menganalisis pengaruh weighted probability terhadap cumulative probability rare item menggunakan pendekatan eksperimen simulasi.

Kebaruan penelitian ini terletak pada fokus evaluasi algoritma weighted probability melalui eksperimen komparatif antara fixed probability dan weighted probability menggunakan metric cumulative probability rare item.

### D. PETA JALAN PENELITIAN

Tahap awal penelitian dimulai dari studi literatur mengenai weighted probability, pity system, dan desain probabilitas pada game gacha modern. Tahap berikutnya adalah perumusan research question, variabel penelitian, dan desain eksperimen.

Setelah tahap perancangan selesai, penelitian dilanjutkan dengan pembuatan prototype simulasi sistem gacha yang terdiri atas probability engine, pull simulator, pity system, dan cumulative probability calculator. Prototype kemudian digunakan untuk menjalankan eksperimen komparatif antara fixed probability dan weighted probability. Tahap akhir penelitian meliputi analisis hasil eksperimen, evaluasi cumulative probability rare item, penyusunan laporan penelitian, dan pengembangan penelitian lanjutan terkait algoritma probabilitas pada game modern.

---

## METODE

### A. DESAIN PENELITIAN DAN UNIT ANALISIS

Penelitian ini menggunakan desain eksperimen komparatif kuantitatif berbasis simulasi komputer. Unit analisis dalam penelitian ini adalah log transaksi pull individu yang merekam status perolehan item (rare atau non-rare) pada setiap percobaan. Populasi penelitian ini adalah seluruh log data probabilitas pull historis yang dapat dibangkitkan oleh algoritma probability engine pada simulasi gacha. Sampel diambil sebanyak 100.000 iterasi pull menggunakan teknik random sampling dengan kriteria inklusi berupa rentang percobaan dari pull ke-1 hingga rare item diperoleh (maksimal 90 pull). Data penelitian berasal dari data primer hasil observasi log mesin simulasi (pull simulator) yang merepresentasikan 100.000 pemain virtual, dengan karakteristik 100.000 baris data observasi per kondisi, dieksekusi dalam 1 periode pengujian simulasi, dan disimpan dalam format CSV.

### B. Kondisi Eksperimen (Baseline VS Intervention)

Untuk menguji hipotesis, skenario pengujian dibagi menjadi dua kondisi pembanding secara eksplisit:
- **Kondisi A (Baseline)**: Sistem *Fixed Probability*. Pada kondisi ini, probabilitas mendapatkan rare item bersifat konstan (misal: 0.6%) pada setiap pull, terlepas dari berapa banyak pull yang telah gagal sebelumnya (tanpa pity system).
- **Kondisi B (Intervention)**: Sistem *Weighted Probability*. Pada kondisi ini, probabilitas dasar adalah 0.6%, namun diberikan intervensi berupa penambahan bobot probabilitas secara dinamis setelah pemain melewati batas tertentu (soft pity pada pull ke-70) hingga mencapai jaminan 100% (hard pity pada pull ke-90).

### C. Variabel Penelitian

Variabel-variabel dalam penelitian ini didefinisikan secara eksplisit sebagai berikut:
1. **Variabel Independen (Variabel Bebas)**: Algoritma Distribusi Probabilitas. Variabel ini memiliki dua kategori nilai, yaitu *Fixed Probability* (Kondisi A) dan *Weighted Probability* (Kondisi B).
2. **Variabel Dependen (Variabel Terikat)**:
   - *Cumulative Probability*: Peluang kumulatif eksperimental keberhasilan mendapatkan rare item pada pull ke-N.
   - *Average Pulls to Rare*: Jumlah pull rata-rata yang dibutuhkan untuk memicu satu rare item.
3. **Variabel Kontrol**: Probabilitas dasar (Base Probability = 0.6%), jumlah responden virtual (100.000), dan spesifikasi random number generator (RNG) yang digunakan pada mesin simulasi.

### D. Metrik Pengukuran dan Instrumen/Cara Ukur

Metrik pengujian diukur menggunakan metode komputasi statistik deskriptif dari data log simulasi.
- **Instrumen Ukur**: Penelitian menggunakan perangkat lunak prototype gacha simulator kustom yang dikembangkan menggunakan bahasa pemrograman Python. Prototype ini memiliki cumulative probability calculator bawaan untuk mencatat dan menghitung keluaran secara otomatis.
- **Cara Ukur Cumulative Probability**: Diukur dengan membagi jumlah iterasi sukses mendapatkan rare item pada atau sebelum pull ke-N dengan total sampel percobaan (100.000 iterasi). Hasil metrik ditampilkan dalam format persentase (%).
- **Cara Ukur Average Pulls**: Diukur dengan menjumlahkan seluruh pull yang dibutuhkan hingga sukses, lalu dibagi dengan total iterasi percobaan.

### E. Teknik Analisis, Asumsi, dan Validitas

Hasil penelitian dianalisis menggunakan perbandingan cumulative probability antara kondisi baseline dan intervention. Teknik analisis dilakukan dengan membandingkan perubahan peluang rare item pada jumlah pull tertentu. Untuk membuktikan signifikansi perbedaan secara kuantitatif, data log dari kedua kondisi akan diuji menggunakan uji komparatif statistik dua sampel tidak berpasangan (*Independent Sample T-Test*). Penelitian mengasumsikan bahwa parameter simulasi merepresentasikan sistem gacha modern secara umum. Ancaman validitas utama penelitian adalah keterbatasan simulasi yang belum sepenuhnya merepresentasikan seluruh mekanisme game gacha asli. Untuk mengurangi ancaman tersebut, penelitian menggunakan parameter probability dan pity system yang umum digunakan pada game gacha modern.

---

## HASIL YANG DIHARAPKAN

Penelitian ini diharapkan menghasilkan analisis evaluatif mengenai pengaruh weighted probability terhadap cumulative probability rare item pada sistem gacha game. Selain itu, penelitian juga diharapkan menghasilkan prototype simulasi sistem gacha dan dasar eksperimen yang dapat digunakan untuk penelitian lanjutan terkait algoritma probabilitas game modern.

---

## JADWAL PENELITIAN

| No | Nama kegiatan | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|:---|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | Identifikasi masalah dan topik | ✔ | ✔ | | | | | | |
| 2 | Literatur dan gap | | ✔ | ✔ | | | | | |
| 3 | RQ dan desain metode | | | ✔ | ✔ | | | | |
| 4 | Implementasi atau instrumen | | | | ✔ | ✔ | | | |
| 5 | Pengujian atau eksperimen | | | | | ✔ | ✔ | | |
| 6 | Analisis dan penulisan | | | | | | ✔ | ✔ | |
| 7 | Revisi final | | | | | | | ✔ | ✔ |

---

## DAFTAR PUSTAKA

Chen, C., & Fang, Z. (2023). Gacha game analysis and design. *Proceedings of the ACM on Measurement and Analysis of Computing Systems*, 7(1), 1-45.

Xiao, L. Y., Fraser, T. C., & Newall, P. W. (2023). Opening pandora’s loot box: Weak links between gambling and loot box expenditure in China, and player opinions on probability disclosures and pity-timers. *Journal of Gambling Studies*, 39(2), 645-668.

Gan, T. (2022). Gacha game: When prospect theory meets optimal pricing. *arXiv preprint arXiv:2208.03602*.

Han, J., Ryan, C. T., & Tong, X. T. (2026). Algorithms for loot box design. *Operations Research*.

Xiao, L. Y., Henderson, L. L., & Newall, P. W. (2023). What are the odds? Poor compliance with UK loot box probability disclosure industry self-regulation. *Plos one*, 18(9), e0286681.

Cokki, C., Maupa, H., Wanstum, W., & Sulaiman, S. (2025). Gacha Addiction and In-App Purchases: a Study on Genshin Impact Players in Indonesia. *Matrik: Jurnal Manajemen, Strategi Bisnis, dan Kewirausahaan*, 19(1).

Priyangga, R. Y., & Salehudin, I. (2025). Engagement and Consumption Behavior in Gacha Games: A PLS-SEM Study on Generation Z in Indonesia. *Journal of Games, Game Art, and Gamification*, 10(2), 65-73.

Han, J. W. (2025). Effects of Mobile Gacha Games on Gambling Behavior and Psychological Health. *arXiv preprint arXiv:2504.00057*.

Cao, R., Zhang, W., & Sun, F. (2024). Price discrimination in mobile gacha games: A comprehensive study of the scarcity–pricing, gachaing–user profiling, and recharging–profiting models. *Managerial and Decision Economics*, 45(6), 3716-3733.

Bakrie, N. O. M., Aditama, C., & Sanny, L. (2024). The art of the gacha lure: Determinants of the continuous use of mobile role-playing games (RPG) with gacha system in Indonesia. *JOURNAL OF APPLIED ENGINEERING AND TECHNOLOGICAL SCIENCE (JAETS) Учредители: Yayasan Riset dan Pengembangan Intelektual*, 6(1), 626-640.
