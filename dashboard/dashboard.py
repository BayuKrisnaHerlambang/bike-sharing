import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
df = pd.read_csv("main_data.csv")

# ini perubahan 1
# Streamlit UI
st.title("Dashboard Analisis Bike Sharing")
st.sidebar.header("Filter Data")

# Filter
season = st.sidebar.multiselect("Pilih Musim", df["season_label"].unique())
hour_range = st.sidebar.slider("Pilih Jam", min_value=int(df["hr"].min()), max_value=int(df["hr"].max()), value=(0, 23))

# Filter Data
filtered_df = df.copy()
if season:
    filtered_df = filtered_df[filtered_df["season_label"].isin(season)]
filtered_df = filtered_df[(filtered_df["hr"] >= hour_range[0]) & (filtered_df["hr"] <= hour_range[1])]

# Visualisasi
st.subheader("Total Peminjaman Sepeda per Musim")
fig, ax = plt.subplots()
sns.barplot(x="season_label", y="cnt", data=filtered_df, estimator=sum, palette="coolwarm", ax=ax)
ax.set_xlabel("Musim")
ax.set_ylabel("Total Peminjaman")
st.pyplot(fig)

st.subheader("Total Peminjaman Sepeda berdasarkan Jam")
fig, ax = plt.subplots()
sns.lineplot(x="hr", y="cnt", data=filtered_df, estimator=sum, marker="o", ax=ax)
ax.set_xlabel("Jam")
ax.set_ylabel("Total Peminjaman")
st.pyplot(fig)

st.write("\n\n**Insight:** Berdasarkan visualisasi, kita dapat melihat pola penggunaan sepeda berdasarkan musim dan jam tertentu.")
