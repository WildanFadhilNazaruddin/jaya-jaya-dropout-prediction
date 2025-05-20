import streamlit as st
import pickle
import numpy as np

# Load model
with open('submission/model/random_forest_model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("Prediksi Status Mahasiswa (Dropout/Graduate/Enrolled)")

# Hanya input fitur yang digunakan model (11 fitur)
course = st.number_input("Kode Program Studi", min_value=1, max_value=9999, value=9500)
daytime_evening_attendance = st.selectbox("Waktu Kuliah", [1,0], format_func=lambda x: 'Siang' if x==1 else 'Malam')
admission_grade = st.number_input("Nilai Masuk", min_value=0.0, max_value=200.0, value=120.0)
educational_special_needs = st.selectbox("Berkebutuhan Khusus?", [1,0], format_func=lambda x: 'Ya' if x==1 else 'Tidak')
debtor = st.selectbox("Memiliki Tunggakan?", [1,0], format_func=lambda x: 'Ya' if x==1 else 'Tidak')
tuition_fees_up_to_date = st.selectbox("Pembayaran Kuliah Lunas?", [1,0], format_func=lambda x: 'Ya' if x==1 else 'Tidak')
gender = st.selectbox("Jenis Kelamin", [1,0], format_func=lambda x: 'Laki-laki' if x==1 else 'Perempuan')
scholarship_holder = st.selectbox("Penerima Beasiswa?", [1,0], format_func=lambda x: 'Ya' if x==1 else 'Tidak')
age_at_enrollment = st.number_input("Usia Saat Mendaftar", min_value=15, max_value=70, value=20)
curr_1st_sem_grade = st.number_input("Nilai Rata-rata Semester 1", min_value=0.0, max_value=20.0, value=12.0)
curr_2nd_sem_grade = st.number_input("Nilai Rata-rata Semester 2", min_value=0.0, max_value=20.0, value=12.0)

if st.button("Prediksi Status Mahasiswa"):
    fitur = np.array([[
        course, daytime_evening_attendance, admission_grade, educational_special_needs, debtor,
        tuition_fees_up_to_date, gender, scholarship_holder, age_at_enrollment,
        curr_1st_sem_grade, curr_2nd_sem_grade
    ]])
    hasil = model.predict(fitur)
    label_status = {0: "Dropout", 1: "Enrolled", 2: "Graduate"}
    st.success(f"Status Prediksi Mahasiswa: {label_status.get(hasil[0], 'Tidak diketahui')}")