# Riski SDK 🚀

Riski SDK adalah command-line interface (CLI) tool canggih yang dirancang untuk membantu programmer dan developer dalam dua hal utama:
1. **AI Coder Assistant**: Terhubung ke sistem AI untuk membantu memberikan solusi dari *prompt* atau pertanyaan yang Anda ajukan.
2. **Language Creator**: Membuat kerangka kerja (scaffolding/boilerplate) struktur dasar untuk membangun bahasa pemrograman Anda sendiri, lengkap dengan file `lexer`, `parser`, `interpreter`, dan `main`.

---

## 🛠️ Fitur Utama

- **`ai`** : Berkomunikasi dengan AI Coder menggunakan API canggih secara langsung dari terminal.
- **`create-lang`** : Men-generate arsitektur folder dan file secara otomatis untuk mendesain bahasa pemrograman baru (Lexer, Parser, Interpreter, Main Runtime).

---

## 📥 Instalasi

1. Clone repositori ini ke komputer lokal Anda:
   ```bash
   git clone https://github.com/USERNAME/riski-sdk.git
   cd riski-sdk
   ```

2. Berikan izin eksekusi (*execute permission*) pada file `riski_sdk.py`:
   ```bash
   chmod +x riski_sdk.py
   ```

3. (Opsional) Untuk mempermudah pemakaian, Anda bisa membuat symlink ke `/usr/local/bin` agar bisa dipanggil darimana saja dengan perintah `riski`:
   ```bash
   sudo ln -s $(pwd)/riski_sdk.py /usr/local/bin/riski
   ```

---

## 💻 Panduan Penggunaan

Jika Anda tidak melakukan langkah ke-3 (symlink) pada proses instalasi, gunakan `./riski_sdk.py` di terminal. Jika Anda sudah membuat symlink, Anda cukup mengetikkan `riski`.

### 1. Memanggil Bantuan (Help)
Melihat daftar perintah dan parameter yang tersedia:
```bash
./riski_sdk.py --help
```

### 2. Menggunakan Fitur AI Assistant
Tanya AI untuk membuatkan kode, script, atau menjawab pertanyaan teknis Anda.

**Sintaks:**
```bash
./riski_sdk.py ai "<prompt_anda>"
```

**Contoh:**
```bash
./riski_sdk.py ai "buat landing page portfolio modern"
```

**Kustomisasi Session ID:**
Jika Anda ingin mempertahankan sesi obrolan (session), tambahkan flag `--session`:
```bash
./riski_sdk.py ai "bantu perbaiki error di file ini" --session="SesiSaya123"
```

### 3. Membuat Bahasa Pemrograman Baru
Ingin membuat bahasa pemrograman seperti Nusantara, Python, atau Ruby? Tool ini akan membuatkan kerangkanya seketika.

**Sintaks:**
```bash
./riski_sdk.py create-lang <nama_bahasa>
```

**Contoh:**
```bash
./riski_sdk.py create-lang indoscript
```

Perintah di atas akan menghasilkan sebuah folder `indoscript` yang berisi:
- `lexer.py` (Untuk Tokenisasi data)
- `parser.py` (Untuk menyusun Abstract Syntax Tree / AST)
- `interpreter.py` (Untuk mengeksekusi logika AST)
- `main.py` (Entry point, CLI dan file eksekusi bahasa)

---

## 🤝 Kontribusi
Kami sangat menyambut kontribusi dari siapa pun! Jika Anda ingin menambahkan fitur, memperbaiki bug, atau memperbarui dokumentasi, silakan buat *Pull Request*.

1. Fork repository ini
2. Buat branch fitur baru (`git checkout -b fitur-baru`)
3. Commit perubahan Anda (`git commit -m 'Menambahkan fitur keren'`)
4. Push ke branch (`git push origin fitur-baru`)
5. Buat Pull Request

## 📄 Lisensi
Distributed under the MIT License. See `LICENSE` for more information.
