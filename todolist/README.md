# Tugas 4 PBP - todolist
## Rania Maharani Narendra - 2106650222

## Link to app
[![LINK](https://img.shields.io/badge/-Itemmate-8A2BE2?style=for-the-badge&logoColor=blueviolet)](https://itemmate.herokuapp.com/todolist)

## Kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
csrf token atau Cross Site Request Forgery token adalah sebuah token untuk keamanan berupa string yang akan digenerate secara random setiap halaman form muncul. Jadi tidak ada situs yang memiliki token yang sama. Fungsi dari token tersebut adalah untuk mencegah terjadinya serangan CSRF. Jika ```{% csrf_token %}``` tidak ditambahkan, maka request yang masuk tidak akan dieksekusi (aplikasi kita tidak akan dibiarkan untuk dideploy) oleh django. Hal ini karena apabila tidak ada csrf token, attacker dapat menyerang user (mengirimkan request juga) dan situs, sehingga perlu dimasukkan.

## Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
Ya, bisa. dengan menggunakan tag html ```<input>``` untuk membuat field sesuai dengan type yang bisa kita berikan (untuk login, typenya text, password typenya password, dan sebagainya). dari tag tersebut, kita bisa menerima input dari user dan data input user dikirimkan dari form ke database, kita bisa mengaksesnya data tertentu dengan ```request.POST.get(<String nama atribut data>)``` .

## Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
User mengisi fields yang ada pada halaman form dan melakukan submit sehingga data terkirim. Setelah itu data dikirimkan ke server (dengan method) ```save()```) jika data yang dikirimkan valid, dan database pada server akan berubah sesuai dengan input tersebut . Jika ada yang tidak valid, maka sesuai implementasi akan dilakukan sesuatu seperti pemberian peringatan.  Setelah itu, views mengembalikan render yang berisi data serta kemana dia akan dikirimkan (template HTML filenya) selanjutnya elemen terbaru akan ditampilkan.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
### Aplikasi todolist
``` django-admin startapp todolist ```
dengan melakukan command tersebut, secara otomatis akan ada folder aplikasi todolist berisi beberapa file python yang di-generate, berupa init, admin, apps, models, views, urls, dan tests. Dalam file settings.py, tambahkan 'todolist' ke dalam variable ```INSTALLED_APPS```. 

### Membuat model Task
Pada folder ```models.py```, buat sebuah class (Task) yang akan merepresentasikan tiap data/object yang nantinya akan dibuat (terdapat 4 variabel dan masing2nya merupakan jenis field yang berbeda-beda). 

untuk atribut user, menggunakan field ```ForeignKey()``` yaitu menandakan User berhubungan dengan modelnya. Ini juga akan membantu saat login dengan user yang bersangkutan untuk mendapatkan data-datanya. kemudian dilakukan migration untuk menerapkan skema model yang telah dibuat ke dalam database django lokal. 

### form registrasi, login, dan logout
Buat sebuah fungsi untuk merepresentasikan masing-masing form tersebut. Untuk register, menerima parameter request, melakukan pembuatan akun. Jika format yang diisi oleh user bersifat valid, maka jawaban disimpan dan akan memunculkan pesan akun berhasil dibuat, kemudian user akan di arahkan ke page login. masih dengan konsep MTV, dari views ini mengembalikan fungsi render sehingga akan muncul di ```register.html```. 

fungsi view dari login kurang lebih sama, menerima parameter request kemudian jika metode yang dikirimkan post, maka dapatkan username dan password dari input user. kemudian dengan fungsi authenticate memakai argumen request, username, dan password yang didapat. jika user ada, maka lakukan login menggunakan fungsi login dari ```django.contrib.auth```. kemudian user di arahkan ke halaman utama, jika tidak ada maka akan muncul pesan password atau username salah. Terakhir, return render dengan argumen request, ```login.html``` (untuk menampilkan halaman form login) dan context (tapi dalam hal ini kosong)

untuk logout, masih sama menerima parameter request tetapi tinggal menggunakan fungsi dari ```django.contrib.auth``` yaitu logout(request) dan diarahkan ke page login. 

### HTML untuk login dan register
sama seperti yang diajarkan pada lab sebelumnya, membuat template html untuk dipassing value dari views, perbedaannya di sini ada tag form karena kita meminta input dari user berupa username dan password. Untuk codenya ada pada ```login.html``` dan ```register.html``` pada todolist/templates.

### halaman utama todolist
Pada halaman menggunakan ```request.user``` pada ```views.py``` untuk mendapatkan data username. kemudian dipassing ke ```todolist.html``` untuk ditampilkan. data lainnya diambil dari database dengan menggunakan ```Task.objects.filter(user=username)``` untuk mengambil data tasks user yang sedang login saja. kemudian context dipassing ke HTML untuk ditampilkan. Template yang digunakan masih mirip dengan tugas-tugas sebelumnya, menggunakan table dan dilakukan looping untuk menampilkan setiap atribut dari tiap instance tasks. 

### form pembuatan task
Pertama-tama membuat ```forms.py``` dan class ```TaskForm``` yang menyimpan atribut field yang akan ditampilkan pada create-task nantinya, berisi juga sebuah inner class bernama Meta yang berisi model dan fields. model berarti class model yang kita pakai untuk generate form (dalam aplikasi ini berarti Task) dan fields yang nantinya akan di generate (untuk ini hanya title dan description saja). kemudian membuat fungsi pada ```views.py``` 

fungsi tersebut teretriksi dapat dibuka hanya jika ada pengguna yang login. Kemudian membuat object form dengan memanggil class yang ada pada ```forms.py``` dengan passing parameter ```request.POST```. kemudian save form ```form.save()``` untuk memasukkan datanya ke database jika inputnya valid dan arahkan user ke halaman utama. fungsi ini juga mengembalikan render ke ```create_task.html``` untuk passing context berupa form. 

Pada ```create_task.html```, kita hanya perlu menggunakan ```{{form}}``` untuk memunculkan fields untuk diisi user dan buat sebuah button dengan tag ```input``` dan type ```submit``` untuk mengirimkan data input user ke database.

### Routing
di dalam urls pada project_django, pada variable urlpatterns, menambahkan 
```path('todolist/', include('todolist.urls'))```
agar bisa mengakses aplikasi yang dibuat dengan path tersebut. Kemudian membuat file urls.py pada folder aplikasi yang dibuat untuk melakukan routing terhadap fungsi tadi, sehingga bisa ditampilkan di browser. urls.py berisi variable app_name dan urlpatterns yang berupa list berisi paths. Seperti berikut:
```
urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create_task'),
    path('delete-task/<str:pk>/', delete_task, name='delete_task'),
    path('edit-task/<str:pk>/', edit_task, name='edit_task'),
]
```
jadi parameternya terdiri dari route untuk url agar bisa diakses, fungsi, dan nama.

### Deployment
Karena menggunakan project yang sama dengan sebelumnya, maka apps yang dipakai masih sama. Tetapi jika dari awal, untuk memulai deploy, buat aplikasinya terlebih dahulu di Heroku, update Procfile, berkas dpl.yml untuk mengeksekusi deployment, menambahkan middleware white noise, membuat 2 variable repository secret di GitHub berupa nama aplikasi dan API Key. Setiap terjadi commit baru, buka GitHub Actions dan jalankan workflow yang gagal. Sambungkan juga aplikasi Heroku dengan repo GitHub agar langsung melakukan deploy tiap ada perubahan.

### menambahkan dua akun dan 3 dummy data
mengakses aplikasi yang sudah dibuat dan buat 2 akun pada halaman registrasi. kemudian tambahkan task sebanyak 3 task untuk masing-masing akun. Untuk melihat data pada admin dengan membuat akun staff atau superuser dengan cara berikut pada heroku console
```python manage.py createsuperuser```
masukkan email, username, dan password, dan selesai, kita bisa melihat data yang masuk dan mengaturnya lagi.
