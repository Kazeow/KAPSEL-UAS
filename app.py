import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Setel tema Streamlit
st.set_page_config(
    page_title="Student Mental Health Analysis",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Judul aplikasi
st.title("📊 Student Mental Health Analysis")
st.markdown("Aplikasi ini menganalisis **kesehatan mental mahasiswa** berdasarkan data survei.")

# Sidebar navigasi
with st.sidebar:
    st.header("🔍 Navigasi")
    page = st.radio("Pilih Analisis", [
        "📋 Dataset Overview",
        "📈 Visualisasi Umur",
        "🎯 Gender Distribution",
        "🤯 Anxiety & Depression Analysis",
        "📊 Panic Attack vs CGPA"
    ])
    st.info("Gunakan sidebar untuk menavigasi analisis.")

# Load dataset
if os.path.exists("StudentMentalhealth.csv"):
    data = pd.read_csv("StudentMentalhealth.csv")
    data.rename(columns={'Choose your gender': 'gender'}, inplace=True)

    if page == "📋 Dataset Overview":
        # Menampilkan dataset
        st.subheader("📋 Dataset Overview")
        st.dataframe(data)
        st.write("### Informasi Dataset")
        st.write(f"- Dimensi Dataset: {data.shape}")
        st.write("- **Jumlah Nilai Kosong per Kolom:**")
        st.write(data.isnull().sum())
        st.success("Dataset berhasil dimuat dan diperiksa!")

    elif page == "📈 Visualisasi Umur":
        # Distribusi umur
        st.subheader("📈 Distribusi Umur")
        fig, ax = plt.subplots(figsize=(6, 4))  # Ukuran kecil
        ax.hist(data['Age'], bins=10, color='#4CAF50', edgecolor='black', alpha=0.8)
        ax.set_title("Distribusi Umur", fontsize=12)
        ax.set_xlabel("Umur")
        ax.set_ylabel("Frekuensi")
        st.pyplot(fig)

    elif page == "🎯 Gender Distribution":
        # Distribusi gender
        st.subheader("🎯 Distribusi Gender")
        fig, ax = plt.subplots(figsize=(5, 5))  # Ukuran kecil
        data['gender'].value_counts().plot.pie(
            ax=ax,
            autopct='%1.1f%%',
            colors=['#FF9999', '#66B3FF'],
            startangle=140,
            explode=(0.1, 0),
            textprops={'fontsize': 10}
        )
        ax.set_ylabel("")
        ax.set_title("Proporsi Gender", fontsize=12)
        st.pyplot(fig)

    elif page == "🤯 Anxiety & Depression Analysis":
        # Anxiety berdasarkan gender
        st.subheader("🤯 Anxiety Berdasarkan Gender")
        fig, ax = plt.subplots(figsize=(6, 4))  # Ukuran kecil
        sns.countplot(y="Do you have Anxiety?", hue="gender", data=data, palette="coolwarm", ax=ax)
        ax.set_title("Anxiety Berdasarkan Gender", fontsize=12)
        ax.set_xlabel("Jumlah")
        ax.set_ylabel("Anxiety")
        st.pyplot(fig)

        # Depression berdasarkan gender
        st.subheader("😔 Depression Berdasarkan Gender")
        fig, ax = plt.subplots(figsize=(6, 4))  # Ukuran kecil
        sns.countplot(y="Do you have Depression?", hue="gender", data=data, palette="coolwarm", ax=ax)
        ax.set_title("Depression Berdasarkan Gender", fontsize=12)
        ax.set_xlabel("Jumlah")
        ax.set_ylabel("Depression")
        st.pyplot(fig)

    elif page == "📊 Panic Attack vs CGPA":
        # Panic attack vs CGPA
        st.subheader("📊 Panic Attack Berdasarkan CGPA")
        fig, ax = plt.subplots(figsize=(6, 4))  # Ukuran kecil
        sns.countplot(x="Do you have Panic attack?", hue="What is your CGPA?", data=data, palette="plasma", ax=ax)
        ax.set_title("Panic Attack Berdasarkan CGPA", fontsize=12)
        ax.set_xlabel("Panic Attack")
        ax.set_ylabel("Jumlah")
        st.pyplot(fig)

else:
    st.error("❌ File 'StudentMentalhealth.csv' tidak ditemukan. Pastikan file ada di direktori yang benar!")
