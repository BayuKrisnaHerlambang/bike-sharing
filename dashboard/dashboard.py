import os
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

file_path = os.path.join(os.path.dirname(__file__), "main_data.csv")

if os.path.exists(file_path):
    df = pd.read_csv(file_path)
else:
    st.error(f"File tidak ditemukan: {file_path}. Pastikan file sudah diupload.")
    st.stop()  

st.title("📊 Bike Sharing Dashboard")
st.write("Selamat datang di dashboard analisis peminjaman sepeda!")

st.subheader("🔍 Tinjauan Data")
st.write(df.head())

st.subheader("📈 Statistik Peminjaman Sepeda")
st.write(df[['cnt', 'season_label', 'weathersit']].groupby(['season_label', 'weathersit']).mean().reset_index())

st.subheader("⏰ Tren Peminjaman Berdasarkan Waktu")
fig, ax = plt.subplots(figsize=(10,5))
sns.lineplot(x='hr', y='cnt', data=df, ax=ax)
plt.xlabel("Jam")
plt.ylabel("Jumlah Peminjaman")
st.pyplot(fig)

st.subheader("🌦️ Pengaruh Cuaca terhadap Peminjaman")
fig, ax = plt.subplots(figsize=(8,5))
sns.boxplot(x='weathersit', y='cnt', data=df, palette='coolwarm')
st.pyplot(fig)

st.subheader("🔥 Distribusi Peminjaman Berdasarkan Suhu & Angin")
option = st.selectbox("Pilih Kategori", ['temp_category', 'wind_category'])
fig, ax = plt.subplots(figsize=(8,5))
sns.boxplot(x=option, y='cnt', data=df, palette='coolwarm')
st.pyplot(fig)

st.write("\n\n**Insight:** Berdasarkan analisis, peminjaman sepeda sangat dipengaruhi oleh musim, cuaca, suhu, dan jam tertentu.")
