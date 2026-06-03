import streamlit as st
import random

# Konfigurasi halaman
st.set_page_config(page_title="Kuis Kation & Anion", page_icon="🧪", layout="centered")

# Database soal kuis
# Anda bisa menambah soal sesuka hati di sini
SOAL_BANK = [
    {
        "pertanyaan": "Manakah di bawah ini yang merupakan kation?",
        "pilihan": ["Na+", "Cl-", "SO4^2-", "NO3-"],
        "jawaban": "Na+",
        "pembahasan": "Kation adalah ion bermuatan positif. Na+ (Natrium) adalah kation, sedangkan yang lainnya adalah anion (bermuatan negatif)."
    },
    {
        "pertanyaan": "Pereaksi apa yang digunakan untuk menguji keberadaan anion Klorida (Cl-)?",
        "pilihan": ["AgNO3 (Perak Nitrat)", "BaCl2 (Barium Klorida)", "HCl (Asam Klorida)", "NaOH (Natrium Hidroksida)"],
        "jawaban": "AgNO3 (Perak Nitrat)",
        "pembahasan": "Anion Cl- jika bereaksi dengan AgNO3 akan menghasilkan endapan putih Perak Klorida (AgCl)."
    },
    {
        "pertanyaan": "Jika kation Ca2+ ditambahkan larutan amonium oksalat, endapan warna apa yang akan terbentuk?",
        "pilihan": ["Putih", "Kuning", "Biru", "Merah Bata"],
        "jawaban": "Putih",
        "pembahasan": "Kalsium (Ca2+) bereaksi dengan oksalat membentuk kalsium oksalat yang merupakan endapan putih."
    },
    {
        "pertanyaan": "Gas berbau menyengat yang mengubah kertas lakmus merah menjadi biru saat kation NH4+ dipanaskan dengan NaOH adalah...",
        "pilihan": ["Amonia (NH3)", "Klorin (Cl2)", "Oksigen (O2)", "Karbon Dioksida (CO2)"],
        "jawaban": "Amonia (NH3)",
        "pembahasan": "Pemanasan amonium (NH4+) dengan basa kuat (NaOH) akan melepaskan gas amonia (NH3) yang bersifat basa."
    },
    {
        "pertanyaan": "Anion yang memberikan hasil uji positif berupa 'cincin cokelat' dengan FeSO4 dan H2SO4 pekat adalah...",
        "pilihan": ["Nitrat (NO3-)", "Sulfat (SO4^2-)", "Karbonat (CO3^2-)", "Asetat (CH3COO-)"],
        "jawaban": "Nitrat (NO3-)",
        "pembahasan": "Uji cincin cokelat (brown ring test) adalah uji spesifik untuk mengidentifikasi keberadaan ion nitrat."
    }
]

# Inisialisasi session state agar data tidak hilang saat halaman di-refresh oleh Streamlit
if "skor" not in st.session_state:
    st.session_state.skor = 0
if "index_soal" not in st.session_state:
    st.session_state.index_soal = 0
if "jawaban_terpilih" not in st.session_state:
    st.session_state.jawaban_terpilih = None
if "sudah_jawab" not in st.session_state:
    st.session_state.sudah_jawab = False

# Tampilan Header
st.title("🧪 Kuis Identifikasi Kation & Anion")
st.write("Uji kemampuan Kimia Analisis Anda di sini!")
st.markdown("---")

# Cek apakah kuis sudah selesai
if st.session_state.index_soal < len(SOAL_BANK):
    soal_sekarang = SOAL_BANK[st.session_state.index_soal]
    
    # Progress Bar
    progress = (st.session_state.index_soal) / len(SOAL_BANK)
    st.progress(progress, text=f"Soal {st.session_state.index_soal + 1} dari {len(SOAL_BANK)}")
    
    # Tampilkan Pertanyaan
    st.subheader(soal_sekarang["pertanyaan"])
    
    # Tampilkan Pilihan Jawaban dengan Radio Button
    # Menggunakan index=None agar tidak ada yang terpilih otomatis di awal
    pilihan = st.radio("Pilih jawaban yang benar:", soal_sekarang["pilihan"], index=None, key=f"q_{st.session_state.index_soal}")
    
    # Tombol Submit
    if not st.session_state.sudah_jawab:
        if st.button("Kirim Jawaban"):
            if pilihan is not None:
                st.session_state.jawaban_terpilih = pilihan
                st.session_state.sudah_jawab = True
                # Cek Jawaban
                if pilihan == soal_sekarang["jawaban"]:
                    st.session_state.skor += 1
                st.rerun()
            else:
                st.warning("Silakan pilih salah satu jawaban terlebih dahulu!")
                
    # Jika sudah menjawab, tampilkan pembahasan dan tombol lanjut
    else:
        if st.session_state.jawaban_terpilih == soal_sekarang["jawaban"]:
            st.success(f"🎉 Benar! Jawaban Anda: {st.session_state.jawaban_terpilih}")
        else:
            st.error(f"❌ Salah. Jawaban Anda: {st.session_state.jawaban_terpilih}. Jawaban yang benar: {soal_sekarang['jawaban']}")
            
        st.info(f"**Pembahasan:** {soal_sekarang['pembahasan']}")
        
        if st.button("Soal Selanjutnya ➡️"):
            st.session_state.index_soal += 1
            st.session_state.sudah_jawab = False
            st.session_state.jawaban_terpilih = None
            st.rerun()

else:
    # Tampilan Skor Akhir
    st.balloons()
    st.success("✨ Kuis Selesai! ✨")
    skor_akhir = (st.session_state.skor / len(SOAL_BANK)) * 100
    st.metric(label="Skor Akhir Anda", value=f"{skor_akhir:.0f} / 100")
    st.write(f"Anda menjawab benar {st.session_state.skor} dari {len(SOAL_BANK)} soal.")
    
    # Tombol Reset Kuis
    if st.button("Ulangi Kuis 🔄"):
        st.session_state.skor = 0
        st.session_state.index_soal = 0
        st.session_state.sudah_jawab = False
        st.session_state.jawaban_terpilih = None
        st.rerun()
