[Cilla's Minimart](http://priscilla-natanael-cillasminimart.pbp.cs.ui.ac.id/)


## Tugas 1

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

## Tugas 2
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
