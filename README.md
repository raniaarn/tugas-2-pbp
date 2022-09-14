nama: Rania Maharani Narendra
npm: 2106650222
kelas: PBP B

# Link menuju aplikasi

https://itemmate.herokuapp.com/katalog/

# Bagan request client ke web aplikasi berbasis Django
![bagan request drawio](https://user-images.githubusercontent.com/87572562/190277465-3a77513d-69f6-4273-ac6b-37623d0a1106.png)

# Kenapa menggunakan virtual environment?
Tanpa menggunakan virtual environment, project yang kita buat tetap berjalan tetapi dengan adanya virtual environment akan membantu kita untuk mejaga dependensi yang diperlukan oleh berbagai proyek, jadi virtual environment membuat python virtual environment yang terisolasi untuk masing-masing project. (memisahkan antar project agar tidak tercampur).
salah satu project kita mungkin membutuhkan library dengan version yang berbeda dengan project kita yang lainnya. Tanpa ada virtual environment, hanya ada satu tempat untuk install packages, sehingga kita tidak bisa bekerja dengan library berbeda versi. Virtual environment mengelola hal tersebut, memberi tempat berbeda sehingga bisa install library berbeda buat project lain.

# bagaimana cara saya mengimplementasikan poin 1 sampai dengan 4

1. **Membuat sebuah fungsi pada views.py yang dapat melakukan pengambilan data dari model dan dikembalikan ke dalam sebuah HTML.**
pada file views.py yang ada pada folder aplikasi yang kita buat, dibuat sebuah fungsi untuk pengambilan data dari models.py dan nantinya data yang akan di-passing berupa dictionary (ada key dan valuenya, key nanti yang akan digunakan pada file html aplikasi yang kita buat dan akan mengembalikan value sesuai yang kita assign, akan muncul di tampilan aplikasi nantinya). Data dari models.py berupa items yang akan muncul di aplikasi dan data lainnya, dalam project ini terdapat name dan student_id.
fungsi pada views.py ini akan return dengan memanfaatkan render() function dari django (harus diimport terlebih dahulu). render ini mengambil request (argumen pertama), mengirimkan/passing data ke template html yang akan ditampilkan (argumen kedua), dan dictionary berisi data yang kita akan kirimkan (argumen ketiga).

2. **Membuat sebuah routing untuk memetakan fungsi yang telah kamu buat pada views.py.**
dalam folder aplikasi yang dibuat (katalog), dalam file urls.py, dalam variable urlpatterns, dilakukan routing terhadap fungsi views yaitu dengan menambahkan list berisi path sehingga bisa dipetakan fungsi pada poin 1 dengan file template html (katalog.html). Path berisi argumen route, view, dan nama.
route berupa string yang mengandung path di url (ex: route = 'hello/', maka url= http://localhost:8000/hello/) jika string kosong maka tidak ada path lanjutan. argumen kedua berisi nama fungsi yang kita buat tadi untuk nantinya di eksekusi, dan argumen ketiga untuk penamaan url pattern tersebut. Kita juga menambahkan path baru di url patterns yang ada pada file urls.py di file project_django. di sana menambahkan route dengan string nama aplikasi yang kita buat dan argumen kedua berisi include('katalog.urls') untuk import path yang telah dibuat sebelumnya di urls.py folder katalog.
dengan ini path aplikasi yang kita buath sudah linked dengn urls.py sehingga saat terjadi request, fungsi pada poin 1 dipanggil dan return tampilan aplikasi.

3. **Memetakan data yang didapatkan ke dalam HTML dengan sintaks dari Django untuk pemetaan data template.**
lakukan mapping dengan menggunakan sintaks khusus yaitu {{ data }} (double curly braces). template akan mengambil data dari fungsi pada poin 1. Untuk menampilkan data daftar item, kita harus melakukan iterasi karena daftar tersebut berupa kontainer berisi object items. Maka dilakukan looping dengan syntax:
``` 
{% for item in list_of_items %}
      <tr>
        <th>{{item.attributes}}</th>
      </tr>
    {% endfor %}
```
kemudian ada syntax untuk membuat sebuah table dengan data kita.

4. **Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.**
push semua perubahan yang tersimpan pada lokal ke repository GitHub, membuat file bernama Procfile yang akan digunakan heroku untuk membaca aktivitas log aplikasi ke sistem monitoring internal heroku. Kemudian dalam repo yang sama, juga buat file dpl.yml berisi script yang digunakan untuk mengeksekusi deployment oleh runner dari GitHub Actions. kita jga harus menmbahkan konfigurasi terkait ditectory pada folder project_django pada settings.py yang berisi segala setting mengenai project kit, allowed host pada settings.py juga disetting agar bisaa diakses semua host dengan mamasukkan bintang. 
agar tersedia static files (biar kita bisa deploy dimana saja taanpa bergantung kepada layanan external) ditaambahkan whitenoise middleware pada variable middleware yang ada di settings.py
membuat 2 variable repository secret yang berisi nama aplikasi dan API key dari akun heroku, setelah itu deployment sukses. Saya juga melakukan automatic deployment dengan menyambungkan heroku dan repository saya agar jika ada perubahan bisa terdeploy.
 

## Credits

Template ini dibuat berdasarkan [PBP Ganjil 2021](https://gitlab.com/PBP-2021/pbp-lab) yang ditulis oleh Tim Pengajar Pemrograman Berbasis Platform 2021 ([@prakashdivyy](https://gitlab.com/prakashdivyy)) dan [django-template-heroku](https://github.com/laymonage/django-template-heroku) yang ditulis oleh [@laymonage, et al.](https://github.com/laymonage). Template ini dirancang sedemikian rupa sehingga mahasiswa dapat menjadikan template ini sebagai awalan serta acuan dalam mengerjakan tugas maupun dalam berkarya.
