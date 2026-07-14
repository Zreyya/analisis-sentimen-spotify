# 🎵 Analisis Sentimen Ulasan Spotify

Aplikasi ini merupakan implementasi **Analisis Sentimen** terhadap ulasan pengguna aplikasi Spotify menggunakan algoritma **Multinomial Naive Bayes** dan metode ekstraksi fitur **TF-IDF**. Aplikasi dibangun menggunakan **Python** dan **Streamlit** sehingga dapat digunakan secara interaktif melalui web.

---

## 📌 Deskripsi

Analisis sentimen bertujuan untuk mengklasifikasikan suatu ulasan ke dalam dua kategori, yaitu:

- 😊 **Positif**
- 😠 **Negatif**

Model dilatih menggunakan dataset ulasan aplikasi Spotify dari Google Play Store.

---

## 🚀 Teknologi yang Digunakan

- Python 3.14
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Pickle

---

## 🤖 Algoritma Machine Learning

- **Algoritma** : Multinomial Naive Bayes
- **Ekstraksi Fitur** : TF-IDF (Term Frequency - Inverse Document Frequency)

---

## 📊 Dataset

Dataset yang digunakan merupakan dataset ulasan aplikasi Spotify yang berjumlah sekitar **100.000 ulasan**.

Pelabelan sentimen dilakukan berdasarkan rating:

| Rating | Sentimen |
|--------|----------|
| 4 - 5 | Positif |
| 1 - 2 | Negatif |
| 3 | Tidak digunakan |

---

## 📈 Hasil Pengujian

Hasil evaluasi model:

- **Accuracy** : **92.16%**

Model dievaluasi menggunakan:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

---

## 📂 Struktur Project

```
Sentimen-Spotify/
│
├── app.py
├── train_model.py
├── model_nb.pkl
├── tfidf.pkl
├── requirements.txt
├── ulasan_com.spotify.music.csv
└── README.md
```

---

## ▶️ Cara Menjalankan

### 1. Clone Repository

```bash
git clone https://github.com/username/Sentimen-Spotify.git
```

### 2. Masuk ke Folder Project

```bash
cd Sentimen-Spotify
```

### 3. Install Library

```bash
pip install -r requirements.txt
```

### 4. Jalankan Aplikasi

```bash
streamlit run app.py
```

---

## 💻 Tampilan Aplikasi

Aplikasi menyediakan fitur:

- Input teks ulasan Spotify
- Analisis sentimen secara otomatis
- Menampilkan hasil Positif atau Negatif

---

## 👨‍💻 Kelompok Penelitian

Proyek ini dikembangkan oleh:

| Nama | NIM |
|------|------|
| HAYDAR RAFA SATYA PUTRA | A11.2024.15700 |
| HANDIKA | A11.2024.15755 |
| MUHAMMAD DITA ADINATA | A11.2024.15695 |
| RIO VERNANDA SAPUTRA | A11.2024.15749 |
| ARYA EKA | A11.2024.15782 |

# 🎵 Analisis Sentimen Ulasan Spotify

Proyek ini merupakan implementasi analisis sentimen terhadap ulasan pengguna aplikasi Spotify menggunakan algoritma **Multinomial Naive Bayes** dan metode ekstraksi fitur **TF-IDF**.

**Mata Kuliah:** Pembelajaran Mesin  
**Program Studi:** Teknik Informatika  
**Universitas:** Universitas Dian Nuswantoro

---

## 📄 Lisensi

Project ini dibuat untuk keperluan pembelajaran dan penelitian.