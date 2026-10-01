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
    "🏆 Rekap Hasil Lomba",
    "📄 Generator CV Prestasi",
    "📊 Statistik & Analisis",
    "🗓️ Timeline Program",
    "🧭 Tes Minat & Rekomendasi"
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
                    nisn_kelas = st.text_input("Kelas / NISN", value="SMA BPIBS")
                    target_karier = st.text_input("Target / Minat Studi", value="Sains & Teknologi / PTN")
                with col_cv2:
                    email_kontak = st.text_input("Kontak / Email", value="siswa@bpibs.sch.id")
                    keahlian = st.text_input("Keahlian Utama", value="Matematika Lanjut, Algoritma C++/Python, Analisis Data")

                if st.button("🎨 Render & Generate Gambar CV"):
                    # Filter prestasi siswa
                    df_prestasi_siswa = df_lomba[df_lomba[kolom_nama].astype(str).str.strip() == str(selected_student).strip()]
                    
                    # Membuat Plot Matplotlib sebagai Gambar CV
                    fig, ax = plt.subplots(figsize=(8.5, 11))
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
                    
                    profil_text = f"Siswa aktif di SMA BPIBS dengan fokus kompetensi di bidang akademik dan riset.\nKeahlian: {keahlian}"
                    ax.text(0.05, 0.64, profil_text, fontsize=9.5, color='#333333', transform=ax.transAxes, va='top', wrap=True)
                    
                    # Bagian 2: Rekam Jejak Prestasi (Difilter sesuai kolom pilihan Anda)
                    ax.text(0.05, 0.53, "DAFTAR PRESTASI & KOMPETISI", fontsize=11, fontweight='bold', color='#1f4e78', transform=ax.transAxes)
                    ax.axhline(y=0.515, xmin=0.05, xmax=0.95, color='#1f4e78', linewidth=1.5)
                    
                    y_pos = 0.47
                    if not df_prestasi_siswa.empty:
                        for idx, row in df_prestasi_siswa.iterrows():
                            if y_pos < 0.05:
                                break
                            
                            # Mencari kolom secara fleksibel yang mendekati kata kunci yang Anda inginkan
                            val_hasil = next((str(row[c]) for c in df_prestasi_siswa.columns if 'hasil' in c.lower() or 'juara' in c.lower()), "-")
                            val_lomba = next((str(row[c]) for c in df_prestasi_siswa.columns if 'nama' in c.lower() and c != kolom_nama or 'lomba' in c.lower() or 'event' in c.lower()), "-")
                            val_jenis = next((str(row[c]) for c in df_prestasi_siswa.columns if 'jenis' in c.lower() or 'kategori' in c.lower() or 'bidang' in c.lower()), "-")
                            val_waktu = next((str(row[c]) for c in df_prestasi_siswa.columns if 'waktu' in c.lower() or 'tanggal' in c.lower() or 'tahun' in c.lower()), "-")
                            
                            # Format teks baris prestasi sesuai permintaan: Hasil | Nama Lomba | Jenis Lomba | Waktu
                            baris_prestasi = f"• [{val_hasil}] {val_lomba} ({val_jenis}) — {val_waktu}"
                            
                            ax.text(0.05, y_pos, baris_prestasi, fontsize=9, color='#222222', transform=ax.transAxes, wrap=True)
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


# ================= MENU 6: STATISTIK & ANALISIS PRESTASI =================
elif menu == "📊 Statistik & Analisis":
    st.subheader("📊 Dashboard Statistik & Analisis Prestasi Siswa")
    st.write("Visualisasi data perolehan prestasi dan kompetisi yang terhubung langsung dari Google Sheet.")

    if st.button("🔄 Muat Ulang Statistik"):
        st.rerun()

    try:
        sheet_id_lomba = "1ANrCscXUyYv3oh-WSbTVfSptcc7iqDfJggjun6ec5Z4"
        csv_url_lomba = f"https://docs.google.com/spreadsheets/d/{sheet_id_lomba}/export?format=csv"
        df_lomba = pd.read_csv(csv_url_lomba)
        
        if df_lomba.empty:
            st.info("File Google Sheet lomba saat ini masih kosong, belum ada statistik yang dapat ditampilkan.")
        else:
            # Menampilkan Metrik Utama (Angka Ringkasan)
            total_prestasi = len(df_lomba)
            
            # Mendeteksi kolom bidang/jenis lomba dan hasil secara fleksibel
            kolom_jenis = next((c for c in df_lomba.columns if 'jenis' in c.lower() or 'kategori' in c.lower() or 'bidang' in c.lower()), None)
            kolom_hasil = next((c for c in df_lomba.columns if 'hasil' in c.lower() or 'juara' in c.lower()), None)
            
            col_m1, col_m2 = st.columns(2)
            with col_m1:
                st.metric(label="🏆 Total Rekor Prestasi Tercatat", value=total_prestasi)
            with col_m2:
                jumlah_siswa_berprestasi = len(df_lomba.iloc[:, 0].dropna().unique()) if not df_lomba.empty else 0
                st.metric(label="👥 Jumlah Talenta Siswa Terdata", value=jumlah_siswa_berprestasi)

            st.markdown("---")

            # Grafik 1: Distribusi Berdasarkan Bidang / Jenis Lomba
            if kolom_jenis:
                st.markdown("#### 📈 Distribusi Prestasi Berdasarkan Bidang / Jenis Lomba")
                df_jenis_count = df_lomba[kolom_jenis].value_counts().reset_index()
                df_jenis_count.columns = ['Bidang / Jenis', 'Jumlah']
                
                # Menampilkan Bar Chart Interaktif
                st.bar_chart(df_jenis_count.set_index('Bidang / Jenis'))
            else:
                st.info("Kolom kategori/jenis lomba tidak terdeteksi secara otomatis untuk grafik bidang.")

            st.markdown("---")

            # Grafik 2: Distribusi Berdasarkan Hasil / Capaian Juara
            if kolom_hasil:
                st.markdown("#### 🥇 Rangkuman Capaian / Medali")
                df_hasil_count = df_lomba[kolom_hasil].value_counts().reset_index()
                df_hasil_count.columns = ['Capaian', 'Jumlah']
                
                st.bar_chart(df_hasil_count.set_index('Capaian'))
            else:
                st.info("Kolom hasil/juara tidak terdeteksi secara otomatis untuk grafik capaian.")

    except Exception as e:
        st.error(f"Gagal memuat data statistik dari Google Drive. Pastikan pengaturan sharing Google Sheet sudah benar. Detail error: {e}")  


# ================= MENU 7: TIMELINE PROGRAM BINA PRESTASI =================
elif menu == "🗓️ Timeline Program":
    st.subheader("🗓️ Timeline Program Bina Prestasi BPIBS")
    st.markdown("**Tahun Pelajaran 2026 / 2027** — Program pembinaan berkelanjutan untuk mencetak generasi berprestasi yang unggul dalam akademik dan kompetisi tingkat nasional.")
    st.markdown("---")

    # Data timeline sesuai dengan infografis resmi
    timeline_data = [
        {"Periode": "20 - 25 Juli 2026", "Agenda Kegiatan": "Pekan Matrikulasi"},
        {"Periode": "27 Juli - 8 Agustus 2026", "Agenda Kegiatan": "Seleksi Peserta Pembinaan"},
        {"Periode": "10 Agustus - 12 September 2026", "Agenda Kegiatan": "Pembinaan Materi Dasar I"},
        {"Periode": "14 - 26 September 2026", "Agenda Kegiatan": "Masa ASTS"},
        {"Periode": "28 September - 28 November 2026", "Agenda Kegiatan": "Pembinaan Materi Dasar II"},
        {"Periode": "30 November - 12 Desember 2026", "Agenda Kegiatan": "Masa ASAS"},
        {"Periode": "14 - 18 Desember 2026", "Agenda Kegiatan": "Pembinaan Materi Lanjutan I"},
        {"Periode": "21 Desember 2026 - 9 Januari 2027", "Agenda Kegiatan": "Libur"},
        {"Periode": "11 Januari - 13 Februari 2027", "Agenda Kegiatan": "Pembinaan Materi Lanjutan II"},
        {"Periode": "15 - 20 Februari 2027", "Agenda Kegiatan": "Seleksi OSN Tingkat Sekolah"},
        {"Periode": "22 - 28 Februari 2027", "Agenda Kegiatan": "Perkiraan Pendaftaran OSN-K"},
        {"Periode": "1 - 28 Maret 2027", "Agenda Kegiatan": "Libur dan Masa ASTS"},
        {"Periode": "29 Maret - 29 Mei 2027", "Agenda Kegiatan": "Pembinaan OSN-K"},
        {"Periode": "31 Mei - 5 Juni 2027", "Agenda Kegiatan": "Masa ASAT"},
        {"Periode": "6 Juni 2027 hingga Pelaksanaan OSN-K", "Agenda Kegiatan": "Pembinaan OSN-K"}
    ]

    df_timeline = pd.DataFrame(timeline_data)

    # Menampilkan dalam bentuk tabel interaktif yang rapi
    st.dataframe(df_timeline, use_container_width=True, hide_index=True)

    st.markdown("---")
    st.info("💡 **Catatan:** Timeline ini menjadi acuan utama pelaksanaan program pembinaan akademik dan persiapan kompetisi sains di lingkungan SMA BPIBS Bogor T.A. 2026/2027.")


# ================= MENU 8: TES MINAT BAKAT & REKOMENDASI PUSPRESNAS =================
elif menu == "🧭 Tes Minat & Rekomendasi":
    st.subheader("🧭 Tes Minat Bakat & Pemetaan Talenta Ajang Puspresnas")
    st.write("Jawab pertanyaan berikut untuk memetakan minat dan mencocokkan Anda dengan ajang talenta resmi Puspresnas (OSN, OPSI, LDBI, NSDC, FLS2N, dll.).")

    with st.form("form_minat_puspresnas"):
        nama_peserta = st.text_input("Nama Siswa", placeholder="Contoh: Ahmad")
        
        st.markdown("---")
        st.markdown("#### Berikan penilaian ketertarikan Anda (Skala 1 = Sangat Tidak Setuju s.d. 5 = Sangat Setuju):")

        # Pertanyaan diperluas spesifik per bidang
        m_mat = st.slider("1. Saya sangat menikmati pemecahan masalah aljabar, teori bilangan, dan logika hitung tingkat lanjut (OSN Matematika).", 1, 5, 3)
        m_fis = st.slider("2. Saya senang menganalisis fenomena mekanika, kelistrikan, dan hukum-hukum alam secara matematis (OSN Fisika).", 1, 5, 3)
        m_kim = st.slider("3. Saya antusias mempelajari struktur molekul, stoikiometri, dan praktikum reaksi kimia (OSN Kimia).", 1, 5, 3)
        m_bio = st.slider("4. Saya tertarik mempelajari sistem makhluk hidup, genetika, sel, dan ekosistem (OSN Biologi).", 1, 5, 3)
        m_inf = st.slider("5. Saya suka ngoding, merancang struktur data, dan memecahkan masalah komputasi/algoritma (OSN Informatika).", 1, 5, 3)
        m_eko = st.slider("6. Saya tertarik menganalisis ilmu ekonomi mikro/makro, pasar, dan fenomena keuangan (OSN Ekonomi).", 1, 5, 3)
        m_opsi = st.slider("7. Saya suka meneliti, mencari solusi permasalahan nyata, dan menulis karya tulis ilmiah (OPSI / KTI).", 1, 5, 3)
        m_ldbi = st.slider("8. Saya aktif berpendapat, suka berdebat kritis, dan menguasai teknik retorika berbahasa Indonesia (LDBI / Debat Bahasa Indonesia).", 1, 5, 3)
        m_nsdc = st.slider("9. Saya percaya diri menyampaikan argumen kritis dan berpikir analitis menggunakan Bahasa Inggris (NSDC / National Schools Debating Championship).", 1, 5, 3)
        m_fls = st.slider("10. Saya memiliki bakat dan ketertarikan tinggi pada bidang seni kreatif, musik, atau sastra (FLS2N).", 1, 5, 3)

        submitted_tes_pro = st.form_submit_button("Analisis & Petakan Ajang Puspresnas")

        if submitted_tes_pro:
            st.markdown("---")
            st.markdown(f"### 🎯 Hasil Pemetaan Talenta Puspresnas: **{nama_peserta}**")

            # Kamus pemetaan skor lengkap dengan ajang resminya
            skor_pilihan = {
                "OSN Matematika": (m_mat * 2, "Olimpiade Sains Nasional (OSN) - Bidang Matematika"),
                "OSN Fisika": (m_fis * 2, "Olimpiade Sains Nasional (OSN) - Bidang Fisika"),
                "OSN Kimia": (m_kim * 2, "Olimpiade Sains Nasional (OSN) - Bidang Kimia"),
                "OSN Biologi": (m_bio * 2, "Olimpiade Sains Nasional (OSN) - Bidang Biologi"),
                "OSN Informatika": (m_inf * 2, "Olimpiade Sains Nasional (OSN) - Bidang Informatika"),
                "OSN Ekonomi": (m_eko * 2, "Olimpiade Sains Nasional (OSN) - Bidang Ekonomi"),
                "Karya Tulis Ilmiah (OPSI)": (m_opsi * 2, "Olimpiade Penelitian Siswa Indonesia (OPSI) / KTI"),
                "Debat Bahasa Indonesia (LDBI)": (m_ldbi * 2, "Lomba Debat Bahasa Indonesia (LDBI)"),
                "Debat Bahasa Inggris (NSDC)": (m_nsdc * 2, "National Schools Debating Championship (NSDC)"),
                "Seni & Sastra (FLS2N)": (m_fls * 2, "Festival Lomba Seni Siswa Nasional (FLS2N)")
            }

            # Mencari skor tertinggi
            bidang_tertinggi = max(skor_pilihan, key=lambda k: skor_pilihan[k][0])
            info_utama = skor_pilihan[bidang_tertinggi]

            st.success(f"🏆 **Rekomendasi Utama Ajang Talenta:** **{info_utama[1]}**")
            
            # Membuat tabel rekap seluruh bidang
            data_tabel = []
            for bidang, (skor, ajang) in skor_pilihan.items():
                data_tabel.append({"Bidang Minat": bidang, "Ajang Puspresnas": ajang, "Skor Kecocokan": skor})
            
            df_hasil_tes = pd.DataFrame(data_tabel)
            df_hasil_tes = df_hasil_tes.sort_values(by="Skor Kecocokan", ascending=False)

            st.markdown("#### 📊 Rangkuman Peringkat Kecocokan Bidang:")
            st.dataframe(df_hasil_tes, use_container_width=True, hide_index=True)

            st.markdown("#### 💡 Rekomendasi Fokus Pembinaan Bina Prestasi:")
            if "Matematika" in bidang_tertinggi:
                st.info("Fokus Pembinaan: Bedah modul aljabar tingkat lanjut, teori bilangan, kombinatorika, dan geometri bidang datar.")
            elif "Fisika" in bidang_tertinggi:
                st.info("Fokus Pembinaan: Penguatan konsep mekanika analitik, termodinamika, elektromagnetisme, dan kalkulus fisika.")
            elif "Kimia" in bidang_tertinggi:
                st.info("Fokus Pembinaan: Pendalaman kesetimbangan kimia, termokimia, kimia organik dasar, dan stoikiometri kompleks.")
            elif "Biologi" in bidang_tertinggi:
                st.info("Fokus Pembinaan: Kajian fisiologi tumbuhan & hewan, genetika molekuler, biokimia, dan ekologi.")
            elif "Informatika" in bidang_tertinggi:
                st.info("Fokus Pembinaan: Latihan pemrograman kompetitif (C++/Python), struktur data (Tree, Graph), dan algoritma greedy/DP.")
            elif "Ekonomi" in bidang_tertinggi:
                st.info("Fokus Pembinaan: Pendalaman ekonomi mikro/makro, akuntansi perusahaan, perbankan, dan analisis kebijakan fiskal/moneter.")
            elif "Karya Tulis" in bidang_tertinggi:
                st.info("Fokus Pembinaan: Pelatihan metodologi penelitian ilmiah, penyusunan proposal riset, pengolahan data statistik, dan penulisan artikel ilmiah OPSI.")
            elif "Bahasa Indonesia" in bidang_tertinggi:
                st.info("Fokus Pembinaan: Latihan mosi debat nasional, teknik argumentasi, public speaking, dan pemahaman isu sosial kenegaraan (LDBI).")
            elif "Bahasa Inggris" in bidang_tertinggi:
                st.info("Fokus Pembinaan: Latihan mosi World Schools Style (WSDC/NSDC), pembendaharaan kosakata global, dan teknik sanggahan cepat dalam Bahasa Inggris.")
            else:
                st.info("Fokus Pembinaan: Eksplorasi kreativitas seni, latihan teknis penjiwaan/penulisan sastra, dan persiapan portofolio karya FLS2N.")



