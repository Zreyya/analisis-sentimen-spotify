import pandas as pd
import re
import pickle

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# ======================================================
# STEP 1 : LOAD DATASET
# ======================================================
df = pd.read_csv("ulasan_com.spotify.music.csv")

# Menghapus data kosong
df = df.dropna(subset=["Ulasan", "Rating"])

print("Dataset berhasil dimuat")
print("Jumlah data :", len(df))

# ======================================================
# STEP 2 : PELABELAN SENTIMEN
# ======================================================
# Rating 4-5 = Positif
# Rating 1-2 = Negatif
# Rating 3 dihapus

df = df[df["Rating"] != 3]

df["Sentimen"] = df["Rating"].apply(lambda x: 1 if x > 3 else 0)

print(df["Sentimen"].value_counts())

# ======================================================
# STEP 3 : PREPROCESSING
# ======================================================
def preprocessing(teks):
    teks = str(teks).lower()
    teks = re.sub(r'[^a-zA-Z0-9\s]', ' ', teks)
    teks = re.sub(r'\s+', ' ', teks).strip()
    return teks

df["Ulasan_Clean"] = df["Ulasan"].apply(preprocessing)

# ======================================================
# STEP 4 : TRAIN TEST SPLIT
# ======================================================
X = df["Ulasan_Clean"]
y = df["Sentimen"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("Data Training :", len(X_train))
print("Data Testing  :", len(X_test))

# ======================================================
# STEP 5 : TF-IDF
# ======================================================
vectorizer = TfidfVectorizer(
    max_features=5000
)

X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# ======================================================
# STEP 6 : TRAINING MODEL
# ======================================================
model_nb = MultinomialNB()

model_nb.fit(X_train_vec, y_train)

print("Training selesai.")

# ======================================================
# STEP 7 : EVALUASI
# ======================================================
y_pred = model_nb.predict(X_test_vec)

print("\nClassification Report")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix")
print(confusion_matrix(y_test, y_pred))

akurasi = accuracy_score(y_test, y_pred)

print(f"\nAkurasi : {akurasi*100:.2f}%")

# ======================================================
# STEP 8 : SIMPAN MODEL
# ======================================================
pickle.dump(model_nb, open("model_nb.pkl", "wb"))
pickle.dump(vectorizer, open("tfidf.pkl", "wb"))

print("\nModel berhasil disimpan.")
print("File model_nb.pkl berhasil dibuat.")
print("File tfidf.pkl berhasil dibuat.")