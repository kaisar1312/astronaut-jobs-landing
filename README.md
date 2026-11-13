# Astronaut Jobs — Landing Page

Landing page statis (HTML + CSS + JS murni, tanpa build step) untuk Astronaut Jobs:
platform pencari kerja all-in-one — 30+ platform, Fit Check 0–100, CV Studio, dan pelacakan lamaran.

## Struktur

```
index.html              halaman utama (semua CSS & JS sudah inline)
assets/hero-rocket.png  gambar hero roket
assets/favicon.svg      ikon tab browser
```

## Menjalankan secara lokal

Buka `index.html` langsung di browser, atau jalankan server statis apa pun, misalnya:

```bash
python3 -m http.server 8080
```

lalu buka http://localhost:8080.

## Hosting

- **GitHub Pages**: Settings → Pages → Source: *Deploy from a branch*, branch `main`, folder `/ (root)`.
- **Hostinger**: unggah `index.html` dan folder `assets/` ke `public_html/` lewat File Manager atau FTP.
