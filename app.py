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
    "📄 Generator CV Prestasi"
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


# ================= MENU 5: GENERATOR CV PRESTASI SISWA =================
elif menu == "📄 Generator CV Prestasi":
    st.subheader("📄 Generator CV Berbasis Prestasi Siswa")
    st.write("Fitur ini secara otomatis menarik data prestasi siswa dari Google Sheet Rekap Hasil Lomba untuk menyusun draf Curriculum Vitae (CV) secara instan.")

    # Mengambil data dari Google Sheet Lomba yang sudah ada
    try:
        sheet_id_lomba = "1ANrCscXUyYv3oh-WSbTVfSptcc7iqDfJggjun6ec5Z4"
        csv_url_lomba = f"https://docs.google.com/spreadsheets/d/{sheet_id_lomba}/export?format=csv"
        df_lomba = pd.read_csv(csv_url_lomba)
        
        if df_lomba.empty:
            st.warning("Data rekap lomba masih kosong, sehingga CV belum dapat digenerate.")
        else:
            # Asumsi kolom nama siswa di Google Sheet bernama "Nama" atau "Nama Siswa" 
            # (Sesuaikan nama kolom di bawah jika berbeda dengan header di Google Sheet Anda)
            # Kita berikan opsi deteksi kolom secara fleksibel
            kolom_nama_pilihan = [col for col in df_lomba.columns if 'nama' in col.lower()]
            
            if kolom_nama_pilihan:
                kolom_nama = kolom_nama_pilihan[0]
                daftar_siswa = df_lomba[kolom_nama].dropna().unique().tolist()
                
                st.markdown("---")
                selected_student = st.selectbox("Pilih / Ketik Nama Siswa", options=daftar_siswa)
                
                # Input tambahan untuk memperlengkap CV
                col_cv1, col_cv2 = st.columns(2)
                with col_cv1:
                    nisn_kelas = st.text_input("Kelas / NISN", placeholder="Contoh: XII IPA 1 / SMA BPIBS Bogor")
                    cita_cita = st.text_input("Target / Minat Studi Lanjutan", placeholder="Contoh: Jurusan Teknik Elektro PTN")
                with col_cv2:
                    email_kontak = st.text_input("Email / Kontak", placeholder="Contoh: siswa@email.com")
                    keahlian = st.text_input("Keahlian Utama / Skills", placeholder="Contoh: Matematika Lanjut, Python, C++, Public Speaking")

                if st.button("✨ Buat Curriculum Vitae (CV)"):
                    # Filter data prestasi berdasarkan siswa yang dipilih
                    df_prestasi_siswa = df_lomba[df_lomba[kolom_nama].astype(str).str.strip() == str(selected_student).strip()]
                    
                    st.markdown("---")
                    st.markdown("### 📋 Preview Curriculum Vitae")
                    
                    # Tampilan Dokumen CV Bergaya Profesional
                    st.markdown(f"""
                    <div style="border: 2px solid #ddd; padding: 30px; border-radius: 10px; background-color: #f9f9f9; color: #333;">
                        <h2 style="text-align: center; margin-bottom: 0px; color: #1f77b4;">{selected_student}</h2>
                        <p style="text-align: center; font-style: italic; color: #555;">{nisn_kelas} | Kontak: {email_kontak if email_kontak else '-'}</p>
                        <hr>
                        
                        <h4>🎯 Ringkasan Profil & Minat</h4>
                        <p>Siswa aktif bina prestasi di SMA BPIBS Bogor dengan minat dan fokus pengembangan di bidang <b>{target_jurusan if 'target_jurusan' in locals() and target_jurusan else 'Sains & Teknologi'}</b>. Memiliki rekam jejak kompetisi dan prestasi akademik yang konsisten.</p>
                        
                        <h4>💻 Keahlian / Kompetensi Utama</h4>
                        <p>{keahlian if keahlian else 'Matematika, Pemecahan Masalah, Logika Algoritma'}</p>
                        
                        <h4>🏆 Rekam Jejak Prestasi & Kompetisi</h4>
                    """, unsafe_allow_html=True)

                    if not df_prestasi_siswa.empty:
                        # Tampilkan daftar prestasinya dalam bentuk list/tabel di dalam CV
                        for index, row in df_prestasi_siswa.iterrows():
                            # Menampilkan kolom-kolom selain nama secara dinamis
                            row_info = " | ".join([f"<b>{col}:</b> {val}" for col, val in row.items() if col != kolom_nama])
                            st.markdown(f"- 🌟 {row_info}", unsafe_allow_html=True)
                    else:
                        st.markdown("- *Belum ada catatan prestasi spesifik yang tercatat di sistem.*")

                    st.markdown("""
                        <hr>
                        <p style="text-align: center; font-size: 12px; color: #777;">Dokumen ini digenerate secara otomatis melalui Sistem Bina Prestasi SMA BPIBS Bogor.</p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    st.success("✅ CV Berhasil Disusun! Anda dapat menyalin teks di atas atau mencetak halaman ini (Ctrl + P -> Simpan sebagai PDF).")
            else:
                st.error("Kolom 'Nama' tidak ditemukan pada Google Sheet Rekap Hasil Lomba Anda. Pastikan ada kolom yang memuat nama siswa.")

    except Exception as e:
        st.error(f"Gagal memuat data dari Google Drive untuk pembuatan CV. Detail error: {e}")



