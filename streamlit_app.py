import streamlit as st
import random

# Konfigurasi halaman
st.set_page_config(page_title="Kuis K3 & APD Laboratorium Kimia", page_icon="🦺", layout="centered")

# ==========================================
# DATABASE 20 SOAL K3 & APD KATION/ANION
# ==========================================
SOAL_MASTER = [
    {
        "pertanyaan": "Saat menguji kation Amonium (NH4+) dengan memanaskan sampel bersama NaOH, gas amonia yang menyengat akan terlepas. Di manakah sebaiknya reaksi pemanasan ini dilakukan?",
        "pilihan": ["Di dalam Lemari Asam (Fume Hood)", "Di meja praktikum terbuka", "Di dekat jendela laboratorium", "Di ruang gelap"],
        "jawaban": "Di dalam Lemari Asam (Fume Hood)",
        "pembahasan": "Gas amonia ($NH_3$) bersifat korosif dan mengiritasi saluran pernapasan. Semua reaksi yang menghasilkan gas berbahaya harus dilakukan di dalam lemari asam."
    },
    {
        "pertanyaan": "Ketika mereaksikan anion Sulfida (S^2-) dengan asam untuk mendeteksi gas H2S (bau telur busuk), APD tambahan apa yang paling krusial digunakan selain jas lab dan kacamata?",
        "pilihan": ["Masker respirator gas / Masker filter karbon", "Sarung tangan kain", "Face shield plastik biasa", "Celemek plastik tipis"],
        "jawaban": "Masker respirator gas / Masker filter karbon",
        "pembahasan": "Gas $H_2S$ sangat beracun (bahkan pada konsentrasi tinggi dapat melumpuhkan saraf penciuman). Penggunaan masker dengan filter karbon aktif membantu menyaring uap gas beracun."
    },
    {
        "pertanyaan": "Uji cincin cokelat untuk anion Nitrat (NO3-) menggunakan Asam Sulfat (H2SO4) pekat. Bagaimana cara menuangkan H2SO4 pekat melalui dinding tabung reaksi dengan aman?",
        "pilihan": ["Dituangkan perlahan dengan posisi tabung miring menggunakan pipet tetes, memakai sarung tangan nitril", "Dituangkan langsung dari botol reagen dengan cepat", "Ditiup menggunakan mulut melalui pipet ukur", "Dituangkan sambil digojog (dikocok) kuat-kuat"],
        "jawaban": "Dituangkan perlahan dengan posisi tabung miring menggunakan pipet tetes, memakai sarung tangan nitril",
        "pembahasan": "Asam sulfat pekat sangat eksotermik (menghasilkan panas tinggi) dan korosif. Menuangkan lewat dinding secara perlahan mencegah cairan memercik keluar. Sarung tangan nitril memberikan perlindungan kimia yang baik."
    },
    {
        "pertanyaan": "Mengapa kita dilarang keras menggunakan sarung tangan berbahan kain saat memegang larutan asam pekat seperti HCl atau HNO3 untuk uji kation?",
        "pilihan": ["Kain dapat menyerap cairan asam dan menahannya langsung di kulit", "Kain membuat tangan menjadi terlalu panas", "Sarung tangan kain terlalu mahal", "Kain dapat mengubah warna larutan asam"],
        "jawaban": "Kain dapat menyerap cairan asam dan menahannya langsung di kulit",
        "pembahasan": "Sarung tangan kain bersifat porous (berpori). Jika terkena asam, cairan akan terserap dan menempel langsung pada kulit dalam waktu lama, memperparah luka bakar kimia. Gunakan sarung tangan berbahan nitril atau karet/latex."
    },
    {
        "pertanyaan": "Saat melakukan uji nyala (flame test) menggunakan kawat nikrom dan pembakar spiritus/Bunsen, tindakan K3 apa yang harus diperhatikan terkait rambut panjang?",
        "pilihan": ["Rambut harus diikat rapi ke belakang atau dimasukkan ke dalam kerudung/topi", "Rambut diberi gel agar kaku", "Rambut dibasahi dengan air", "Tidak perlu tindakan apa pun"],
        "jawaban": "Rambut harus diikat rapi ke belakang atau dimasukkan ke dalam kerudung/topi",
        "pembahasan": "Rambut yang terurai sangat mudah menyambar api dari pembakar Bunsen saat praktikan membungkuk untuk melihat warna nyala kation."
    },
    {
        "pertanyaan": "Jika mata Anda tidak sengaja kecipratan larutan perak nitrat (AgNO3) saat uji anion halida, tindakan pertama K3 yang paling tepat adalah...",
        "pilihan": ["Segera menuju Eye Washer dan membilas mata dengan air mengalir selama minimal 15 menit", "Mengusapnya dengan tisu kering sampai bersih", "Meneteskan obat tetes mata warung", "Membilasnya dengan larutan sabun cuci tangan"],
        "jawaban": "Segera menuju Eye Washer dan membilas mata dengan air mengalir selama minimal 15 menit",
        "pembahasan": "Pertolongan pertama kontaminasi bahan kimia pada mata adalah membilasnya segera di *eye washer* dengan air mengalir yang banyak untuk mengencerkan dan membuang zat kimia tersebut."
    },
    {
        "pertanyaan": "Simbol bahaya (GHS) yang biasanya tertera pada botol reagen Kalium Sianida (KCN) atau gas H2S yang digunakan dalam analisis kualitatif adalah...",
        "pilihan": ["Tengkorak dan tulang silang (Acute Toxicity)", "Api di atas lingkaran (Oxidizing)", "Pohon dan ikan mati (Environmental Hazard)", "Tanda seru (Irritant)"],
        "jawaban": "Tengkorak dan tulang silang (Acute Toxicity)",
        "pembahasan": "Simbol tengkorak menunjukkan zat tersebut memiliki racun akut (toksik tinggi) yang dapat menyebabkan kematian atau cedera serius meski dalam jumlah sedikit."
    },
    {
        "pertanyaan": "Mengapa Anda diwajibkan menggunakan sepatu tertutup (bukan sandal atau sepatu sandal) saat melakukan analisis kation dan anion?",
        "pilihan": ["Untuk melindungi kaki dari risiko ketumpahan cairan asam/basa pekat atau pecahan kaca tabung reaksi", "Agar terlihat formal dan rapi", "Supaya kaki tidak kedinginan di laboratorium", "Mengikuti tren fashion laboratorium"],
        "jawaban": "Untuk melindungi kaki dari risiko ketumpahan cairan asam/basa pekat atau pecahan kaca tabung reaksi",
        "pembahasan": "Sandal atau sepatu terbuka membiarkan kulit kaki telanjang, sehingga sangat rentan terkena tetesan bahan kimia korosif atau luka akibat pecahan kaca."
    },
    {
        "pertanyaan": "Saat memanaskan tabung reaksi yang berisi kation tertentu dan NaOH, ke mana arah mulut tabung reaksi harus dihadapkan?",
        "pilihan": ["Diarahkan ke area yang kosong (tidak menghadap diri sendiri atau orang lain)", "Diarahkan langsung ke wajah kita agar terlihat jelas", "Diarahkan ke wajah teman kelompok agar mereka ikut mengamati", "Diarahkan ke bawah meja"],
        "jawaban": "Diarahkan ke area yang kosong (tidak menghadap diri sendiri atau orang lain)",
        "pembahasan": "Pemanasan cairan dalam tabung reaksi dapat memicu efek *bumping* (cairan muncrat mendadak). Mengarahkannya ke tempat kosong mencegah cedera pada orang di sekitar."
    },
    {
        "pertanyaan": "Apa fungsi utama dari penggunaan 'Safety Goggles' (kacamata pelindung) dibandingkan kacamata baca biasa di laboratorium kimia?",
        "pilihan": ["Melindungi mata dari percikan kimia dari segala arah karena memiliki pelindung samping yang rapat", "Membuat penglihatan menjadi lebih tajam", "Mencegah mata lelah akibat radiasi Bunsen", "Sebagai pembeda antara praktikan dan dosen"],
        "jawaban": "Melindungi mata dari percikan kimia dari segala arah karena memiliki pelindung samping yang rapat",
        "pembahasan": "Safety goggles menutup rapat area sekitar mata, mencegah cairan atau uap kimia masuk dari sisi atas, bawah, maupun samping, berbeda dengan kacamata biasa yang memiliki celah terbuka."
    },
    {
        "pertanyaan": "Zat seperti Dimetilglioksim (DMG) atau KSCN sering digunakan dalam analisis kation. Setelah selesai melakukan praktikum, apa tindakan hygiene K3 yang wajib dilakukan?",
        "pilihan": ["Mencuci tangan dengan sabun dan air mengalir sebelum meninggalkan laboratorium", "Cukup mengelap tangan dengan jas lab", "Menyemprotkan handsanitizer saja tanpa cuci tangan", "Langsung pergi ke kantin untuk makan"],
        "jawaban": "Mencuci tangan dengan sabun dan air mengalir sebelum meninggalkan laboratorium",
        "pembahasan": "Handsanitizer tidak menghilangkan residu logam atau zat kimia. Mencuci tangan dengan sabun dan air mengalir adalah cara terbaik membuang sisa reagen yang menempel di kulit."
    },
    {
        "pertanyaan": "Di manakah tempat yang tepat untuk membuang limbah sisa uji kation logam berat seperti Pb^2+, Cu^2+, dan Hg^2+?",
        "pilihan": ["Botol penampung limbah khusus logam berat / limbah B3", "Bak cuci piring (wastafel) laboratorium langsung", "Tempat sampah domestik organik", "Disiramkan ke tanaman di luar lab"],
        "jawaban": "Botol penampung limbah khusus logam berat / limbah B3",
        "pembahasan": "Logama berat ($Pb, Hg, Cu$) bersifat toksik bagi lingkungan dan tidak dapat terurai secara alami. Limbahnya harus dikumpulkan dalam wadah jeriken khusus B3 untuk diolah lebih lanjut."
    },
    {
        "pertanyaan": "Jika jas laboratorium Anda terkena tumpahan Asam Nitrat (HNO3) pekat dalam jumlah yang cukup banyak, tindakan K3 yang benar adalah...",
        "pilihan": ["Segera melepas jas lab dan membilas bagian tubuh yang terkena di bawah Safety Shower", "Menunggu sampai praktikum selesai baru dilepas", "Mengelap jas lab menggunakan kertas isap/tisu", "Meniup-niup jas lab agar asamnya menguap"],
        "jawaban": "Segera melepas jas lab dan membilas bagian tubuh yang terkena di bawah Safety Shower",
        "pembahasan": "Jas lab berfungsi sebagai pelindung pertama. Jika zat kimia pekat menembus jas lab, jas harus segera dilepas dan tubuh dibasuh di *safety shower* untuk mencegah luka bakar kimia pada kulit."
    },
    {
        "pertanyaan": "Jas laboratorium yang ideal dan aman untuk bekerja di laboratorium kimia analisis kualitatif sebaiknya terbuat dari bahan...",
        "pilihan": ["Katun 100% atau campuran katun tebal", "Plastik tipis sekali pakai", "Kain polyester/sintetis murni yang mudah terbakar", "Wol tebal bulu domba"],
        "jawaban": "Katun 100% atau campuran katun tebal",
        "pembahasan": "Bahan katun tebal tidak mudah meleleh jika terkena panas atau api (tidak seperti poliester/sintetis) dan memberikan daya serap sementara yang baik sebelum cairan kimia menembus ke kulit."
    },
    {
        "pertanyaan": "Sebelum menggunakan tabung reaksi untuk menguji anion, kita melihat ada retakan rambut (hairline crack) kecil di bagian bawah tabung. Apa yang harus dilakukan?",
        "pilihan": ["Membuang tabung tersebut ke tempat sampah khusus kaca dan menggantinya dengan yang baru", "Tetap menggunakannya selama tidak bocor air", "Melapisinya dengan selotip bening", "Menggunakannya hanya untuk reaksi dingin tanpa pemanasan"],
        "jawaban": "Membuang tabung tersebut ke tempat sampah khusus kaca dan menggantinya dengan yang baru",
        "pembahasan": "Kaca yang retak, sekecil apa pun, berisiko tinggi pecah atau meledak saat menerima tekanan termal (dipanaskan) atau tekanan kimia, yang bisa menciderai praktikan."
    },
    {
        "pertanyaan": "Bahan kimia cair dipipet menggunakan alat bantu. Alat bantu K3 apa yang dilarang keras digunakan untuk memipet asam/basa pekat dalam uji kation?",
        "pilihan": ["Mulut langsung (pipetting by mouth)", "Rubber bulb (filler karet)", "Pipet pump otomatis", "Pipet tetes plastik"],
        "jawaban": "Mulut langsung (pipetting by mouth)",
        "pembahasan": "Memipet menggunakan mulut sangat berbahaya karena risiko cairan kimia pekat tertelan atau uap beracun langsung masuk ke paru-paru dan saluran pencernaan."
    },
    {
        "pertanyaan": "Simbol GHS berupa gambar 'Api bergolak di atas lingkaran' (Oxidizing) sering ditemukan pada botol reagen asam nitrat (HNO3) pekat. Apa arti dari simbol ini?",
        "pilihan": ["Zat tersebut dapat melepaskan oksigen dan memicu/memperparah kebakaran", "Zat tersebut mudah terbakar oleh percikan api kecil", "Zat tersebut dapat meledak jika terguncang", "Zat tersebut mengeluarkan gas panas"],
        "jawaban": "Zat tersebut dapat melepaskan oksigen dan memicu/memperparah kebakaran",
        "pembahasan": "Zat pengoksidasi (*oxidizing agents*) menyediakan oksigen bagi zat lain untuk terbakar. Penyimpanannya harus dijauhkan dari bahan organik atau zat yang mudah terbakar (*flammable*)."
    },
    {
        "pertanyaan": "Saat terjadi kebakaran kecil akibat tumpahan spiritus dari pembakar Bunsen di meja kerja Anda, alat apa yang paling tepat digunakan untuk memadamkannya dengan cepat?",
        "pilihan": ["APAR (Alat Pemadam Api Ringan) jenis CO2 atau Powder, atau kain lap basah", "Ditiup sekuat tenaga", "Disiram menggunakan satu gelas air minum", "Dikibas-kibas menggunakan jas lab"],
        "jawaban": "APAR (Alat Pemadam Api Ringan) jenis CO2 atau Powder, atau kain lap basah",
        "pembahasan": "Menyiram alkohol/spiritus yang terbakar dengan sedikit air justru bisa memperluas aliran api. Menggunakan APAR atau memutus pasokan oksigen dengan kain basah adalah metode pemadaman yang benar."
    },
    {
        "pertanyaan": "Dokumen standar internasional yang berisi informasi detail mengenai sifat fisik, bahaya kimia, APD yang diperlukan, dan pertolongan pertama suatu reagen (misal: AgNO3) disebut...",
        "pilihan": ["MSDS / SDS (Material Safety Data Sheet)", "Logbook Praktikum", "Jurnal Ilmiah Kimia", "Buku Panduan Inventaris Lab"],
        "jawaban": "MSDS / SDS (Material Safety Data Sheet)",
        "pembahasan": "MSDS/SDS adalah dokumen wajib di laboratorium yang memuat seluruh informasi keselamatan, penanganan, penyimpanan, dan regulasi darurat suatu bahan kimia."
    },
    {
        "pertanyaan": "Tindakan K3 apa yang harus dilakukan jika Anda mencium bau gas yang mencurigakan di laboratorium saat analisis anion sedang berlangsung?",
        "pilihan": ["Melaporkan segera kepada laboran/dosen pembimbing dan membuka jendela untuk meningkatkan ventilasi", "Mengabaikannya selama kepala tidak pusing", "Mencari sumber bau dengan mendekatkan hidung ke semua tabung", "Langsung berlari keluar berteriak histeris"],
        "jawaban": "Melaporkan segera kepada laboran/dosen pembimbing dan membuka jendela untuk meningkatkan ventilasi",
        "pembahasan": "Identifikasi awal kebocoran gas harus ditangani secara tenang namun cepat. Melaporkan ke pengawas dan membuka ventilasi membantu menurunkan konsentrasi gas berbahaya di ruangan."
    }
]

# ==========================================
# INISIALISASI SESSION STATE
# ==========================================
if "soal_acak" not in st.session_state:
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
st.title("🦺 Kuis K3 & APD Laboratorium")
st.subheader("Modul: Identifikasi Kation & Anion Secara Aman")
st.write("Uji kesiapan keselamatan kerja Anda sebelum melakukan praktikum kimia basah!")
st.markdown("---")

# Cek jalannya kuis
if st.session_state.index_soal < len(st.session_state.soal_acak):
    soal_sekarang = st.session_state.soal_acak[st.session_state.index_soal]
    
    total_soal = len(st.session_state.soal_acak)
    progress = (st.session_state.index_soal) / total_soal
    st.progress(progress, text=f"Soal {st.session_state.index_soal + 1} dari {total_soal}")
    
    st.markdown(f"#### **Pertanyaan Keselamatan {st.session_state.index_soal + 1}:**")
    st.markdown(f"### {soal_sekarang['pertanyaan']}")
    
    pilihan = st.radio(
        "Pilih tindakan atau jawaban yang paling aman sesuai prosedur K3:", 
        soal_sekarang["pilihan"], 
        index=None, 
        key=f"k3_{st.session_state.index_soal}"
    )
    
    st.write("")
    
    if not st.session_state.sudah_jawab:
        if st.button("Kirim Jawaban 🛡️", use_container_width=True):
            if pilihan is not None:
                st.session_state.jawaban_terpilih = pilihan
                st.session_state.sudah_jawab = True
                
                if pilihan == soal_sekarang["jawaban"]:
                    st.session_state.skor += 1
                st.rerun()
            else:
                st.warning("⚠️ Utamakan keselamatan, silakan pilih salah satu opsi terlebih dahulu!")
                
    else:
        if pilihan == soal_sekarang["jawaban"]:
            st.success(f"✅ **Tindakan Benar!** Anda memahami prosedur keselamatan dengan sangat baik.")
        else:
            st.error(f"❌ **Tindakan Kurang Tepat / Berbahaya.** Pilihan Anda: *{pilihan}*")
            st.warning(f"🛡️ **Prosedur Aman yang Benar:** {soal_sekarang['jawaban']}")
            
        with st.expander("🦺 Penjelasan Regulasi K3", expanded=True):
            st.write(soal_sekarang["pembahasan"])
        
        teks_tombol = "Lihat Evaluasi K3 🏆" if st.session_state.index_soal == total_soal - 1 else "Soal K3 Selanjutnya ➡️"
        if st.button(teks_tombol, type="primary", use_container_width=True):
            st.session_state.index_soal += 1
            st.session_state.sudah_jawab = False
            st.session_state.jawaban_terpilih = None
            st.rerun()

else:
    # ==========================================
    # HALAMAN SKOR AKHIR K3
    # ==========================================
    st.balloons()
    st.success("🎉 Luar biasa! Anda telah menyelesaikan Kuis Pembekalan K3 Laboratorium.")
    
    total_soal = len(st.session_state.soal_acak)
    skor_akhir = (st.session_state.skor / total_soal) * 100
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Skor K3", f"{skor_akhir:.0f} / 100")
    col2.metric("Aman (Benar)", f"{st.session_state.skor}")
    col3.metric("Beresiko (Salah)", f"{total_soal - st.session_state.skor}")
    
    st.markdown("---")
    if skor_akhir == 100:
        st.subheader("🟢 Lolos Sertifikasi Lab! Anda siap bekerja 100% aman di laboratorium.")
    elif skor_akhir >= 80:
        st.subheader("🟡 Diizinkan Masuk Lab! Pemahaman K3 Anda sudah sangat baik, tetap waspada saat praktikum.")
    else:
        st.subheader("🔴 Evaluasi Ulang Diperlukan! Anda wajib meninjau kembali berkas MSDS dan aturan APD sebelum melakukan praktikum kation-anion demi keselamatan diri sendiri.")
        
    st.write("")
    
    if st.button("Ulangi Kuis K3 (Acak Soal Baru) 🔄", use_container_width=True):
        st.session_state.skor = 0
        st.session_state.index_soal = 0
        st.session_state.sudah_jawab = False
        st.session_state.soal_acak = random.sample(SOAL_MASTER, len(SOAL_MASTER))
        st.rerun()
