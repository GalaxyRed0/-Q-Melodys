import os

# İzin/Dizin Kontrolleri
BASE_DIR = "/sdcard/@Q"
try:
    if not os.path.exists(BASE_DIR):
        os.makedirs(BASE_DIR, exist_ok=True)
except:
    BASE_DIR = "./@Q"

LIB_DIR = os.path.join(BASE_DIR, "lib")
os.makedirs(LIB_DIR, exist_ok=True)

SONG_NAMES = [
    "Yakamoz", "Gece_Treni", "Kizil_Gokyuzu", "Bahar_Yagmuru", "Sonbahar_Ruzgari",
    "Kayip_Kita", "Derin_Uzay", "Galaksi_Yolu", "Sonsuzluk", "Zaman_Yolcusu",
    "Neon_Sehir", "Siber_Gece", "Matrix_Kacis", "Kuantum_Sicramasi", "Yapay_Zeka",
    "Gunes_Tutulmasi", "Ay_Isigi", "Yildiz_Tozu", "Kozmik_Dans", "Meteor_Yagmuru",
    "Okyanus_Kalbi", "Mavi_Derinlik", "Mercan_Resifi", "Yunuslarin_Sarkisi", "Girdap",
    "Col_Ruzgari", "Vaha", "Kum_Firtinasi", "Piramit_Sirri", "Firavun_Gozu",
    "Orman_Ruhu", "Yesil_Deniz", "Yaprak_Hirtisi", "Agac_Golgeleri", "Doga_Ana",
    "Yanardag", "Ates_Dansi", "Lav_Nehri", "Kullerden_Dogus", "Anka_Kusu",
    "Buzul_Cagi", "Kar_Tanesi", "Kutup_Isiklari", "Buz_Dagi", "Donmus_Gemi",
    "Eski_Caglar", "Antik_Tapinak", "Unutulmus_Kral", "Efsanevi_Kilic", "Zafer_Marsi"
]

BESTE_SABLON = "bpm(140) vol(75) wave(sine) loop(2){ !##### _ } wave(square) loop(2){ ?@@@@@ _ } wave(saw) [#@*] _ wave(zigzag) ####"

for isim in SONG_NAMES:
    dosya_yolu = os.path.join(LIB_DIR, f"{isim}.txt")
    if not os.path.exists(dosya_yolu):
        with open(dosya_yolu, "w", encoding="utf-8") as f:
            f.write(BESTE_SABLON)

OZEL_SARKILAR = {
    "Toby_Fox_Finale": "bpm(140) vol(85) wave(saw) loop(8){ !#### _ ?@@ _ [ # @ * ] }",
    "Toby_Fox_Fallen_Down": "bpm(100) vol(75) wave(sine) loop(10){ ## @@ ** _ time(1) }",
    "Toby_Fox_Chaos_King": "bpm(155) vol(90) wave(square) loop(9){ !##### [#@*] _ ?@@@@ }",
    "Aytekin_Atas_Donmek": "bpm(90) vol(70) wave(zigzag) loop(6){ ### *** _ time(2) ## }",
    "Istiklal_Marsi": "bpm(115) vol(85) wave(square) loop(7){ #### @@@@ !### _ [#@*] }",
    "Tetris_Song": "bpm(145) vol(75) wave(square) loop(12){ @@ ## ** ## _ @@ *** }"
}

for isim, beste in OZEL_SARKILAR.items():
    dosya_yolu = os.path.join(LIB_DIR, f"{isim}.txt")
    if not os.path.exists(dosya_yolu):
        with open(dosya_yolu, "w", encoding="utf-8") as f:
            f.write(beste)