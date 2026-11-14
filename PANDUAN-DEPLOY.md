# Panduan Deploy — Astronaut Jobs Landing Page

Situs ini statis: cukup `index.html` (gambar latar sudah tertanam di dalamnya). Tidak perlu Node, build, atau database.

## 1. GitHub Pages

1. Pastikan file sudah ada di branch `main` repo GitHub.
2. Buka repo → **Settings** → **Pages**.
3. **Source**: *Deploy from a branch* → Branch `main` → Folder `/ (root)` → **Save**.
4. Tunggu 1–2 menit. Situs tayang di `https://<username>.github.io/<nama-repo>/`.

Setiap `git push` ke `main` otomatis memperbarui situs.

## 2. Hostinger (hPanel)

### Cara A — File Manager (paling cepat)
1. Login hPanel → **Websites** → pilih domain → **File Manager**.
2. Masuk ke folder `public_html/`. Hapus `default.php` bawaan jika ada.
3. Klik **Upload** → pilih `astronaut-jobs-hostinger.zip`.
4. Klik kanan file zip → **Extract** ke `public_html/`. Hasilnya harus:
   ```
   public_html/index.html
   public_html/assets/og-image.jpg
   public_html/.htaccess
   ```
5. Hapus file zip, lalu buka domain kamu di browser.

### Cara B — FTP (FileZilla)
1. hPanel → **Files** → **FTP Accounts** → catat host, username, password (port 21).
2. Hubungkan lewat FileZilla, buka `public_html/`.
3. Seret `index.html`, folder `assets/`, dan `.htaccess` ke `public_html/`.

### Cara C — Deploy dari GitHub (otomatis)
1. hPanel → **Advanced** → **GIT**.
2. Masukkan URL repo `https://github.com/<username>/astronaut-jobs-landing`, branch `main`, direktori kosong (= `public_html`).
3. Klik **Create**, lalu **Deploy**. Untuk update berikutnya, klik **Auto Deploy** dan tempelkan webhook-nya ke GitHub (Settings → Webhooks).

### Setelah tayang
- Aktifkan SSL gratis: hPanel → **Security** → **SSL** → Install, lalu nyalakan **Force HTTPS**.
- Jika tampilan lama masih muncul, kosongkan cache: hPanel → **Website** → **Cache Manager** → Purge.
