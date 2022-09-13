# Tugas 2 

## Link to [Heroku](https://pbp-tugas2-alvaro.herokuapp.com/)

### Soal

#### 1. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html! <br>

Hubungan `urls.py` dengan `views.py` adalah hubungan passing. Hal yang di passing merupakan HTTP Request yang user inginkan agar `views.py` dapat memberikan respon yang tepat. Contohnya, apabila user menginginkan untuk **GET** data dari suatu URL yang dibuat dan dihubungkan dengan suatu fungsi/class di `views.py` maka itulah hubungan passing yang dilakukan. Sehingga `views.py` dan `urls.py` saling membutuhkan satu sama lain agar bisa saling menyalurkan informasi, sehingga informasi tersebut bisa diperlihatkan kepada user.

`models.py` dan `urls.py` tidak berhubungan secara langsung namun dihubungkan melewati fungsi/class pada `views.py`. Model ini diperlihatkan untuk memberikan data yang ingin dikeluarkan/dimasukkan melewati views. Maksud dikeluarkan/dimasukkan, akan saya berikan contoh. Contoh, apabila user menginginkan untuk **GET**, maka apabila data model dipanggil, models akan memberikan data yang sudah ada kepada views agar kedepannya mungkin akan digunakan itu.

`models.py`, `views.py`, `berkas html` berhubungan dalam rangka untuk merender data. Berkas HTML digunakkan oleh `views.py` untuk mengetahui apa saja yang perlu dikeluarkan. Lalu `models.py` digunakkan `views.py` untuk menentukan data-data yang akan diberikan sebagai context kepada berkas html supaya data tersebut dapat dipakai. Sehingga `views.py` memiliki tugas sebagai penengah/penerus data agar dapat di show melalui `urls.py`. 

Sehingga `views.py` berfungsi untuk memberikan respon (HTTP Response/HTML), `urls.py` digunakkan untuk meneruskan request user kepada `views.py` dan `models.py` digunakkan untuk menulis dan membaca data berdasarkan respon dari `views.py`.

#### 2. Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment? <br>

Virtual environment digunakan pada Django digunakan untuk mengeksekusi aplikasi Django. Virtual Environment ini digunakan untuk memisahkan environment Django dengan environment yang kita gunakan. Virtual environment membantu kita agar mempunyai environment yang stabil dan portable, kita bisa mengontrol versi package-package yang kita inginkan. Dengan begini, apabila kita memiliki banyak project Django, maka requirementnya tidak akan mempengaruhi package secara global.  

Tentu saja kita masih bisa membuat aplikasi web berbasis Django tanpa menggunakan virtual environment. Namun itu artinya kita akan memutuskan untuk overwrite global package kita dengan package pada project requirement kita. Hal ini tidaklah di rekomendasi karena apabila kita ingin melakukan development beberapa project maka kita dapat bertemu dengan yang namanya dependency error yang disebabkan karena conflict package pada system.  

### 3. Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas. <br>

Untuk mengimplementasikan poin 1-4 diatas, saya menggunakan beberapa cara yang pernah dilakukan pada lab 1. Saya membuat fungsi pada views.py bernama `show_katalog`. Pada file views.py tersebut saya merender file html pada `katalog.html`. 

Lalu saya membuat routing pada `urls.py` di folder katalog . Namun sebelum itu saya tambahkan routing pada main url di `project_django` agar `urls.py` di folder katalog dapat diakses. 

Setelah itu saya lakukan banyak hal yang sama seperti yang saya lakukan pada Lab 1. Saya melakukan "makemigrations", "migrate", dan "loaddata" untuk menginisialisasi model dan memasukkan nilai pada model yang disediakan. Setelah itu, saya hanya perlu untuk mengubah bagian di `katalog.html` agar dapat dinamis sesuai dengan data pada `initial_catalog_data.json`.

Setelah selesai, saya mengecek apakah sudah betul, apabila sudah saya lalu tambahkan, commit, dan push ke reporsitori milik saya. Saya memasukkan secret heroku saya pada reporsitory saya baik app name dan API_Key. Lalu saya menunggu sampai digithub berhasil terdeploy. Saat berhasil di deploy saya hanya perlu untuk memastikan bahwa server django yang saya buat berhasil. 
