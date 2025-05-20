# jaya-jaya-dropout-prediction

Proyek **jaya-jaya-dropout-prediction** adalah pipeline data science end-to-end untuk memprediksi kemungkinan mahasiswa melakukan dropout di Jaya Jaya Institut. Proyek ini mencakup beberapa tahapan utama:

## Fitur Proyek

- **Eksplorasi Data (EDA):** Analisis awal untuk memahami pola dan karakteristik data mahasiswa.
- **Pra-pemrosesan Data:** Penanganan data hilang, encoding, dan normalisasi fitur.
- **Pemodelan:** Implementasi beberapa algoritma machine learning seperti Logistic Regression, Random Forest, dan XGBoost untuk prediksi dropout.
- **Evaluasi Model:** Pengukuran performa model menggunakan metrik seperti ROC/AUC.
- **Interpretasi Model:** Analisis interpretabilitas model menggunakan SHAP untuk memahami faktor-faktor utama yang mempengaruhi prediksi.
- **Aplikasi Streamlit:** Aplikasi web interaktif untuk melakukan prediksi dropout secara langsung.
- **Dashboard Metabase:** Visualisasi KPI utama terkait dropout mahasiswa untuk monitoring dan pengambilan keputusan.

## Cara Menjalankan

1. **Klon repositori ini:**
    ```bash
    git clone https://github.com/username/jaya-jaya-dropout-prediction.git
    cd jaya-jaya-dropout-prediction
    ```
2. **Instal dependensi:**
    ```bash
    pip install -r requirements.txt
    ```
3. **Jalankan aplikasi Streamlit:**
    ```bash
    streamlit run app.py
    ```

## Struktur Direktori

- `notebooks/` — Notebook EDA dan eksperimen model
- `src/` — Script utama untuk preprocessing dan training
- `app.py` — Aplikasi Streamlit
- `dashboard/` — File terkait dashboard Metabase

## Kontribusi

Kontribusi sangat terbuka! Silakan buat issue atau pull request untuk perbaikan atau penambahan fitur.

## Lisensi

Proyek ini menggunakan lisensi MIT.

