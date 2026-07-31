import streamlit as st
import pandas as pd

# Konfigurasi halaman Streamlit
st.set_page_config(
    page_title="Jadwal & Jurnal Bina Prestasi BPIBS",
    page_icon="📚",
    layout="wide"
)

# Judul Utama Web
st.title("📚 Bina Prestasi SMA BPIBS")
st.markdown("Tahun Pelajaran 2026/2027 — Sistem Jurnal Mengajar & Rekapitulasi")

# Menu Navigasi di Sidebar
menu = st.sidebar.selectbox("Pilih Menu", [
    "📝 Input Jurnal & Absensi", 
    "📊 Rekapitulasi Jurnal", 
    "📅 Jadwal Pelajaran",
    "🏆 Rekap Hasil Lomba",
    "🎯 Prediksi Nilai & Jurusan"
])

# ================= MENU 1: INPUT JURNAL =================
if menu == "📝 Input Jurnal & Absensi":
    st.subheader("Form Jurnal & Presensi Mengajar")
    st.write("Silakan isi jurnal dan absensi mengajar melalui Google Form di bawah ini:")
    
    # Menampilkan Google Form secara langsung (embedded iframe)
    google_form_url = "https://forms.gle/cotZpQoxS4CxxKDr6"
    st.markdown(f'<iframe src="{google_form_url}" width="100%" height="800px" frameborder="0" marginheight="0" marginwidth="0">Memuat…</iframe>', unsafe_allow_html=True)
    
    st.markdown("---")
    st.write("Atau klik tombol berikut jika form di atas tidak muncul:")
    st.link_button("Buka Google Form Jurnal & Absensi", google_form_url)

# ================= MENU 2: REKAPITULASI JURNAL =================
elif menu == "📊 Rekapitulasi Jurnal":
    st.subheader("Rekapitulasi Jurnal & Kegiatan Mengajar")
    st.write("Berikut adalah daftar seluruh jurnal mengajar yang terhubung dari Google Sheets.")

    if st.button("🔄 Muat Ulang Data Jurnal"):
        st.rerun()

    try:
        sheet_id_jurnal = "1JeHrxcJBPG-mzqOsHinefcsbtoMsEBLtf6RAkoFYyH0"
        csv_url_jurnal = f"https://docs.google.com/spreadsheets/d/{sheet_id_jurnal}/export?format=csv"
        
        df_jurnal = pd.read_csv(csv_url_jurnal)
        
        if not df_jurnal.empty:
            st.dataframe(df_jurnal, use_container_width=True)
            st.info(f"Total jurnal tercatat: {len(df_jurnal)} baris.")
        else:
            st.info("File Google Sheet rekap jurnal saat ini masih kosong.")
            
    except Exception as e:
        st.error(f"Gagal memuat data rekap dari Google Drive. Pastikan link Google Sheet sudah disetel 'Anyone with the link can view'. (Error: {e})")

# ================= MENU 3: JADWAL PELAJARAN =================
elif menu == "📅 Jadwal Pelajaran":
    st.subheader("Jadwal Bina Prestasi SMA BPIBS")
    
    tab1, tab2 = st.tabs(["🧔 Ikhwan", "🧕 Akhwat"])
    
    with tab1:
        st.markdown("#### Kelompok Ikhwan")
        data_ikhwan = [
            {"JP": "JP 3", "X.1": "Kimia (Ust. Andi)", "X.2": "Informatika (Ust. Bayu)", "XI.1": "-", "XI.2": "-"},
            {"JP": "JP 4", "X.1": "Bahasa Inggris (Ust. Moechlis)", "X.2": "Bahasa Arab (Ust. Habib)", "XI.1": "-", "XI.2": "-"},
            {"JP": "JP 5", "X.1": "Biologi (Ust. Amir)", "X.2": "Fisika (Ust. Mardanih)", "XI.1": "Ekonomi (Ust. Gunawan)", "XI.2": "Matematika (Ust. Rusdi)"}
        ]
        st.table(pd.DataFrame(data_ikhwan))
        
    with tab2:
        st.markdown("#### Kelompok Akhwat")
        data_akhwat = [
            {"JP": "JP 3", "X.3": "Matematika (Ustadzah Hasri)", "X.4": "Kimia (Ustadzah Vetty)", "XI.3": "-", "XI.4": "-"},
            {"JP": "JP 4", "X.3": "Biologi (Ustadzah Windy)", "X.4": "Fisika (Ustadzah Erlina)", "XI.3": "-", "XI.4": "-"},
            {"JP": "JP 5", "X.3": "Diniyah (Ustadzah Nanda)", "X.4": "Bahasa Indonesia (Ustadzah Yullie)", "XI.3": "Ekonomi (Ustadzah Nashibah)", "XI.4": "Matematika (Ustadzah Hasri)"}
        ]
        st.table(pd.DataFrame(data_akhwat))

# ================= MENU 4: REKAP HASIL LOMBA =================
elif menu == "🏆 Rekap Hasil Lomba":
    st.subheader("🏆 Rekapitulasi Hasil Lomba")
    st.write("Berikut adalah data rekap hasil lomba yang terhubung langsung dari Google Drive.")

    if st.button("🔄 Muat Ulang Data Lomba"):
        st.rerun()

    try:
        sheet_id_lomba = "1ANrCscXUyYv3oh-WSbTVfSptcc7iqDfJggjun6ec5Z4"
        csv_url_lomba = f"https://docs.google.com/spreadsheets/d/{sheet_id_lomba}/export?format=csv"
        
        df_lomba = pd.read_csv(csv_url_lomba)
        
        if not df_lomba.empty:
            st.dataframe(df_lomba, use_container_width=True)
            st.info(f"Total data lomba tercatat: {len(df_lomba)} baris.")
        else:
            st.info("File Google Sheet lomba saat ini masih kosong.")
            
    except Exception as e:
        st.error(f"Gagal memuat data dari Google Drive. Pastikan link Google Sheet sudah disetel 'Anyone with the link can view'. (Error: {e})")


# ================= MENU 5: PREDIKSI NILAI & JURUSAN =================
elif menu == "🎯 Prediksi Nilai & Jurusan":
    st.subheader("🎯 Simulasi & Prediksi Peluang Jurusan PTN / Peminatan")
    st.write("Gunakan simulasi ini untuk memetakan estimasi peluang berdasarkan rata-rata nilai akademik atau hasil tryout siswa.")

    with st.form("prediksi_form"):
        col1, col2 = st.columns(2)
        with col1:
            nama_siswa = st.text_input("Nama Siswa", placeholder="Contoh: Ahmad")
            pilihan_jurusan = st.text_input("Target Jurusan / Program Studi", placeholder="Contoh: Kedokteran / Teknik Informatika")
        with col2:
            ptn_tujuan = st.text_input("Target Perguruan Tinggi (PTN)", placeholder="Contoh: Universitas Indonesia / ITB")
            rata_nilai = st.number_input("Rata-rata Nilai / Skor Tryout (Skala 0 - 1000 atau 0 - 100)", min_value=0.0, max_value=1000.0, value=750.0)
        
        submitted_prediksi = st.form_submit_button("Analisis & Prediksi Peluang")

        if submitted_prediksi:
            st.markdown("---")
            st.markdown(f"### Hasil Analisis untuk: **{nama_siswa}**")
            st.write(f"🎯 **Target:** {pilihan_jurusan} di {ptn_tujuan}")
            st.write(f"📊 **Skor/Nilai Masukan:** {rata_nilai}")

            # Logika Simulasi Sederhana (Bisa disesuaikan standarnya)
            if rata_nilai >= 800:
                st.success("🔥 **Peluang Sangat Tinggi!** Skor Anda sangat kompetitif untuk target jurusan tersebut. Pertahankan konsistensi belajar!")
            elif rata_nilai >= 700:
                st.info("👍 **Peluang Kompetitif (Sedang-Tinggi).** Nilai Anda sudah bagus, namun perlu dioptimalkan pada subtes yang masih menjadi kelemahan.")
            elif rata_nilai >= 600:
                st.warning("⚠️ **Peluang Cukup / Butuh Perjuangan Ekstra.** Perlu peningkatan intensitas latihan soal dan pendalaman materi spesifik di bimbingan.")
            else:
                st.error("🚨 **Peluang Masih Rendah.** Disarankan untuk memperkuat konsep dasar materi atau mempertimbangkan strategi pemilihan jurusan alternatif.")
                
            st.info("💡 *Catatan: Hasil analisis ini bersifat simulasi prediktif mandiri sebagai acuan motivasi belajar.*")

    st.markdown("---")
    st.subheader("📁 Panduan & Rekomendasi Jurusan Berdasarkan Minat")
    st.write("Anda juga dapat melampirkan dokumen panduan rumpun ilmu (Saintek/Soshum) atau kuesioner minat bakat di sini.")
    
    # Tombol atau info tambahan jika ingin dihubungkan ke file panduan di Drive
    st.markdown("- [🔗 Lihat Panduan Pemilihan Jurusan SNBT/UTBK (Google Drive)](https://drive.google.com)")
