# Tugas 6 PBP - todolist
## Rania Maharani Narendra - 2106650222

## **Link to app**
[![LINK](https://img.shields.io/badge/-Itemmate-8A2BE2?style=for-the-badge&logoColor=blueviolet)](https://itemmate.herokuapp.com/todolist)


<hr>

## **Perbedaan antara Asynchronous Programming dengan Synchronous Programming.**

### *Asynchronous Programming:*
Pemrograman Asinkronus adalah suatu pendekatan dimana kita bisa menjalankan banyak proses sekaligus (paralel), tanpa terikat dengan proses lainnya (independen). Dengan ini waktu eksekusi akan lebih cepat. Dengan menerapkan Asynchronous programming, user tidak perlu melakuakan reload/refresh page secara keseluruhan karena instruksi dijalankan dikelola AJAX secara asynchronous

### *Synchronous Programming*
Berbeda dengan Asynchronous, Synchronous Programming hanya dapat berjalan satu persatu prosesnya, jadi untuk menjalankan suatu proses, harus menunggu proses sebelumnya selesai terlebih dahulu. User harus menunggu response hingga page terload/refresh secara keseluruhan baru melakukan aktivitas lain pada suatu page.


<hr>


## **paradigma Event-Driven Programming dan penerapannya pada tugas kali ini**
suatu paradigma dimana user bisa berinteraksi dengan page lalu terjadinya suatu event tertentu yang ditangkap oleh sebuah function JS, dan fungsi tersebut dieksekusi. Artinya flow dari program bergantung kepada event yang dilakukan oleh user. Contoh dari event seperti menggeser mouse (hover), click, keypress, focus, onscroll, dan lain-lain.

Pada tugas ini, saya banyak memakai onclick event seperti contohnya:
```
document.getElementById("button").onclick = addTodo
```
ketika menekan tombol create task yang memiliki id button, maka akan menambahkan task baru sesuai input yang dimasukkan, event tersebut akan memanggil fungsi addTodo. Selain itu ada juga `.ready(function ())` dimana akan selalu menjalankan fungsi tersebut setiap halaman dibuka.

<hr>


## **penerapan asynchronous programming pada AJAX**
dengan AJAX, kita dimungkinkan untuk mengambil data dari database tanpa harus melakukan refresh/reload keseluruhan page, dengan kata lain secara asinkronus. Implementasinya dilakukan dengan event driven programming dan dengan menggunakan AJAX GET dan AJAX POST. Fungsi pada views.py juga mengembalikan HttpResponse agar langsung mengirimkan respon. Contoh cara pengimplementasiannya bisa dilihat pada poin selanjutnya, ada pada `todolist.html`, berikut contoh fungsi asinkronus dengan ajax:
```
function addTodo() {
  let message ='';
  fetch("{% url 'todolist:add_task' %}", {
    method: "POST",
    body: new FormData(document.querySelector('#form'))
  }).then(showTask)
  return false
}
```
pada `views.py`:
```
@login_required(login_url='/todolist/login/')
def add_task(request):
  if request.method == 'POST':
    title = request.POST.get("title")
    description = request.POST.get("description")
    user = request.user

    new_task = Task(user=user, title=title, description=description)
    new_task.save()
    return HttpResponse(b"CREATED")

  return HttpResponseNotFound()
```
saat button yang dihubungkan dengan addTodo diclick, secara asinkronus, task akan bertambah tanpa load halaman

<hr>


## **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.**
### **AJAX GET**
- membuat view baru yang mengambil data task dalam bentuk json yaitu dengan cara membuat fungsi yang mengambil data dari database dan mengirimkan HttpResponse yang berisi parameter data hasil query yang diserialisasi menjadi json `return HttpResponse(serializers.serialize("json", data))`
- Melakukan routing sehingga data dalam bentuk json bisa diakses, dilakukan dengan menambahkan path `/todolist/json` pada urls.py yang mengarah ke view `get_todolist_json` pada `views.py`
- dengan tag `<script>` pada todolist.html, import Jquery Ajax kemudian buat dalam js, buat sebuah fungsi untuk menampilkan data-data tasks pada HTML. fungsi ini menggunakan method GET yang diarahkan ke fungsi `get_todolist_json` pada `views.py`, kemudian masukkan ke dalam id tag yang sesuai
- Menambahkan code berikut:
```
$(document).ready(function () {
        showTask();
      }); 
```
untuk merender data-data yang sudah ada setiap website dibuka

### **AJAX POST**
- membuat modal dengan bootstrap, code mengacu pada https://getbootstrap.com/docs/5.2/components/modal/. Ketika button `add task` diclick, akan muncul popup modal yang berisi form pembuatan task dan sebuah button submit create task.
- membuat view baru untuk menambahkan task ke database, ini dilakukan dengan membuat fungsi `add_task` pada `views.py`. Fungsi ini membuat object Task baru dengan atribut sesuai dari model Task kemudian mengembalikan HttpResponse.
- melakukan routing, membuat path `/todolist/add` pada `urls.py`
- menutup modal setelah penambahan task berhasil dengan menambahkan atribut `data-bs-dismiss="modal"` pada button create task
- melakukan refresh secara asinkronus menggunakan AJAX, menggunakan fetch dan method POST, kemudian memanggil fungsi get yang telah dibuat sebelumnya untuk melakukan load data dari database (fungsi showTask)
