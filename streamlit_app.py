import streamlit as st

# 1. KONFIGURASI HALAMAN
st.set_page_config(
    page_title="Pusat Respon Darurat Kimia",
    page_icon="🚨",
    layout="wide"
)

# 2. HEADER UTAMA
st.title("🚨 Pusat Respon Cepat: Terkena Bahan Kimia")
st.write("Aplikasi panduan K3 instan untuk pertolongan pertama kecelakaan kerja di laboratorium.")
st.markdown("---")

# 3. LAYOUT DUA KOLOM (Kiri: Navigasi Kasus, Kanan: Kontak & Alat Bantu)
col_utama, col_info = st.columns([3, 1])

with col_utama:
    st.subheader("⚠️ PILIH KONDISI DARURAT")
    
    # Menggunakan Tabs untuk navigasi yang anti-lag dan super stabil
    tab_mata, tab_kulit, tab_tertelan, tab_terhirup = st.tabs([
        "👁️ Terkena Mata", 
        "🦺 Terkena Kulit", 
        "👄 Tertelan Zat", 
        "🫁 Terhirup Gas"
    ])
    
    # --- TAB 1: TERKENA MATA ---
    with tab_mata:
        st.error("### Prosedur Evakuasi Mata (Kontaminasi Okular)")
        st.markdown("""
        1. **LANGSUNG MENUJU EYE WASH STATION:** Jangan menunda waktu bahkan untuk 1 detik pun.
        2. **BILAS DENGAN AIR MENGALIR:** Buka kelopak mata lebar-lebar menggunakan jari tangan. Arahkan aliran air langsung ke bola mata.
        3. **DURASI WAJIB:** Bilas terus-menerus selama **minimal 15 menit**.
        4. **LEPAS LENSA KONTAK:** Jika menggunakan softlens, lepaskan di tengah-tengah pembilasan secara hati-hati.
        5. **JANGAN DIKUCEK:** Menggosok mata dapat menggores kornea dan mempercepat penyerapan zat korosif.
        """)
        
        # Tombol konfirmasi pengganti timer otomatis yang rawan error
        if st.button("Sudah Membilas 15 Menit? Cek Langkah Selanjutnya", key="btn_mata"):
            st.info("ℹ️ **Langkah Selanjutnya:** Tutup mata korban menggunakan kain kasa steril secara longgar (jangan ditekan), lalu segera bawa ke dokter spesialis mata.")

    # --- TAB 2: TERKENA KULIT ---
    with tab_kulit:
        st.error("### Prosedur Tumpahan Bahan Kimia pada Tubuh/Kulit")
        st.markdown("""
        1. **GUNAKAN SAFETY SHOWER:** Jika tumpahan cairan asam/basa pekat mengenai pakaian atau area kulit yang luas.
        2. **LEPAS PAKAIAN TERKONTAMINASI:** Lepaskan jas lab, baju, jam tangan, atau perhiasan selagi tubuh diguyur air.
        3. **BILAS 15 MENIT:** Pastikan area kulit yang terkena dibilas air mengalir dalam jumlah banyak untuk mengencerkan zat kimia.
        4. **JANGAN NETRALKAN DI KULIT:** Jangan menyiramkan larutan basa (seperti sabun) pada kulit yang terkena asam, karena reaksi penetralan menghasilkan panas tinggi yang memperparah luka bakar.
        """)
        if st.button("Sudah Membilas Kulit? Cek Langkah Selanjutnya", key="btn_kulit"):
            st.info("ℹ️ **Langkah Selanjutnya:** Jangan oleskan pasta gigi, mentega, atau minyak. Tutup luka dengan kain bersih dan segera cari bantuan medis.")

    # --- TAB 3: TERTELAN ZAT ---
    with tab_tertelan:
        st.error("### Prosedur Pertolongan Pertama Zat Tertelan (Ingesti)")
        st.markdown("""
        1. **JANGAN DIPAKSA MUNTAH:** Jika zat yang tertelan bersifat korosif (seperti asam sulfat atau soda api), memaksa muntah akan merusak dinding kerongkongan untuk kedua kalinya.
        2. **KUMUR DENGAN AIR:** Jika korban sadar, minta untuk berkumur dengan air bersih berkali-kali untuk membersihkan sisa zat di mulut.
        3. **MINUM AIR PUTIH:** Berikan 1-2 gelas air putih untuk mengencerkan racun di dalam lambung (hanya jika korban sadar penuh dan bisa menelan).
        """)
        if st.button("Lihat Peringatan Medis Pent
