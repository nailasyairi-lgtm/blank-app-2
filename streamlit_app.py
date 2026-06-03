import streamlit as st
import random

# Konfigurasi halaman
st.set_page_config(page_title="Kuis Interaktif Kation & Anion", page_icon="🧪", layout="centered")

# ==========================================
# DATABASE 20 SOAL (10 KATION & 10 ANION)
# ==========================================
SOAL_MASTER = [
    # --- SOAL KATION (1-10) ---
    {
        "pertanyaan": "Kation kelompok mana yang mengendap sebagai klorida jika ditambahkan asam klorida (HCl) encer?",
        "pilihan": ["Golongan I (Ag+, Pb2+, Hg2^2+)", "Golongan II (Cu2+, Cd2+, As3+)", "Golongan III (Fe3+, Al3+, Cr3+)", "Golongan IV (Ba2+, Ca2+, Sr2+)"],
        "jawaban": "Golongan I (Ag+, Pb2+, Hg2^2+)",
        "pembahasan": "Kation Golongan I adalah kation yang mengendap sebagai garam klorida yang tidak larut dalam suasana asam encer."
    },
    {
        "pertanyaan": "Jika larutan yang mengandung kation Fe^3+ ditambahkan pereaksi KSCN (Kalium Tiosianat), warna larutan akan berubah menjadi...",
        "pilihan": ["Merah darah", "Biru tua", "Hijau muda", "Kuning jernih"],
        "jawaban": "Merah darah",
        "pembahasan": "Reaksi Fe^3+ dengan SCN- membentuk kompleks [Fe(SCN)]^2+ yang berwarna merah darah yang sangat khas."
    },
    {
        "pertanyaan": "Endapan kuning terang PbI2 terbentuk ketika kation Timbal (Pb^2+) direaksikan dengan...",
        "pilihan": ["Kalium Iodida (KI)", "Natrium Hidroksida (NaOH)", "Asam Sulfat (H2SO4)", "Amonia (NH3)"],
        "jawaban": "Kalium Iodida (KI)",
        "pembahasan": "Pb^2+ bereaksi dengan ion I- menghasilkan endapan timbal(II) iodida (PbI2) yang berwarna kuning emas/terang."
    },
    {
        "pertanyaan": "Kation Cu^2+ jika ditambahkan sedikit larutan Amonia (NH3) akan membentuk endapan biru muda. Jika Amonia ditambahkan berlebih, endapan tersebut akan larut kembali membentuk larutan berwarna...",
        "pilihan": ["Biru tua/intens", "Hijau zamrud", "Ungu", "Tak berwarna"],
        "jawaban": "Biru tua/intens",
        "pembahasan": "Kelebihan amonia menyebabkan pembentukan ion kompleks tetraminatembaga(II) [Cu(NH3)4]^2+ yang larut dan berwarna biru tua."
    },
    {
        "pertanyaan": "Uji nyala (flame test) untuk kation Kalsium (Ca^2+) memberikan warna nyala yang khas, yaitu...",
        "pilihan": ["Merah bata", "Kuning", "Ungu", "Hijau"],
        "jawaban": "Merah bata",
        "pembahasan": "Ca2+ memberikan warna merah bata. Sebagai tambahan, Na+ memberikan warna kuning, K+ berwarna ungu, dan Ba2+ berwarna hijau apel."
    },
    {
        "pertanyaan": "Uji spesifik untuk kation Amonium (NH4+) melibatkan pemanasan sampel dengan basa kuat (NaOH). Gas yang dilepaskan dapat diidentifikasi karena...",
        "pilihan": ["Mengubah kertas lakmus merah basah menjadi biru", "Mengubah kertas lakmus biru menjadi merah", "Membentuk endapan hitam dengan air", "Menghasilkan bau harum melati"],
        "jawaban": "Mengubah kertas lakmus merah basah menjadi biru",
        "pembahasan": "Gas amonia (NH3) yang terlepas bersifat basa, sehingga akan mengubah lakmus merah menjadi biru dan memiliki bau menyengat."
    },
    {
        "pertanyaan": "Kation Al^3+ dan Zn^2+ sama-sama membentuk endapan putih jika ditambahkan sedikit NaOH. Cara membedakannya adalah dengan menambahkan NaOH berlebih, lalu dialiri gas H2S. Kation yang akan membentuk endapan putih kembali adalah...",
        "pilihan": ["Zn^2+", "Al^3+", "Dua-duanya larut", "Dua-duanya mengendap"],
        "jawaban": "Zn^2+",
        "pembahasan": "Aluminium tidak mengendap dengan H2S, sedangkan Seng (Zn^2+) akan membentuk endapan seng sulfida (ZnS) yang berwarna putih."
    },
    {
        "pertanyaan": "Warna nyala kuning yang sangat dominan dan terang pada uji nyala disebabkan oleh keberadaan kation...",
        "pilihan": ["Natrium (Na+)", "Kalium (K+)", "Litium (Li+)", "Barium (Ba2+)"],
        "jawaban": "Natrium (Na+)",
        "pembahasan": "Natrium (Na+) memberikan warna nyala kuning emas yang sangat kuat bahkan pada intensitas konsentrasi yang kecil."
    },
    {
        "pertanyaan": "Pereaksi spesifik yang digunakan untuk mengidentifikasi kation Ni^2+ (Nikel) dalam suasana amoniakal sehingga menghasilkan endapan merah rose/merah muda adalah...",
        "pilihan": ["Dimetilglioksim (DMG)", "Asam Oksalat", "Kalson", "Ditianon"],
        "jawaban": "Dimetilglioksim (DMG)",
        "pembahasan": "Uji DMG adalah uji spesifik untuk nikel (Ni2+) yang menghasilkan kompleks kelat Ni(DMG)2 berwarna merah rose."
    },
    {
        "pertanyaan": "Kation Golongan IV (Ba2+, Sr2+, Ca2+) dipisahkan dari golongan lainnya dengan mengendapkannya sebagai garam...",
        "pilihan": ["Karbonat", "Klorida", "Sulfida", "Hidroksida"],
        "jawaban": "Karbonat",
        "pembahasan": "Kation golongan IV diendapkan menggunakan amonium karbonat (NH4)2CO3 dalam suasana netral atau sedikit basa."
    },
    
    # --- SOAL ANION (11-20) ---
    {
        "pertanyaan": "Anion yang jika ditambahkan asam kuat (seperti HCl atau H2SO4 encer) langsung menghasilkan gas CO2 yang dapat mengeruhkan air kapur adalah...",
        "pilihan": ["Karbonat (CO3^2-)", "Sulfat (SO4^2-)", "Klorida (Cl-)", "Nitrat (NO3-)"],
        "jawaban": "Karbonat (CO3^2-)",
        "pembahasan": "Karbonat terdekomposisi oleh asam membentuk gas CO2. Gas CO2 jika dialirkan ke air kapur Ca(OH)2 akan membentuk endapan putih CaCO3."
    },
    {
        "pertanyaan": "Larutan barium klorida (BaCl2) digunakan sebagai pereaksi utama untuk menguji adanya anion...",
        "pilihan": ["Sulfat (SO4^2-)", "Klorida (Cl-)", "Nitrat (NO3-)", "Asetat (CH3COO-)"],
        "jawaban": "Sulfat (SO4^2-)",
        "pembahasan": "Ion Ba^2+ akan berikatan dengan SO4^2- membentuk endapan putih Barium Sulfat (BaSO4) yang sangat stabil dan tidak larut dalam asam encer."
    },
    {
        "pertanyaan": "Uji cincin cokelat (brown ring test) yang menggunakan FeSO4 dan H2SO4 pekat digunakan untuk mengidentifikasi anion...",
        "pilihan": ["Nitrat (NO3-)", "Klorida (Cl-)", "Bromida (Br-)", "Fosfat (PO4^3-)"],
        "jawaban": "Nitrat (NO3-)",
        "pembahasan": "Cincin cokelat terbentuk akibat adanya kompleks [Fe(H2O)5(NO)]^2+ pada batas kedua cairan, menandakan adanya ion nitrat."
    },
    {
        "pertanyaan": "Anion Halida yang memberikan endapan kuning muda (pale yellow) dengan AgNO3 dan endapan tersebut sukar larut dalam amonia encer adalah...",
        "pilihan": ["Bromida (Br-)", "Klorida (Cl-)", "Iodida (I-)", "Fluorida (F-)"],
        "jawaban": "Bromida (Br-)",
        "pembahasan": "AgCl (putih, mudah larut amonia), AgBr (kuning muda, sukar larut), AgI (kuning kuat, tidak larut amonia)."
    },
    {
        "pertanyaan": "Jika sampel yang mengandung anion S^2- (Sulfida) ditambahkan asam kuat, akan tercium bau khas seperti...",
        "pilihan": ["Telur busuk", "Cuka", "Buah busuk", "Amonia menyengat"],
        "jawaban": "Telur busuk",
        "pembahasan": "Asam akan mendesak sulfida membentuk gas H2S (Hidrogen Sulfida) yang terkenal memiliki bau menyengat seperti telur busuk."
    },
    {
        "pertanyaan": "Anion yang jika digerus dengan sedikit H2SO4 pekat akan melepaskan uap berbau cuka yang tajam adalah...",
        "pilihan": ["Asetat (CH3COO-)", "Oksalat (C2O4^2-)", "Klorida (Cl-)", "Nitrat (NO3-)"],
        "jawaban": "Asetat (CH3COO-)",
        "pembahasan": "Reaksi asetat dengan asam kuat akan membebaskan molekul asam asetat (CH3COOH) alias asam cuka yang mudah menguap."
    },
    {
        "pertanyaan": "Pereaksi Amonium Molybdat dalam suasana asam nitrat digunakan untuk menguji keberadaan anion...",
        "pilihan": ["Fosfat (PO4^3-)", "Sulfat (SO4^2-)", "Kromat (CrO4^2-)", "Sianida (CN-)"],
        "jawaban": "Fosfat (PO4^3-)",
        "pembahasan": "Ion fosfat bereaksi dengan amonium molybdat membentuk endapan kristal kuning amonium fosfomolybdat."
    },
    {
        "pertanyaan": "Anion yang memiliki warna larutan kuning asli, dan berubah menjadi jingga jika suasana larutan diubah menjadi asam adalah...",
        "pilihan": ["Kromat (CrO4^2-)", "Dikromat (Cr2O7^2-)", "Permanganat (MnO4-)", "Tiosianat (SCN-)"],
        "jawaban": "Kromat (CrO4^2-)",
        "pembahasan": "Ion kromat (CrO4^2-, kuning) berkesetimbangan dengan dikromat (Cr2O7^2-, jingga). Penambahan asam mendesak kesetimbangan ke arah dikromat."
    },
    {
        "pertanyaan": "Larutan AgNO3 jika ditambahkan ke dalam larutan yang mengandung anion Iodida (I-) akan menghasilkan endapan berwarna...",
        "pilihan": ["Kuning", "Putih", "Hitam", "Merah bata"],
        "jawaban": "Kuning",
        "pembahasan": "Reaksi menghasilkan endapan Perak Iodida (AgI) yang berwarna kuning cerah dan tidak larut dalam larutan amonia."
    },
    {
        "pertanyaan": "Anion manakah di bawah ini yang tidak menghasilkan endapan dengan larutan AgNO3 maupun BaCl2 dalam suasana netral?",
        "pilihan": ["Nitrat (NO3-)", "Klorida (Cl-)", "Sulfat (SO4^2-)", "Karbonat (CO3^2-)"],
        "jawaban": "Nitrat (NO3-)",
        "pembahasan": "Hampir semua garam nitrat ($\text{NO}_3^-$) larut dalam air, sehingga tidak membentuk endapan dengan pereaksi kation umum."
    }
]

# ==========================================
# INISIALISASI SESSION STATE
# ==========================================
if "soal_acak" not in st.session_state:
    # Mengacak urutan 20 soal saat pertama kali web dibuka
    st.session_state.soal_acak = random.sample(SOAL_MASTER, len(SOAL_MASTER))

if "skor" not in st.session_state:
    st.session_state.skor = 0
if "index_soal" not in st.session_state:
    st.session_state.index_soal = 0
if "jawaban_terpilih" not in st.session_state:
    st.session_state.jawaban_terpilih = None
if "sudah_jawab" not in st.session_state:
    st.session_state.sudah_jawab = False

# ==========================================
# TAMPILAN INTERFACE
# ==========================================
st.title("🧪 Kuis Akbar: Kation & Anion")
st.write("Uji pemahaman mendalam Anda mengenai reaksi identifikasi kimia kualitatif di sini!")
st.markdown("---")

# Cek apakah kuis masih berlangsung
if st.session_state.index_soal < len(st.session_state.soal_acak):
    soal_sekarang = st.session_state.soal_acak[st.session_state.index_soal]
    
    # Progress Bar & Info Soal
    total_soal = len(st.session_state.soal_acak)
    progress = (st.session_state.index_soal) / total_soal
    st.progress(progress, text=f"Kemajuan: Soal {st.session_state.index_soal + 1} dari {total_soal}")
    
    # Tampilkan Pertanyaan
    st.markdown(f"### **Soal {st.session_state.index_soal + 1}**")
    st.subheader(soal_sekarang["pertanyaan"])
    
    # Tampilkan Pilihan Jawaban (Radio Button tanpa pilihan awal otomatis)
    pilihan = st.radio(
        "Pilih salah satu jawaban:", 
        soal_sekarang["pilihan"], 
        index=None, 
        key=f"q_{st.session_state.index_soal}"
    )
    
    st.write("") # Spasi bawah
    
    # Logika Tombol Aksi
    if not st.session_state.sudah_jawab:
        if st.button("Kirim Jawaban 📩", use_container_width=True):
            if pilihan is not None:
                st.session_state.jawaban_terpilled = pilihan # Menyimpan pilihan
                st.session_state.sudah_jawab = True
                
                # Cek JawabanBenar
                if pilihan == soal_sekarang["jawaban"]:
                    st.session_state.skor += 1
                st.rerun()
            else:
                st.warning("⚠️ Tolong pilih salah satu opsi terlebih dahulu sebelum mengirim!")
                
    else:
        # Menampilkan status benar/salah menggunakan radio button yang dipilih sebagai acuan visual
        if pilihan == soal_sekarang["jawaban"]:
            st.success(f"🎯 **Benar!** Jawaban Anda tepat sekali.")
        else:
            st.error(f"❌ **Salah.** Jawaban Anda: *{pilihan}*")
            st.warning(f"💡 **Jawaban yang Benar:** {soal_sekarang['jawaban']}")
            
        # Box Pembahasan
        with st.expander("📖 Lihat Pembahasan Lengkap", expanded=True):
            st.write(soal_sekarang["pembahasan"])
        
        # Tombol navigasi lanjut
        teks_tombol = "Lihat Hasil Akhir 🏆" if st.session_state.index_soal == total_soal - 1 else "Soal Selanjutnya ➡️"
        if st.button(teks_tombol, type="primary", use_container_width=True):
            st.session_state.index_soal += 1
            st.session_state.sudah_jawab = False
            st.rerun()

else:
    # ==========================================
    # HALAMAN SKOR AKHIR
    # ==========================================
    st.balloons()
    st.success("🎉 Selamat! Anda telah menyelesaikan seluruh rangkaian kuis.")
    
    total_soal = len(st.session_state.soal_acak)
    skor_akhir = (st.session_state.skor / total_soal) * 100
    
    # Tampilan statistik skor
    col1, col2, col3 = st.columns(3)
    col1.metric("Skor Akhir", f"{skor_akhir:.0f} / 100")
    col2.metric("Benar", f"{st.session_state.skor} Soal")
    col3.metric("Salah", f"{total_soal - st.session_state.skor} Soal")
    
    # Kalimat feedback berdasarkan skor
    st.markdown("---")
    if skor_akhir == 100:
        st.subheader("🥇 Luar Biasa! Anda Master Kimia Analisis Kualitatif!")
    elif skor_akhir >= 75:
        st.subheader("🥈 Kinerja Sangat Baik! Pemahaman Anda sudah sangat kuat.")
    elif skor_akhir >= 50:
        st.subheader("🥉 Cukup Baik! Sedikit belajar lagi untuk mengingat reaksi spesifiknya, ya.")
    else:
        st.subheader("📚 Jangan Menyerah! Yuk baca lagi tabel identifikasi kation-anion dan coba lagi.")
        
    st.write("")
    
    # Tombol Reset Kuis (Mengacak ulang soal)
    if st.button("Ulangi Kuis (Soal akan Diacak Lagi) 🔄", use_container_width=True):
        st.session_state.skor = 0
        st.session_state.index_soal = 0
        st.session_state.sudah_jawab = False
        st.session_state.soal_acak = random.sample(SOAL_MASTER, len(SOAL_MASTER)) # Acak ulang bank soal
        st.rerun()
