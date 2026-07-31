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
    st.subheader("🎯 Simulasi Prediksi Skor Per Subtes & Peluang Jurusan PTN")
    st.write("Masukkan perkiraan atau hasil nilai tryout pada masing-masing subtes untuk melihat analisis rata-rata dan proyeksi peluang kelulusan target jurusan.")

    with st.form("form_prediksi_subtes"):
        st.markdown("#### 1. Identitas & Target Akademik")
        col_id1, col_id2 = st.columns(2)
        with col_id1:
            nama_siswa = st.text_input("Nama Siswa", placeholder="Contoh: Ahmad")
            target_jurusan = st.text_input("Target Program Studi / Jurusan", placeholder="Contoh: Teknik Informatika / Kedokteran")
        with col_id2:
            target_ptn = st.text_input("Target Perguruan Tinggi (PTN)", placeholder="Contoh: Universitas Indonesia / ITB")
            kategori_jurusan = st.selectbox("Kelompok Ujian", ["Saintek / Exacta", "Soshum / Humaniora", "Campuran (Saintek & Soshum)"])

        st.markdown("---")
        st.markdown("#### 2. Masukkan Skor Nilai Per Subtes (Rentang 0 - 1000)")
        
        col_sub1, col_sub2 = st.columns(2)
        with col_sub1:
            pu = st.number_input("Penalaran Umum (PU)", min_value=0.0, max_value=1000.0, value=650.0)
            ppu = st.number_input("Pengetahuan & Pemahaman Umum (PPU)", min_value=0.0, max_value=1000.0, value=650.0)
            pbm = st.number_input("Pemahaman Bacaan & Menulis (PBM)", min_value=0.0, max_value=1000.0, value=650.0)
            pk = st.number_input("Pengetahuan Kuantitatif (PK)", min_value=0.0, max_value=1000.0, value=650.0)
        with col_sub2:
            lb_indo = st.number_input("Literasi dalam Bahasa Indonesia", min_value=0.0, max_value=1000.0, value=650.0)
            lb_inggris = st.number_input("Literasi dalam Bahasa Inggris", min_value=0.0, max_value=1000.0, value=650.0)
            pm = st.number_input("Penalaran Matematika (PM)", min_value=0.0, max_value=1000.0, value=650.0)

        submitted_simulasi = st.form_submit_button("Analisis Skor & Prediksi Jurusan")

        if submitted_simulasi:
            # Hitung rata-rata dari 7 subtes
            total_skor = pu + ppu + pbm + pk + lb_indo + lb_inggris + pm
            rata_rata = total_skor / 7.0

            st.markdown("---")
            st.markdown(f"### 📊 Hasil Analisis untuk: **{nama_siswa}**")
            
            col_res1, col_res2 = st.columns(2)
            with col_res1:
                st.metric(label="Skor Rata-Rata Gabungan", value=f"{rata_rata:.2f}")
                st.write(f"🎯 **Target:** {target_jurusan} di {target_ptn}")
                st.write(f"📁 **Kelompok:** {kategori_jurusan}")
            
            with col_res2:
                st.markdown("#### Rekap Skor Subtes:")
                df_subtes_result = pd.DataFrame({
                    "Subtes": ["PU", "PPU", "PBM", "PK", "Lit. Indo", "Lit. Eng", "PM"],
                    "Skor": [pu, ppu, pbm, pk, lb_indo, lb_inggris, pm]
                })
                st.dataframe(df_subtes_result, use_container_width=True, hide_index=True)

            st.markdown("---")
            st.markdown("#### 🔍 Evaluasi & Proyeksi Peluang Kelulusan")
            
            # Logika rekomendasi berdasarkan rata-rata skor UTBK standar
            if rata_rata >= 720:
                st.success("🔥 **Peluang Sangat Tinggi!** Skor rata-rata Anda berada di zona aman untuk menembus PTN top and target jurusan tersebut. Pertahankan performa belajar!")
            elif rata_rata >= 650:
                st.info("👍 **Peluang Kompetitif (Sedang - Tinggi).** Skor Anda sudah cukup bersaing. Fokuskan peningkatan latihan pada subtes yang nilainya masih di bawah rata-rata gabungan.")
            elif rata_rata >= 580:
                st.warning("⚠️ **Peluang Cukup / Perlu Perjuangan Ekstra.** Skor berada di batas menengah. Perlu evaluasi mendalam pada konsep dasar subtes penalaran dan kuantitatif/matematika.")
            else:
                st.error("🚨 **Peluang Masih Rendah.** Target jurusan tersebut memiliki keketatan tinggi. Disarankan memperbanyak tryout intensif atau mempertimbangkan opsi strategi pemilihan jurusan alternatif.")

            # Analisis subtes terlemah
            subtes_dict = {"Penalaran Umum": pu, "PPU": ppu, "PBM": pbm, "Pengetahuan Kuantitatif": pk, "Literasi Bahasa Indonesia": lb_indo, "Literasi Bahasa Inggris": lb_inggris, "Penalaran Matematika": pm}
            subtes_terendah = min(subtes_dict, key=subtes_dict.get)
            st.info(💡 **Catatan Evaluasi Belajar:** Subtes yang paling perlu Anda tingkatkan latihannya adalah **{subtes_terendah}** (skor terendah dibanding subtes lainnya).)
