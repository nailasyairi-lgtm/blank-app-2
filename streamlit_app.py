import streamlit as st
import time

# Konfigurasi halaman utama
st.set_page_config(
    page_title="Panduan Darurat Kontaminasi Kimia",
    page_icon="🚨",
    layout="wide"
)

# Judul Utama Aplikasi
st.title("🚨 Panduan Darurat: Penanganan Terkena Bahan Kimia")
st.write("Aplikasi respons cepat K3 untuk pertolongan pertama kecelakaan kerja akibat kontaminasi bahan kimia di laboratorium.")
st.markdown("---")

# Menggunakan kolom untuk memisahkan menu utama dan alat bantu timer
col_menu, col_timer = st.columns([2, 1])

with col_menu:
    st.subheader("📌 Pilih Area Tubuh yang Terkontaminasi:")
    
    # Navigasi menggunakan komponen selectbox agar responsif dan cepat
    kategori = st.selectbox(
        "Pilih kategori insiden di bawah ini:",
        [
            "--- Silakan Pilih ---",
            "👁️ 1. Terkena Mata (Kontaminasi Okular)",
            "🦺 2. Terkena Kulit / Badan (Tumpahan Skala Besar)",
            "👄 3. Tertelan Bahan Kimia (Ingesti)",
            "🫁 4. Terhirup Gas Beracun (Inhalasi)"
        ]
    )

    st.markdown("---")

    # LOGIKA UNTUK MASING-MASING KATEGORI INSIDEN
    if kategori == "--- Silakan Pilih ---":
        st.info("💡 **Petunjuk:** Pilih salah satu jenis insiden di atas untuk melihat langkah penanganan darurat secara instan.")
        
    elif kategori == "👁️ 1. Terkena Mata (Kontaminasi Okular)":
        st.error("### 👁️ PENANGANAN DARURAT: TERKENA MATA")
        st.markdown("""
        **Langkah yang WAJIB segera dilakukan:**
        1. **Jangan Menggosok Mata:** Mengucek mata dapat mempercepat penyerapan zat kimia atau menggores kornea.
        2. **Bawa ke Eye Wash Station:** Segera lari atau tuntun korban menuju pancuran pembilas mata (*eye washer*).
        3. **Bilas 15-20 Menit:** Buka kelopak mata lebar-lebar dengan jari, biarkan air mengalir membasahi bola mata secara terus-menerus.
        4. **Lepas Lensa Kontak:** Jika korban menggunakan lensa kontak, lepaskan di tengah-tengah pembilasan jika bisa dilepas dengan mudah.
        5. **Cari Bantuan Medis:** Setelah dibilas minimal 15 menit, segera bawa ke dokter spesialis mata dengan membawa info label reagen/MSDS.
        """)
        st.warning("⚠️ *Catatan: Gunakan fitur 'Safety Timer' di sebelah kanan untuk memandu durasi pembilasan mata Anda.*")

    elif kategori == "🦺 2. Terkena Kulit / Badan (Tumpahan Skala Besar)":
        st.error("### 🦺 PENANGANAN DARURAT: TERKENA KULIT / BADAN")
        st.markdown("""
        **Langkah yang WAJIB segera dilakukan:**
        1. **Gunakan Safety Shower:** Jika tumpahan asam/basa pekat mengenai area baju dan tubuh yang luas, segera berdiri di bawah pancuran darurat (*safety shower*).
        2. **Lepas Pakaian Kontaminasi:** Sembari diguyur air, lepas semua pakaian, jas lab, sepatu, dan perhiasan yang terkena bahan kimia tanpa menunda waktu.
        3. **Bilas Air Mengalir:** Biarkan air mengalir membilas area kulit yang terkena selama minimal 15 menit untuk mengencerkan konsentrasi zat korosif.
        4. **Jangan Gunakan Sabun Obat/Zat Penetral:** Jangan mencoba menetralkan asam dengan basa (atau sebaliknya) pada kulit karena reaksi netralisasi justru menghasilkan panas eksotermik yang memperparah luka bakar.
        5. **Tutup Luka:** Tutup longgar kulit yang melepuh dengan kain kasa steril, jangan diolesi pasta gigi atau minyak. Segera ke rumah sakit.
        """)

    elif kategori == "👄 3. Tertelan Bahan Kimia (Ingesti)":
        st.error("### 👄 PENANGANAN DARURAT: TERTELAN BAHAN KIMIA")
        st.markdown("""
        **Langkah yang WAJIB segera dilakukan:**
        1. **Identifikasi Zat:** Cari tahu segera apa yang tertelan (Asam kuat, basa pekat, atau senyawa logam berat).
        2. **Bilas Mulut:** Jika korban masih sadar, minta mereka berkumur dengan air bersih berkali-kali untuk membersihkan sisa zat di mulut.
        3. **JANGAN PAKSA MUNTAH (Kecuali Instruksi MSDS):** Memaksa muntah pada zat korosif (seperti $H_2SO_4$ atau $NaOH$) akan menyebabkan kerusakan/luka bakar kedua kalinya pada kerongkongan saat zat tersebut keluar kembali.
        4. **Minum Air/Susu (Jika Diizinkan):** Berikan air putih dalam jumlah sedang jika zat bersifat korosif untuk pengenceran, hanya jika korban sadar penuh dan bisa menelan.
        5. **Bawa ke IGD Segera:** Segera bawa korban ke rumah sakit terdekat bersama wadah bahan kimia atau lembar MSDS-nya.
        """)

    elif kategori == "🫁 4. Terhirup Gas Beracun (Inhalasi)":
        st.error("### 🫁 PENANGANAN DARURAT: TERHIRUP GAS BERACUN")
        st.markdown("""
        **Langkah yang WAJIB segera dilakukan:**
        1. **Utamakan Keselamatan Penolong:** Jangan masuk ke area ruangan penuh gas beracun (seperti gas $H_2S$, amonia, atau klorin) tanpa menggunakan masker respirator gas yang sesuai.
        2. **Evakuasi ke Udara Segar:** Segera pindahkan atau tuntun korban keluar dari ruangan laboratorium menuju area terbuka yang kaya oksigen bersih.
        3. **Longgarkan Pakaian:** Longgarkan kancing baju bagian atas atau dasi korban untuk mempermudah jalur pernapasan.
        4. **Cek Kesadaran & Napas:** Jika korban berhenti bernapas dan Anda telah terlatih, lakukan resusitasi jantung paru (RPR/CPR) atau berikan bantuan oksigen tabung jika tersedia.
        5. **Panggil Ambulans:** Gas beracun dapat menyebabkan edema paru-paru yang tertunda, korban wajib diperiksa oleh dokter sesegera mungkin.
        """)

# AREA SEBELAH KANAN: ALAT BANTU (SAFETY TIMER PEMBILASAN)
with col_timer:
    st.info("### ⏱️ Safety Timer Pembilasan")
    st.write("Standar internasional K3 mewajibkan pembilasan minimal selama **15 menit** (900 detik) tanpa henti saat terpapar bahan kimia cair korosif.")
    
    # Pilihan mode timer (mode demonstrasi 15 detik atau mode asli 15 menit)
    mode_timer = st.radio("Pilih Mode Waktu:", ["Mode Tes Cepat (15 Detik)", "Mode Asli Darurat (15 Menit)"])
    durasi = 15 if mode_timer == "Mode Tes Cepat (15 Detik)" else 900
    
    if st.button("▶️ Mulai Hitung Mundur Pembilasan", use_container_width=True):
        placeholder = st.empty()
        progres_bar = st.progress(0.0)
        
        for t in range(durasi, -1, -1):
            menit = t // 60
            detik = t % 60
            
            # Update tampilan waktu sisa
            placeholder.metric(label="Sisa Waktu Pembilasan Wajib", value=f"{menit:02d}:{detik:02d}")
            
            # Update progress bar
            persen_progres = (durasi - t) / durasi
            progres_bar.progress(persen_progres)
            
            time.sleep(1)
            
        st.success("🚨 **WAKTU PEMBILAS
