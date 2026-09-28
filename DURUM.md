# PROJE DURUMU (Kaldigimiz yer)

> Her oturum sonunda bu dosyayi guncelle.
> YENI OTURUMDA AI'ya: "Desktop'taki hafiza projesinin DURUM.md dosyasini oku" de.
> Kaldigimiz yerden devam ederiz.

===============================================================
## PROJE: Hafiza - Kisisel hayat arsivi (AI destekli)
===============================================================

## FIKIR (neden yapiyoruz?)
Iki proje fikri konusuldu:
  1) "Ters Sosyal Medya" -> SADECE kendi hayatini arsivle, baskalarini degil.
     "3 ay once ne dusunuyordum?" diye sorunca cevap veren kisisel hafiza.
  2) Abonelik/bosa harcama dedektifi (yedek fikir)
SECILEN: 1 numarali fikir -> "Hafiza" projesi

Neden tutar:
- Herkes gecmisini unutur
- AI cagi bunu bedava mumkun kildi
- Gizlilik: veri SENIN bilgisayarinda kalir (buyuk rakipler yapamaz)
- Hasan'in Jarvis projesindeki altyapi (ses, AI, pencere) tekrar kullanilabilir

## MALIYET / OLCEK (konusuldu)
- 0-100 kullanici      : 0 TL (hepsi free tier)
- 100-5.000 kullanici  : ~1000 TL/ay max (sadece AI asilirsa)
- 5.000-50.000         : ~8000 TL/ay (burada gelir de baslar)
- 50.000+              : ~86000 TL/ay (ama kar var)
SONUC: Baslangic bedava, tek gercek yatirim ZAMAN.

## YOL HARITASI
- [ ] Faz 1: Iskelet (kaydet + listele + ara)
- [ ] Faz 2: AI beyin (Groq ile dogal dil sorgu) - Groq anahtari zaten var
- [ ] Faz 3: Otomatik yakalama (tarayici eklenti / ekran)
- [ ] Faz 4: Yayin (web: Supabase + Vercel, buyume)

## MIMARI KARARI
- Python ile basla (Hasan Python + VS Code biliyor)
- Ama kodu "backend mantigi" ile yaz -> sonra web'e kolay tasinsin
- A, B, C hepsi hedef: once masaustu calissin, sonra web

## BUGUN (Oturum 1) YAPILANLAR
- Proje klasoru olusturuldu: C:\Users\HP\OneDrive\Desktop\hafiza
- Git baslatildi (main dali)
- 3 dosya eklendi: README.md, .gitignore, DURUM.md
- ILK COMMIT atildi: b66684e
- "Kaldigimiz yeri hatirlama" sistemi kuruldu (DURUM.md + Git)

## OTURUM 2 (GitHub baglama) YAPILANLAR
- gh (GitHub CLI) kuruldu: winget install GitHub.cli (v2.101.0)
- gh auth login yapildi -> hesap: hcan0x
- GitHub repo olusturuldu ve push edildi: https://github.com/hcan0x/hafiza (PUBLIC)
- Yerel repo = uzak repo senkron (main -> origin/main)
- DURUM.md icindeki cop satirlar (Write-Output active_line) temizlendi
- Python sanal ortami (venv) kuruldu: .venv (Python 3.11.9), pip guncellendi (26.2.1)
- .venv .gitignore sayesinde git'e gitmiyor (dogrulandi)

## SIRADAKI ADIM (buradan basla!)
1. [TAMAM] GitHub'a baglama -> https://github.com/hcan0x/hafiza
2. [TAMAM] Python sanal ortami (venv) kuruldu -> .venv (Python 3.11.9)
3. Veri modelini tasarlamak (not nasil saklanacak? SQLite mi JSON mi?)  <-- SIRADAKI
4. Ilk calisan sey: pencere + not ekle + listele

## HATIRLATMA
- Hasan: yazilim muhendisligi ogrencisi, Python + VS Code var
- Birlikte calisma sekli: EN BASA cikar, Hasan 0'dan kendisi yazar, AI yol gosterir
- Her oturum sonunda bu dosya guncellenecek

## ORTAM BILGISI
- Desktop: C:\Users\HP\OneDrive\Desktop
- Git user: Hasan Can <hasanjohanson@gmail.com>
- Git versiyon: 2.51.1
- gh (GitHub CLI): KURULU (v2.101.0), hesap: hcan0x
- GitHub repo: https://github.com/hcan0x/hafiza
- Python: 3.11.9 (venv: .venv)
