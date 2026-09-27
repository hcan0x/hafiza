Write-Output "##active_line2##"
# PROJE DURUMU (Kaldigimiz yer)
Write-Output "##active_line3##"
Write-Output "##active_line4##"
> Her oturum sonunda bu dosyayi guncelle.
Write-Output "##active_line5##"
> YENI OTURUMDA AI'ya: "Desktop'taki hafiza projesinin DURUM.md dosyasini oku" de.
Write-Output "##active_line6##"
> Kaldigimiz yerden devam ederiz.
Write-Output "##active_line7##"
Write-Output "##active_line8##"
===============================================================
Write-Output "##active_line9##"
## PROJE: Hafiza - Kisisel hayat arsivi (AI destekli)
Write-Output "##active_line10##"
===============================================================
Write-Output "##active_line11##"
Write-Output "##active_line12##"
## FIKIR (neden yapiyoruz?)
Write-Output "##active_line13##"
Iki proje fikri konusuldu:
Write-Output "##active_line14##"
  1) "Ters Sosyal Medya" -> SADECE kendi hayatini arsivle, baskalarini degil.
Write-Output "##active_line15##"
     "3 ay once ne dusunuyordum?" diye sorunca cevap veren kisisel hafiza.
Write-Output "##active_line16##"
  2) Abonelik/bosa harcama dedektifi (yedek fikir)
Write-Output "##active_line17##"
SECILEN: 1 numarali fikir -> "Hafiza" projesi
Write-Output "##active_line18##"
Write-Output "##active_line19##"
Neden tutar:
Write-Output "##active_line20##"
- Herkes gecmisini unutur
Write-Output "##active_line21##"
- AI cagi bunu bedava mumkun kildi
Write-Output "##active_line22##"
- Gizlilik: veri SENIN bilgisayarinda kalir (buyuk rakipler yapamaz)
Write-Output "##active_line23##"
- Hasan'in Jarvis projesindeki altyapi (ses, AI, pencere) tekrar kullanilabilir
Write-Output "##active_line24##"
Write-Output "##active_line25##"
## MALIYET / OLCEK (konusuldu)
Write-Output "##active_line26##"
- 0-100 kullanici      : 0 TL (hepsi free tier)
Write-Output "##active_line27##"
- 100-5.000 kullanici  : ~1000 TL/ay max (sadece AI asilirsa)
Write-Output "##active_line28##"
- 5.000-50.000         : ~8000 TL/ay (burada gelir de baslar)
Write-Output "##active_line29##"
- 50.000+              : ~86000 TL/ay (ama kar var)
Write-Output "##active_line30##"
SONUC: Baslangic bedava, tek gercek yatirim ZAMAN.
Write-Output "##active_line31##"
Write-Output "##active_line32##"
## YOL HARITASI
Write-Output "##active_line33##"
- [ ] Faz 1: Iskelet (kaydet + listele + ara)
Write-Output "##active_line34##"
- [ ] Faz 2: AI beyin (Groq ile dogal dil sorgu) - Groq anahtari zaten var
Write-Output "##active_line35##"
- [ ] Faz 3: Otomatik yakalama (tarayici eklenti / ekran)
Write-Output "##active_line36##"
- [ ] Faz 4: Yayin (web: Supabase + Vercel, buyume)
Write-Output "##active_line37##"
Write-Output "##active_line38##"
## MIMARI KARARI
Write-Output "##active_line39##"
- Python ile basla (Hasan Python + VS Code biliyor)
Write-Output "##active_line40##"
- Ama kodu "backend mantigi" ile yaz -> sonra web'e kolay tasinsin
Write-Output "##active_line41##"
- A, B, C hepsi hedef: once masaustu calissin, sonra web
Write-Output "##active_line42##"
Write-Output "##active_line43##"
## BUGUN (Oturum 1) YAPILANLAR
Write-Output "##active_line44##"
- Proje klasoru olusturuldu: C:\Users\HP\OneDrive\Desktop\hafiza
Write-Output "##active_line45##"
- Git baslatildi (main dali)
Write-Output "##active_line46##"
- 3 dosya eklendi: README.md, .gitignore, DURUM.md
Write-Output "##active_line47##"
- ILK COMMIT atildi: b66684e
Write-Output "##active_line48##"
- "Kaldigimiz yeri hatirlama" sistemi kuruldu (DURUM.md + Git)
Write-Output "##active_line49##"
Write-Output "##active_line50##"
## SIRADAKI ADIM (Yarin buradan basla!)
Write-Output "##active_line51##"
1. GitHub'a baglama (henuz YAPILMADI):
Write-Output "##active_line52##"
   - Secenek A: "winget install GitHub.cli" -> "gh auth login" -> "gh repo create hafiza --public --source=. --push"
Write-Output "##active_line53##"
   - Secenek B: GitHub'da elle repo ac, link ver, "git remote add origin <link>" + "git push -u origin main"
Write-Output "##active_line54##"
2. Python sanal ortami (venv) kurmak
Write-Output "##active_line55##"
3. Veri modelini tasarlamak (not nasil saklanacak? SQLite mi JSON mi?)
Write-Output "##active_line56##"
4. Ilk calisan sey: pencere + not ekle + listele
Write-Output "##active_line57##"
Write-Output "##active_line58##"
## HATIRLATMA
Write-Output "##active_line59##"
- Hasan: yazilim muhendisligi ogrencisi, Python + VS Code var
Write-Output "##active_line60##"
- Birlikte calisma sekli: EN BASA cikar, Hasan 0'dan kendisi yazar, AI yol gosterir
Write-Output "##active_line61##"
- Her oturum sonunda bu dosya guncellenecek
Write-Output "##active_line62##"
Write-Output "##active_line63##"
## ORTAM BILGISI
Write-Output "##active_line64##"
- Desktop: C:\Users\HP\OneDrive\Desktop
Write-Output "##active_line65##"
- Git user: Hasan Can <hasanjohanson@gmail.com>
Write-Output "##active_line66##"
- Git versiyon: 2.51.1
Write-Output "##active_line67##"
- gh (GitHub CLI): KURULU DEGIL
Write-Output "##active_line68##"
