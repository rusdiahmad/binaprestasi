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
    st.subheader("📄 Generator Gambar CV Prestasi Siswa")
    st.write("Pilih nama siswa untuk menghasilkan gambar Curriculum Vitae (CV) formal bergaya profesional secara instan.")

    import matplotlib.pyplot as plt
    import io

    try:
        sheet_id_lomba = "1ANrCscXUyYv3oh-WSbTVfSptcc7iqDfJggjun6ec5Z4"
        csv_url_lomba = f"https://docs.google.com/spreadsheets/d/{sheet_id_lomba}/export?format=csv"
        df_lomba = pd.read_csv(csv_url_lomba)
        
        if df_lomba.empty:
            st.warning("Data rekap lomba masih kosong.")
        else:
            # Mencari kolom nama siswa secara otomatis
            kolom_nama_pilihan = [col for col in df_lomba.columns if 'nama' in col.lower()]
            
            if kolom_nama_pilihan:
                kolom_nama = kolom_nama_pilihan[0]
                daftar_siswa = df_lomba[kolom_nama].dropna().unique().tolist()
                
                st.markdown("---")
                selected_student = st.selectbox("Pilih Nama Siswa", options=daftar_siswa)
                
                col_cv1, col_cv2 = st.columns(2)
                with col_cv1:
                    nisn_kelas = st.text_input("Kelas / NISN", value="SMA BPIBS Bogor")
                    target_karier = st.text_input("Target / Minat Studi", value="Sains & Teknologi / PTN")
                with col_cv2:
                    email_kontak = st.text_input("Kontak / Email", value="siswa@bpibs.sch.id")
                    keahlian = st.text_input("Keahlian Utama", value="Matematika Lanjut, Algoritma C++/Python, Analisis Data")

                if st.button("🎨 Render & Generate Gambar CV"):
                    # Filter prestasi siswa
                    df_prestasi_siswa = df_lomba[df_lomba[kolom_nama].astype(str).str.strip() == str(selected_student).strip()]
                    
                    # Membuat Plot Matplotlib sebagai Gambar CV
                    fig, ax = plt.subplots(figsize=(8.5, 11)) # Ukuran standar kertas surat (Letter/A4 aspect)
                    ax.axis('off')
                    
                    # Background putih bersih
                    fig.patch.set_facecolor('white')
                    
                    # Header Background (Kotak Biru Profesional di Atas)
                    header_box = plt.Rectangle((0.05, 0.78), 0.90, 0.17, transform=ax.transAxes, color="#1f4e78", ec="none", zorder=1)
                    ax.add_patch(header_box)
                    
                    # Teks Header (Nama & Kontak)
                    ax.text(0.10, 0.90, str(selected_student).upper(), fontsize=20, fontweight='bold', color='white', transform=ax.transAxes, zorder=2)
                    ax.text(0.10, 0.84, f"Pelajar & Talenta Berprestasi | {nisn_kelas}", fontsize=11, color='#d9d9d9', transform=ax.transAxes, zorder=2)
                    ax.text(0.10, 0.80, f"Email/Kontak: {email_kontak} | Target: {target_karier}", fontsize=9, color='#d9d9d9', transform=ax.transAxes, zorder=2)
                    
                    # Bagian 1: Ringkasan Profil
                    ax.text(0.05, 0.72, "PROFIL & KEAHLIAN UTAMA", fontsize=11, fontweight='bold', color='#1f4e78', transform=ax.transAxes)
                    ax.axhline(y=0.705, xmin=0.05, xmax=0.95, color='#1f4e78', linewidth=1.5)
                    
                    profil_text = f"Siswa aktif di Bina Prestasi SMA BPIBS Bogor dengan fokus kompetensi di bidang akademik dan riset.\nKeahlian: {keahlian}"
                    ax.text(0.05, 0.64, profil_text, fontsize=9.5, color='#333333', transform=ax.transAxes, va='top', wrap=True)
                    
                    # Bagian 2: Rekam Jejak Prestasi
                    ax.text(0.05, 0.53, "DAFTAR PRESTASI & KOMPETISI", fontsize=11, fontweight='bold', color='#1f4e78', transform=ax.transAxes)
                    ax.axhline(y=0.515, xmin=0.05, xmax=0.95, color='#1f4e78', linewidth=1.5)
                    
                    # Menuliskan daftar prestasi ke gambar
                    y_pos = 0.47
                    if not df_prestasi_siswa.empty:
                        for idx, row in df_prestasi_siswa.iterrows():
                            if y_pos < 0.05:
                                break # Batasi jika terlalu banyak
                            # Ambil isi baris selain kolom nama
                            row_details = " | ".join([f"{val}" for col, val in row.items() if col != kolom_nama])
                            ax.text(0.05, y_pos, f"• {row_details}", fontsize=9, color='#222222', transform=ax.transAxes, wrap=True)
                            y_pos -= 0.055
                    else:
                        ax.text(0.05, 0.45, "• Belum ada catatan prestasi spesifik yang terinput di sistem.", fontsize=9, style='italic', color='#555555', transform=ax.transAxes)
                    
                    # Footer kecil
                    ax.text(0.5, 0.02, "Dokumen resmi draf portofolio digenerate otomatis oleh Sistem Bina Prestasi SMA BPIBS", fontsize=8, color='#888888', transform=ax.transAxes, ha='center')

                    # Simpan plot ke buffer memori sebagai file gambar PNG
                    buf = io.BytesIO()
                    plt.tight_layout()
                    plt.savefig(buf, format="png", dpi=300, bbox_inches='tight')
                    buf.seek(0)
                    plt.close(fig)
                    
                    st.success("🎉 Gambar CV Berhasil Dibuat!")
                    st.image(buf, caption=f"Preview CV - {selected_student}", use_container_width=True)
                    
                    # Tombol Download Gambar CV
                    st.download_button(
                        label="📥 Download Gambar CV (PNG)",
                        data=buf,
                        file_name=f"CV_{selected_student.replace(' ', '_')}.png",
                        mime="image/png"
                    )
            else:
                st.error("Kolom 'Nama' tidak ditemukan di Google Sheet Rekap Hasil Lomba.")
    except Exception as e:
        st.error(f"Terjadi kesalahan saat membuat gambar CV: {e}")
