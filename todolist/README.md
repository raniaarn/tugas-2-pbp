# Tugas 3 PBP - todolist
## Rania Maharani Narendra - 2106650222

## Link to app
https://itemmate.herokuapp.com/todolist

## Kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?

## Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.

## Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
### Aplikasi mywatchlist
``` django-admin startapp todolist ```
dengan melakukan command tersebut, secara otomatis akan ada folder aplikasi mywatchlist berisi beberapa file python yang di-generate, berupa init, admin, apps, models, views, urls, dan tests. Dalam file settings.py, tambahkan 'mywatchlist' ke dalam variable INSTALLED_APPS. Pada folder models.py, buat sebuah class yang akan merepresentasikan tiap data/object yang nantinya akan dibuat (terdapat 4 variabel dan masing2nya merupakan jenis field yang berbeda-beda). 

untuk atribut user, menggunakan field ForeignKey() yaitu menandakan User berhubungan dengan modelnya. Ini juga akan membantu saat login dengan user yang bersangkutan.kemudian dilakukan migration untuk menerapkan skema model yang telah dibuat ke dalam database django lokal. 

### form registrasi, login, dan logout
Buat sebuah fungsi untuk merepresentasikan masing-masing form tersebut. Untuk register, menerima parameter request, melakukan pembuatan akun, dan disimpan jika isi formnya valid. 

### halaman utama todolist

### form pembuatan task

### Path todolist
di dalam urls pada project_django, pada variable urlpatterns, menambahkan 
```path('todolist/', include('todolist.urls'))```
agar bisa mengakses aplikasi yang dibuat dengan path tersebut. Membuat fungsi pada views.py yang akan mereturn render berisi parameter request, template HTML, dan context (dictionary berisi data yang mau dipetakan). template HTML sebagaimana HTML pada umumnya yang akan mengambil data dari views.py. Kemudian membuat file urls.py pada folder aplikasi yang dibuat untuk melakukan routing terhadap fungsi tadi, sehingga bisa ditampilkan di browser. urls.py berisi variable app_name dan urlpatterns yang berupa list berisi paths.

### Menambahkan 10 data untuk objek MyWatchList

### routing


### Deployment
Karena menggunakan project yang sama dengan sebelumnya, maka apps yang dipakai masih sama. Tetapi jika dari awal, untuk memulai deploy, buat aplikasinya terlebih dahulu di Heroku, update Procfile, berkas dpl.yml untuk mengeksekusi deployment, menambahkan middleware white noise, membuat 2 variable repository secret di GitHub berupa nama aplikasi dan API Key. Setiap terjadi commit baru, buka GitHub Actions dan jalankan workflow yang gagal. Sambungkan juga aplikasi Heroku dengan repo GitHub agar langsung melakukan deploy tiap ada perubahan.

### menambahkan dua akun dan 3 dummy data

