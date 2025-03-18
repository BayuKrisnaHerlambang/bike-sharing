import os
import pandas as pd
import streamlit as st

# Path ke main_data.csv
file_path = os.path.join(os.path.dirname(__file__), "main_data.csv")

# Cek apakah file tersedia sebelum membacanya
if os.path.exists(file_path):
    df = pd.read_csv(file_path)
else:
    st.error(f"❌ File tidak ditemukan: {file_path}. Pastikan file sudah diupload.")
    st.stop()  # Hentikan eksekusi jika file tidak ditemukan

# Tampilan di Streamlit
st.title("📊 Bike Sharing Dashboard")
st.write("Selamat datang di dashboard analisis peminjaman sepeda!")

# Menampilkan beberapa baris pertama data
st.subheader("🔍 Tinjauan Data")
st.write(df.head())

# Visualisasi jumlah peminjaman berdasarkan jam
st.subheader("⏰ Jumlah Peminjaman Berdasarkan Jam")
import matplotlib.pyplot as plt
import seaborn as sns

fig, ax = plt.subplots(figsize=(10,5))
sns.lineplot(x='hr', y='cnt', data=df, ax=ax)
plt.xlabel("Jam")
plt.ylabel("Jumlah Peminjaman")
st.pyplot(fig)
