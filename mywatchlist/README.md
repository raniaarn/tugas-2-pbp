# Tugas 3 PBP - mywatchlist
## Rania Maharani Narendra - 2106650222

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
Dengan bantuan data delivery, aplikasi diizinkan untuk bertukar informasi antar platform, aplikasi, devicees dan juga antar sistem operasi. 

Ada beberapa 




## cara mengimplementasikan Tugas 3
### Aplikasi mywatchlist
``` django-admin startapp mywatchlist ```
dengan melakukan command tersebut, secara otomatis akan ada folder aplikasi mywatchlist berisi beberapa file python yang di-generate, berupa init, admin, apps, models, views, urls, dan tests. Dalam file settings.py, tambahkan 'mywatchlist' ke dalam variable INSTALLED_APPS. Pada folder models.py, buat sebuah class yang akan merepresentasikan tiap data/object yang nantinya akan dibuat (terdapat 5 variabel dan masing2nya merupakan jenis field yang berbeda-beda). kemudian dilakukan migration untuk menerapkan skema model yang telah dibuat ke dalam database django lokal. 

### Path mywatchlist
di dalam urls pada project_django, pada variable urlpatterns, menambahkan 
```path('mywatchlist/', include('mywatchlist.urls'))```
agar bisa mengakses aplikasi yng dibuat dengan path tersebut. Kemudian buat folder urls pada folder mywatchlist 



## Screenshot postman
![messageImage_1663699690024](https://user-images.githubusercontent.com/87572562/191407355-0e6f8efd-a02f-4dcd-a003-f1d33f9865ad.jpg)
![messageImage_1663699724833](https://user-images.githubusercontent.com/87572562/191407363-c9cac190-4807-44d2-a2ac-c838de41d76b.jpg)
![messageImage_1663699745280](https://user-images.githubusercontent.com/87572562/191407368-a751040b-4e63-49a2-95bd-0394507e146f.jpg)

sumber:
Slide Data Delivery - https://scele.cs.ui.ac.id/pluginfile.php/161284/mod_resource/content/1/04%20-%20Data%20Delivery.pdf
https://www.interviewbit.com/blog/difference-between-html-and-xml/

