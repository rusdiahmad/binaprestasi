import streamlit as st
from supabase import create_client, Client
import pandas as pd
from datetime import date

# Konfigurasi halaman Streamlit
st.set_page_config(
    page_title="Jadwal & Jurnal Bina Prestasi BPIBS",
    page_icon="📚",
    layout="wide"
)

# Inisialisasi koneksi Supabase menggunakan st.secrets (aman untuk deployment)
@st.cache_resource
def init_supabase():
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_ANON_KEY"]
    return create_client(url, key)

supabase: Client = init_supabase()

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
            nama_guru = st.text_input("Nama Guru", placeholder="Contoh: Ust. Rusdi")
            kelas = st.text_input("Kelas", placeholder="Contoh: X.1, X.2 (Bisa lebih dari satu kelas)")
        with col2:
            waktu = st.text_input("Waktu (JP / Jam)", placeholder="Contoh: JP 3 (08.00 - 09.30)")
            mapel_bidang = st.text_input("Mapel / Bidang", placeholder="Contoh: OSN Matematika / Matematika Wajib")
        
        materi = st.text_area("Materi Pembelajaran", placeholder="Tuliskan pokok bahasan atau materi yang diajarkan...")
        
        submitted = st.form_submit_button("Simpan Jurnal Mengajar")

        if submitted:
            if not nama_guru or not mapel_bidang or not kelas or not materi:
                st.warning("⚠️ Mohon lengkapi semua kolom yang wajib diisi!")
            else:
                try:
                    # Data yang akan dikirim ke tabel 'attendance' Supabase
                    data_to_insert = {
                        "tanggal_mengajar": str(tanggal_mengajar),
                        "waktu": waktu,
                        "nama_guru": nama_guru,
                        "mapel_bidang": mapel_bidang,
                        "kelas": kelas,
                        "materi": materi
                    }
                    
                    response = supabase.table("attendance").insert(data_to_insert).execute()
                    st.success("✅ Berhasil! Jurnal mengajar telah tersimpan ke database Supabase.")
                except Exception as e:
                    st.error(f"❌ Gagal menyimpan data: {e}")

# ================= MENU 2: REKAPITULASI JURNAL =================
elif menu == "📊 Rekapitulasi Jurnal":
    st.subheader("Rekapitulasi Jurnal & Kegiatan Mengajar")
    st.write("Berikut adalah daftar seluruh jurnal mengajar yang telah terekam di database.")

    # Tombol Refresh Data
    if st.button("🔄 Muat Ulang Data"):
        st.rerun()

    try:
        # Ambil data dari tabel 'attendance'
        response = supabase.table("attendance").select("*").order("tanggal_mengajar", desc=True).execute()
        data = response.data

        if data:
            df = pd.DataFrame(data)
            
            # Rapikan nama kolom untuk ditampilkan ke tabel
            df = df.rename(columns={
                "tanggal_mengajar": "Tanggal",
                "waktu": "Waktu",
                "nama_guru": "Nama Guru",
                "mapel_bidang": "Mapel / Bidang",
                "kelas": "Kelas",
                "materi": "Materi"
            })
            
            # Tampilkan sebagai tabel interaktif
            st.dataframe(df[["Tanggal", "Waktu", "Nama Guru", "Mapel / Bidang", "Kelas", "Materi"]], use_container_width=True)
            st.info(f"Total jurnal tercatat: {len(df)} kegiatan.")
        else:
            st.info("Belum ada data jurnal yang tersimpan.")
    except Exception as e:
        st.error(f"Gagal memuat data dari database: {e}")

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
