# 🎓 Proyek Akhir: Prediksi Dropout Mahasiswa Perguruan Tinggi

## 🏢 Business Understanding

Jaya Jaya Maju adalah institusi pendidikan tinggi yang menaungi berbagai program studi seperti agronomi, desain, pendidikan, keperawatan, jurnalisme, manajemen, pelayanan sosial, dan teknologi. Meskipun telah berkembang pesat, institusi ini menghadapi tantangan serius terkait tingginya angka mahasiswa yang keluar (dropout). Tingginya dropout rate dapat berdampak pada reputasi, efektivitas pendidikan, dan efisiensi operasional kampus.

Untuk mengatasi masalah ini, tim manajemen meminta bantuan untuk mengidentifikasi faktor-faktor utama yang memengaruhi risiko dropout mahasiswa serta membangun sistem prediksi dan dashboard monitoring berbasis data.

---

## ❓ Permasalahan Bisnis

Institusi menghadapi masalah dropout mahasiswa yang cukup tinggi. Dari total 4.425 mahasiswa, dropout rate mencapai 32,11%. Hal ini berdampak pada kualitas lulusan, efisiensi sumber daya, dan citra institusi. Diperlukan analisis mendalam untuk memahami faktor-faktor utama penyebab dropout dan solusi prediktif untuk meminimalisirnya.

---

## 📋 Cakupan Proyek

- 📈 Analisis data mahasiswa untuk memahami pola dan faktor yang memengaruhi dropout.
- 🤖 Pengembangan model machine learning untuk memprediksi risiko dropout.
- 📊 Pembuatan dashboard interaktif untuk visualisasi dan monitoring faktor dropout.
- 💡 Memberikan rekomendasi actionable bagi institusi berdasarkan hasil analisis.

---

## 🛠️ Persiapan

### Sumber Data

Dataset yang digunakan adalah `data.csv`, berisi data mahasiswa Jaya Jaya Maju dengan fitur demografi, akademik, dan sosial-ekonomi.  
Sumber dataset: [https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv)

### Setup Environment

**Menggunakan Anaconda:**
```bash
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```

**Menggunakan Pipenv:**
```bash
pip install pipenv
pipenv install
pipenv shell
pip install -r requirements.txt
```

### Menjalankan Notebook Analisis

Buka dan jalankan notebook analisis di:

- `model/model.ipynb`
---

## 📊 Business Dashboard

Dashboard dibuat menggunakan Metabase untuk membantu manajemen memonitor faktor-faktor utama dropout, seperti usia, nilai masuk, gender, status pernikahan, dan performa akademik. Dashboard menampilkan visualisasi interaktif yang memudahkan pengambilan keputusan.

**File database Metabase:**  
[metabase.db.mv.db](http://_vscodecontentref_/1)
### Cara Menjalankan Aplikasi Streamlit

#### ✅ Menjalankan Secara Lokal

1. Pastikan environment sudah aktif dan dependensi sudah terinstall.
2. Jalankan perintah berikut di terminal:
  ```bash
  streamlit run app.py
  ```
3. Buka browser dan akses: [http://localhost:8501](http://localhost:8501)

#### 🌐 Mengakses Demo Online (Claude)

Aplikasi juga dapat diakses secara online melalui tautan berikut:  
[https://jaya-jaya-dropout-prediction-ffanpntlcjvxcwzsytrmkc.streamlit.app/](https://jaya-jaya-dropout-prediction-ffanpntlcjvxcwzsytrmkc.streamlit.app/)
### Cara Mengakses Dashboard Metabase

#### ✅ Melalui Antarmuka Web (Metabase Lokal dengan Docker)

1. Pastikan file database Metabase (`metabase.db.mv.db`) sudah ada di direktori `/submission/`.
2. Jalankan Metabase menggunakan Docker:
    ```bash
    docker run -d -p 3000:3000 \
      -v $(pwd)/submission:/metabase-data \
      -e "MB_DB_FILE=/metabase-data/metabase.db.mv.db" \
      --name metabase metabase/metabase
    ```
3. Buka browser dan akses: [http://localhost:3000](http://localhost:3000)  
   Login:  
   - Email: `root@mail.com`  
   - Password: `root123`
4. Navigasi ke menu Dashboard untuk melihat visualisasi.

#### 🖥️ Melalui API Metabase

- **Autentikasi (Mendapatkan Token Session):**
    ```bash
    curl -X POST http://localhost:3000/api/session \
      -H "Content-Type: application/json" \
      -d '{"username":"232153079@student.unsil.ac.id","password":"KsXV6Trq$C8L5uB"}'
    ```
- **Mendapatkan Daftar Dashboard:**
    ```bash
    curl -X GET http://localhost:3000/api/dashboard \
      -H "X-Metabase-Session: your_token"
    ```
  Ganti `your_token` dengan token session dari langkah sebelumnya.

- **Menampilkan Data JSON dengan jq (opsional):**
    ```bash
    curl -X GET http://localhost:3000/api/dashboard \
      -H "X-Metabase-Session: your_token" | jq
    ```

> **Catatan Penting:**  
> - Pastikan Metabase sudah berjalan dan file database sudah terhubung.  
> - Jika ada error, cek log Metabase.

---

## 📝 Conclusion

Berdasarkan analisis data dan pemodelan, ditemukan beberapa faktor utama yang berkontribusi terhadap tingginya dropout rate di Jaya Jaya Maju, antara lain:

- Nilai masuk (admission grade)
- Usia saat mendaftar
- Gender dan status pernikahan
- Performa akademik semester 1 & 2
- Status beasiswa dan ekonomi

Model prediksi yang dikembangkan dapat membantu institusi dalam mengidentifikasi mahasiswa berisiko tinggi dropout, sehingga intervensi dapat dilakukan lebih dini.

---

## ⚡ Rekomendasi Action Items

### Peningkatan Program Retensi Mahasiswa 🏆

Fokus pada peningkatan motivasi belajar dan dukungan psikologis, terutama bagi mahasiswa dengan nilai masuk rendah atau performa akademik menurun.

### Pengembangan Karir dan Bimbingan Akademik 📚

Sediakan program pengembangan karir dan bimbingan belajar untuk meningkatkan loyalitas dan motivasi mahasiswa.

### Monitoring Berkelanjutan 📈

Gunakan dashboard secara rutin untuk memonitor faktor-faktor dropout dan melakukan evaluasi kebijakan pendidikan secara berkala.

---

**Wildan Fadhil Nazaruddin**