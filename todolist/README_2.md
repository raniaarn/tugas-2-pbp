# Tugas 5 PBP - todolist
## Rania Maharani Narendra - 2106650222

## Link to app
[![LINK](https://img.shields.io/badge/-Itemmate-8A2BE2?style=for-the-badge&logoColor=blueviolet)](https://itemmate.herokuapp.com/todolist)

## Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
### Internal CSS
Internal CSS adalah kode CSS yang diletakan langsung pada file HTML. Untuk melakukan ini, kita perlu menambahkan tag ``` style ``` di dalam head section. Contohnya :

```
<style>
    body {
        background-image: linear-gradient(-45deg, rgb(153, 251, 215), rgb(164, 183, 251));
        background-position: center center;
        margin: 0;
        padding: 0;
        min-height: 100vh;
        background-repeat: no-repeat;
    }
</style>
```
#### Kelebihan:
- kita bisa langsung menggunakan class dan id selectors untuk mempermudah design
- kita tidak perlu menambahkan files lain sehingga memudahkan kita
#### Kekurangan:
- menambahkan kode ke file HTML akan menaikkan memory dan loading time dari page yang sedang dibuat

### External CSS
Dengan external css, kita akan menghubungkan web pages yang dibuat dengan sebuah .css file (dibuat dengan text editor). Dengan 1 file css, kita bisa mengubah tampilan situs dengan beberapa pages secara bersamaan. 

kita juga perlu menambahkan reference ke file css kita dengan melakukan menambahkan kode berikut pada head section file HTML:
``` <link rel="stylesheet" type="text/css" href="<filename>.css" /> ```

style rules yang diletakkan pada .css files:
```
.xleftcol {
   float: left;
   width: 33%;
   background:#809900;
}
```
#### Kelebihan 
- dengan external CSS, file HTML akan lebih 'rapih' secara struktur dan lebih kecil ukurannya
- kita bisa menggunakan style yang sama untuk beberapa halaman web
#### Kekurangan
- page yang kita buat mungkin tidak melakukan render secara tepat sampai external CSS terload
- mengunggah atau menghubungan beberapa file CSS akan meningkatkan waktu dalam men-download situs yang kita buat

### Inline CSS
Hanya untuk menaruh style secara spesifik ke satu element HTML, kita hanya perlu menambahkan atribut style pada tag HTML yang mau kita terapkan style. Contoh:
``` 
<p style="color: rgb(182, 127, 234); padding-top: 20px; font-family: sans-serif; text-align: center;">Have an account? <a class="redirect_link" href="{% url 'todolist:login' %}">Log in</a></p>
```
#### Kelebihan
- kita bisa dengan mudah dan cepat menambahkan CSS rules ke dalam HTML page. Jadi mudah untuk testing dan melakukan perubahan lagi
- kita tidak perlu membuat file lain
#### Kekurangan
- akan membuat struktur file HTML kita menjadi berantakan dan memakan waktu untuk menulis ke satu-satu elemennya
- Menambah ukuran page dan waktu downloadnya.

## Jelaskan tag HTML5 yang kamu ketahui.
|       tags                     |     description                                               |
| :----------------------------: | :-----------------------------------------------------------: |
| ``` <a> ``` | sebuah hyperlink, menghubungkan ke page lain |
| ``` <b> ``` | menampilkan text dalam huruf tebal |
| ``` <body> ``` | mendefinisikan body dari file HTML |
| ``` <br> ``` | membuat sebuah baris kosong (line break) |
| ``` <button> ``` | membuat sebuah tombol yang dapat diclick |
| ``` <div> ``` | sebuah section pada file HTML |
| ``` <form> ``` | sebuah HTML form untuk mengambil input user |
| ``` <head> ``` | mendefinisikan head dari file HTML yang berisi informasi mengenai file HTML (title, etc) |
| ``` <h1> ``` to ``` <h6> ```  | headings
| ``` <hr> ``` | sebuah garis horizontal |
| ``` <html> ``` | root dari HTML file |
| ``` <img> ``` | sebuah foto |
| ``` <li> ``` | list item |
| ``` <meta> ``` | menyediakan struktur metadata mengenai konten dari file |
| ``` <ul> ``` | unrordered list |
| ``` <tr> ``` | row dari cells di tabel |
| ``` <th> ``` | header cell di table |
| ``` <td> ``` | suatu cell pada table |
| ``` <table> ``` | sebuah table |
| ``` <style> ``` | informasi style untuk file, biasanya CSS |

## Jelaskan tipe-tipe CSS selector yang kamu ketahui.
Selector adalah sebuah pattern dari elements dimana browser akan menerima informasi element HTML apa saja yang 'selected' untuk memiliki properti CSS yang di spesifikasikan. 

### Type
selectors yang menargetkan HTML elements seperti h1, p, body, dan sebagainya (tags). Contoh:
``` 
body {
    background-image: linear-gradient(-45deg, rgb(129, 237, 156), rgb(194, 163, 236));
    background-position: center center;
    margin: 0;
    padding: 0;
    min-height: 100vh;
    background-repeat: no-repeat;
}  
```
### Class
Selectors yang menargetkan elemen yang memiliki atribut class secara spesifik. Contoh (todolist.html):
```
.success {
    padding: 20px;
    background-color: rgb(115, 115, 236);
    color: white;
    margin-bottom: 15px;
    font-weight: bold;
}

```
### ID selector
Selectors yang menargetkan elemen yang memiliki atribut id tertentu
contoh:
```
#namaID {
}
```
### Pseudo-classes and pseudo-elements
selectors yang stylenya untuk states/kondisi tertentu dari suatu element, contohnya hover, visited, link. Contoh (todolist.html):
``` 
.delete_link:hover {
    color: rgb(71, 71, 226);
}
```
artinya bila terjadi hover, elemen a akan menyesuaikan.

### Universal Selectors
memilih semua elemen HTML pada file/halaman. Contoh (register.html):
``` 
  * {
    font-family: sans-serif;
  }
```

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
### 1.   Kustomisasi templat HTML
Untuk menggunakan Bootstrap, kita perlu menambahkan code berikut pada template HTML:

in head:

```<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">```

in body:

```<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-OERcA2EqjJCMA+/3y+gxIOqMEjwtxJY7qPCqsdltbNJuaOe923+mo//f6V8Qbsw3" crossorigin="anonymous"></script>```
Selain itu juga menggunakan internal CSS styling pada masing-masing template HTML (login, register, todolist, dan create-task)

### 2. Kustomisasi halaman utama todo list menggunakan cards.
dengan mengacu pada https://getbootstrap.com/docs/4.0/components/card/ ubah tampilan todolist yang tadinya berbentuk table, menjadi bentuk cards. Mengganti table dengan ``` <div class="card"> ```. Untuk menyajikan card dengan menarik, kita bisa menggunakan grid (row and column), yaitu dengan menerapkan class ```row``` dan ```row-cols-md-3``` agar terdiri dari 3 card per baris dan ``` g-4 ``` untuk gutter.

### 3. Membuat keempat halaman yang dikustomisasi menjadi responsive.
dalam head, tambahkan kode meta berikut untuk menerapkan responsive behavior:
``` 
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1"> 
```
dan dengan menggunakan CSS untuk mengubah ukuran suatu elemen. Menambahkan efek hover juga pada beberapa elemen agar halaman menjadi interactive.

credits:
1. https://www.hostinger.com/tutorials/difference-between-inline-external-and-internal-css
2. https://www.tutorialrepublic.com/html-reference/html5-tags.php
3. https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Selectors#:~:text=A%20CSS%20selector%20is%20the,the%20rule%20applied%20to%20them.
