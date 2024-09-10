[Cilla's Minimart](http://priscilla-natanael-cillasminimart.pbp.cs.ui.ac.id/)



**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**
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


**Jelaskan fungsi git dalam pengembangan perangkat lunak!**

Git merupakan sistem kontrol versi yang dalam pengembangan perangkat lunak berguna untuk memungkinkan tim mengembangkan proyek secara kolaboratif dan terorganisir. Beberapa fungsi utama Git, yaitu version control, kolaborasi tim, branching dan merging, reversibilitas, serta backup dan keamanan. Version control, yaitu Git mencatat setiap perubahan yang terjadi pada proyek, sehingga mudah untuk melacak apa perubahan yang sudah dilakukan, siapa yang membuat perubahan, dan kapan perubahan dilakukan. Kolaborasi tim, Git memungkinkan para pengembang dalam tim untuk mempunyai salinan lokal, sehingga mereka dapat melakukan perubahan masing-masing tanpa mengganggu satu sama lain. Perubahan-perubahan ini kemudian dapat Git gabungkan ke dalam satu repositori pusat. Branching dan merging, yaitu setiap pengembang bisa membuat branchnya sendiri untuk mengerjakan fitur baru/memperbaiki kode yang ada, lalu branch ini dapat dimerge ke cabang utama. Reversibilitas, pada Git pengembang dapat kembali ke versi sebelumnya jika terjadi kesalahan dalam pengembangan. Backup dan keamanan, yaitu Git berfungsi sebagai cloud yang menyimpan cadangan untuk proyek perangkat lunak, sehingga jika terjadi kerusakan pada komputer lokal, proyek masih aman dalam cloud Git. Semua fitur ini sangat berguna dalam pengembangan perangkat lunak, terutama jika skala proyek besar, Git mempermudah tim untuk bekerja secara kolaboratif dan minim kesalahan fatal.

**Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?**
Untuk menjadi permulaan pembelajaran pengembangan perangkat lunak, suatu framework perlu memiliki fitur fitur yang mempermudah para pemula membangun aplikasi dan memahami konsep-konsep dasar. Pertama, Django merupakan framework yang sudah mencakup banyak fitur penting, seperti autentikasi pengguna, manajemen URL, validasi form, ORM (Object-Relational Mapping), dan admin panel bawaan. Oleh karena itu, pemula tidak perlu repot membuat fitur-fitur di atas dari nol. Django juga memiliki dokumentasi yang komprehensif, mempermudah pemula untuk memahami proses kerja framework. Pola arsitektur berupa MVT (Model-View-Template) pada Django juga memudahkan para pemula mempelajari struktur aplikasi yang terorganisir karena pemisahan yang jelas antara logika bisnis (model), tampilan (template), dan logika pengontrol (view) jelas. Bahasa pemrograman yang digunakan pada Django adalah Python, bahasa yang juga terkenal beginner-friendly  karena sederhana dan mudah dipelajari. 

**Mengapa model pada Django disebut sebagai ORM?**
