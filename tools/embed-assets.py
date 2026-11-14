#!/usr/bin/env python3
"""Tanam gambar dari assets/ ke dalam index.html, di antara penanda ART-START dan ART-END.

Jalankan ulang setiap kali file gambar di assets/ diganti:
    python3 tools/embed-assets.py
"""
import base64, pathlib, re

root = pathlib.Path(__file__).resolve().parent.parent

def uri(name):
    return "data:image/webp;base64," + base64.b64encode((root / "assets" / name).read_bytes()).decode()

css = (
    '@media (min-width:1280px){.poster-bg{background-image:url("%s")}}\n'
    '@media (max-width:1279.98px){.scene-m{background-image:url("%s")}.scene-m .astro{background-image:url("%s")}}'
    % (uri("hero-scene.webp"), uri("hero-scene-mobile.webp"), uri("astronaut.webp"))
)
page = root / "index.html"
html = page.read_text(encoding="utf-8")
html, n = re.subn(r"/\*ART-START\*/.*?/\*ART-END\*/", lambda m: "/*ART-START*/\n" + css + "\n/*ART-END*/", html, flags=re.S)
assert n == 1, "penanda ART-START/ART-END tidak ditemukan tepat satu kali"
page.write_text(html, encoding="utf-8")
print("index.html:", round(len(html.encode()) / 1024), "KB")
