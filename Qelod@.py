import array
import math
import os
import re
import sys
import time
import wave
import pygame

# =====================================================================
# [*] AUTO.PY KAYNAK KODU (OTOMATİK OLUŞTURUCU V1.5.3)
# =====================================================================
AUTO_PY_KODU = """
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
"""

COMP_JSON_KODU = """{
  "VERSION": "1.5.3",
  "WAVE_TYPES": ["square", "sine", "saw", "zigzag"],
  "FREK_KALIN": [440, 494, 523, 587, 659],
  "FREK_TIZ": [987, 1046, 1174, 1318, 1396],
  "FREK_BOGUK": [1200, 900, 600, 300, 150],
  "MODIFIERS": {
    "REVERSE_START": "{",
    "REVERSE_END": "}",
    "LOOP_PATTERN": "loop\\\\((\\\\d+)\\\\)\\\\{\\\\s*([^}]+)\\\\s*\\\\}",
    "CHORD_START": "[",
    "CHORD_END": "]"
  }
}"""

COMP_PY_KODU = """import os
import json
import re

def konfigurasyon_yukle():
    yol = "/sdcard/@Q/comp.json" if os.path.exists("/sdcard/@Q") else "./@Q/comp.json"
    if os.path.exists(yol):
        try:
            with open(yol, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            pass
    return {
        "VERSION": "1.5.3",
        "WAVE_TYPES": ["square", "sine", "saw", "zigzag"],
        "FREK_KALIN": [440, 494, 523, 587, 659],
        "FREK_TIZ": [987, 1046, 1174, 1318, 1396],
        "FREK_BOGUK": [1200, 900, 600, 300, 150],
        "MODIFIERS": {
            "REVERSE_START": "{",
            "REVERSE_END": "}",
            "LOOP_PATTERN": "loop\\\\((\\\\d+)\\\\)\\\\{\\\\s*([^}]+)\\\\s*\\\\}",
            "CHORD_START": "[",
            "CHORD_END": "]"
        }
    }

def degiskenleri_genislet(metin):
    config = konfigurasyon_yukle()
    pattern = config["MODIFIERS"]["LOOP_PATTERN"]
    while True:
        match = re.search(pattern, metin)
        if not match:
            break
        tekrar = int(match.group(1))
        icerik = match.group(2)
        genislemis = (icerik + " ") * tekrar
        metin = metin.replace(match.group(0), genislemis)
    return metin

def ters_modifikatoru_isle(metin):
    pattern = r"\\{([^}]+)\\}"
    while True:
        match = re.search(pattern, metin)
        if not match:
            break
        icerik = match.group(1)
        tokens = re.findall(r'\\[[^\\]]+\\]|\\\\S+', icerik)
        reversed_tokens = tokens[::-1]
        genislemis = " ".join(reversed_tokens)
        metin = metin.replace(match.group(0), genislemis)
    return metin

def beste_derle(metin):
    if metin.count("{") != metin.count("}"):
        return ["__ERR__", "Süslü parantez kapatılmamış veya eşleşmiyor [ERR-C01]"]
    if metin.count("[") != metin.count("]"):
        return ["__ERR__", "Akor (Köşeli) parantezleri eşleşmiyor [ERR-C02]"]
    if "loop" in metin:
        if not re.search(r"loop\\\\(\\\\d+\\\\)\\\\\{", metin.replace(" ", "")):
            return ["__ERR__", "Geçersiz loop komut dizilimi [ERR-C03]"]

    metin = degiskenleri_genislet(metin)
    metin = ters_modifikatoru_isle(metin)
    parcalar = re.findall(r'\\[[^\\]]+\\]|\\\\S+', metin)
    return parcalar
"""

def sistem_baslangici_ve_auto_kontrol():
    try:
        if not os.path.exists("/sdcard/@Q"):
            os.makedirs("/sdcard/@Q", exist_ok=True)
        base = "/sdcard/@Q"
    except:
        if not os.path.exists("./@Q"):
            os.makedirs("./@Q", exist_ok=True)
        base = "./@Q"
        
    auto_yol = os.path.join(base, "auto.py")
    with open(auto_yol, "w", encoding="utf-8") as f:
        f.write(AUTO_PY_KODU.strip())
        
    json_yol = os.path.join(base, "comp.json")
    if not os.path.exists(json_yol):
        with open(json_yol, "w", encoding="utf-8") as f:
            f.write(COMP_JSON_KODU.strip())

    comp_py_yol = os.path.join(base, "comp.py")
    if not os.path.exists(comp_py_yol):
        with open(comp_py_yol, "w", encoding="utf-8") as f:
            f.write(COMP_PY_KODU.strip())
        
    exec(open(auto_yol, encoding="utf-8").read())

ekranı_temizle = lambda: os.system("cls" if os.name == "nt" else "clear")
ekranı_temizle()
sistem_baslangici_ve_auto_kontrol()

sys.path.append("/sdcard/@Q")
sys.path.append("./@Q")
import comp

pygame.mixer.init(frequency=22050, size=-16, channels=1)

GUNCEL_DALGA = "square"
GUNCEL_BPM = 120
GUNCEL_SES = 4000  

FREK_KALIN = [440, 494, 523, 587, 659]
FREK_TIZ = [987, 1046, 1174, 1318, 1396]
FREK_BOGUK = [1200, 900, 600, 300, 150]
WAVE_TYPES = ["square", "sine", "saw", "zigzag"]


def dalga_formu_uret(frekans, sure_saniye, dalga_tipi="square", ses_seviyesi=4000):
    ornekleme_orani = 22050
    kalan_ornek = int(ornekleme_orani * sure_saniye)
    ham = []
    
    for i in range(kalan_ornek):
        t = i / ornekleme_orani
        if dalga_tipi == "sine":
            val = ses_seviyesi * math.sin(2 * math.pi * frekans * t)
        elif dalga_tipi == "saw":
            val = ses_seviyesi * 2 * (t * frekans - math.floor(t * frekans + 0.5))
        elif dalga_tipi == "zigzag":
            val = ses_seviyesi * 2 * abs(2 * (t * frekans - math.floor(t * frekans + 0.5))) - ses_seviyesi
        else: # square
            val = ses_seviyesi if (i * frekans // ornekleme_orani) % 2 == 0 else -ses_seviyesi
        ham.append(int(val))
        
    return ham


def play_and_get_wave(frekanslar, temel_sure, dalga_tipi, ses_seviyesi):
    bpm_factor = 120 / GUNCEL_BPM
    gecikme = temel_sure * bpm_factor
    ham_sesler = []
    
    for f in frekanslar:
        if f == 0:
            ham = [0] * int(22050 * gecikme)
            ham_sesler.extend(ham)
            time.sleep(gecikme)
        else:
            ham = dalga_formu_uret(f, gecikme, dalga_tipi, ses_seviyesi)
            ham_sesler.extend(ham)
            snd = pygame.mixer.Sound(buffer=array.array("h", ham))
            snd.play()
            time.sleep(gecikme)
    return ham_sesler


def play_chord_and_get_wave(frekanslar, temel_sure, dalga_tipi, ses_seviyesi):
    bpm_factor = 120 / GUNCEL_BPM
    gecikme = temel_sure * bpm_factor
    if not frekanslar: return []
    
    max_len = int(22050 * gecikme)
    mixed_ham = [0] * max_len
    
    for f in frekanslar:
        if f != 0:
            ham = dalga_formu_uret(f, gecikme, dalga_tipi, ses_seviyesi)
            snd = pygame.mixer.Sound(buffer=array.array("h", ham))
            snd.play()
            for i in range(min(len(ham), max_len)):
                mixed_ham[i] += ham[i]
                
    for i in range(len(mixed_ham)):
        if mixed_ham[i] > 32767: mixed_ham[i] = 32767
        elif mixed_ham[i] < -32768: mixed_ham[i] = -32768
        
    time.sleep(gecikme)
    return mixed_ham


def degiskenleri_genislet(metin):
    return comp.degiskenleri_genislet(metin)


def unlem_tekrar_sayisi(sembol_boyutu):
    if sembol_boyutu == 1: return 2
    elif sembol_boyutu == 2: return 4
    elif sembol_boyutu == 3: return 5
    elif sembol_boyutu == 4: return 6
    elif sembol_boyutu == 5: return 7
    return 1


def soru_isareti_tekrar_sayisi(sembol_boyutu):
    if sembol_boyutu == 1: return 3
    elif sembol_boyutu == 2: return 4
    elif sembol_boyutu == 3: return 6
    elif sembol_boyutu == 4: return 5
    elif sembol_boyutu == 5: return 7
    return 1


def yardim_menusu():
    print("\n" + "=" * 55)
    print("QELOD@ YARDIM MENÜSÜ (V1.5.3)")
    print("=" * 55)
    print("1. Standart Notalar (Arada boşluk bırakarak yazın):")
    print("   Kalınlar -> #  ##  ###  ####  #####")
    print("   Tizler   -> @  @@  @@@  @@@@  @@@@@")
    print("   İnceler  -> * ** *** **** *****")
    print("\n2. Zamanlayıcı Komutu:")
    print("   time(sayı) -> 1 ile 99 arasında bir saniye kadar bekletir.")
    print("   Örnek: # time(2) @  (Kalın nota çalar, 2 saniye bekler, tiz çalar)")
    print("   *Not: Parantez zorunludur. 0, negatif veya 99'dan büyük olamaz.")
    print("\n3. Ünlem Modifikatörü (!):")
    print("   Melodiyi özel adetlerde tekrar eder.")
    print("   !@ veya !#       -> 2 kere kalın")
    print("   !@@ veya !##     -> 4 kere kalın")
    print("   !@@@ veya !###   -> 5 kere kalın")
    print("   !@@@@ veya !#### -> 6 kere kalın")
    print("   !@@@@@ veya !##### -> 7 kere kalın")
    print("   !* -> 2 kere ince tiz ses")
    print("   !** -> 4 kere ince tiz ses")
    print("   !*** -> 5 kere ince tiz ses")
    print("   !**** -> 6 kere ince tiz ses")
    print("   !***** -> 7 kere ince tiz ses")
    print("\n4. Soru İşareti Modifikatörü (?):")
    print("   Melodiyi ince çalar ve özel adetlerde tekrar eder.")
    print("   ?@      -> 3 kere ince")
    print("   ?@@     -> 4 kere ince")
    print("   ?@@@    -> 6 kere ince")
    print("   ?@@@@   -> 5 kere ince")
    print("   ?@@@@@  -> 7 kere ince")
    print("\n5. Dalga Formları (Sesi Değiştirir):")
    print("   wave(sine)   -> Sinüs dalgası üretir (Yumuşak ton).")
    print("   wave(square) -> Kare dalga üretir (Varsayılan standart).")
    print("   wave(zigzag) -> Zigzag (üçgen) dalgası üretir.")
    print("   wave(saw)    -> Testere dişi dalga üretir.")
    print("\n6. Sistem Komutları:")
    print("   $help -> Bu yardım menüsünü gösterir.")
    print("   $set  -> Yazılım bilgilerini ve hakkında bölümünü gösterir.")
    print("   $sv   -> Yazılan bestenin sonuna eklenirse, parça çalındıktan sonra /sdcard/Music/ dizinine .mp3 formatında kaydeder.")
    print("   çıkış -> Programdan güvenli bir şekilde çıkar.")
    print("\n7. Kütüphane ve Yönetim (V1.4):")
    print("   $mls  -> Kütüphanedeki (.txt formatlı) şarkıları listeler.")
    print("   $lib  -> Library Manager'ı açar (Şarkı ekle/sil/listele).")
    print("   $play {şarkı adı} -> Kütüphanedeki şarkıyı çalar (Örn: $play Yakamoz).")
    print("\n8. V1.5 İleri Seviye Müzik Özellikleri:")
    print("   bpm(sayı) -> Parçanın temposunu ayarlar (Örn: bpm(140)). Varsayılan: 120.")
    print("   vol(sayı) -> Ses yüksekliğini ayarlar. 0-100 arası (Örn: vol(80)).")
    print("   _ veya -  -> Ritmik Es (Sessizlik) sembolüdür. Tempo hızına göre es verir.")
    print("   loop(N){...} -> Süslü parantez içindeki grubu N kere döngüye sokar (Örn: loop(3){ # @ }).")
    print("   [...]     -> Köşeli parantez içindeki notaları aynı anda (AKOR) çalar (Örn: [#@*]).")
    print("   $queue {ş1} {ş2} -> Belirtilen şarkıları sıra listesi yapıp arka arkaya çalar (Örn: $queue Yakamoz Vaha).")
    print("\n9. V1.5.2 Derleyici ve Ters Çevirme Özelliği:")
    print("   {...}     -> Süslü parantez içindeki notaları sondan başa (tersine) çalar.")
    print("   Örnek     -> Örn: {[@@##*]} sembolünü * ## @@ sırasıyla (tersine) işler.")
    print("\n10. V1.5.3 Hata Yönetimi ve Boğuk Ses Sembolü (&):")
    print("   &         -> İnce ve boğuk ses üretir. Sayısı arttıkça kalınlaşır (&&&&&).")
    print("   [&]       -> Akor yapılarıyla ([...]) %100 uyumludur.")
    print("   {&&}      -> Ters çevirme modülüyle ({...}) uyumludur.")
    print("   *NOT: ! veya ? modifikatörleriyle kullanılamaz (Derleme Hatası verir).")
    print("=" * 55 + "\n")


def parca_cal(parca):
    global GUNCEL_DALGA, GUNCEL_BPM, GUNCEL_SES
    ham_sesler = []
    
    # --- YENİ V1.5.3: Çalışma Zamanı (Runtime) Modifikatör Hata Kontrolü ---
    if ("!" in parca or "?" in parca) and "&" in parca:
        print(f"[!] HATA: Boğuk ses sembolü modifikatör kabul etmez [ERR-R01]")
        return []

    # --- BPM KONTROLÜ ---
    bpm_match = re.match(r"^bpm\((\d+)\)$", parca)
    if bpm_match:
        val = int(bpm_match.group(1))
        GUNCEL_BPM = max(1, val)
        print(f"[*] Tempo (BPM) ayarlandı: {GUNCEL_BPM}")
        return []

    # --- VOLUME (SES) KONTROLÜ ---
    vol_match = re.match(r"^vol\((\d+)\)$", parca)
    if vol_match:
        val = int(vol_match.group(1))
        val = max(0, min(100, val))
        GUNCEL_SES = int(val * 80)
        print(f"[*] Ses seviyesi ayarlandı: %{val}")
        return []

    # --- RİTMİK ES (SESSİZLİK) ---
    if parca in ["_", "-"]:
        return play_and_get_wave([0], 0.15, GUNCEL_DALGA, GUNCEL_SES)

    # --- POLİFONİ (AKOR YAPISI) - V1.5.3 (& Desteği Eklendi) ---
    if parca.startswith("[") and parca.endswith("]"):
        # Eski işlevleri bozmadan yalnızca & için tekrar desteklendi
        ic_notalar = re.findall(r"&{1,5}|[#@*]", parca[1:-1])
        frekanslar = []
        for n in ic_notalar:
            if n == "#": frekanslar.append(440)
            elif n in ["@", "*"]: frekanslar.append(987)
            elif n.startswith("&"): 
                frekanslar.append(FREK_BOGUK[len(n)-1])
        print(f"[*] Akor çalınıyor (Polifoni): {ic_notalar}")
        return play_chord_and_get_wave(frekanslar, 0.15, GUNCEL_DALGA, GUNCEL_SES)

    # --- WAVE() KONTROLÜ ---
    wave_match = re.match(r"^wave\((.+)\)$", parca)
    if wave_match:
        tip = wave_match.group(1).lower()
        if tip in WAVE_TYPES:
            GUNCEL_DALGA = tip
            print(f"[*] Dalga formu değiştirildi: {tip}")
            return []
        else:
            print(f"[!] HATA: Geçersiz dalga formu '{tip}' [ERR-R02]")
            return []
            
    if "wave" in parca and not (parca.startswith("wave(") and parca.endswith(")")):
        print(f"[!] HATA: wave kullanımı için parantez zorunludur! [ERR-R03]")
        return []

    # --- TIME(SAYI) KONTROLÜ ---
    time_match = re.match(r"^time\((.+)\)$", parca)
    if time_match:
        sure_metni = time_match.group(1)
        if sure_metni.isdigit():
            sure = int(sure_metni)
            if 1 <= sure <= 99:
                print(f"[*] {sure} saniye bekleniyor...")
                time.sleep(sure)
                return [0] * int(22050 * sure)
            else:
                print(f"[!] HATA: Süre 1-99 arasında olmalıdır! [ERR-R04]")
                return []
        else:
            print(f"[!] HATA: time() içinde sadece pozitif tam sayı olmalıdır [ERR-R05]")
            return []

    if "time" in parca and not (parca.startswith("time(") and parca.endswith(")")):
        print(f"[!] HATA: time kullanımı için parantez zorunludur! [ERR-R06]")
        return []

    # --- ! MODİFİKATÖRÜ KONTROLÜ ---
    if parca.startswith("!"):
        temiz_parca = parca[1:]
        karakter = temiz_parca[0] if temiz_parca else ""
        boyut = len(temiz_parca)

        if karakter in ["#", "@", "*"] and 1 <= boyut <= 5 and len(set(temiz_parca)) == 1:
            tekrar = unlem_tekrar_sayisi(boyut)
            if karakter == "*":
                frekanslar = FREK_TIZ[:boyut]
                gecikmeler = [0.12, 0.09, 0.09, 0.08, 0.07]
            else:
                frekanslar = FREK_KALIN[:boyut]
                gecikmeler = [0.15, 0.12, 0.12, 0.10, 0.09]

            gecikme = gecikmeler[boyut - 1]
            print(f"[*] Ünlem Etkisi: {parca} ({tekrar} kez çalınıyor)")
            for _ in range(tekrar):
                ham_sesler.extend(play_and_get_wave(frekanslar, gecikme, GUNCEL_DALGA, GUNCEL_SES))
            return ham_sesler
        else:
            print(f"[!] HATA: Geçersiz ünlem kombinasyonu -> {parca} [ERR-R07]")
            return []

    # --- ? MODİFİKATÖRÜ KONTROLÜ ---
    if parca.startswith("?"):
        temiz_parca = parca[1:]
        karakter = temiz_parca[0] if temiz_parca else ""
        boyut = len(temiz_parca)

        if karakter == "@" and 1 <= boyut <= 5 and set(temiz_parca) == {"@"}:
            tekrar = soru_isareti_tekrar_sayisi(boyut)
            frekanslar = FREK_TIZ[:boyut]
            gecikmeler = [0.12, 0.09, 0.09, 0.08, 0.07]
            gecikme = gecikmeler[boyut - 1]

            print(f"[*] Soru İşareti Etkisi: {parca} ({tekrar} kez ince çalınıyor)")
            for _ in range(tekrar):
                ham_sesler.extend(play_and_get_wave(frekanslar, gecikme, GUNCEL_DALGA, GUNCEL_SES))
            return ham_sesler
        else:
            print(f"[!] HATA: Geçersiz soru işareti kombinasyonu -> {parca} [ERR-R08]")
            return []

    # --- YENİ V1.5.3: BOGUK SES (&) KONTROLÜ ---
    if set(parca) == {"&"} and 1 <= len(parca) <= 5:
        frek_idx = len(parca) - 1
        # Boğuk etki yaratmak için sine dalgası ve kısık genlik zorlanır
        ham_sesler.extend(play_and_get_wave([FREK_BOGUK[frek_idx]], 0.15, "sine", int(GUNCEL_SES * 0.6)))
        return ham_sesler

    # --- STANDART ORİJİNAL NOTALAR ---
    elif parca == "#":
        ham_sesler.extend(play_and_get_wave([440], 0.15, GUNCEL_DALGA, GUNCEL_SES))
    elif parca == "##":
        ham_sesler.extend(play_and_get_wave([440, 494], 0.12, GUNCEL_DALGA, GUNCEL_SES))
    elif parca == "###":
        ham_sesler.extend(play_and_get_wave([440, 494, 523], 0.12, GUNCEL_DALGA, GUNCEL_SES))
    elif parca == "####":
        ham_sesler.extend(play_and_get_wave([440, 494, 523, 587], 0.10, GUNCEL_DALGA, GUNCEL_SES))
    elif parca == "#####":
        ham_sesler.extend(play_and_get_wave([440, 494, 523, 587, 659], 0.09, GUNCEL_DALGA, GUNCEL_SES))

    elif parca in ["@", "*"]:
        ham_sesler.extend(play_and_get_wave([987], 0.12, GUNCEL_DALGA, GUNCEL_SES))
    elif parca in ["@@", "**"]:
        ham_sesler.extend(play_and_get_wave([987, 1046], 0.09, GUNCEL_DALGA, GUNCEL_SES))
    elif parca in ["@@@", "***"]:
        ham_sesler.extend(play_and_get_wave([987, 1046, 1174], 0.09, GUNCEL_DALGA, GUNCEL_SES))
    elif parca in ["@@@@", "****"]:
        ham_sesler.extend(play_and_get_wave([987, 1046, 1174, 1318], 0.08, GUNCEL_DALGA, GUNCEL_SES))
    elif parca in ["@@@@@", "*****"]:
        ham_sesler.extend(play_and_get_wave([987, 1046, 1174, 1318, 1396], 0.07, GUNCEL_DALGA, GUNCEL_SES))
    
    else:
        print(f"[!] HATA: Geçersiz veya bilinmeyen sembol algılandı: '{parca}' [ERR-R09]")

    return ham_sesler


def beste_oynat(metin):
    global GUNCEL_DALGA, GUNCEL_BPM, GUNCEL_SES
    GUNCEL_DALGA = "square"
    GUNCEL_BPM = 120
    GUNCEL_SES = 4000
    
    kaydet_bayragi = False
    if metin.endswith("$sv"):
        kaydet_bayragi = True
        metin = metin[:-3].strip()

    parcalar = comp.beste_derle(metin)
    
    # Derleme Hatası Kontrolü (V1.5.3)
    if parcalar and parcalar[0] == "__ERR__":
        print(f"[!] DERLEME HATASI: {parcalar[1]}")
        return

    master_kayit = []

    for parca in parcalar:
        ses_verisi = parca_cal(parca)
        if ses_verisi:
            master_kayit.extend(ses_verisi)
            
        if not (parca.startswith("time(") or parca.startswith("wave(") or parca.startswith("bpm(") or parca.startswith("vol(")):
            bpm_factor = 120 / GUNCEL_BPM
            duraksama = 0.15 * bpm_factor
            time.sleep(duraksama)
            master_kayit.extend([0] * int(22050 * duraksama))

    if kaydet_bayragi and master_kayit:
        hedef_dizin = "/sdcard/Music"
        try: os.makedirs(hedef_dizin, exist_ok=True)
        except: hedef_dizin = "."

        dosya_adi = os.path.join(hedef_dizin, f"qelod_beste_{int(time.time())}.mp3")
        try:
            with wave.open(dosya_adi, "wb") as wf:
                wf.setnchannels(1)
                wf.setsampwidth(2)
                wf.setframerate(22050)
                wf.writeframes(array.array("h", master_kayit).tobytes())
            print(f"[*] Beste başarıyla kaydedildi: {dosya_adi}")
        except Exception as e:
            print(f"[!] Kayıt esnasında hata oluştu: {e}")


# =====================================================================
# [*] KÜTÜPHANE VE YÖNETİM MODÜLÜ
# =====================================================================

def lib_yolunu_al():
    if os.path.exists("/sdcard/@Q"): return "/sdcard/@Q/lib"
    return "./@Q/lib"


def sarkilari_listele():
    dizin = lib_yolunu_al()
    dosyalar = sorted([f for f in os.listdir(dizin) if f.endswith(".txt")])
    print("\nKÜTÜPHANEDEKİ ŞARKILAR:")
    print("-" * 40)
    if not dosyalar:
        print("Kütüphane boş.")
    else:
        for i, d in enumerate(dosyalar, 1):
            print(f"{i}. {d[:-4]}")
    print("-" * 40)


def lib_manager():
    dizin = lib_yolunu_al()
    while True:
        ekranı_temizle()
        print("=" * 40)
        print("[i] QELOD@ LIBRARY MANAGER")
        print("=" * 40)
        print("1. Kütüphanedeki Şarkıları Listele")
        print("2. Yeni Şarkı Ekle")
        print("3. Şarkı Sil")
        print("4. Ana Menüye Dön")
        print("=" * 40)
        
        sec = input("Seçiminiz: ").strip()
        if sec == "1":
            sarkilari_listele()
            input("\nDevam etmek için Enter'a basın...")
        elif sec == "2":
            isim = input("\nŞarkı adı (boşluksuz): ").strip()
            beste = input("Şarkı notalarını girin: ").strip()
            if isim and beste:
                if not isim.endswith(".txt"): isim += ".txt"
                with open(os.path.join(dizin, isim), "w", encoding="utf-8") as f:
                    f.write(beste)
                print(f"[*] '{isim}' başarıyla kütüphaneye eklendi!")
            input("\nDevam etmek için Enter'a basın...")
        elif sec == "3":
            sarkilari_listele()
            isim = input("\nSilmek istediğiniz şarkının tam adı: ").strip()
            if isim:
                if not isim.endswith(".txt"): isim += ".txt"
                dosya_yolu = os.path.join(dizin, isim)
                if os.path.exists(dosya_yolu):
                    os.remove(dosya_yolu)
                    print(f"[*] '{isim}' kütüphaneden silindi!")
                else:
                    print(f"[!] HATA: Şarkı bulunamadı [ERR-L01]")
            input("\nDevam etmek için Enter'a basın...")
        elif sec == "4":
            ekranı_temizle()
            break


# =====================================================================
# [*] CANLI BESTEKAR DÖNGÜSÜ
# =====================================================================

while True:
    print("======= [*] Qelod@ v1.5.3 =======")
    print("Komut listesi ve semboller için '$help' yazabilirsiniz.")
    print("Çıkmak için 'çıkış' yazmanız yeterli.\n")

    girdi = input("(: Bestenizi yazın veya komut girin: ").strip()

    if girdi.lower() == "çıkış":
        print("[*] Qelod@ Stüdyosundan çıkılıyor. Kulaklarına sağlık!")
        break

    if not girdi:
        ekranı_temizle()
        print("[!] HATA: Skor boş bırakılamaz! [ERR-S01]\n")
        continue

    if girdi == "$help":
        yardim_menusu()
        input("Devam etmek ve ekranı temizlemek için Enter'a basın...")
        ekranı_temizle()
        continue

    if girdi == "$mls":
        sarkilari_listele()
        input("\nDevam etmek için Enter'a basın...")
        ekranı_temizle()
        continue

    if girdi == "$lib":
        lib_manager()
        continue

    if girdi.startswith("$queue "):
        sarkilar = girdi.split(" ")[1:]
        print("\n[*] Sıralı oynatma listesi başlatılıyor...")
        for sarki in sarkilar:
            sarki = sarki.strip()
            if sarki:
                if not sarki.endswith(".txt"): sarki += ".txt"
                hedef_dosya = os.path.join(lib_yolunu_al(), sarki)
                if os.path.exists(hedef_dosya):
                    with open(hedef_dosya, "r", encoding="utf-8") as f:
                        okunan_beste = f.read().strip()
                    print(f"--> Şu an çalıyor: {sarki[:-4]}")
                    beste_oynat(okunan_beste)
                    time.sleep(0.5)
                else:
                    print(f"[!] HATA: '{sarki}' bulunamadı [ERR-L02]")
        print("[*] Liste bitti!\n" + "-" * 40)
        input("\nDevam etmek için Enter'a basın...")
        ekranı_temizle()
        continue

    if girdi.startswith("$play "):
        istenen = girdi.split(" ", 1)[1].strip()
        if istenen:
            if not istenen.endswith(".txt"): istenen += ".txt"
            hedef_dosya = os.path.join(lib_yolunu_al(), istenen)
            if os.path.exists(hedef_dosya):
                with open(hedef_dosya, "r", encoding="utf-8") as f:
                    okunan_beste = f.read().strip()
                print(f"\n[*] Kütüphaneden Çalınıyor: {istenen[:-4]}")
                beste_oynat(okunan_beste)
                print("[*] Şarkı Bitti!\n" + "-" * 40)
            else:
                print(f"[!] HATA: '{istenen}' kütüphanede bulunamadı [ERR-L03]")
        input("\nDevam etmek için Enter'a basın...")
        ekranı_temizle()
        continue

    if girdi == "$set":
        ekranı_temizle()
        print("\n" + "=" * 50)
        print("[i] YAZILIM BİLGİLERİ")
        print("Yazılım Adı: Qelod@")
        print("Versiyon: 1.5.3")
        print("-" * 50)
        print("Hakkında: Gelişmiş sentezleme modülleri ve tempo/ses")
        print("kontrollerine sahip terminal tabanlı müzik istasyonu.")
        print("Güncelleme Notu: Benzersiz hata kodlama sistemi (ERR-XXX) ")
        print("ve boğuk ses (&) eklendi.")
        print("=" * 50 + "\n")
        input("Devam etmek ve ekranı temizlemek için Enter'a basın...")
        ekranı_temizle()
        continue

    print("[*] Çalınıyor...")
    beste_oynat(girdi)
    print("[*] Bitti!\n" + "-" * 40)

    input("Ekranı temizlemek ve yeni işlem yapmak için Enter'a basın...")
    ekranı_temizle()
