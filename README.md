# Water_System
Sistem pengairan otomatis menggunakan komponen elektronika sederhana berdasarkan deteksi lokasi objek.

Dibuat oleh tim Mekatronika dan Kecerdasan Buatan 2021 UPI Purwakarta

- Aisyah Aira Putri Maharani - aisyahairaputrim@upi.edu
- Tri Seda Mulya - trisedamulya929@gmail.com

## Daftar Isi
1. Latar Belakang
2. Demo
3. Metode dan Hasil

## Latar Belakang
Air merupakan unsur kritis dalam keberlanjutan kehidupan, terutama dalam konteks pertanian dan penjagaan lingkungan. Sistem pengairan adalah solusi yang dirancang secara khusus untuk mendistribusikan air secara teratur dan efisien ke area tertentu, dengan tujuan meningkatkan produktivitas pertanian, keberlanjutan lingkungan, dan kenyamanan urban. Dalam berbagai konteks, sistem pengairan telah menjadi pilar dalam mengatasi tantangan terkait manajemen air di berbagai daerah di seluruh dunia.

Oleh karena itu, projek ini ditujukan untuk membentuk sebuah sistem pengairan yang cerdas. Sistem ini menggunakan komponen elektronika sederhana dengan arduino sebagai mikrokontroler utamanya. Sistem ini juga berkerja berdasarkan lokasi mana yang terdeteksi oleh objek yang telah dirancang sebelumnya sehingga akan menghasilkan output yang berbeda-beda. 

## Demo 
Komponen yang digunakan pada projek ini adalah:
- Arduino Uno
- Kabel Jumper
- Motor DC
- L298N
- Relay
- Motor Servo
- Adaptor
- Project Board
- Selang Air
- Pompa

Bahan pendukung: 
- Cutter
- Kabel
- Lakban
- SOlder
- Air
- Wadah Air

Berikut cuplikan sisten:
![WhatsApp Image 2024-01-30 at 11 15 13_6bfce799](https://github.com/aisyaaaptr/Water_System/assets/157786477/50e24a4d-a183-4382-9dc4-dfe5247462a2)

Video demo alat dapat dilihat disini: https://youtu.be/V1T_ewJL2a0?si=3TsD0SAaZLc5SRSf  

## Metode dan Hasil 
Sistem ini dioperasikan berdasarkan lokasi mana yang terdeteksi oleh objek berwarna hijau dengan kode warna: 
- Hmin = 42
- Hmax = 88
- Smin = 62
- Smax = 255
- Vmin = 45
- Vmax = 150

Macam-macam lokasi dan output yang dihasilkan:
- Posisi A: Menyalakan Pompa Air
- Posisi B: Mematikan Pompa Air
- Posisi C: Menyalakan Motor 1
- Posisi D&E: Menyalakan Motor 2
- Posisi F, G , H, dan J: Mengubah Sudut Servo 

Dalam proses pelaksanaan pengujian alat, terdapat beberapa kendala kecil seperti komponen yang tidak berfungsi dengan baik. Namun, semua dapat teratasi dengan baik. 
