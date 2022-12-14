# Tugas 3 PBP - mywatchlist
## Rania Maharani Narendra - 2106650222

## Link to app
https://itemmate.herokuapp.com/mywatchlist/html

https://itemmate.herokuapp.com/mywatchlist/json

https://itemmate.herokuapp.com/mywatchlist/xml

## Perbedaan antara JSON, XML, dan HTML
JSON adalah JavaScript Object Notation. JSON digunakan untuk merepresentasikan data (data delivery) sebagai pasangan key dan value yang bisa dengan mudah dikonversi dari dan menjadi object JavaScript.

XML adalah eXtensible Markup Language. XML secara umum digunakan untuk struktur data atau sebuah pesan, dan dugunakan juga untuk mendeskripsikan suatu data jadi fokus utama dari XML bukanlah untuk memberikan tampilan suatu data.

Jadi JSON dan XML digunakan untuk penyimpanan dan pertukaran data. Untuk perbedaan keduanya:

| JSON                                                                      | XML                                                        |
| :-----------------------------------------------------------------------: | :--------------------------------------------------------: |
| mengambil data dalam bentuk JSON String                                   | dalam bentuk XML Document                                  |
| memakai JSON.parse() untuk dikonversi jadi native Javasctript object      | melakukan looping di masing-masing node untuk mengambil informasi menggunakan XML DOM
| lebih mudah dan capet daripada XML (ukurannya juga lebih kecil)           | Bisa melakukan esktraksi data dan menyimpannya di variable |

berbeda dengan JSON dan XML, HTML lebih digunakan untuk mengatur tampilan serta presentasi dari suatu data.

HTML adalah Hypertext Markup Language. HTML menyediakan code yang akan digunakan untuk membuat tampilan halaman website dan juga aplikasi web. 

beberapa perbedaan lagi:
- jika ada multi white-space di HTML, akan dijadikan single white-space. Sedangkan di XML, tidak akan dipotong. JSON juga mengabaikan white-space
- dalam HTML, data secara langsung dapat dipetakan dengan aplikasi, sedangkan XML tidak langsung
- size dari HTML lebih kecil dibandingkan XML, tetapi JSON lebih kecil karena lebih pendek
- HTML case insensitive, sedangkan XML dan JSON case-sensitive

## mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform
Dengan bantuan data delivery, aplikasi diizinkan untuk bertukar informasi antar platform, aplikasi, devices dan juga antar sistem operasi. 

Ada beberapa alasan mengapa penggunaan data delivery diperlukan selain untuk melakukan pertukaran antar platform, dengan data delivery, keamanan lebih meningkat karena dari banyak sistem yang dibuat, hanya ada 1 sistem pusat yang akan menyimpan data dan sistem lain menerima data yang dikirimkan sistem pusat. Kemudian dengan bantuan data delivery, akan memungkinkan kita untuk membuat mobile apps karena akan mudah berkomunikasi dengan web apps. Dengan data delivery, akan ada integrasi internal atau external systems (integrasi antara sistem-sistem informasi).

## cara mengimplementasikan Tugas 3
### Aplikasi mywatchlist
``` django-admin startapp mywatchlist ```
dengan melakukan command tersebut, secara otomatis akan ada folder aplikasi mywatchlist berisi beberapa file python yang di-generate, berupa init, admin, apps, models, views, urls, dan tests. Dalam file settings.py, tambahkan 'mywatchlist' ke dalam variable INSTALLED_APPS. Pada folder models.py, buat sebuah class yang akan merepresentasikan tiap data/object yang nantinya akan dibuat (terdapat 5 variabel dan masing2nya merupakan jenis field yang berbeda-beda). kemudian dilakukan migration untuk menerapkan skema model yang telah dibuat ke dalam database django lokal. 

### Path mywatchlist
di dalam urls pada project_django, pada variable urlpatterns, menambahkan 
```path('mywatchlist/', include('mywatchlist.urls'))```
agar bisa mengakses aplikasi yang dibuat dengan path tersebut. Membuat fungsi pada views.py yang akan mereturn render berisi parameter request, template HTML, dan context (dictionary berisi data yang mau dipetakan). template HTML sebagaimana HTML pada umumnya yang akan mengambil data dari views.py. Kemudian membuat file urls.py pada folder aplikasi yang dibuat untuk melakukan routing terhadap fungsi tadi, sehingga bisa ditampilkan di browser. urls.py berisi variable app_name dan urlpatterns yang berupa list berisi paths.

### Menambahkan 10 data untuk objek MyWatchList
menambahkan 10 data dengan menggunakan file JSON yang di dalamnya berupa list of dictionaries (menandakan sebuah object), setiap data memiliki atribut yang sebelumnya telah dibuat pada models.py. Setelah dibuat, melakukan ```python manage.py loaddata initial_wishlist_data.json```
tambahkan juga pada Procfile.

### HTML, XML, JSON dan routing
HTML sudah dijelaskan pada path mywatchlist. Untuk json dan xml membuat fungsi baru lagi untuk masing-masing. fungsi tersebut menerima parameter request. Sama dengan HTML, buat vaariable yang menyimpan hasil query dari data pada MyWatchList yaitu dengan cara ```MyWatchList.objects.all()```. Kemudian fungsi tersebut akan return HttpResponse parameternya content yang menggunakan serializers (converting objects ke tipe data yang mudah di render (ke JSON, XML, dsb)), memakai method serialize menerima parameter json/xml dan data yang mau diconvert. Parameter kedua dari HttpResponse adalah content type ```content_type="application/<xml atau json>")```
kemudian tambahkan path url ke dalam urlpatterns pada mywatchlist.urls berisi parameter path, fungsi yang mau di routing, dan nama fungsinya. ```path('json/', show_json, name="show_json")```

### Deployment
Karena menggunakan project yang sama dengan sebelumnya, maka apps yang dipakai masih sama. Tetapi jika dari awal, untuk memulai deploy, buat aplikasinya terlebih dahulu di Heroku, update Procfile, berkas dpl.yml untuk mengeksekusi deployment, menambahkan middleeware white noise, membuat 2 variable repository secret di GitHub berupa nama aplikasi dan API Key. Setiap terjadi commit baru, buka GitHub Actions dan jalankan workflow yang gagal. Sambungkan juga aplikasi Heroku dengan repo GitHub agar langsung melakukan deploy tiap ada perubahan.

### Screenshot postman
<img width="890" alt="Screenshot 2022-09-22 101427" src="https://user-images.githubusercontent.com/87572562/191650996-f20cb16f-67ad-4fa3-82b1-bfe35b5b4469.png">
<img width="886" alt="Screenshot 2022-09-22 101516" src="https://user-images.githubusercontent.com/87572562/191651038-aa0fcf3b-d9fa-4840-88ea-2f1b0d2387b9.png">
<img width="896" alt="Screenshot 2022-09-22 101447" src="https://user-images.githubusercontent.com/87572562/191651045-73ae95fd-fbda-43c6-b073-9caa1abe6323.png">

sumber:

Slide Data Delivery - https://scele.cs.ui.ac.id/pluginfile.php/161284/mod_resource/content/1/04%20-%20Data%20Delivery.pdf

https://www.interviewbit.com/blog/difference-between-html-and-xml/

