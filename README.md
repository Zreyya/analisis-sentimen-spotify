# 🎵 Analisis Sentimen Spotify

Proyek ini bertujuan untuk melakukan analisis sentimen terhadap ulasan atau komentar pengguna mengenai aplikasi Spotify. Dengan menggunakan teknik Pemrosesan Bahasa Alami (Natural Language Processing / NLP) dan Machine Learning, proyek ini mengklasifikasikan opini pengguna menjadi sentimen **Positif**, **Netral**, atau **Negatif**.

## 📌 Latar Belakang
Spotify adalah salah satu platform streaming musik terbesar di dunia. Memahami sentimen pengguna dari ulasan (misalnya dari Google Play Store, App Store, atau Twitter) sangat penting untuk melihat tingkat kepuasan pelanggan, mengidentifikasi *bug*, serta menemukan fitur yang paling disukai atau perlu ditingkatkan.

## 🚀 Fitur Utama
- **Pengumpulan Data**: Dataset ulasan Spotify.
- **Pra-pemrosesan Teks (Text Preprocessing)**: Pembersihan teks dengan menghapus simbol, emoji, dan tanda baca, serta *Case Folding*.
- **Pemodelan Machine Learning**: Menggunakan algoritma klasifikasi Naive Bayes (MultinomialNB).
- **Evaluasi Model**: Metrik performa berupa *Accuracy* dan *Classification Report*.

## 🛠️ Teknologi & Library yang Digunakan
- **Bahasa Pemrograman**: Python 3.x
- **Pengolahan Data**: Pandas, NumPy, Regex
- **Machine Learning & NLP**: Scikit-learn
- **Environment**: Jupyter Notebook / Google Colab

## 🌐 Demo Aplikasi
Aplikasi analisis sentimen ini telah di-deploy menjadi aplikasi web interaktif menggunakan Streamlit. Kamu bisa langsung mencoba memprediksi sentimen ulasan Spotify melalui tautan berikut:

👉 **[Coba Aplikasi Sentimen Spotify di Sini](https://sentimen-spotify-kel2.streamlit.app/)**

## 📂 Struktur Repositori
```text
analisis-sentimen-spotify/
│
├── mesin_spotify.ipynb      # Eksperimen model dan analisis data
└── README.md                # Dokumentasi proyek
