# TUGAS 2

**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**

Implementasi proyek dimulai dengan membuat kerangka proyek Django menggunakan django-admin startproject kosinduy_YNWA dan aplikasi main dengan python manage.py startapp main. Setelah itu, saya melakukan beberapa konfigurasi: di kosinduy_YNWA/settings.py, saya mendaftarkan aplikasi baru dengan menambahkan 'main' ke dalam list INSTALLED_APPS. Selanjutnya, pada file kosinduy_YNWA/urls.py, saya mengimpor include dan menambahkan path('', include('main.urls')) untuk melakukan routing ke aplikasi main. Di dalam aplikasi main, saya membuat file urls.py baru dan mendefinisikan path('', show_main, name='show_main') untuk memetakan URL root ke view yang sesuai. Pada main/models.py, saya membuat class Product(models.Model) dan mendefinisikan semua atribut, yaitu: name dengan tipe CharField, price dengan tipe IntegerField, description dengan tipe TextField, thumbnail dengan tipe URLField, category dengan tipe CharField, is_featured dengan tipe BooleanField, dan stock dengan tipe PositiveIntegerField. Kemudian, di main/views.py, saya membuat fungsi show_main yang mengimpor model Product, mengambil semua datanya melalui Product.objects.all(), dan mengirimkannya dalam sebuah context ke template. Saya juga membuat direktori main/templates/ dan file main.html di dalamnya, yang saya isi dengan kode HTML dan sintaks Django untuk menampilkan data produk secara dinamis. Terakhir, untuk persiapan deployment, saya membuat file requirements.txt, mengkonfigurasi .env.prod dengan kredensial PWS, dan menyesuaikan settings.py untuk ALLOWED_HOSTS serta database produksi yang digunakan.

**Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.**

Alur request-response di aplikasi saya adalah sebagai berikut:

1. Client (Browser) mengirim request ke URL.
2. kosinduy_YNWA/urls.py menerima request dan meneruskannya ke main/urls.py.
3. main/urls.py mencocokkan URL dengan pola yang ada dan memanggil fungsi show_main di views.py.
4. views.py (fungsi show_main) berinteraksi dengan models.py untuk mengambil data semua produk dari database (Product.objects.all()).
5. views.pykemudian mengirimkan data tersebut ke main.html.
6. Template main.html me-render data menjadi halaman HTML yang utuh.
7. Halaman HTML tersebut dikirim kembali sebagai response ke Client.

```mermaid
sequenceDiagram
    participant Client as Browser
    participant ProjectUrls as kosinduy_YNWA/urls.py
    participant AppUrls as main/urls.py
    participant Views as main/views.py
    participant Models as main/models.py
    participant Template as main.html

    Client->>+ProjectUrls: HTTP Request (misal: GET /)
    ProjectUrls->>+AppUrls: Meneruskan request via include()
    AppUrls->>+Views: Mencocokkan path dan memanggil view 'show_main'
    Views->>+Models: Mengambil data produk (Product.objects.all())
    Models-->>-Views: Mengembalikan data produk (QuerySet)
    Views->>+Template: Mem-passing data ke template via render()
    Template-->>-Views: Menghasilkan halaman HTML
    Views-->>-Client: HTTP Response (Halaman HTML)
```

Kaitannya adalah urls.py bertindak sebagai pemetaan URL yang mengarahkan request ke views.py. Kemudian, views.py berfungsi sebagai otak yang memproses logika, berinteraksi dengan models.py untuk mengelola data, dan memilih html template yang sesuai untuk ditampilkan. Terakhir, berkas .html adalah lapisan presentasi yang menerima data dari view dan menampilkannya kepada pengguna.

**Jelaskan peran settings.py dalam proyek Django!**

'settings.py' adalah file konfigurasi utama proyek Django. Perannya adalah sebagai pusat kendali di mana saya mengatur dan mengkonfigurasi semua hal penting, seperti mendaftarkan aplikasi di 'INSTALLED_APPS', mengkonfigurasi koneksi database di 'DATABASES', menyimpan 'SECRET_KEY' untuk keamanan, mengatur mode 'DEBUG', dan mendaftarkan 'ALLOWED_HOST' yang diizinkan mengakses aplikasi.

**Bagaimana cara kerja migrasi database di Django?**

Migrasi database di Django bekerja dalam dua langkah. Pertama, 'python manage.py makemigrations' akan menyimpan perubahan pada models.py dan membuat file rencana migrasi di directory migrations (0001_initial.py etc). File ini berisi instruksi tentang perubahan yang akan dilakukan pada database. Kedua, 'python manage.py migrate' akan mengeksekusi rencana tersebut dan menerapkan perubahan pada struktur database yang sebenarnya. Proses ini memastikan perubahan database dilakukan secara aman dan terkontrol dengan pertama menyimpan blueprint kemudian baru menerapkannya.

**Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?**

Menurut saya, Django adalah pilihan yang sangat tepat untuk memulai belajar pengembangan perangkat lunak/web.
Django adalah framework yang sangat lengkap. Terdapat banyak fitur penting yang sudah tersedia langsung untuk digunakan sehingga tidak perlu repot mencari dan memasang fitur tambahan tambahan. Contohnya adalah panel admin bawaan Django yang bisa dibuat otomatis untuk mengelola data dan sistem untuk berinteraksi dengan database menggunakan Python (ORM) yang lebih intuitif dari menulis SQL. Ini membuat pemula bisa fokus memahami alur kerja pengembangan web, tidak terjebak di aspek teknis pemasangan komponen.
Selain itu, Django menggunakan bahasa Python yang dikenal sebagai bahasa yang mudah dipelajari karena sintaksnya yang sederhana dan mudah dibaca. Terutama di Fasilkom UI, Python merupakan bahasa pemrograman pertama yang diajarkan sehingga rata-rata mahasiswa paling mahir menggunakan python dibanding bahasa pemrograman lain. Dengan itu, keterampilan pemrograman rata-rata mahasiswa Fasilkom UI sudah cukup untuk membangun aplikasi web menggunakan Python (Django). Jadi, proses belajar tidak terlalu berat karena tidak perlu mempelajari bahasa dan framework baru di saat yang bersamaan.

**Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?**

Saya ingin mengucapkan terima kasih kak sudah membantu selama tutorial, walaupun terkadang pertanyaannya agak konyol 😅. Penjelasannya kakak-kakak asdos sangat jelas dan mudah diikuti. Untuk kedepannya, mungkin penjelasan lebih dalam mengenai cara kerja program/apa yang dilakukan kode yang baru kita tulis bisa diberi penjelasan karena setelah kelas saya banyak mencari tahu sendiri. Selain itu, best practice dalam penulisan kode Django juga boleh diberikan ke kita. Terima Kasih Kak!

# TUGAS 3

**Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?**

Data delivery diperlukan agar data yang tersimpan di server dapat dikirim dan diakses oleh client (seperti aplikasi web atau mobile) secara efisien. Dengan adanya data delivery, client bisa mendapatkan data terbaru dari server, menampilkan informasi yang relevan kepada pengguna, dan melakukan sinkronisasi data antar perangkat. Tanpa mekanisme data delivery, aplikasi hanya akan bersifat statis dan tidak bisa menampilkan data dinamis atau melakukan interaksi dua arah antara client dan server.

**Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?**

Menurut saya, JSON lebih baik untuk kebanyakan aplikasi modern karena formatnya lebih sederhana, mudah dibaca manusia, dan langsung bisa diproses oleh JavaScript di browser tanpa parsing tambahan. JSON juga menghasilkan data yang lebih ringkas sehingga lebih hemat bandwidth. Sementara itu, XML memang lebih fleksibel dan bisa digunakan untuk validasi data yang kompleks, tetapi sintaksnya lebih rumit dan ukuran file biasanya lebih besar. Karena alasan kemudahan penggunaan dan efisiensi, JSON menjadi standar utama untuk pertukaran data di web saat ini.

**Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?**

Method is_valid() pada form Django digunakan untuk melakukan validasi otomatis terhadap data yang diinputkan user, sesuai dengan aturan yang sudah didefinisikan di form atau model. Jika data yang dikirim user tidak sesuai (misal: format email salah, field wajib kosong, dsb), maka form akan dianggap tidak valid dan error bisa ditampilkan ke user. Dengan is_valid(), kita memastikan hanya data yang benar dan aman yang akan diproses atau disimpan ke database.

**Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?**

csrf_token dibutuhkan untuk melindungi aplikasi dari serangan Cross-Site Request Forgery (CSRF), yaitu serangan di mana penyerang mencoba memanfaatkan sesi login user untuk mengirimkan permintaan palsu ke server tanpa sepengetahuan user. Jika kita tidak menambahkan csrf_token pada form, penyerang bisa membuat user yang sedang login tanpa sadar melakukan aksi berbahaya seperti mengubah data, menghapus akun, atau transaksi ilegal hanya dengan mengunjungi website lain. Dengan adanya csrf_token, server bisa memastikan setiap permintaan POST benar-benar berasal dari form yang sah di aplikasi kita, sehingga serangan CSRF bisa dicegah.

**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**

Saya mulai dengan menambahkan empat fungsi baru di views.py, yaitu fungsi untuk menampilkan data produk dalam format XML, JSON, XML by ID, dan JSON by ID. Masing-masing fungsi ini menggunakan modul serializers dari Django untuk mengubah queryset produk menjadi format XML atau JSON, lalu mengembalikannya sebagai response. Untuk fungsi by ID, saya menggunakan filter berdasarkan primary key agar hanya data produk tertentu yang diambil. Selain itu, saya juga menambahkan fungsi add_product untuk menangani form penambahan produk baru ke database, serta fungsi show_product untuk menampilkan detail dari setiap produk berdasarkan ID-nya. Setelah itu, saya membuat file forms.py dan mendefinisikan sebuah class form berbasis ModelForm untuk model Product. Dengan form ini, saya bisa membuat halaman tambah produk yang otomatis sudah ada validasi dan field-nya sesuai dengan model.

Saya kemudian membuat template dasar base.html yang berisi struktur HTML utama (seperti tag <html>, <head>, dan <body>) serta block konten yang bisa di-extend oleh template lain. Supaya Django bisa menemukan template ini, saya menambahkan konfigurasi direktori template di settings.py dengan menambahkan path ke folder templates pada bagian DIRS di variabel TEMPLATES. Selanjutnya, saya menambahkan dua file template baru, yaitu create_product.html untuk halaman form tambah produk dan product_detail.html untuk menampilkan detail produk. Pada create_product.html, saya menggunakan {% extends 'base.html' %} dan menampilkan form yang sudah dibuat di forms.py. Pada product_detail.html, saya juga extend dari base.html dan menampilkan detail lengkap dari produk yang dipilih. Selain itu, saya juga mengedit template main.html agar menampilkan tombol "Add Product" yang mengarah ke halaman tambah produk, serta menambahkan tombol "More Detail" pada setiap div produk yang akan mengarahkan ke halaman detail produk tersebut.

Terakhir, saya menambahkan routing baru di urls.py untuk menghubungkan setiap fungsi view yang sudah dibuat tadi dengan URL yang sesuai. Saya menambahkan path untuk halaman utama, tambah produk, detail produk, serta empat path tambahan untuk akses data produk dalam format XML, JSON, XML by ID, dan JSON by ID.

**Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?**

Menurut saya tidak ada feedback lebih lanjut dari tutorial 1. Saya sangat merasa terbantu ketika bertanya dan tutorial yang ada juga sudah sangat jelas dan informatif. Mungkin saya bisa sebutkan terkait demo tugas yang awalnya saya kira akan sangat tegang karena pemahaman saya yang mungkin masih terbatas, tetapi ternyata saya lumayan paham dan kak Isa baik juga 😁.

** Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman**

![alt text](image.png)
![alt text](image-1.png)
![alt text](image-2.png)
![alt text](image-3.png)

# TUGAS 4

**Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.**

Django AuthenticationForm adalah form bawaan yang disediakan oleh Django untuk menangani proses login user. Form ini sudah otomatis menyediakan field username dan password, serta melakukan validasi kredensial terhadap database user yang ada di aplikasi. Dengan AuthenticationForm, developer tidak perlu membuat form login dari awal karena semua proses validasi, pengecekan user aktif, dan keamanan seperti hashing password sudah di-handle oleh Django.

Kelebihan utama dari AuthenticationForm adalah kemudahan integrasi dengan sistem autentikasi Django sehingga proses login bisa dilakukan dengan sedikit kode dan sudah aman dari berbagai serangan umum seperti brute force. Namun, kekurangannya adalah form ini hanya cocok untuk autentikasi standar dan kurang fleksibel jika ingin menambahkan fitur login yang lebih kompleks seperti OTP, social login, atau custom error message. Selain itu, tampilan dan pesan error default kadang perlu diubah agar lebih sesuai dengan kebutuhan aplikasi.

**Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?**

Perbedaan antara autentikasi dan otorisasi adalah tujuan dan prosesnya. Autentikasi adalah proses untuk memastikan identitas user dengan memverifikasi apakah user benar-benar yang dia klaim. Sementara itu, otorisasi adalah proses untuk menentukan hak akses user, yaitu apakah user yang sudah terautentikasi boleh melakukan aksi tertentu di aplikasi.

Pada Django, autentikasi diimplementasikan melalui User model bawaan, AuthenticationForm, dan session framework yang menyimpan status login user. Django juga menyediakan decorator seperti @login_required untuk membatasi akses hanya kepada user yang sudah login. Untuk otorisasi, Django memiliki sistem permission yang bisa diatur per model (add, change, delete, view), group untuk mengelompokkan user dengan hak akses tertentu, serta method seperti user.has_perm() dan decorator @permission_required untuk mengecek dan membatasi akses berdasarkan hak user. Dengan kombinasi autentikasi dan otorisasi ini, Django memastikan hanya user yang berhak yang bisa mengakses dan melakukan aksi tertentu di aplikasi.

**Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?**

Dalam konteks menyimpan state di aplikasi web, session dan cookies memiliki kelebihan dan kekurangan masing-masing. Session menyimpan data di server sehingga lebih aman dari manipulasi user dan cocok untuk data yang sifatnya sensitif atau kompleks. Namun, session membutuhkan storage di server dan bisa menjadi masalah jika aplikasi harus di-scale ke banyak server, karena session biasanya tersimpan di satu tempat. Selain itu, session bisa hilang jika server restart kecuali menggunakan persistent storage. Di sisi lain, cookies menyimpan data di browser user sehingga tidak membebani server dan cocok untuk data sederhana yang tidak sensitif. Cookies bisa bertahan lama di browser user, tetapi ukurannya terbatas dan mudah diubah atau dihapus oleh user. Selain itu, cookies dikirim di setiap request sehingga bisa mempengaruhi bandwidth dan tidak cocok untuk data yang sifatnya rahasia.

**Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?**

Penggunaan cookies dalam pengembangan web tidak sepenuhnya aman. Ada beberapa risiko yang harus diwaspadai, seperti session hijacking, XSS, CSRF, dan pencurian data jika tidak menggunakan HTTPS. Django menangani risiko-risiko ini dengan beberapa mekanisme keamanan seperti cryptographic signing pada session cookie menggunakan SECRET_KEY, pengaktifan HttpOnly dan Secure flag untuk session cookie agar tidak bisa diakses oleh JavaScript dan hanya dikirim lewat HTTPS, serta proteksi CSRF otomatis lewat middleware dan token. Django juga mendukung pengaturan SameSite attribute untuk mencegah serangan CSRF dan memungkinkan developer mengatur SESSION_COOKIE_SECURE, SESSION_COOKIE_HTTPONLY, dan CSRF_COOKIE_SECURE di settings.py untuk keamanan maksimal. Dengan pengaturan yang tepat, risiko penggunaan cookies bisa diminimalisir, tetapi developer tetap harus waspada dan mengaktifkan fitur keamanan tambahan terutama di production environment.

**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**

Saya mulai dengan menambahkan fitur autentikasi di aplikasi, yaitu register, login, dan logout menggunakan form bawaan Django. Dengan fitur ini, user bisa membuat akun baru, login, dan keluar dari aplikasi dengan mekanisme yang sudah aman dan terintegrasi dengan session Django. Setelah user berhasil login, saya menyimpan waktu terakhir login ke dalam cookie last_login, lalu menampilkannya di halaman utama agar user bisa tahu kapan terakhir kali mereka login. Cookie ini juga saya hapus saat user melakukan logout agar data yang ditampilkan tetap akurat.

Akses ke halaman utama dan detail produk saya batasi hanya untuk user yang sudah login dengan menambahkan decorator @login_required di beberapa fungsi views. Di halaman utama, saya juga menambahkan filter agar user bisa memilih untuk melihat semua produk atau hanya produk yang mereka buat sendiri. Filter ini diambil dari query parameter di URL yang dikirim ke template.

Di bagian model, setiap produk saya hubungkan ke user pembuatnya dengan ForeignKey ke model User. Dengan cara ini, setiap produk yang ditambahkan akan tercatat siapa pembuatnya, dan fitur filter "My Products" bisa berjalan dengan baik. Setelah mengubah model, saya jalankan migrasi database agar struktur data sesuai kebtuhan.

# TUGAS 5

**Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!**

Prioritas CSS ditentukan oleh specificity. Urutan dari yang tertinggi hingga terendah adalah: deklarasi dengan `!important`, gaya inline pada elemen (`style="…"`), selector berbasis ID (`#id`), selector berbasis class/attribute/pseudo-class (`.class`, `[type=…]`, `:hover`), lalu selector tag/pseudo-element (`div`, `p`, `::before`). Apabila nilai specificity sama, aturan yang muncul paling akhir pada berkas CSS yang dipakai. Perlu diperhatikan bahwa pewarisan (inheritance) hanya berlaku untuk properti tertentu dan tidak mengalahkan aturan yang lebih spesifik; penggunaan `!important` sebaiknya dibatasi karena menyulitkan pemeliharaan kode.

**Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!**

Responsive design memastikan antarmuka dan konten dapat beradaptasi dengan beragam ukuran layar dan kepadatan piksel, sehingga keterbacaan, navigasi, dan aksesibilitas tetap terjaga pada ponsel, tablet, hingga desktop. Penerapan ini juga berdampak pada performa bisnis dan teknis: pengalaman pengguna lebih baik, tingkat pentalan berkurang, serta mendapat penilaian positif pada mesin pencari yang memprioritaskan situs ramah perangkat bergerak.

Aplikasi yang telah menerapkan responsive design ditandai oleh tata letak yang berubah secara proporsional, tipografi yang menyesuaikan, serta komponen yang tetap mudah diinteraksi pada layar kecil. Sebaliknya, aplikasi yang belum responsif biasanya memaksa pengguna melakukan zoom dan scroll horizontal karena layout tetap (fixed) dan tidak memanfaatkan media query, unit fluida, atau sistem layout modern.

**Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!**

Margin adalah ruang di luar kotak elemen yang berfungsi memisahkan elemen dari elemen lainnya. Border adalah garis pembatas yang mengelilingi elemen di antara margin dan padding. Padding adalah ruang di dalam elemen, yaitu jarak antara konten dan border. Dalam box model urutannya dari luar ke dalam adalah: margin -> border -> padding -> konten. Implementasi dilakukan melalui properti CSS terkait, misalnya `margin`, `border` (dengan ketebalan, gaya, dan warna), serta `padding`. Seluruh properti tersebut mendukung penulisan ringkas (shorthand) maupun per sisi, sehingga jarak dan batas dapat diatur sesuai kebutuhan tata letak.

**Jelaskan konsep flex box dan grid layout beserta kegunaannya!**

Flexbox adalah model tata letak satu dimensi yang mengatur distribusi ruang dan perataan item pada satu sumbu (baris atau kolom). Flexbox efektif untuk menyusun komponen seperti navbar, toolbar, dan deretan kartu karena menyediakan kontrol perataan (alignment) dan distribusi (justification) yang fleksibel.

Grid adalah model tata letak dua dimensi yang memungkinkan pengaturan baris dan kolom secara bersamaan. Grid lebih sesuai untuk menyusun kerangka halaman, galeri, atau dashboard dengan pola yang kompleks. Dalam praktiknya, grid dapat digunakan untuk struktur utama halaman, sedangkan flexbox dimanfaatkan di dalam masing‑masing area grid untuk merapikan isi komponen. Pendekatan ini menghasilkan tata letak yang bersih, konsisten, dan responsif.

**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!**

Saya mulai dengan mengimplementasikan fitur edit dan delete product di aplikasi. Pertama, saya membuat fungsi edit_product di views.py yang menerima parameter id untuk mencari product berdasarkan primary key. Fungsi ini menggunakan ProductForm dengan parameter instance=product sehingga data product yang ada bisa diedit lewat form. Setelah form valid dan disubmit, perubahan langsung tersimpan ke database, lalu diarahkan kembali ke halaman utama. Selanjutnya, saya membuat template edit_product.html untuk menampilkan form edit.

Untuk fitur delete, saya menambahkan fungsi delete_product di views.py yang mengambil product berdasarkan id lalu menghapusnya dengan method .delete(). Setelah itu, user diarahkan kembali ke halaman utama. Kedua fungsi ini saya tambahkan ke urls.py agar bisa diakses, misalnya /product/<uuid:id>/edit dan /product/<uuid:id>/delete. Di template daftar product, saya menambahkan tombol Edit dan Delete pada setiap card product yang hanya muncul jika user adalah pemilik produk tersebut.

Setelah fitur edit dan delete berjalan, saya melanjutkan ke kustomisasi desain template dengan Tailwind CSS. Pertama, saya menyambungkan aplikasi Django dengan Tailwind menggunakan script CDN di base.html. Saya menambahkan meta viewport agar tampilan lebih responsif di mobile.

Kemudian, saya melakukan styling. Pada halaman login dan register saya buat lebih menarik dengan menambahkan form yang terpusat di tengah layar, menggunakan card dengan shadow, border rounded, serta warna tombol yang konsisten dengan tema aplikasi. Halaman tambah product dan edit product saya kustomisasi agar form tampil rapi dengan padding, margin, dan tombol submit berwarna hijau menggunakan utility classes dari Tailwind. Halaman detail product saya tambahkan styling pada judul, deskripsi, dan gambar product agar lebih rapi dan mudah dibaca. Untuk halaman daftar product, saya membuat layout responsive menggunakan grid Tailwind. Jika belum ada product, halaman menampilkan gambar ilustrasi kosong dan teks "Belum ada product yang terdaftar". Jika ada product, setiap product ditampilkan dalam bentuk card yang berisi gambar thumbnail, nama produk, harga, deskripsi singkat, serta tombol Edit dan Delete. Card ini saya lengkapi dengan hover effect dan shadow agar lebih interaktif.

Terakhir, saya menambahkan navigation bar (navbar) di file navbar.html lalu menyertakannya di template utama menggunakan {% include 'navbar.html' %}. Navbar berisi link menuju halaman utama, tambah product, login/register atau logout sesuai status autentikasi user. Dengan bantuan Tailwind, navbar ini bersifat responsive: pada layar desktop, menu tampil horizontal, sedangkan pada layar mobile menu berubah menjadi stacked agar tetap mudah digunakan.
