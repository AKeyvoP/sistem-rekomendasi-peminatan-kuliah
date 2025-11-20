import json
import os

def tanya(pertanyaan, opsi):
    print("\n" + pertanyaan)
    for huruf in opsi:
        print(f"{huruf}. {opsi[huruf]}")
    jawaban = ""
    while jawaban not in opsi:
        jawaban = input("Jawaban (huruf): ").lower()
    return jawaban

def tanya_fasih():
    while True:
        try:
            nilai = int(input("Seberapa fasih kamu dalam bidang ini? (0–10): "))
            if 0 <= nilai <= 10:
                return nilai
        except:
            pass
        print("Masukkan angka 0–10!")

def tampilkan_penjelasan(jurusan):
    penjelasan = {
        "Teknik Informatika": {
            "lingkup": "Mempelajari pembangunan perangkat lunak, algoritma, kecerdasan buatan, sistem komputer, dan teknologi digital.",
            "belajar": "Pemrograman, struktur data, basis data, AI, jaringan komputer, keamanan siber.",
            "kampus": "ITB, UI, UGM, ITS, Telkom University"
        },
        "Teknik Elektro": {
            "lingkup": "Mempelajari listrik, elektronika, telekomunikasi, kontrol, dan sistem tenaga.",
            "belajar": "Rangkaian listrik, telekomunikasi, mikrokontroler, robotika.",
            "kampus": "ITB, UI, ITS, UGM"
        },
        "Fisika": {
            "lingkup": "Ilmu dasar tentang energi, materi, dan fenomena alam.",
            "belajar": "Mekanika, elektromagnetik, optik, fisika kuantum.",
            "kampus": "ITB, UI, UGM"
        },
        "Matematika": {
            "lingkup": "Logika, analisis, statistika, dan struktur matematika.",
            "belajar": "Kalkulus, aljabar, peluang, statistik, optimasi.",
            "kampus": "ITB, UI, UGM"
        },
        "Statistika": {
            "lingkup": "Analisis data, probabilitas, pemodelan statistik.",
            "belajar": "Probabilitas, machine learning dasar, analisis data.",
            "kampus": "IPB, UI, UGM, ITS"
        },
        "Kedokteran": {
            "lingkup": "Tubuh manusia, penyakit, diagnosis, dan penanganan.",
            "belajar": "Anatomi, fisiologi, patologi, farmakologi.",
            "kampus": "UI, UGM, Unpad, Unair"
        },
        "Keperawatan": {
            "lingkup": "Perawatan medis dasar dan keperawatan klinis.",
            "belajar": "Keperawatan dasar, gawat darurat, komunitas.",
            "kampus": "UI, UGM, Unair"
        },
        "Farmasi": {
            "lingkup": "Obat, kimia medis, formulasi obat.",
            "belajar": "Kimia organik, farmakologi, farmasetika.",
            "kampus": "UI, ITB, UGM"
        },
        "Gizi": {
            "lingkup": "Nutrisi manusia dan manajemen diet.",
            "belajar": "Biokimia nutrisi, dietetik, mikrobiologi pangan.",
            "kampus": "UGM, IPB, Unair"
        },
        "Manajemen": {
            "lingkup": "Bisnis, organisasi, dan pengelolaan sumber daya.",
            "belajar": "Marketing, keuangan, SDM, manajemen operasi.",
            "kampus": "UI, UGM, Undip"
        },
        "Akuntansi": {
            "lingkup": "Keuangan, audit, perpajakan.",
            "belajar": "Akuntansi biaya, audit, perpajakan.",
            "kampus": "UI, UGM, Unair"
        },
        "Ekonomi Pembangunan": {
            "lingkup": "Ekonomi makro, pembangunan negara, kebijakan publik.",
            "belajar": "Ekonomi mikro, makro, matematika ekonomi.",
            "kampus": "UI, UGM, Undip"
        },
        "Psikologi": {
            "lingkup": "Perilaku dan mental manusia.",
            "belajar": "Psikologi klinis, sosial, industri.",
            "kampus": "UI, UGM, Unpad"
        },
        "Hukum": {
            "lingkup": "Hukum publik, perdata, pidana, dan bisnis.",
            "belajar": "Hukum pidana, perdata, tata negara.",
            "kampus": "UI, UGM, Unair"
        },
        "Ilmu Komunikasi": {
            "lingkup": "Media, PR, broadcasting.",
            "belajar": "Jurnalistik, PR, komunikasi pemasaran.",
            "kampus": "UI, Unpad, Undip"
        },
        "Hubungan Internasional": {
            "lingkup": "Diplomasi, politik global.",
            "belajar": "Politik luar negeri, organisasi internasional.",
            "kampus": "UI, UGM, Unair"
        },
        "Multimedia / Desain Komunikasi Visual": {
            "lingkup": "Desain visual, multimedia, animasi, branding.",
            "belajar": "Ilustrasi, desain grafis, UI/UX, animasi.",
            "kampus": "ITB FSRD, ISI Yogyakarta, BINUS"
        }
    }

    data = penjelasan.get(jurusan)
    if data:
        print("\n--- Informasi Tambahan ---")
        print("Lingkup Kuliah :", data["lingkup"])
        print("Yang Dipelajari:", data["belajar"])
        print("Kampus Favorit :", data["kampus"])
        print("--------------------------\n")
        return data
    return None

def analisa(score):
    kategori = max(score, key=score.get)

    kelompok_jurusan = {
        "saintek": ["Teknik Informatika",
                    "Teknik Elektro",
                    "Fisika",
                    "Matematika",
                    "Statistika"],

        "kesehatan": ["Kedokteran",
                      "Keperawatan",
                      "Farmasi",
                      "Gizi"],

        "ekonomi": ["Manajemen",
                    "Akuntansi",
                    "Ekonomi Pembangunan"],

        "soshum": ["Psikologi",
                   "Hukum",
                   "Ilmu Komunikasi",
                   "Hubungan Internasional"],

        "seni": ["Multimedia / Desain Komunikasi Visual"]
    }

    print("\n======================================")
    print("HASIL PEMINATAN UTAMA:", kategori.upper())
    print("Rekomendasi jurusan yang cocok:")
    print("======================================\n")

    daftar = kelompok_jurusan[kategori]
    for jurusan in daftar:
        print("- " + jurusan)
        tampilkan_penjelasan(jurusan)

    return kategori, daftar

def simpan_hasil(score, kategori, daftar_jurusan, filepath):
    data = {
        "skor_bidang": score,
        "peminatan_utama": kategori,
        "penjelasan_jurusan": {}
    }

    for jurusan in daftar_jurusan:
        data["penjelasan_jurusan"][jurusan] = tampilkan_penjelasan(jurusan)

    with open(filepath, "w") as file:
        json.dump(data, file, indent=4)

    print(f"\nData berhasil disimpan ke: {filepath}\n")

def main():
    print("======================================")
    print(" SISTEM REKOMENDASI PEMINATAN KULIAH ")
    print("======================================")

    score = {"saintek":0,
             "kesehatan":0,
             "ekonomi":0,
             "soshum":0,
             "seni":0
             }

    pertanyaan_list = [
        (
            "1. Pelajaran apa yang paling kamu sukai?",
            {"a": "Matematika / Fisika", "b": "Biologi", "c": "Ekonomi", "d": "Sosiologi / Bahasa", "e": "Seni / Desain"},
            {"a": "saintek", "b": "kesehatan", "c": "ekonomi", "d": "soshum", "e": "seni"}
        ),
        (
            "2. Aktivitas mana yang paling kamu nikmati?",
            {"a": "Soal logika", "b": "Menghafal biologi", "c": "Bisnis", "d": "Diskusi sosial", "e": "Menggambar / Editing / Desain"},
            {"a": "saintek", "b": "kesehatan", "c": "ekonomi", "d": "soshum", "e": "seni"}
        ),
        (
            "3. Nilai sekolah mana yang paling tinggi?",
            {"a": "Matematika / IPA", "b": "Biologi", "c": "Ekonomi / Akuntansi", "d": "Sejarah / Bahasa", "e": "Seni Budaya / Praktik Desain"},
            {"a": "saintek", "b": "kesehatan", "c": "ekonomi", "d": "soshum", "e": "seni"}
        ),
        (
            "4. Kamu lebih suka pekerjaan seperti apa?",
            {"a": "Teknis", "b": "Medis", "c": "Bisnis", "d": "Komunikatif", "e": "Kreatif & Visual"},
            {"a": "saintek", "b": "kesehatan", "c": "ekonomi", "d": "soshum", "e": "seni"}
        ),
        (
            "5. Kamu ingin kuliah di bidang yang lebih banyak:",
            {"a": "Hitungan & teknologi", "b": "Medis", "c": "Keuangan", "d": "Sosial", "e": "Seni, desain, dan kreativitas"},
            {"a": "saintek", "b": "kesehatan", "c": "ekonomi", "d": "soshum", "e": "seni"}
        )
    ]

    for pertanyaan, opsi, mapping in pertanyaan_list:
        jawab = tanya(pertanyaan, opsi)
        bidang = mapping[jawab]
        score[bidang] += 2
        print("\nBidang terkait jawaban:", bidang.upper())
        score[bidang] += tanya_fasih()

    kategori, daftar_jurusan = analisa(score)

    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    filepath = os.path.join(desktop, "hasil_akhir.json")

    simpan_hasil(score, kategori, daftar_jurusan, filepath)

main()
