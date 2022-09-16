# Tugas 3

## Link to 👉 [Heroku](https://pbp-tugas2-alvaro.herokuapp.com/) 👈

### Soal

#### 1. Jelaskan perbedaan antara JSON, XML, dan HTML! <br>
JSON merupakan suatu format data yang berfungsi untuk menyimpan, membaca, serta menukar informasi dari web server agar mudah untuk dibaca oleh para pengguna. JSON memiliki 2 struktur yaitu value yang saling berpasangan (object) dan value yang saling berurutan (arra). XML (eXtensible Markup Language) sendiri adalah bahasa markup yang berfungsi untuk menyederhanakan proses penyimpanan dan pengiriman data antar sever. HTML sendiri adalah bahasa standar pemrograman yang digunakan untuk mneampilkan data. 

Perbedaan JSON, XML dengan HTML adalah kegunaannya, HTML sendiri tidak digunakan untuk menyimpan data, melainkan sekedar untuk menampilkan data kepada user. Oleh karena itu saya akan lebih membahas mengenai JSON dan XML, seperti:
1. Elemen
- JSON: menyimpan elemen secara efisien namun kurang rapih (apabila tanpa extension/plug-in).
- XML: menyimpan elemen secara rapi namun kurang efisien

2. Ekstensi
- JSON: ekstensinya berupa JSON
- XML: ekstensinya berupa XML

3. Penerapan
- JSON: pengiriman data dengan cara penguraian dan dikirimkan melalui internet
- XML: pengiriman data seperti menambahkan catatan. 

#### 2. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform? <br>

Data delivery ini dapat pembantu web platform atau mobile platform untuk mendapatkan data yang mereka perlukan. Contoh apabila kita menggunakan web framework dan kita dapat mengambil/fetch data melalui link yang sudah kita buat. Data tersebut adalah hasil dari data delivery yang kita kirimkan, seperti JSON, XML, HTML, dll. Tentunya data delivery yang paling mudah untuk kita gunakan adalah JSON, karena bentuknya yang simple dan efisien. Data-data hasil delivery ini akan memperlengkap website kita. 

#### 3. Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 3 di atas.

Awal awal saya menggunakan perintah `python manage.py startapp mywatchlist`. Hal ini digunakan agar saya bisa menambahkan app bernama mywatchlist. Lalu saya menambahkan `urls.py` di folder **mywatchlist** untuk dapat saya link dengan `urls.py` di folder **project_django**. Saya juga tambahkan fixtures dan template agar dapat memasukkan JSON dan template HTML. Dalam kedua file tersebut saya masukkan data-data yang diperlukan. Untuk file JSON saya gunakan models sebagai referensi data yang saya butuhkan (pada fields). 

Setelah saya membuat models dan data JSON, saya membuat views.py berdasarkan models yang saya punya. Saya memanggil `MyWatchList` (model) untuk mendapatkan seluruh data yang ada lalu akan saya render pada HTML. Untuk HTML sendiri, saya menggunakan template seperti tugas dan lab/tutorial minggu lalu. Lalu saya lakukan `python manage.py makemigrations` dam `python manage.py migrate` untuk mengupdate model agar server tau. Setelah itu saya lakukan perintah `python manage.py loaddata initial_mywatchlist_data.json` untuk mengakses data JSON yang telah saya buat. 

Untuk views, saya lakukan hal yang sama dengan tutorial minggu lalu untuk menambahkan XML dan JSON. Untuk itu, saya tinggal menghubungkan fungsi yang telah saya buat kepada URL. Lalu tinggal saya lakukan `python maange.py runserver 8000` untuk cek apakah sudah benar atau belum. 

### Screenshot Postman
<img width="970" alt="Postman_HTML" src="https://user-images.githubusercontent.com/91789098/190676324-5b774c17-d067-4fba-8981-2130309260e0.png">
<img width="965" alt="Postman_JSON" src="https://user-images.githubusercontent.com/91789098/190676335-773337a8-37ba-498b-8e84-8363685a8cc7.png">
<img width="969" alt="Postman_XML" src="https://user-images.githubusercontent.com/91789098/190676336-633ad7f8-5e75-4ed7-a2fb-b17bfe1fbd73.png">
