# Tugas 6

## Link to 👉 [Heroku](https://pbp-tugas2-alvaro.herokuapp.com/) 👈

### Soal

#### 1. Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
Asynchronous programming adalah teknik programming tanpa menunggu, atau artinya dapat dilakukan secara bersamaan. Apabila saya beri contoh, asynchronous programming, apabila kita melakukan proses CRUD, maka kita tidak perlu untuk merefresh/reload website kita. Kita hanya perlu menunggu beberapa saat sampai proses itu selesai. Synchronus programming adalah kebalikan dari asynchronus programming, artinya membutuhkan proses mengulag/refresh apabila ingin melakukan perubahan data seperti **UPDATE/DELETE/POST**.

Programming synchronus merupakan teknik programming yang menurut saya paling straightforward karena tidak memerlukan logic untuk memanipulasi pemanggilan data. Sedangkan asynchronous programming membutuhkan manipulasi data. 

#### 2. Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.

Event-Driven programming juga bisa dibilang suatu paradigma pemrograman yang alur programnya ditentukan oleh suatu event / peristiwa yang merupakan keluaran atau tindakan pengguna atau bisa berupa pesan dari program lainnya. (source: OSF)

Aritnya Event-Driven Programming ini adalah paradigma pemrograman yang terjadi apabila ada penyebab (kejadian). Contoh penerapan hal ini yang dapat kita temukan dalam tugas ini adalah proses POST data yang kita lakukan. Apabila kita menekan tombol **Save Changes** pada modal (apabila data semua sudah terisi), maka kita bisa melihat bahwa akan ada data baru yang muncul. Hal ini adalah salah satu penerapan Event-Driven Programming ini. 

#### 3. Jelaskan penerapan asynchronous programming pada AJAX.
Kita bisa memanggil ajax pada program yang mempunyai tag `<scripts> </scripts>`. Kita bisa memasukkan logic AJAX kita. Pada proses kali ini saya akan menjelaskan proses POST pada AJAX karena paling mudah untuk memberikan visualisasi. Pada proses POST, pada ajax saya memanggil kode ini:
```
    $("#idForm").submit(function(e){
      e.preventDefault();
      var form = $(this);
      var actionUrl = form.attr("action");

      $.ajax({
        type: "POST",
        url: actionUrl,
        data: form.serialize(),
        success: function(data){
          console.log(data)
          var text = addText(data.data.title, data.data.description, data.is_finished, data.date, data.id)
          $(text).appendTo("#div")
          // $(text).replaceAll("#div")
          $("#exampleModal").modal('hide')
        },
        error: function(error){
          console.log(error)
          alert(error)
        }
      })
    })
```

Jadi saya memproses terlebih dahulu apabila button sudah di tekan atau belum. Lalu apabila sudah benar di tekan maka saya akan memanggil perintah AJAX yang menerima tipe POST dan URL yang telah disediakan. Saya akan serialize form untuk memvalidasi input form tersebut dan mengubah form tersebut menjadi dalam bentuk JSON. Saya menggunakan views untuk memvalidate data tersebut juga lalu menyimpan response data tersebut. Apabila berhasil maka saya akan menambahkan data yang saya terima dalam `<div> </div>` yang telah saya buat. Setelah itu maka data akan keluar.

#### 4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

Pertama saya membuat views untuk proses AJAX GET dengan membuat /json pada /todolist. Hal ini saya lakukan untuk menyimpan data dalam bentuk JSON agar ajax dapat GET data tersebut. Saya mengambil data ajax lalu menambahkan data tersebut pada div selectors yang saya buat.

Lalu saya mengimplementasi modal dengan COPAS dari halaman bootstrap, saya menambahkan logic AJAX POST serta menambahkan logic juga di views. Saya menambahkan data tersebut dengan save ke dalam database. Setelah itu saya menambahkan 1 data yang merupakan response dari AJAX kepada div yang telah saya buat. 

Untuk bagian DELETE saya melakukan hal yang sama seperti POST, hanya tetapi memanipulasi data yang didapat, dapat dibilang sedikit rumit. 
