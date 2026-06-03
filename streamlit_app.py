import streamlit as st

# 1. Judul Aplikasi
st.title("🚨 Respon Cepat Terkena Bahan Kimia")
st.write("Klik salah satu tombol di bawah ini sesuai dengan insiden yang terjadi untuk melihat panduan pertolongan pertama secara instan.")
st.markdown("---")

# 2. Navigasi Menggunakan Tombol Sederhana
# Kita membuat 4 tombol besar yang mudah diklik saat darurat
pilihan_menu = st.radio(
    "PILIH JENIS KECELAKAAN KERJA:",
    ("Silakan Pilih", "Terkena Mata", "Terkena Kulit / Badan", "Tertelan Bahan Kimia", "Terhirup Gas Beracun")
)

st.markdown("---")

# 3. Logika Menampilkan Informasi Berdasarkan Pilihan
if pilihan_menu == "Silakan Pilih":
    st.info("💡 Pilih salah satu opsi di atas untuk langsung menampilkan panduan K3.")

elif pilihan_menu == "Terkena Mata":
    st.error("### 👁️ PANDUAN: TERKENA MATA")
    st.markdown("""
    * **Langkah 1:** Segera bawa korban ke pancuran pembilas mata (*Eye Wash Station*).
    * **Langkah 2:** Bilas mata menggunakan air bersih mengalir selama **minimal 15 menit**.
    * **Langkah 3:** Paksa kelopak mata tetap terbuka lebar saat dibilas agar zat kimia encer dan keluar.
    * **Langkah 4:** Jangan menggosok atau mengucek mata dengan tangan atau tisu.
    * **Langkah 5:** Setelah 15 menit, tutup mata secara longgar dengan kain bersih dan segera bawa ke dokter.
    """)

elif pilihan_menu == "Terkena Kulit / Badan":
    st.error("### 🦺 PANDUAN: TERKENA KULIT / BADAN")
    st.markdown("""
    * **Langkah 1:** Jika tumpahan zat kimia pekat mengenai area baju/tubuh yang luas, segera berdiri di bawah *Safety Shower* (pancuran darurat).
    * **Langkah 2:** Sambil diguyur air, lepaskan semua pakaian, jas lab, dan perhiasan yang terkena bahan kimia.
    * **Langkah 3:** Bilas kulit yang terkena di bawah air mengalir selama **minimal 15 menit**.
    * **Langkah 4:** Jangan mengoleskan pasta gigi, mentega, minyak, atau zat penetral (reaksi penetralan justru memicu panas berlebih pada luka).
    * **Langkah 5:** Segera bawa korban ke fasilitas medis terdekat.
    """)

elif pilihan_menu == "Tertelan Bahan Kimia":
    st.error("### 👄 PANDUAN: TERTELAN BAHAN KIMIA")
    st.markdown("""
    * **Langkah 1:** Jika korban masih sadar, minta mereka berkumur dengan air bersih berkali-kali untuk membersihkan sisa zat di mulut.
    * **Langkah 2:** **JANGAN MEMAKSA KORBAN UNTUK MUNTAH** (terutama jika yang tertelan adalah asam/basa kuat, karena memicu muntah akan merusak dinding kerongkongan untuk kedua kalinya).
    * **Langkah 3:** Berikan 1 atau 2 gelas air putih murni untuk mengencerkan zat di lambung (HANYA jika korban sadar penuh).
    * **Langkah 4:** Segera hubungi ambulans atau bawa ke IGD rumah sakit.
    """)

elif pilihan_menu == "Terhirup Gas Beracun":
    st.error("### 🫁 PANDUAN: TERHIRUP GAS BERACUN")
    st.markdown("""
    * **Langkah 1:** Amankan diri Anda dulu (pakai masker respirator khusus) sebelum menolong korban di area penuh gas.
    * **Langkah 2:** Evakuasi korban secepatnya ke area terbuka yang memiliki **udara segar dan bersih**.
    * **Langkah 3:** Longgarkan pakaian bagian atas korban (seperti kerah baju atau dasi) untuk melancarkan pernapasan.
    * **Langkah 4:** Jika korban berhenti bernapas dan Anda menguasai tekniknya, berikan bantuan napas buatan (CPR).
    """)

# 4. Footer Kontak Darurat Tetap Ada di Bawah
st.markdown("---")
st.warning("📞 **Nomor Telepon Darurat Medis (Ambulans): 118 / 119**")
