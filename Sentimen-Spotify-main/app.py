import streamlit as st
import pickle
import re

# ==========================
# LOAD MODEL
# ==========================
model = pickle.load(open("model_nb.pkl", "rb"))
vectorizer = pickle.load(open("tfidf.pkl", "rb"))

# ==========================
# PREPROCESSING
# ==========================
def preprocessing(teks):
    teks = str(teks).lower()
    teks = re.sub(r'[^a-zA-Z0-9\s]', ' ', teks)
    teks = re.sub(r'\s+', ' ', teks).strip()
    return teks

# ==========================
# KONFIGURASI HALAMAN
# ==========================
st.set_page_config(
    page_title="Analisis Sentimen Spotify",
    page_icon="🎵",
    layout="centered"
)

# ==========================
# HEADER
# ==========================
st.title("🎵 Analisis Sentimen Ulasan Spotify")

st.markdown("""
Aplikasi ini dibuat untuk **menganalisis sentimen ulasan pengguna Spotify**
menggunakan algoritma **Multinomial Naive Bayes** dan ekstraksi fitur
**TF-IDF**.
""")

st.info("""
📊 **Informasi Model**

- Algoritma : Multinomial Naive Bayes
- Ekstraksi Fitur : TF-IDF
- Dataset : 100.000 ulasan Spotify
- Akurasi Model : **92,16%**
""")

st.divider()

# ==========================
# INPUT
# ==========================
ulasan = st.text_area(
    "✍️ Masukkan Ulasan Spotify",
    placeholder="Contoh: Spotify sangat bagus dan lagunya lengkap...",
    height=170
)

# ==========================
# PREDIKSI
# ==========================
if st.button("🔍 Analisis Sentimen", use_container_width=True):

    if ulasan.strip() == "":
        st.warning("Silakan masukkan ulasan terlebih dahulu.")
    else:

        teks = preprocessing(ulasan)
        data = vectorizer.transform([teks])
        hasil = model.predict(data)

        st.divider()

        st.subheader("📈 Hasil Analisis")

        if hasil[0] == 1:
            st.success("😊 Sentimen Positif")
            st.balloons()

            st.write("""
Ulasan yang Anda masukkan menunjukkan kecenderungan **positif** terhadap aplikasi Spotify.
            """)

        else:
            st.error("😠 Sentimen Negatif")

            st.write("""
Ulasan yang Anda masukkan menunjukkan kecenderungan **negatif** terhadap aplikasi Spotify.
            """)

st.divider()

st.caption("© 2026 | Analisis Sentimen Spotify menggunakan Naive Bayes")