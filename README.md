# Bike Sharing Dashboard

## Deskripsi Proyek

Proyek ini adalah analisis data peminjaman sepeda berdasarkan dataset Bike Sharing. Dashboard ini dibangun menggunakan Streamlit untuk memvisualisasikan tren peminjaman sepeda berdasarkan waktu, musim, cuaca, suhu, dan kecepatan angin.

## Fitur Dashboard

Tinjauan Data → Menampilkan ringkasan dataset. <p>
Visualisasi Tren Peminjaman → Grafik peminjaman berdasarkan waktu (jam, hari, musim). <p>
Pengaruh Cuaca terhadap Peminjaman → Boxplot peminjaman berdasarkan kondisi cuaca. <p>
Distribusi Berdasarkan Suhu & Kecepatan Angin → Filter interaktif untuk eksplorasi data. <p>

## Hasil Analisis

### Tren Peminjaman Berdasarkan Waktu

- Peminjaman sepeda meningkat pada jam sibuk (07:00 - 09:00 & 17:00 - 19:00), menandakan pola commuting.

- Akhir pekan memiliki pola peminjaman lebih santai dan menyebar sepanjang hari.

### Pengaruh Musim terhadap Peminjaman

- Peminjaman tertinggi terjadi di musim panas dan gugur.

- Musim dingin memiliki peminjaman terendah, kemungkinan karena cuaca ekstrem.

### Pengaruh Cuaca terhadap Peminjaman

- Cuaca cerah memiliki jumlah peminjaman tertinggi.

- Saat hujan atau kabut, jumlah peminjaman turun drastis.

### Pengaruh Suhu dan Kecepatan Angin

- Peminjaman meningkat pada suhu yang lebih hangat (~20-30°C).

- Kecepatan angin tinggi tidak berpengaruh signifikan terhadap peminjaman.

## Hasil Clustering

### Clustering Berdasarkan Permintaan Sepeda:

- Kategori High Demand memiliki jumlah peminjaman jauh lebih tinggi dibanding Medium dan Low Demand.

- Permintaan sepeda tertinggi terjadi pada jam sibuk dan musim panas.

### Clustering Berdasarkan Suhu:

- Suhu hangat dan panas memiliki jumlah peminjaman tertinggi.

- Suhu dingin menyebabkan penurunan signifikan dalam peminjaman.

### Clustering Berdasarkan Kecepatan Angin:

- Kecepatan angin tidak memiliki dampak signifikan terhadap jumlah peminjaman.

- Peminjaman sedikit lebih rendah pada kategori Tinggi, tetapi tidak terlalu berbeda dibanding Sedang dan Rendah.
