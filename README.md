# Capstone Project: Deteksi SMS Penipuan
Proyek ini adalah aplikasi web untuk mendeteksi SMS penipuan menggunakan teknik machine learning. Aplikasi ini dibangun dengan menggunakan Streamlit dan dapat diakses di link ini.

**Anggota Tim 19**

1. Aditya Priadi Pradana
2. Marchel Ferry Timoteus S
3. Riski Nur Rohman
4. Linda Septiana
5. Monixca Fernandes Awangga Tirta

# Daftar Isi
- Deskripsi
- Fitur
- Instalasi
- Penggunaan
- Struktur Proyek
- Kontribusi

# Deskripsi
Aplikasi ini dirancang untuk membantu pengguna mendeteksi SMS penipuan dengan cepat dan mudah. Dengan memasukkan teks SMS, aplikasi akan memberikan prediksi apakah SMS tersebut merupakan penipuan atau tidak berdasarkan model machine learning yang telah dilatih.

# Fitur
Deteksi SMS penipuan secara real-time.
Antarmuka pengguna yang sederhana dan intuitif.
Dibangun dengan framework Streamlit untuk kemudahan penggunaan dan pengembangan.

# Instalasi
Untuk menjalankan proyek ini secara lokal, ikuti langkah-langkah berikut:

1. Clone repositori ini:
git clone https://github.com/username/capstone-project-deteksi-sms-penipuan.git

2. Masuk ke direktori proyek:
cd capstone-project

3. Buat dan aktifkan virtual environment (opsional tapi disarankan):
python -m venv env
source env/bin/activate  # Untuk Windows, gunakan `env\Scripts\activate`

4. Instal dependensi:
pip install -r requirements.txt

5. Jalankan aplikasi:
streamlit run stream_nlp.py (untuk yang ada tampilan login)
streamlit run stream-nlp.py (bisa langsung diakses)

6. Login
username : "appradana", "mfsamosir", "rnrohman", "lsana", "mfatirta"

password : abc123

# Penggunaan
1. Buka aplikasi di browser Anda melalui link yang disediakan setelah menjalankan Streamlit.
2. Masukkan teks SMS yang ingin Anda periksa.
3. Klik tombol "Deteksi" untuk mendapatkan hasil prediksi.
   
# Struktur Proyek
..\capstone-project

    README.md                        # Dokumentasi project
    clean_data.csv                   # Cleaned-Dataset
    dataset_sms_spam_v1.csv          # Raw dataset
    feature_tf-idf.sav               # 
    key_norm.csv                     # Kata kunci utk kata singkatan
    model_fraud.sav                  # Model deteksi penipuan yang sudah dilatih
    new_selected_feature_tf-idf.sav  # pre-defined vocabulary 
    nlp.ipynb                        # File jupyter notebook model machine learning
    requirements.txt                 # Daftar dependensi python
    stream_nlp.py                    # File utama Streamlit
    generate_keys.py                 # Generate hashed key program
    hashed_pw.pkl                    # Hashed password user authentification

# Kontribusi
Kami sangat menghargai kontribusi dari komunitas. Jika Anda ingin berkontribusi, silakan fork repositori ini, buat branch baru, dan ajukan pull request. Langkah-langkah kontribusi:
1. Fork repositori ini.
2. Buat branch baru (git checkout -b fitur-baru).
3. Lakukan perubahan dan commit (git commit -am 'Menambahkan fitur baru').
4. Push ke branch (git push origin fitur-baru).
5. Buat pull request baru.
