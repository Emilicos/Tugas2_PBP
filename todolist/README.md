# Tugas 4

## Link to 👉 [Heroku](https://pbp-tugas2-alvaro.herokuapp.com/) 👈

### Soal

#### 1. Apa kegunaan `{% csrf_token %}` pada elemen `<form>`? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen `<form>`? <br>
Kegunaan dari `{% csrf_token %}` adalah untuk mencegah serangan pada website kita. Sehingga orang yang tidak mempunyai token tidak dapat melakukan operasi pada object-object yang ada. **CSRF Token** adalah nilai yang bersifat unik, rahasia, dan tidak dapat di prediksi. **CSRF Token** sangat berguna untuk melindung aplikasi kita dari serangan-serangan yang tidak diinginkan artinya penyerang harus memberikan token yang valid untuk meminta request yang valid. Tanpa **CSRF Token** Browser tidak dapat membuat cookie yang bersifat aman dan tidak bisa memberikan authorisasi terhadap akun kita. Contohnya seseorang dapat menipu website kita untuk melakukan suatu aksi seakan seorang user malakukan aksi tersebut. Dengan **CSRF Token** semua bisa teratasi dengan baik dan benar. 

#### 2. Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual. <br>
Tentu saja kita bisa membuat elemen secara manual tanpa menggunakan generator. Namun apabila kita membuat form kita sendiri akan menyulitkan developer. Seperti yang kita pelajari pada awal-awal minggu di PBP, lebih baik untuk tidak menyulitkan developer, kita bisa saja menggunakan form yang telah disediakan oleh Django itu sendiri. Django memiliki banyak sekali method yang sangat berguna untuk mempermudahkan pekerjaan developer Django. Tanpa generator table, Template Django tidak dapat mengetahui bagaimana cara merender HTML Output. Walaupun kita bisa melihat hasil, namun tidak akan menjadi indah. Saya membuat form saya sendiri dalam mengerjakan `create-task`. Terlihat bahwa akan lebih sulit untuk membuat form sendiri walaupun sudah ada method. 

<img width="638" alt="Diagram_Form_Manual" src="https://user-images.githubusercontent.com/91789098/192094383-05bdbb45-ed4b-4ed4-a911-c131242c89b2.png">

Saya memberikan gambaran diatas bagaimana kita bisa form bekerja, dan akan saya jelaskan bagaimana form bekerja secara manual. Gambar tersebut saya dapatkan dari [website ini](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms). Apabila kita membuat form secara manual banyak sekali step yang harus dilakukan. Pertama browser harus request page dari form yang ada lalu dari request tersebut form akan diupdate. Setelah diupdate maka form tersebut akan dikirimkan ke URL untuk divalidate datanya apabila belum. Apabila data valid maka browser akan menredirect kita ke URL yang success. Namun apabila gagal, maka Django akan memberikan pesan bahwa data tersebut gagal. 

Oleh karena itu apabila kita membuat form secara manual maka kita harus mengimplementasikan segala sesuatu tersebut. Apabila kita memakai generator maka tugas kita akan jauh lebih cepat diselesaikan. 

#### 3. Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML. <br>

Awal-awal user diperintahkan untuk mengisi form yang ada pada saat kita submit maka website tersebut akan meyuruh data untuk di **POST**. Melalui post ini data akan diolah di `views.py` melalui bantuan `urls.py`. Setelah data ini diolah maka kita akan memastikan terlebih dahulu apakah data tersebut sesuai dengan model/form yang diinginkan. Apabila valid/sesuai. Apabila sesuai maka kita save form tersebut ke data base kita dan kemudian kita mengarahkan data tersebut melalui context yang diberikan di `view.py`. Melalui context ini kita bisa menggunakan data untuk dikeluarkan dalam bentuk HTML sesuai dengan template yang kita inginkan. Apabila context tersebut valid dan sudah di save maka HTML dapat melakukan looping untuk mengakses data yang kita miliki tersebut. 

#### 4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas. <br>

Awal-awal saya membuka virtual environment saya terlebih dahulu berdasarkan `env\Scripts\activate`. Setelah terbuka saya lalu melakukan `python manage.py startapp todolist` untuk membuat aplikasi baru pada project django kita. Setelah itu saya ubah url seperti tugas-tugas sebelumnya. Lalu saya buat semuah model bernama **Task** untuk memberikan schema kepada database kita. Lalu saya menggunakan kode pada lab 3 untuk membuat fungsi login, register, dan logout. Saya memuat user, tabel, dan button yang diinginkan. Lalu saya membuat file baru bernama `forms.py` untuk memudahkan saya validate data yang dinginkan, setelah valid saya save data tersebut ke database kita. Namun user dan date tidak ada dalam input type sehingga saya harus memasukkan user instance secara manual dan menambahkan auto add pada field model di `models.py` saya. Saya menggunakan method **forms.Model** untuk memberikan metaclass agar model dapat digunakan dengan baik. Lalu saya perbaiki routing saya agar sesuai dengan tugas. Kemudian saya buka heroku dan membuat dummy data. Saya juga mengerjakan bonus dengan membuat fungsi baru yaitu **change_task_status** agar melakukan proses PUT (Update). Lalu saya membuat fungsi lagi bernama **delete_task** untuk mendelete data sedsuai dengan pk (primary key) yang saya dapat dari context pada HMTL. Lalu saya mengerjakan readme ini :D.  

Dummy user saya:

Username: 123
Password: pbpkelasd

Username: 1234
Password: pbpkelasd

# Tugas 5

## Link to 👉 [Heroku](https://pbp-tugas2-alvaro.herokuapp.com/) 👈


### Soal

#### 1. Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style? <br>
Inline CSS adalah CSS yang dilakukan dalam elemen, artinya apabila suatu elemen memiliki elemen tertentu kita melakukan custom styling pada elemen tersebut. Contohnya 

`   <p style = "color:#009900; font-size:50px;
                font-style:italic; text-align:center;">
            PBP
    </p>
` 

Kekurangan dari inline CSS ini adalah apabila ada banyak elemen yang membutuhkan custom styling juga, maka akan banyak pekerjaan untuk style mereka masing-masing. 

Kelebihan dari inline CSS adalah kemudahan bagi developer untuk melihat informasi mengenai styling pada element tersebut. Menurut saya, styling CSS inline merupakan styling favorit saya apbila menggunakan framework seperti Tailwind CSS. 

Internal CSS adalah CSS yang dilakukan pada bagian `<head> </head>` di suatu file HTML kita. Internal CSS ini dilakukan apabila kita memiliki document HTML yang harus di style secara unik. Contoh:

`<head>
        <title>Internal CSS</title>
        <style>
            .main {
                text-align:center; 
            }
            .class1{
                color:#009900;
                font-size:50px;
                font-weight:bold;
            }
            .class2 {
                font-style:bold;
                font-size:20px;
            }
        </style>
    </head> `

Kekurangan dari cara Internal CSS adalah ketidakbisaan untuk menggunakan styling elemen yang sama dalam 2 dokumen HTML yang berbeda.

Kelebihannya dari cara Internal CSS adalah ketidakperluan membentuk file CSS baru yang dapat membingungkan developer sehingga dapat memudahkan untuk melihat masing-masing atribute class/id.

External CSS adalah CSS yang berada diluar dokumen, sehingga membuat dokumen baru menggunakan .css extension. Contohnya adalah pada folder static/style.css pada project django kita ini. 

Kekurangan menggunakan cara External CSS adalah apabila kita bekerja pada produksi start-up/bisnis yang besar maka akan sulit untuk mengubah styling baru tanpa menambahkan class yang membuat kode menjadi tidak elegan. Banyak developer biasanya bingung untuk mencari class attribute dari suatu elemen di HTML karena external CSS dapat diletakkan sebebasnya.

Kelebihan menggunakan cara External CSS adalah teknik CSS yang paling umum digunakan dan paling mudah untuk diimplementasikan.

CC: Geeks for geeks

#### 2. Jelaskan tag HTML5 yang kamu ketahui. <br>

Tag `<!DOCTYPE html>` merupakan identifikasi bagi browser agar browser bisa dapat menentukan cara untuk merender dokumen tertentu (HTML)

Tag `<html> </html>` merupakan root sebuah browser pada website yang menerapkan HTML. 

Tag `<head> </head>` merupakan tag yang berguna untuk memberikan informasi kepada dokumen HTML seperti CSS yang digunakan, judul dokumen, dll.

Tag `<body> </body>` adalah tag yang bertugas untuk memberikan informasi kepada browser bahwa dibawah tag ini adalah isi dari HTML

Tag `<a> </a>` adalah tag untuk melakukan refer kepada link melewati tulisan

Tag `<p> </p>` adalah tag yang berfungsi untuk membuat paragraf

Tag `<button> </button>` untuk membuat button

Tag `<div> </div>` untuk membuat sebuah pembagian elemen 

Tag `<form> </form>` untuk membuat form

Tentunya masih banyak lagi seperti `<table> </table>`, dll. Namun semua tag tentunya mempunyai fungsi, dan setiap fungsi tersebut sangat berguna

#### 3. Jelaskan tipe-tipe CSS selector yang kamu ketahui <br>
`:hover`: apabila mouse hover kepada elemen tersebut kita maka akan nyala

`:active`: apabila ditoggle maka elemen tersebut dinyatakan active

`:disabled` apabila terjadi maka elemen di disabled.

`#id` Untuk memberikan identifikasi setiap elemen (harus unik)

`.class` untuk memberikan class name pada setiap elemen, biasanya untuk melakukan operasi pada elemen tersebut baik itu styling, dll. 

`*` untuk menselect semua elemen yang ada pada isi. 

#### 3. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas. <br>

Saya awal-awal mengubah `base.html` pada directory `template` saya agar bisa menerima bootstrap. Lalu saya mengubah desain login, register, dan create-task dari menggunakan table menjadi menggunakan div. Hal ini saya lakukan karena div merupakan HTML tag yang menurut saya lebih fleksibel dan mudah untuk menggunakannya. Saya menambahkan beberapa CSS yang penting untuk menambah estetika dari template saya. Lalu saya mengubah `todolist.html` untuk membuat card. Saya menggunakan `flex` pada for loop tersebut dan `flex-wrap` agar apabila suatu elemen sudah lebih besar pada suatu baris, maka elemen tersebut dapat langsung pindah ke baris berikutnya. Penjelasan mengenai hal yang saya lakukan pada checklist diatas tidak lah banyak karena hal-hal yang saya lakukan hanyalah mengubah `table` menjadi `div` dan `tr` menjadi `p`. Untuk bonus saya hanya menambahkan selector `:hover` untuk menambah scale dari card saya. 