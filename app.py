import streamlit as st
import pandas as pd
from datetime import date
import os

# Konfigurasi halaman Streamlit
st.set_page_config(
    page_title="Jadwal & Jurnal Bina Prestasi BPIBS",
    page_icon="📚",
    layout="wide"
)

# Nama file CSV untuk penyimpanan data lokal
CSV_FILE = "data_jurnal.csv"

# Fungsi untuk memuat data dari file CSV
def load_data():
    if os.path.exists(CSV_FILE):
        try:
            return pd.read_csv(CSV_FILE)
        except Exception:
            # Jika file kosong atau rusak, buat dataframe kosong dengan kolom yang sesuai
            return pd.DataFrame(columns=["Tanggal", "Waktu", "Nama Guru", "Mapel / Bidang", "Kelas", "Materi"])
    else:
        return pd.DataFrame(columns=["Tanggal", "Waktu", "Nama Guru", "Mapel / Bidang", "Kelas", "Materi"])

# Judul Utama Web
st.title("📚 Bina Prestasi SMA BPIBS")
st.markdown("Tahun Pelajaran 2026/2027 — Sistem Jurnal Mengajar & Rekapitulasi")

# Menu Navigasi di Sidebar
menu = st.sidebar.selectbox("Pilih Menu", ["📝 Input Jurnal & Absensi", "📊 Rekapitulasi Jurnal", "📅 Jadwal Pelajaran"])

# ================= MENU 1: INPUT JURNAL =================
if menu == "📝 Input Jurnal & Absensi":
    st.subheader("Form Jurnal & Presensi Mengajar")
    st.write("Silakan isi form di bawah ini untuk mencatat kegiatan belajar mengajar.")

    with st.form("attendance_form"):
        col1, col2 = st.columns(2)
        with col1:
            tanggal_mengajar = st.date_input("Tanggal Mengajar", value=date.today())
            nama_guru = st.text_input("Nama Guru", placeholder="Contoh: Fulan")
            kelas = st.text_input("Kelas", placeholder="Contoh: X.1, X.2 (Bisa lebih dari satu kelas)")
        with col2:
            waktu = st.text_input("Waktu (JP / Jam)", placeholder="Contoh:08.00 - 09.30")
            mapel_bidang = st.text_input("Mapel / Bidang", placeholder="Contoh: OSN Matematika / Matematika Wajib")
        
        materi = st.text_area("Materi Pembelajaran", placeholder="Tuliskan pokok bahasan atau materi yang diajarkan...")
        
        submitted = st.form_submit_button("Simpan Jurnal Mengajar")

        if submitted:
            if not nama_guru or not mapel_bidang or not kelas or not materi:
                st.warning("⚠️ Mohon lengkapi semua kolom yang wajib diisi!")
            else:
                try:
                    # Muat data lama
                    df = load_data()
                    
                    # Buat baris data baru
                    new_data = pd.DataFrame([{
                        "Tanggal": str(tanggal_mengajar),
                        "Waktu": waktu,
                        "Nama Guru": nama_guru,
                        "Mapel / Bidang": mapel_bidang,
                        "Kelas": kelas,
                        "Materi": materi
                    }])
                    
                    # Gabungkan data lama dan baru
                    df = pd.concat([new_data, df], ignore_index=True)
                    
                    # Simpan kembali ke file CSV
                    df.to_csv(CSV_FILE, index=False)
                    
                    st.success("✅ Berhasil! Jurnal mengajar telah tersimpan.")
                except Exception as e:
                    st.error(f"❌ Gagal menyimpan data: {e}")

# ================= MENU 2: REKAPITULASI JURNAL =================
elif menu == "📊 Rekapitulasi Jurnal":
    st.subheader("Rekapitulasi Jurnal & Kegiatan Mengajar")
    st.write("Berikut adalah daftar seluruh jurnal mengajar yang telah terekam.")

    if st.button("🔄 Muat Ulang Data"):
        st.rerun()

    df = load_data()

    if not df.empty:
        # Tampilkan sebagai tabel interaktif
        st.dataframe(df, use_container_width=True)
        st.info(f"Total jurnal tercatat: {len(df)} kegiatan.")
    else:
        st.info("Belum ada data jurnal yang tersimpan.")

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

