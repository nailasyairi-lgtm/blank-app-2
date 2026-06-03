import streamlit as st
import pandas as pd

# Konfigurasi Halaman Utama
st.set_page_config(
    page_title="Panduan Interaktif K3 & APD Laboratorium",
    page_icon="🦺",
    layout="wide"
)

# Header Utama
st.title("🦺 Pusat Panduan Interaktif K3 & APD Laboratorium")
st.write("Platform edukasi digital untuk memastikan keselamatan kerja sebelum melakukan praktikum kimia analisis kualitatif.")
st.markdown("---")

# Navigasi Menu menggunakan Tabs di Bagian Atas
tab_apd, tab_simulasi, tab_ghs, tab_darurat = st.tabs([
    "🛡️ 1. Katalog APD Wajib", 
    "🕹️ 2. Simulasi Memakai APD", 
    "⚠️ 3. Simbol Bahaya GHS", 
    "🚨 4. Prosedur Darurat (First Aid)"
])

# =========================================================================
# TAB 1: KATALOG APD WAJIB
# =========================================================================
with tab_apd:
    st.header("Katalog Alat Pelindung Diri (APD) Standar")
    st.write("Berikut adalah spesifikasi APD yang wajib digunakan di laboratorium kimia:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.container(border=True):
            st.subheader("👕 1. Jas Laboratorium")
            st.markdown("""
            * **Bahan:** Katun 100% (Tebal).
            * **Fungsi:** Melindungi tubuh dan pakaian harian dari percikan zat asam/basa pekat.
            * **Aturan K3:** Wajib berlengan panjang dan seluruh kancing harus terpasang rapi. Dilarang menggulung lengan baju.
            """)
            
        with st.container(border=True):
            st.subheader("🥽 2. Safety Goggles (Kacamata Pelindung)")
            st.markdown("""
            * **Bahan:** Polikarbonat anti-pecah dengan pelindung samping rapat.
            * **Fungsi:** Mencegah percikan cairan korosif atau uap tajam langsung mengenai kornea mata.
            * **Aturan K3:** Kacamata baca biasa *tidak diizinkan* sebagai pengganti karena memiliki celah di bagian samping.
            """)

    with col2:
        with st.container(border=True):
            st.subheader("🧤 3. Sarung Tangan Nitril")
            st.markdown("""
            * **Bahan:** Karet Nitril sintetik (bebas latex).
            * **Fungsi:** Melindungi pori-pori kulit dari penetrasi larutan logam berat berbahaya ($Pb^{2+}$, $Hg^{2+}$) dan asam pekat.
            * **Aturan K3:** Jangan gunakan sarung tangan kain karena justru menyerap cairan kimia.
            """)
            
        with st.container(border=True):
            st.subheader("👟 4. Sepatu Tertutup")
            st.markdown("""
            * **Bahan:** Kulit atau sintetik tebal (bukan kain tipis/kanvas).
            * **Fungsi:** Menahan jatuhnya alat kaca yang pecah atau tumpahan reagen cair di lantai.
            * **Aturan K3:** Sandal, sepatu sandal, atau flat-shoes dengan punggung kaki terbuka dilarang keras.
            """)

# =========================================================================
# TAB 2: SIMULASI MEMAKAI APD (INTERAKTIF)
# =========================================================================
with tab_simulasi:
    st.header("🕹️ Simulasi Virtual: Ruang Ganti APD")
    st.write("Sebelum Anda diizinkan klik 'Masuk Laboratorium', lengkapi diri Anda dengan memilih APD yang benar di bawah ini:")
    
    # Komponen Interaktif Pilihan Pengguna
    pilih_jas = st.checkbox("Pakai Jas Laboratorium Katun Lengan Panjang")
    pilih_goggles = st.checkbox("Pakai Safety Goggles Rapat")
    pilih_sarung = st.selectbox("Pilih Jenis Sarung Tangan:", ["Tidak Pakai", "Sarung Tangan Kain", "Sarung Tangan Nitril K3"])
    pilih_sepatu = st.radio("Pilih Alas Kaki:", ["Sandal Santai", "Sepatu Kanvas / Slip-on", "Sepatu Kulit Tertutup"], index=0)
    
    st.markdown("---")
    
    # Tombol Evaluasi Simulasi
    if st.button("Verifikasi Kesiapan APD 🛡️", type="primary"):
        # Logika Pengecekan Keamanan
        is_aman = True
        pesan_error = []
        
        if not pilih_jas:
            is_aman = False
            pesan_error.append("- Anda belum memakai Jas Laboratorium.")
        if not pilih_goggles:
            is_aman = False
            pesan_error.append("- Mata Anda sangat rentan, pasang Safety Goggles!")
        if pilih_sarung != "Sarung Tangan Nitril K3":
            is_aman = False
            pesan_error.append("- Pilihan sarung tangan salah! Gunakan bahan Nitril untuk proteksi kimia.")
        if pilih_sepatu != "Sepatu Kulit Tertutup":
            is_aman = False
            pesan_error.append("- Alas kaki tidak aman. Wajib menggunakan Sepatu Tertutup.")
            
        # Output Hasil Keamanan
        if is_aman:
            st.balloons()
            st.success("🟢 STATUS: AMAN! Seluruh APD Anda memenuhi standar K3. Anda diizinkan masuk ke laboratorium.")
        else:
            st.error("🔴 STATUS: BAHAYA / DITOLAK! Anda belum siap memasuki laboratorium karena:")
            for err in pesan_error:
                st.write(err)

# =========================================================================
# TAB 3: SIMBOL BAHAYA GHS
# =========================================================================
with tab_ghs:
    st.header("⚠️ Sistem Klasifikasi Bahaya GHS (Globally Harmonized System)")
    st.write("Klik ikon di bawah ini untuk mempelajari arti simbol bahaya yang sering ditemukan pada botol reagen kation/anion:")
    
    simbol = st.radio(
        "Pilih Simbol Bahaya untuk Menampilkan Detail:",
        ["💀 Toksik Akut", "🔥 Korosif", "⭕ Pengoksidasi (Oxidizing)", "⚠️ Bahaya Kesehatan Jangka Panjang"],
        index=0
    )
    
    st.markdown("---")
    if simbol == "💀 Toksik Akut":
        st.error("### 💀 Toksik Akut (Acute Toxicity)")
        st.markdown("""
        * **Arti:** Bahan kimia yang dapat menyebabkan kematian atau kerusakan fatal pada tubuh seketika meskipun masuk dalam jumlah sedikit.
        * **Contoh di Lab:** Kalium Sianida ($KCN$), Gas Hidrogen Sulfida ($H_2S$).
        * **Tindakan K3:** Wajib dikerjakan di dalam Lemari Asam dan menggunakan masker respirator.
        """)
    elif simbol == "🔥 Korosif":
        st.warning("### 🔥 Korosif (Corrosive)")
        st.markdown("""
        * **Arti:** Zat yang dapat menghancurkan jaringan hidup (menyebabkan luka bakar kimia parah pada kulit/mata) dan merusak logam.
        * **Contoh di Lab:** Asam Sulfat pekat ($H_2SO_4$), Asam Klorida ($HCl$), Natrium Hidroksida ($NaOH$).
        * **Tindakan K3:** Hindari kontak langsung, gunakan sarung tangan nitril, tuangkan perlahan lewat dinding tabung.
        """)
    elif simbol == "⭕ Pengoksidasi (Oxidizing)":
        st.info("### ⭕ Bahan Pengoksidasi (Oxidizing)")
        st.markdown("""
        * **Arti:** Zat yang tidak mudah terbakar sendiri, namun melepaskan oksigen tinggi yang dapat memicu atau memperparah kebakaran bahan lain.
        * **Contoh di Lab:** Asam Nitrat pekat ($HNO_3$), Hidrogen Peroksida ($H_2O_2$).
        * **Tindakan K3:** Simpan jauh dari bahan organik, alkohol, atau pelarut yang mudah terbakar.
        """)
    elif simbol == "⚠️ Bahaya Kesehatan Jangka Panjang":
        st.warning("### ⚠️ Bahaya Kesehatan (Health Hazard)")
        st.markdown("""
        * **Arti:** Dapat menyebabkan kanker (karsinogenik), mutasi genetik, atau kerusakan organ pernapasan jangka panjang secara akumulatif.
        * **Contoh di Lab:** Indikator Benzena, Larutan Kation Timbal ($Pb^{2+}$), Kation Kadmium ($Cd^{2+}$).
        * **Tindakan K3:** Gunakan masker pelindung secara disiplin, jangan menghirup uap larutan langsung.
        """)

# =========================================================================
# TAB 4: PROSEDUR DARURAT (FIRST AID)
# =========================================================================
with tab_darurat:
    st.header("🚨 Prosedur Tanggap Darurat Laboratorium")
    st.write("Jika terjadi kecelakaan kerja kerja, lakukan tindakan pertolongan pertama berikut secara tenang namun cepat:")
    
    with st.expander("👁️ 1. Kontaminasi Bahan Kimia pada Mata"):
        st.markdown("""
        * **Tindakan:** Segera bawa korban ke **Eye Wash Station**.
        * **Prosedur:** Bilas mata dengan air mengalir bersih selama minimal 15-20 menit dengan posisi kelopak mata dipaksa terbuka. 
        * **Larangan:** Jangan menggosok mata dengan tangan atau tisu. Hubungi tim medis setelah pembilasan selesai.
        """)
        
    with st.expander("🦺 2. Tumpahan Zat Kimia Skala Besar ke Tubuh"):
        st.markdown("""
        * **Tindakan:** Segera menuju ke area **Safety Shower** terdekat.
        * **Prosedur:** Tarik tuas pancuran air, lalu lepaskan jas lab atau pakaian yang terkontaminasi secara cepat di bawah guyuran air. Bilas seluruh tubuh secara menyeluruh.
        """)
        
    with st.expander("🔥 3. Kebakaran Kecil di Meja Praktikum"):
        st.markdown("""
        * **Tindakan:** Gunakan **APAR (Alat Pemadam Api Ringan)**.
        * **Prosedur:** Ingat teknik **PASS** (Pull/Tarik pin, Aim/Arahkan ke sumber api, Squeeze/Tekan tuas, Sweep/Sapukan dari sisi ke sisi). Anda juga bisa menutup api kecil menggunakan kain lap yang telah dibasahi air.
        """)
