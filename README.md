# Astronaut Jobs — Landing Page & Aplikasi

Situs statis (HTML + CSS + JS murni, tanpa build step) untuk Astronaut Jobs:
platform pencari kerja all-in-one — 30+ platform, Fit Check 0–100, CV Studio, dan pelacakan lamaran.

Satu file berisi dua bagian:

- **Landing page** — layar pertama mengikuti desain poster (astronaut, planet bercincin, kota kubah)
  dengan panel kaca: Lowongan Populer, statistik, Fitur Unggulan, dan ajakan bergabung.
  Di bawahnya: pencarian di 30 platform, cara kerja, dan FAQ.
- **Mission Control (aplikasi)** — daftar/masuk akun demo, ringkasan, jelajah platform,
  pelacakan lamaran, Fit Check, CV Studio, dan profil. Semua data tersimpan di browser (localStorage).

## Struktur

```
index.html                      halaman lengkap dalam satu file: CSS, JS, dan gambar latar sudah tertanam
assets/hero-scene.webp          sumber latar poster desktop (2560×1707)
assets/hero-scene-mobile.webp   sumber potongan latar untuk tablet & HP
assets/astronaut.webp           sumber astronaut transparan untuk tablet & HP
assets/favicon.svg              sumber ikon tab
assets/og-image.jpg             gambar pratinjau saat tautan dibagikan (opsional)
tools/embed-assets.py           menanam ulang gambar dari assets/ ke index.html
```

Karena gambar tertanam, `index.html` tetap tampil lengkap walau dibuka sendirian tanpa folder `assets/`.
Jika gambar di `assets/` diganti, jalankan:

```bash
python3 tools/embed-assets.py
```

## Menjalankan secara lokal

Buka `index.html` langsung di browser, atau jalankan server statis apa pun, misalnya:

```bash
python3 -m http.server 8080
```

lalu buka http://localhost:8080.

## Catatan

- Prototipe front-end: akun demo dan data disimpan di browser perangkat, bukan di server.
- Fit Check adalah pencocokan kata kunci lokal, bukan model AI.
- Angka statistik bertanda * dan daftar "Lowongan Populer" adalah contoh tampilan.
- Latar dibuat dari gambar mockup: teks dan panel yang menempel dihapus, lalu diperbesar 2×.

## Hosting

- **GitHub Pages**: Settings → Pages → Source: *Deploy from a branch*, branch `main`, folder `/ (root)`.
- **Hostinger**: unggah `index.html` (dan `assets/og-image.jpg` bila ingin pratinjau tautan) ke `public_html/`.
