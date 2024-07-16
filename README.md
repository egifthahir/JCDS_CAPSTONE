# JCDS_CAPSTONE
Submit Capstone JCDS

	CAPSTONE 1/JCDS-2504-002/MUHAMMAD ABIZAR ALGIFFARY THAHIR

	Sistem Manajemen Pasien Rumah Sakit Darurat PMI

- Deskripsi -

	Sistem Manajemen Pasien adalah aplikasi sederhana yang dirancang menggunakan tampilan baris perintah atau Command-Line Interface(CLI) untuk mengelola data pasien di lingkungan perawatan kesehatan. Aplikasi ini memungkinkan pengguna untuk membuat, membaca, memperbaharui, dan menghapus rekam data pasien dengan efisien.

- Fitur -
- Create: Membuat rekam data pasien baru. 
- Read: Menampilkan rekam data pasien.
- Update: Memperbaharui rekam data pasien.
- Delete: Menghapus rekam data pasien dari sistem.

- Cakupan Data -

Setiap rekam data pasien mencakup beberapa data, sebagai berikut:

 - NRM; Nomor Rekam Medis: Nomor unik registrasi pasien.
 - NAMA: Nama lengkap pasien.
 - TANGGAL_LAHIR: Tanggal lahir pasien (format: DD-MM-YYYY).
 - USIA: Usia pasien dalam tahun.
 - KELAMIN: jenis kelamin pasien (PRIA/WANITA).
 - DIAGNOSIS: Hasil pemeriksaan gejala pasien.
 - ADMISI: Tanggal pasien mulai diopname (format: DD-MM-YYYY).

- Validasi Input Data -

Aplikasi ini memiliki validasi input data yang mencakup berbagai hal guna menjaga integritas data:

 - NRM: Harus unik untuk setiap pasien. 
 - TANGGAL_LAHIR dan ADMISI: harus dalam format DD-MM-YYYY. Menggunakan Kaidah Kalender Kabisat
			     dan jumlah hari pada setiap bulan divalidasi.  
 - KELAMIN: Harus "PRIA" atau "WANITA".
 - DIAGNOSIS: Harus hanya mengandung karakter alphabet.
 - USIA: Menggunakan perhitungan langsung menggunakan TANGGAL_LAHIR dan ADMISI.
	 Jika USIA menghasilkan ERROR maka data pasien tidak dapat disimpan.
 - CHECK: Harus memasukkan "YA" atau "TIDAK".

- Contoh -

	TAMBAHKAN DATA PASIEN BARU
	NRM: 1401
	NAMA: Joko Widodo
	TANGGAL LAHIR (DD-MM-YYYY): 21-06-1961
	KELAMIN (PRIA/WANITA): PRIA
	DIAGNOSA: FLU
	ADMISI (DD-MM-YYYY): 15-07-2024

- Kontak -

Untuk menyampaikan pertanyaan atau saran, dapat melayangkan email ke egifthahir@gmail.com 
