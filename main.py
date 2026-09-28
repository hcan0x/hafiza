import sqlite3
from datetime import datetime
from pathlib import Path
#---------AYARLAR---------
KLASOR = Path(__file__).parent
VERITABANI = KLASOR / "hafiza.db"
NOTLAR_KLASORU = KLASOR / "notlar"

def veritabani_hazirla():
    #fotoğraf ve video klasörü yoksa oluştur
    NOTLAR_KLASORU.mkdir(exist_ok=True)

    #veritabanına bağlan
baglanti = sqlite3.connect(VERITABANI)
imlec = baglanti.cursor()

# tabloyu oluştur (varsa dokunma),
imlec.execute('''
CREATE TABLE IF NOT EXISTS notes (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    title       TEXT,
    content     TEXT,
    mood        TEXT,
    tags        TEXT,
    attachment  TEXT,
    created_at  TEXT,
    updated_at  TEXT
    )
''')

# degisiklikleri kaydet ve baglantiyi gonder
baglanti.commit()
baglanti.close()
print("Veritabani ve klasör hazir.")

def not_ekle(title, content, mood=None, tags=None, attachment=None):
    simdi = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    baglanti = sqlite3.connect(VERITABANI)
    imlec = baglanti.cursor()

    imlec.execute('''
        INSERT INTO notes (title, content, mood, tags, attachment, created_at, updated_at)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (title, content, mood, tags, attachment, simdi, simdi))

    # degisiklikleri kaydet ve baglantiyi gonder
    baglanti.commit()
    yeni_id = imlec.lastrowid
    baglanti.close()
    print(f"Not eklendi (id={yeni_id}): {title}")

def menu_goster():
        print()
        print("           HAFIZA")
        print("----------------------------")
        print("1) Not Ekle")
        print("2) Notlari Listele")
        print("0) Çikis")
        print("----------------------------")

def notlari_listele():
    baglanti = sqlite3.connect(VERITABANI)
    imlec = baglanti.cursor()

    imlec.execute("""
        SELECT id, title, content, mood, tags, created_at
        FROM notes
        ORDER BY created_at DESC
        """)
    notlar = imlec.fetchall()
    baglanti.close()

    if not notlar:
        print("\nHenuz hic not yok. '1' ile ilk notunuzu ekleyin!")
        return

    print(f"\n*** {len(notlar)} Not Bulundu ***")
    print("=" * 50)
    for n in notlar:
        print(f"{n[0]} | {n[1]}")
        print(f"   Icerik : {n[2]}")
        if n[3]:
            print(f"   Ruh Hali : {n[3]}")
        if n[4]:
            print(f"   Etiketler : {n[4]}")
        print(f"   Tarih   : {n[5]}")
        print("-" * 50)

# Bu dosya direkt olarak çalıştırılırsa
if __name__ == "__main__":
    veritabani_hazirla()

    while True:
        menu_goster()
        secim = input("Seciminiz: ").strip()

        if secim == "1":
            title = input("Baslik   : ").strip()
            content = input("Icerik   : ").strip()
            mood = input("Ruh Hali    : ").strip() 
            tags = input("Etiketler   : ").strip()
            not_ekle(title, content, mood, tags)
        elif secim == "2":
            notlari_listele()
        elif secim == "0":
            print("Hoşçakalin, Hafizaniz sizi tekrar bekliyor.\n")
            break
        else:
            print("Gecersiz secim. Lutfen tekrar deneyin.")
