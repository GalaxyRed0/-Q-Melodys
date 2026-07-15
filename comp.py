import os
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
            "LOOP_PATTERN": "loop\\((\\d+)\\)\\{\\s*([^}]+)\\s*\\}",
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
    pattern = r"\{([^}]+)\}"
    while True:
        match = re.search(pattern, metin)
        if not match:
            break
        icerik = match.group(1)
        tokens = re.findall(r'\[[^\]]+\]|\S+', icerik)
        reversed_tokens = tokens[::-1]
        genislemis = " ".join(reversed_tokens)
        metin = metin.replace(match.group(0), genislemis)
    return metin

def beste_derle(metin):
    # --- DERLEME HATALARI (COMPILER ERRORS) ---
    if metin.count("{") != metin.count("}"):
        return ["__ERR__", "Süslü parantez kapatılmamış veya eşleşmiyor [ERR-C01]"]
        
    if metin.count("[") != metin.count("]"):
        return ["__ERR__", "Akor (Köşeli) parantezleri eşleşmiyor [ERR-C02]"]
        
    if "loop" in metin:
        # Basit loop formasyon kontrolü
        if not re.search(r"loop\(\d+\)\{", metin.replace(" ", "")):
            return ["__ERR__", "Geçersiz loop komut dizilimi [ERR-C03]"]

    # Derleme İşlemi
    metin = degiskenleri_genislet(metin)
    metin = ters_modifikatoru_isle(metin)
    parcalar = re.findall(r'\[[^\]]+\]|\S+', metin)
    
    return parcalar
