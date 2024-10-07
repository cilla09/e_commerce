[Cilla's Minimart](http://priscilla-natanael-cillasminimart.pbp.cs.ui.ac.id/)


## Tugas 2

**Checklist Step by Step**
1. Membuat projek Django

Pertama, saya membuat direktori lokal pada komputer saya. Melalui Command Prompt, saya masuk virtual environment pada direktori tersebut, dan juga membuat file berupa requirements.txt yang berisi hal-hal yang akan diinstall berikutnya. Setelah menginstall requirements, saya menjalani command untuk membuat project Django. Untuk mengecek apakah project berhasil dibuat, saya menjalani command runserver dan pergi ke localhost:8000

2. Membuat aplikasi dengan nama main pada proyek tersebut

Saya menjalani command berupa 'python manage.py startapp main' pada cmd direktori utama sehingga terbuat direktori aplikasi bernama 'main'. Kemudian, saya menambahkan aplikasi 'main' ini ke dalam list INSTALLED_APPS pada settings.py di direktori utama.

3. Melakukan routing pada proyek agar dapat menjalankan aplikasi main.

Agar dapat menjalankan aplikasi main, pertama saya membuat file urls.py yang berisi nama aplikasi 'main' dan list urlpatterns dalam direktori aplikasi. Kemudian, saya menambahkan file urls.py dari direktori aplikasi ke list urlpatterns pada file urls.py dalam direktori proyek.

4. Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib name, price, description

Pada file models.py dalam direktori aplikasi, saya membuat model bernama Product dan menambahkan atribut berupa name dengan jenis CharField, price dengan jenis IntegerField, dan description dengan jenis TextField. Atribut-atribut tambahan untuk aplikasi saya akan saya tambahkan nanti.

5. Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.

Pada file views.py dalam direktori aplikasi, saya membuat fungsi bernama 'show_main' yang akan menampilkan key dan value dalam dictionary 'context' yang berisi nama saya, kelas saya, npm saya, beserta nama produk, harga produk, dan deskripsi produk.

6. Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.

Pada file urls.py aplikasi main, saya menulis nama aplikasi yaitu 'main' lalu membuat list urlpatterns yang berisi "path('', show_main, name='show_main')" untuk routing memetakan fungsi show_main dari views.py

7. Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.

Kemudian untuk mendeploy ke PWS, pertama saya menentukan project name berupa 'cillasminimart' sehingga terbentuk URL deployment PWS. URL ini saya masukkan ke list ALLOWED_HOST dalam settings.py pada direktori proyek. Setelah membuat models, views, dan template, saya add commit dan push ke Github saya. Lalu, saya juga push ke PWS sehingga proyek saya dapat diakses melalui internet.


**Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.**
![WhatsApp Image 2024-09-11 at 08 21 35](https://github.com/user-attachments/assets/ddcb0513-e045-4c24-a4dd-3a3d29bd5a95)
Pertama, Client akan mengirim request melalui Browser/Internet yang kemudian diproses oleh urls.py, yaitu URL dari client akan dicocokan dengan URL routing untuk menentukan views.py yang sesuai. Setelah menentukan view mana yang digunakan, kode dalam views.py tersebut akan dijalankan. Jika ada data yang diperlukan maka view akan mengumpulkan data dari models.py. Setelah data berhasil terkumpul, views.py akan menyiapkan respon dari template berkas html dan dirender dengan data yang sudah diperoleh. Lalu, hasil berupa website atau respon JSON akan dikembalikan ke Browser Client.

**Jelaskan fungsi git dalam pengembangan perangkat lunak!**

Git merupakan sistem kontrol versi yang dalam pengembangan perangkat lunak berguna untuk memungkinkan tim mengembangkan proyek secara kolaboratif dan terorganisir. Beberapa fungsi utama Git, yaitu version control, kolaborasi tim, branching dan merging, reversibilitas, serta backup dan keamanan. Version control, yaitu Git mencatat setiap perubahan yang terjadi pada proyek, sehingga mudah untuk melacak apa perubahan yang sudah dilakukan, siapa yang membuat perubahan, dan kapan perubahan dilakukan. Kolaborasi tim, Git memungkinkan para pengembang dalam tim untuk mempunyai salinan lokal, sehingga mereka dapat melakukan perubahan masing-masing tanpa mengganggu satu sama lain. Perubahan-perubahan ini kemudian dapat Git gabungkan ke dalam satu repositori pusat. Branching dan merging, yaitu setiap pengembang bisa membuat branchnya sendiri untuk mengerjakan fitur baru/memperbaiki kode yang ada, lalu branch ini dapat dimerge ke cabang utama. Reversibilitas, pada Git pengembang dapat kembali ke versi sebelumnya jika terjadi kesalahan dalam pengembangan. Backup dan keamanan, yaitu Git berfungsi sebagai cloud yang menyimpan cadangan untuk proyek perangkat lunak, sehingga jika terjadi kerusakan pada komputer lokal, proyek masih aman dalam cloud Git. Semua fitur ini sangat berguna dalam pengembangan perangkat lunak, terutama jika skala proyek besar, Git mempermudah tim untuk bekerja secara kolaboratif dan minim kesalahan fatal.

**Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?**

Untuk menjadi permulaan pembelajaran pengembangan perangkat lunak, suatu framework perlu memiliki fitur fitur yang mempermudah para pemula membangun aplikasi dan memahami konsep-konsep dasar. Pertama, Django merupakan framework yang sudah mencakup banyak fitur penting, seperti autentikasi pengguna, manajemen URL, validasi form, ORM (Object-Relational Mapping), dan admin panel bawaan. Oleh karena itu, pemula tidak perlu repot membuat fitur-fitur di atas dari nol. Django juga memiliki dokumentasi yang komprehensif, mempermudah pemula untuk memahami proses kerja framework. Pola arsitektur berupa MVT (Model-View-Template) pada Django juga memudahkan para pemula mempelajari struktur aplikasi yang terorganisir karena pemisahan yang jelas antara logika bisnis (model), tampilan (template), dan logika pengontrol (view) jelas. Bahasa pemrograman yang digunakan pada Django adalah Python, bahasa yang juga terkenal beginner-friendly  karena sederhana dan mudah dipelajari. 

**Mengapa model pada Django disebut sebagai ORM?**

Model pada Django disebut sebagai ORM atau Object-Relational Mapping karena model di Django menghubungkan kode Python dengan tabel dan data dalam database relasional. Ketika membuat model di Django, pengembang hanya perlu menulis kode Python tanpa perlu menulis kueri SQL secara manual. Hal ini hasil dari ORM yang menerjemahkan objek Python menjadi kueri SQL yang sesuai. Dalam Django, setiap pengembang melakukan perubahan pada model, pengembang dapat melakukan migrasi untuk memperbarui database. Ini dapat dilakukan karena ORM di Django menghasilkan perintah migrasi yang mengubah tabel produk di database tanpa perlu pengembang menulis perintah SQL secara manual.

## Tugas 3
**Checklist Step by Step**
1. Membuat input form untuk menambahkan objek model pada app sebelumnya.

Pertama, saya membuat file baru bernama forms.py di direktori aplikasi main. Pada file tersebut, saya mengimport form berupa ModelForm dari django.forms beserta model Product dari models.py di main. Lalu, saya menambah class ProductForm berisi model yang akan digunakan (Product) dan fields dari form, yaitu name, price, description, stock, dan category.

Pada file views.py, saya menambahkan fungsi baru bernama create_product dengan parameter request. Isinya berupa pemanggilan form ProductForm, validasi input, dan menyimpan data input. Lalu, saya juga import redirect dari django.shortcuts untuk diimplementasikan sebagai berikut: setelah pengguna berhasil mengisi form, pengguna akan dikembalikan ke home. Lalu, pada fungsi show_main saya menambahkan line untuk mengambil seluruh objek Product yang tersimpan di database. Agar fungsi create_product dapat diakses, saya merouting fungsi tersebut dengan cara mengimport ke urls.py dalam direktori main. Saya juga menambahkan path ke fungsi tersebut pada list urlpatterns dalamnya.

Terakhir, saya membuat template untuk pengisian input tersebut, yaitu create_product.html. Di dalamnya berisi form method (POST), csrf_token yang digenerate secara otomatis oleh Django untuk mencegah serangan berbahaya, template variable {{ form.as_table }} untuk menampilkan fields dari forms.py sebagai table. Terakhir, ada juga tombol submit untuk mengirim request ke view create_product(request). Pada template utama main.html, saya juga menambahkan kode untuk menampilkan data yang baru diinput beserta tombol untuk add new product.

   
2. Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.

Pada views.py, saya menambah import HttpResponse dari django.http dan serializers dari django.core. Serializer akan berfungsi untuk menserialisasi parameter data hasil query menjadi XML ataupun JSON. HttpResponse adalah bentuk yang akan direturn oleh fungsi.

Untuk melihat objek yang sudah ditambahkan dalam format XML dan JSON, saya membuat fungsi baru bernama show_xml dan show_json, keduanya memiliki parameter sama yaitu request. Lalu, data pada fungsi tersebut menggunakan Product.objects.all(), yaitu semua objek Product pada database. Masing-masing fungsi akan mereturn HttpResponse berisi parameter data sudah diserialisasi menjadi XML/JSON dan parameter content_type aplikasi XML/JSON.

Untuk melihat objek yang sudah ditambahkan dalam format XML dan JSON menggunakan ID, saya membuat fungsi baru bernama show_xml_by_id dan show_json_by_id, keduanya memiliki parameter sama yaitu request. Isi dari fungsi tersebut akan sama dengan fungsi yang sebelumnya dibuat, kecuali data akan difilter hanya data sesuai ID yang digunakan.
   
3. Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.

Masing-masing views yang sudah dibuat akan diimport pada urls.py. Lalu, saya menambahkan path ke masing-masing view pada list urlpatterns dalam file yang sama.

**Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?**

Suatu platform berfungsi sebagai penghubung antara komponen-komponen yang ada di dalamnya. Data delivery diperlukan supaya data dari satu komponen/aplikasi dapat diteruskan ke komponen yang lain, sehingga suatu platform dapat bekerja dengan baik. Proses otentikasi, pengambilan data, dan penyimpanan data sangat memerlukan data delivery agar para komponen dalam platform dapat berkomunikasi secara real-time dan mendapat informasi tepat waktu.

**Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?**

Menurut saya, JSON lebih baik daripada XML karena lebih mudah digunakan. JSON atau JavaScript Object Notation memiliki struktur yang lebih sederhana dan lebih mudah dibaca oleh manusia maupun mesin. XML sendiri lebih kompleks karena menggunakan tag yang lebih verbose. Ukuran file dari JSON juga lebih kecil dari XML yang menggunakan tag penutup, berujung kepada pemrosesan dan transmisi data yang lebih cepat. JSON juga lebih mudah diparsing daripada XML. Semua sifat dari JSON ini membuatnya lebih baik daripada XML.

**Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?**

Fungsi is_valid() pada form Django berguna untuk memvalidasi input dari pengguna. Input yang dimasukkan harus memenuhi syarat, misalnya input pada IntegerField harus berupa angka, pada CharField tidak boleh melebihi length yang ditentukan, dan sebagainya. Method ini sangat dibutuhkan supaya proses jalannya web bisa lancar dan tidak terganggu oleh input pengguna yang salah. Misalnya, suatu web berisi kalkulator perkalian, jika input sudah divalidasi menjadi angka terlebih dahulu, maka web akan berjalan dengan lancar. Sementara, jika tidak divalidasi, input bisa berupa string atau char yang tidak bisa dikalikan, sehingga web bisa error.

**Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?**

Kita membutuhkan csrf_token saat membuat form di Django karena csrf_token berfungsi sebagai token untuk melindungi aplikasi dari serangan berbahaya CSRF (Cross Site Request Forgery). JIka kita tidak menambahkan csrf_token pada form Django, keamanan aplikasi menjadi rentan terhadap serangan tersebut. Esensinya, csrf_token bekerja dengan cara memastikan suatu permintaan benar-benar berasal dari halaman resmi/aplikasi itu sendiri, bukan dari sumber eksternal yang tidak sah. Apabila permintaan berasal dari sumber tidak sah, csrf_token akan menolak permintaan tersebut. Penyerang dapat memanfaatkan ketiadaan CSRF ini dengan cara membuat suatu link atau form di website lain lalu mengelabui pengguna untuk mengkliknya. Ketika pengguna sudah masuk ke aplikasi target, server target bisa mengolah permintaan tersebut seolah-olah itu adalah yang sah. Karena tidak ada csrf_token, server tidak bisa membedakan permintaan itu sah atau tidak.

**POSTMAN Screenshots**

- XML
![2024-09-18](https://github.com/user-attachments/assets/2c1c35ff-4560-44c7-ad62-6b080331bf5d)

- XML by ID
![2024-09-18 (4)](https://github.com/user-attachments/assets/f0956226-5ccb-4bbc-a86d-946b21b67e03)

- JSON
![2024-09-18 (1)](https://github.com/user-attachments/assets/30f78e87-707f-4aaf-8b68-ea40bb1047db)

- JSON by ID
![2024-09-18 (3)](https://github.com/user-attachments/assets/719e39e9-f3cf-403f-b63b-be4c079dd892)

## Tugas 4
**Checklist Step by Step**
1. Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.

Registrasi:
- Dalam views.py, saya membuat fungsi register(request).
- Dalam fungsi tersebut, saya membuat formulir registrasi dengan UserCreationForm() yang methodnya POST. Saya juga memvalidasi input pengguna menggunakan method is.valid(). Data dari pengguna disimpan dengan form.save(). Lalu, pengguna dialihkan ke halaman login dengan redirect('main:login')
- Membuat register.html sebagai template halaman registrasi
- Fungsi register pada views.py dirouting pada urls.py

Login:
- Dalam views.py, saya membuat fungsi login_user(request).
- Dalam fungsi tersebut, saya membuat formulir login dengan UserCreationForm() yang methodnya POST. Saya juga memvalidasi input pengguna menggunakan method is.valid(). Data dari pengguna akan diautentikasi dengan form.get_user() kemudian sesi disimpan dengan login(request, user). Lalu, pengguna dialihkan ke halaman utama dengan redirect('main:show_main')
- Membuat login.html sebagai template halaman login
- Fungsi login_user pada views.py dirouting pada urls.py

Logout:
- Dalam views.py, saya membuat fungsi logout_user(request). 
- Dalam fungsi tersebut, sesi pengguna dihapus dengan logout(user). Lalu, pengguna dialihkan ke halaman login dengan redirect('main:login')
- Menambahkan button untuk memanggil fungsi logout pada main.html
- Fungsi logout_user pada views.py dirouting pada urls.py
   
2. Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.

Membuat dua akun pengguna dengan mengisi halaman form registrasi (signup/) 2 kali dengan data akun yang berbeda. Lalu, untuk masing-masing akun, saya menambah 3 dummy product melalui halaman Add New Product (create-product-entry/).
   
3. Menghubungkan model Product dengan User.

Untuk menghubungkan model Product dengan User, saya menggunakan ForeignKey. Hal ini saya lakukan dengan menambahkan kode `user = models.ForeignKey(User, on_delete=models.CASCADE)` dalam class Product di models.py
   
4. Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.

Untuk menampilkan detail informasi pengguna yang sedang logged in, saya menambahkan `'name': request.user.username` ke context pada fungsi show_main di views.py. Lalu, saya masukkan `{{ name }}` di main.html untuk menampilkan username pengguna.

Untuk menerapkan cookies, saya menambahkan `response.set_cookie('last_login', str(datetime.datetime.now()))` untuk membuat cookie last login dan menambahkannya ke dalam response. Lalu, saya juga menambahkan `'last_login': request.COOKIES['last_login']` ke context pada fungsi show_main di views.py. Hal ini berfungsi untuk menambahkan informasi cookie last_login pada response yang akan ditampilkan di halaman web. Saya juga menambahkan `response.delete_cookie('last_login')` yang menghapus cookie last_login saat pengguna melakukan logout. Terakhir, agar data waktu last_login pengguna tampil di halaman utama, saya menambahkan {{ last_login }} pada main.html.

**Apa perbedaan antara HttpResponseRedirect() dan redirect()**

Walau keduanya memiliki fungsi yang sama untuk melakukan pengalihan (redirect) ke URL lain, terdapat perbedaan yang dasar di antaranya keduanya. HttpResponseRedirect membutuhkan URL sebagai parameter untuk mengarahkan pengguna, hal ini bisa dilakukan dengan membuat URL secara manual atau menggunakan method reverse(). Sementara, redirect() bisa menerima lebih banyak variasi parameter, yaitu URL, nama view, dan objek model. Sebenarnya, redirect() secara internal juga menggunakan HttpResponseRedirect(). Maka jika dibandingkan, redirect() lebih fleksibel dan mudah digunakan dibanding HttpResponseRedirect() karena kita tidak perlu diharuskan membuat URL untuk digunakan sebagai parameter.

**Jelaskan cara kerja penghubungan model Product dengan User!**

Di Django, menghubungkan model Product dengan User biasa menggunakan ForeignKey. ForeignKey dapat menunjukkan adanya hubungan antara produk dan pengguna. Beberapa kegunaan utama ForeignKey, yaitu relasi many-to-one yang memungkinkan hubungan antara satu pengguna dan banyak produk, integritas data, dan querying yang lebih mudah.

**Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.**

Autentikasi merupakan proses pengecekan identitas pengguna, apakah sudah sesuai semua kredensial dan data dirinya. Autentikasi mengatur tentang siapa pengguna itu. Otorisasi merupakan proses pengecekan setelah memastikan identitas pengguna, apa saja hak yang dimiliki pengguna tersebut. Otorisasi mengatur tentang apa yang bisa dilakukan oleh pengguna tersebut. 

Saat pengguna login, pertama kredensial yang diinput oleh pengguna akan melalui proses autentikasi untuk dicocokan dengan data user pada database. Jika ada yang cocok, maka kredensial tersebut valid dan sistem akan menandai pengguna sebagai “terautentikasi” dengan menyimpan sesi atau token yang terkait dengan pengguna. Setelah proses autentikasi selesai, baru proses otorisasi akan dijalankan untuk menentukan apa saja hak yang dimiliki pengguna dalam aplikasi terkait.

Dalam hal autentikasi, pertama Django menyimpan data pengguna seperti username, password, dan email dalam model User. Django sendiri mempunyai fungsi untuk menangani proses login, yaitu authenticate(request, username, password) untuk memverifikasi kredensial pengguna, login(request, user) untuk menyimpan sesi/token sebagai tanda pengguna “terautentikasi”, dan logout(request) untuk menghapus sesi dan penanda pengguna keluar dari sistem. Setelah pengguna mengisi formulir, formulir itu akan mengirim kredensial ke view Django, di mana autentikasi akan berjalan dan semua fungsi di atas dapat digunakan.

Dalam hal otorisasi, Django menggunakan perizinan (permission) dan grup (groups). Melalui dua hal ini, dapat ditentukan pengguna dapat mengakses bagian aplikasi mana atau melakukan tindakan tertentu pada aplikasi. Grup mengelompokkan hak untuk pengguna, sehingga mempermudah penentuan hak pengguna sesuai dengan kelompoknya. Selain itu, Django juga memiliki decorator @permission_required dan middleware untuk mengecek izin akses pengguna. 

**Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?**

Django mengingat pengguna yang telah login menggunakan cookies dan session framework. Ketika pengguna login, Django akan menyimpan session ID dalam cookies browser. Di lain waktu saat pengguna login lagi menghasilkan adanya permintaan, cookie ini akan dikirim kembali ke server sehingga server dapat mengidentifikasi pengguna yang sedang aktif. 

Cookies memiliki banyak kegunaan selain menyimpan data last login pengguna, seperti menyimpan preferensi pengguna (misal tema browser dan bahasa), tracking dan analytics (untuk melacak aktivitas pengguna, lalu dianalisa untuk meningkatkan pengalaman pengguna), iklan dan personalisasi konten (melalui aktivitas penelusuran pengguna, hal-hal yang disukai pengguna dapat dianalisa sehingga iklan serta konten yang muncul akan sesuai kesukaan pengguna).

Tidak semua cookies aman digunakan. Ada cookies yang jika tidak dikonfigurasi sebagai cookie “secure” atau “http-only”, bisa rentan terhadap serangan Man-in-the-middle atau Cross-Site Scripting. Cookies juga dapat berasal dari pihak ketiga, sehingga data pengguna dalam cookies itu memiliki bahaya diekploitasi oleh perusahaan iklan/pihak ketiga. Jika cookies menyimpan data pribadi yang sensitif (misal: data kartu kredit), informasi tersebut rentan dicuri penyerang jika tidak ada proteksi atau enkripsi yang tepat.

## Tugas 5
**Checklist Step by Step**

* Implementasikan fungsi untuk menghapus dan mengedit product.
1. Menambah fungsi edit_product(request, id) dan delete_product(request, id) pada views.py. Lalu, merouting kedua fungsi tersebut dengan menambahkan import dan path di main/urls.py.
2. Membuat edit_product.html sebagai template untuk halaman edit product.
3. Menambahkan button untuk edit dan delete product pada main.html.

* Kustomisasi desain pada template HTML
1. Styling akan dibuat dengan Tailwind CSS, maka saya menambahkan Tailwind ke aplikasi melalui base.html
2. Menggunakan tailwind, saya membuat styling untuk halaman login, register, add product, dan edit product semenarik mungkin.
3. Membuat folder static/image yang akan diisi foto yang akan digunakan pada web.
4. Agar static dapat digunakan, saya menambah konfigurasi STATIC_URL, STATICFILES_DIRS, dan STATIC_ROOT pada settings.py.
5. Pada halaman yang akan menggunakan file dari static, saya menambah `{% load static %}` di atas kode.
6. Untuk halaman daftar produk, saya membuat `card_product.html` sebagai template untuk setiap kartu produk yang akan ditampilkan pada halaman. Halaman daftar produk saya buat responsive menggunakan card product yang menerapkan flexbox. Lalu, untuk kondisi halaman ketika ada atau tidaknya produk saya menggunakan if-else.
7. Untuk info toko (nama, kelas, dan NPM), saya membuat `store_info.html` yang berperan sebagai halaman About dan `card_info.html` sebagai kartu yang akan ditampilkan pada halaman tersebut.
8. Membuat `profile_info.html` sebagai halaman Profil User yang berisi data last login dan nama user.
9. Membuat dua button edit dan delete untuk setiap card dengan menambahkan button pada `card_product.html` yang dirouting ke fungsi `edit_product` dan `delete_product`.
10. Membuat `navbar.html` sebagai template untuk navigation bar, lalu saya menambah `{% include 'navbar.html' %}` di dalam block content setiap halaman yang menggunakan navigation bar.
11. Membuat navigation bar yang responsive dengan menggunakan pengaturan `md:flex` untuk desktop dan `md:hidden` untuk mobile.

**Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!**

Urutan prioritas pengambilan CSS selector adalah sebagai berikut.
1. !important = sebuah pengecualian, jika ada ini maka semua aturan lain akan disampingkan, dan aturan ini menjadi prioritas tertinggi.
2. Inline styles (`style = …`)= style yang diterapkan langsung di HTML melalui atribut style. Contoh: `<p style="color: purple;">Ini inline style</p>`
3. ID selector (`#id`) = selector yang menunjuk elemen dengan ID tertentu menggunakan tanda pagar (`#`). Contoh: `#main { color: green; }`
4. Classes selector (`.class`), pseudo-class (`:hover`, `:focus`, dll), dan atribut selector (`[attr=“value”]`). Contoh class selector: `.header { color: blue; }`. Contoh atribut selector: `input[type="text"] { background-color: yellow; }`.
5. Element selector/tag selector, pseudo-element. Contoh element selector: `h1`, `p`, `div`. Contoh pseudo-element: `::before`, `::after`.

Jika ada dua atau lebih CSS selector yang memiliki prioritas sama, aturan yang muncul terakhir akan diterapkan.

**Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!**

Responsive design adalah konsep yang penting dalam pengembangan aplikasi web agar web dapat diakses dan digunakan dengan nyaman melalui semua perangkat, yaitu mobile (hp dan tablet) serta desktop. Aksesibilitas suatu web sangat penting untuk pengalaman user, dan responsive design menjadi faktor utama aksesibilitas tersebut. Contoh aplikasi yang sudah menerapkan responsive design, yaitu Netflix, Youtube. Contoh aplikasi yang belum menerapkan responsive design, yaitu klikbca.com.

**Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!**

Margin merupakan ruang/space transparan yang mengelilingi border (di luar content, padding, dan border). Untuk kustomisasi, margin dapat diatur ketebalannya per sisi, yaitu kiri, kanan, atas, dan bawah.
``` html
<div class="m-2 mt-2 mb-2 mr-2 ml-2">
   <!-- m-n margin semua sisi sebesar n*0.25rem -->
   <!-- mt-n margin top/sisi atas sebesar n*0.25rem -->
   <!-- mb-n margin bottom/sisi bawah sebesar n*0.25rem -->
   <!-- mr-n margin right/sisi kanan sebesar n*0.25rem -->
   <!-- ml-n margin left/sisi kiri sebesar n*0.25rem -->
 ...
</div>
   ```

Border merupakan garis yang mengelilingi padding (di luar content dan padding). Untuk kustomisasi, border dapat diatur lebar, jenis, dan warna.
``` html
<!-- Ketebalan border -->
<div class="border-2 border-t-2 border-b-2 border-r-2 border-l-2">
   <!-- border-n margin semua sisi sebesar n px -->
   <!-- border-t-n margin top/sisi atas sebesar n px -->
   <!-- border-b-n margin bottom/sisi bawah sebesar n px -->
   <!-- border-r-n margin right/sisi kanan sebesar n px -->
   <!-- border-l-n margin left/sisi kiri sebesar n px -->
 ...
</div>
   ```
``` html
<!-- Warna border -->
<div class="border border-red-500"></div> <!-- Border merah -->
<div class="border-t border-t-blue-500"></div> <!-- Border atas biru -->
   ```
``` html
<!-- Sudut border -->
<div class="border border-2 rounded-lg"></div> <!-- Sudut dibulatkan sebesar large -->
   ```
Variasi ukuran radius border:
- rounded (small default radius)
- rounded-sm (small radius)
- rounded-md (medium radius)
- rounded-lg (large radius)
- rounded-full (fully rounded, like a circle)
- rounded-none (no rounding)

``` html
<!-- Jenis border -->
<div class="border-2 border-dashed border-blue-500"></div> <!-- Border garis putus-putus -->
   ```

Jenis-jenis border:
- border-solid (default solid border)
- border-dashed
- border-dotted
- border-double
- border-none

Padding merupakan ruang/space transparan yang mengelilingi content di dalam border. Untuk kustomisasi, padding dapat diatur ketebalannya per sisi, yaitu kiri, kanan, atas, dan bawah.
``` html
<div class="p-2 pt-2 pb-2 pr-2 pl-2">
   <!-- p-n padding semua sisi sebesar n*0.25rem -->
   <!-- pt-n padding top/sisi atas sebesar n*0.25rem -->
   <!-- pb-n padding bottom/sisi bawah sebesar n*0.25rem -->
   <!-- pr-n padding right/sisi kanan sebesar n*0.25rem -->
   <!-- pl-n padding left/sisi kiri sebesar n*0.25rem -->
 ...
</div>
   ```

**Jelaskan konsep flex box dan grid layout beserta kegunaannya!**

Flex box merupakan sistem tata letak/layout 1D yang mengatur elemen pada satu baris/kolom. Flex box, sesuai namanya, dapat mengatur elemen secara fleksibel, yaitu otomatis menyesuaikan ukurannya sesuai rusng yang tersedia. Dengan flex box, mudah bagi pengembang untuk membuat layout yang responsif, misal sejajar secara horizontal atau vertikal.

Grid layout merupakan sistem tata letak/layout 2D yang mengatur elemen pada suatu tabel (lebih dari satu baris dan kolom). Grid layout memungkinkan pengembang memiliki lebih banyak kontrol dalam pengaturan posisi elemen. Hal ini berkat posisi elemen yang diatur secara eksplisit, sehingga dapat lebih presisi sesuai keinginan pengembang.

## Tugas 6
**Checklist Step by Step**

**Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!**

1. Mempermudah pembuatan website yang interaktif. Menggunakan JavaScript, pengembang dapat membuat elemen interaktif pada situs web proyek mereka, misalnya tombol yang merespons klik, form untuk diisi pengguna, dan animasi yang responsif.
2. Lebih efisien karena eksekusi di client-side, yaitu sebagian besar operasi JavaScript berjalan di peramban pengguna. Hal ini bermanfaat untuk mengurangi beban server dan mempercepat pemuatan halaman, karena kompleksitas kode JS tidak memengaruhi performa situs web, melainkan peramban pengguna.
3. Membuat web lebih responsif dan dinamis, yaitu JS dapat memperbarui konten halaman web tanpa harus memuat ulang seluruh halaman.
4. Mempermudah pengguna membangun aplikasi dengan cepat karena JavaScript kompatibel dengan sebagian besar browser modern, serta memiliki ekosistem yang besar dengan framework seperti React, Angular, Vue.js, dan Node.js.

**Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?**

Await digunakan untuk menunggu hasil dari fetch() sebelum melanjutkan eksekusi kode, sehingga kode berikutnya dapat menggunakan data hasil tersebut. Jika kita tidak menggunakan await, kode setelah fetch() akan langsung dijalankan tanpa menunggu hasil dari fetch() itu sendiri. Akibatnya, hasil dari fetch() bisa tidak tersedia di saat kode selanjutnya diakses.

**Mengapa kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST?**

Kita perlu menggunakan decorator csrf_exempt karena bisa terdapat skenario permintaan AJAX POST di mana pengiriman token CSRF tidak diperlukan, misalnya endpoint yang berkomunikasi dengan aplikasi eksternal. Pada skenario itu, kita ingin menerima permintaan POST dari aplikasi lain yang tidak memiliki akses ke token CSRF kita. Supaya website tetap berjalan dengan lancar, maka kita perlu decorator csrf_exempt untuk menonaktifkan proteksi middleware CSRF. Jika kita tidak menggunakan csrf_exempt, maka Django dapat merespons dengan HTTP 403 Forbidden karena permintaan itu dianggap tidak aman. 

**Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?**

Pembersihan data input pengguna perlu dilakukan di backend juga karena frontend saja belum cukup untuk menjamin keamanan web. Frontend lebih mudah dimanipulasi oleh pengguna, misal dengan memodifikasi kode JavaScript di browser dan menonaktifkan validasi. Dengan menambah validasi dan pembersihan data di backend juga, kita memastikan input tidak bisa dilewati atau dimodifikasi oleh pengguna. Secara singkat, frontend berperan sebagai lapisan perlindungan pertama, dan backend berperan sebagai lapisan pertahanan utama.
