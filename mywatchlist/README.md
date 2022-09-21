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

Ada beberapa alasan mengapa penggunaan data delivery diperlukan selain untuk melakukan pertukaran antar platform, dengan data delivery, keamanan lebih meningkat karena dari banyak sistem yang dibuat, hanya ada 1 sistem pusat yang akan menyimpan data yang akan dikirimkan ke sistem lain. Kemudian dengan bantuan data delivery, akan memungkinkan kita untuk membuat mobile apps karena akan mudah berkomunikasi dengan web apps. Dengan data delivery, akan ada integrasi internal atau external systems. 

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
![messageImage_1663699690024](https://user-images.githubusercontent.com/87572562/191407355-0e6f8efd-a02f-4dcd-a003-f1d33f9865ad.jpg)
![messageImage_1663699724833](https://user-images.githubusercontent.com/87572562/191407363-c9cac190-4807-44d2-a2ac-c838de41d76b.jpg)
![messageImage_1663699745280](https://user-images.githubusercontent.com/87572562/191407368-a751040b-4e63-49a2-95bd-0394507e146f.jpg)

sumber:

Slide Data Delivery - https://scele.cs.ui.ac.id/pluginfile.php/161284/mod_resource/content/1/04%20-%20Data%20Delivery.pdf

https://www.interviewbit.com/blog/difference-between-html-and-xml/

