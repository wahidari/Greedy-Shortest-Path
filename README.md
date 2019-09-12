# Penentuan Jalur Terpendek Dengan Algoritma Greedy

[![](https://gitlab.com/gitlab-org/gitlab-ee/badges/master/build.svg)](https://wahidari.github.io)
[![](https://semaphoreci.com/api/v1/projects/2f1a5809-418b-4cc2-a1f4-819607579fe7/400484/shields_badge.svg)](https://wahidari.github.io)
[![](https://img.shields.io/badge/docs-latest-brightgreen.svg?style=flat&maxAge=86400)](https://wahidari.github.io)
[![](https://img.shields.io/badge/Find%20Me-%40wahidari-009688.svg?style=social)](https://wahidari.github.io)

## Language

- [![](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/) 

## Tools

- [![Other](https://img.shields.io/badge/spyder-3-red.svg)](https://www.spyder-ide.org/)

## Test coverage

- [![](https://gitlab.com/gnutls/gnutls/badges/master/coverage.svg)](https://wahidari.github.io) python

## Documentation

- Salah satu contoh dari penyelesaian masalah dengan algoritma greedy yaitu mencari jarak terpendek dari peta

    Misalkan kita ingin bergerak dari titik A ke titik I, dan kita telah menemukan beberapa jalur dari peta:

    ![](./ss/a.png)
    
    Dari peta yang ditampilkan di atas, dapat dilihat bahwa terdapat beberapa jalur dari titik A ke titik I. 
    Sistem peta pada gambar secara otomatis telah memilih jalur terpendek (berwarna biru). 
    Kita akan mencoba mencari jalur terpendek juga, dengan menggunakan algoritma greedy.

- Graph Sederhana dari Titik A ke I

    ![](./ss/b.png)
    
    Dari gambar di atas, kita dapat melihat bagaimana sebuah peta jalur perjalanan dapat direpresentasikan dengan 
    menggunakan graph, spesifiknya Directed Graph (graph berarah). Maka dari itu, untuk menyelesaikan permasalahan 
    jarak terpendek ini kita akan menggunakan struktur data graph untuk merepresentasikan peta. 
    Berikut adalah graph yang akan digunakan:

- Graph Berarah dari Titik A ke I

    ![](./ss/c.png)
    
- Graph Berarah Beserta Jarak Masing-Masing Titik dari Titik A ke I

    ![](./ss/d.png)
    
    Untuk mencari jarak terpendek dari A ke B, sebuah algoritma greedy akan menjalankan langkah-langkah seperti berikut:
    
    
    a. Kunjungi satu titik pada graph, dan ambil seluruh titik yang dapat dikunjungi dari titik sekarang.
    
    
    b. Cari local maximum ke titik selanjutnya.
    
    
    c. Tandai graph sekarang sebagai graph yang telah dikunjungi, dan pindah ke local maximum yang telah ditentukan.
    
    
    d. Kembali ke langkah 1 sampai titik tujuan didapatkan.
    
- ScreenShot 5

    ![](./ss/e.png)
    
    Dengan menggunakan algoritma greedy pada graph di atas, hasil akhir yang akan didapatkan sebagai jarak terpendek adalah A-C-D-G-I. 
    Hasi jarak terpendek yang didapatkan ini tidak tepat dengan jarak terpendek yang sebenarnya (A-B-H-I). 
    Algoritma greedy memang tidak selamanya memberikan solusi yang optimal, dikarenakan pencarian local maximum pada setiap langkahnya, 
    tanpa memperhatikan solusi secara keseluruhan.
- ScreenShot 6

    ![](./ss/f.png)

- ScreenShot 7

    ![](./ss/g.png)
    

## License
> This program is Free Software: 
You can use, study, share and improve it at your will. 
Specifically you can redistribute and/or modify it under the terms of the [GNU General Public License](https://www.gnu.org/licenses/gpl.html) 
as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
