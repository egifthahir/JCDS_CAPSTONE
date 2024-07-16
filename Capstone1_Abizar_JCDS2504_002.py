# import module untuk menggunakan tabel dan perhitungan
from tabulate import tabulate

# data pasien opname 
data_pasien = [
    {'NRM': '1191', 'NAMA': 'ALBERT LAMBOK', 'TANGGAL_LAHIR': '23-01-1951', 'USIA': 73, 'KELAMIN': 'PRIA', 'DIAGNOSIS': 'BRONCHITIS', 'ADMISI': '25-12-2023'},
    {'NRM': '1282', 'NAMA': 'SYAHRUL REZA', 'TANGGAL_LAHIR': '29-03-1943', 'USIA': 81, 'KELAMIN': 'PRIA', 'DIAGNOSIS': 'PANCREATITIS', 'ADMISI': '13-01-2024'},
    {'NRM': '1373', 'NAMA': 'ADITYA WIBOWO', 'TANGGAL_LAHIR': '04-04-1978', 'USIA': 46, 'KELAMIN': 'PRIA', 'DIAGNOSIS': 'HEPATITIS', 'ADMISI': '21-03-2024'},
    {'NRM': '1564', 'NAMA': 'KARINA SHAFIRA', 'TANGGAL_LAHIR': '02-07-1982', 'USIA': 41, 'KELAMIN': 'WANITA', 'DIAGNOSIS': 'GASTRITIS', 'ADMISI': '24-05-2024'},
    {'NRM': '1755', 'NAMA': 'WINDA LYDIA', 'TANGGAL_LAHIR': '18-07-1961', 'USIA': 62, 'KELAMIN': 'WANITA', 'DIAGNOSIS': 'APPENDICITIS', 'ADMISI': '10-07-2024'}
]

# fungsi menghitung usia menggunakkan tanggal_lahir dan admisi
def hitung_usia(tanggal_lahir, admisi):
    hari_lahir = int(tanggal_lahir[0:2])
    bulan_lahir = int(tanggal_lahir[3:5])
    tahun_lahir = int(tanggal_lahir[6:10])
    
    hari_admisi = int(admisi[0:2])
    bulan_admisi = int(admisi[3:5])
    tahun_admisi = int(admisi[6:10])

    # perhitungan selisih masing-masing komponen 
    selisih_tahun = tahun_admisi - tahun_lahir
    selisih_bulan = (bulan_admisi - bulan_lahir) / 12
    selisih_hari = (hari_admisi - hari_lahir) / 365.25

    admisi = (tahun_admisi, bulan_admisi, hari_admisi)
    tanggal_lahir = (tahun_lahir, bulan_lahir, hari_lahir)

    # conditional usia jika admisi lebih awal daripada tanggal lahir; jadikan 'ERROR'.
    if admisi < tanggal_lahir:
        return 'ERROR'
    
    # perhitungan usia membulatkan ke atas
    usia =round(selisih_tahun + selisih_bulan + selisih_hari)
    return usia

# fungsi untuk menambahkan data pasien baru
def create_data():
    print('\n\tTAMBAHKAN DATA PASIEN BARU')
    nrm = input('\n\tDAFTARKAN NOMOR REKAM MEDIS  (NRM 4 DIGIT) BARU: ')
    while not (nrm.isdigit() and len(nrm) == 4): # loop untuk memastikan input hanya menerima 4 digit angka
        print('\n\tERROR: MASUKKAN NRM (4 DIGIT)')
        nrm = input('\n\tNRM: ')
    if any(pasien['NRM'] == nrm for pasien in data_pasien): # conditional untuk memastikan primary key bukan duplikat
        print('\n\tERROR: NRM SUDAH TERDAFTAR. SILAHKAN MASUKKAN DATA YANG BENAR.')
        return
    
    # input data baru pasien 
    # input nama
    nama_depan = input('\n\tNAMA DEPAN: ')
    while not (nama_depan.isalpha()): # loop untuk memastikan input hanya menggunakan huruf
        print('\n\tERROR: ANDA MEMASUKKAN BUKAN HURUF' )
        nama_depan = input('\n\tNAMA DEPAN: ')
    
    nama_belakang = input('\n\tNAMA BELAKANG: ')
    while not (nama_belakang.isalpha()): # loop untuk memastikan input hanya menggunakan huruf
        print('\n\tERROR: ANDA MEMASUKKAN BUKAN HURUF' )
        nama_belakang = input('\n\tNAMA BELAKANG: ')

    nama = f'{nama_depan} {nama_belakang}'.upper()# format untuk menggabungkan nama depan dan belakang
        
    #input tanggal lahir
    tahun_lahir = (input('\n\tTAHUN LAHIR 4 DIGIT (CONTOH: 1993): '))
    while not(tahun_lahir.isdigit() # loop untuk memastikan input sesuai set condition
            and len(tahun_lahir) == 4
            and 1900 <= int(tahun_lahir) <= 2024):        
        print('\n\tERROR. SILAHKAN MASUKKAN DATA YANG BENAR')
        tahun_lahir = input('\n\tTAHUN LAHIR 4 DIGIT (CONTOH: 1993): ')
    tahun_lahir_int = int(tahun_lahir)    

    bulan_lahir = (input('\n\tBULAN LAHIR 2 DIGIT (01 SAMPAI 12): '))
    while not(bulan_lahir.isdigit() 
            and len(bulan_lahir) == 2
            and 1 <= int(bulan_lahir) <= 12):
        print('\n\tERROR. SILAHKAN MASUKKAN DATA YANG BENAR')
        bulan_lahir = input('\n\tBULAN LAHIR 2 DIGIT (01 SAMPAI 12): ')
    bulan_lahir_int = int(bulan_lahir)
    
    # input untuk bulan februari sesuai kaidah kalender kabisat   
    if bulan_lahir_int == 2:
        if ((tahun_lahir_int % 4 == 0) and (tahun_lahir_int % 100 != 0) or (tahun_lahir_int % 400 == 0)):          
            hari_lahir = input('\n\tTANGGAL LAHIR 2 DIGIT (01 SAMPAI 29): ')
            while not(hari_lahir.isdigit() 
                    and len(hari_lahir) == 2
                    and 1 <= int(hari_lahir) <= 29):
                print('\n\tERROR. SILAHKAN MASUKKAN DATA YANG BENAR')
                hari_lahir = input('\n\tTANGGAL LAHIR 2 DIGIT (01 SAMPAI 29): ')
        else:   
            hari_lahir = input('\n\tTANGGAL LAHIR 2 DIGIT (01 SAMPAI 28): ')
            while not(hari_lahir.isdigit() 
                    and len(hari_lahir) == 2
                    and 1 <= int(hari_lahir) <= 28):
                print('\n\tERROR. SILAHKAN MASUKKAN DATA YANG BENAR')
                hari_lahir = input('\n\tTANGGAL LAHIR 2 DIGIT (01 SAMPAI 28): ')

    #input untuk bulan 30 hari
    elif bulan_lahir_int in [4,6,9,11]:
        hari_lahir = input('\n\tTANGGAL LAHIR 2 DIGIT (01 SAMPAI 30): ')
        while not(hari_lahir.isdigit() 
                and len(hari_lahir) == 2
                and 1 <= int(hari_lahir) <= 30):
            print('\n\tERROR. SILAHKAN MASUKKAN DATA YANG BENAR')
            hari_lahir = input('\n\tTANGGAL LAHIR 2 DIGIT (01 SAMPAI 30): ')

    # input untuk bulan 31 hari
    else:
        hari_lahir = input('\n\tTANGGAL LAHIR 2 DIGIT (01 SAMPAI 31): ')
        while not(hari_lahir.isdigit() 
                and len(hari_lahir) == 2
                and 1 <= int(hari_lahir) <= 31):
            print('\n\tERROR. SILAHKAN MASUKKAN DATA YANG BENAR')
            hari_lahir = input('\n\tTANGGAL LAHIR 2 DIGIT (01 SAMPAI 31): ')

    tanggal_lahir = f'{hari_lahir}-{bulan_lahir}-{tahun_lahir}' # fromat DD-MM-YYYY

    # input jenis kelamin pasien
    kelamin = input('\n\tKELAMIN (PRIA/WANITA): ')
    while kelamin.upper() not in ['PRIA', 'WANITA']: # loop untuk memastikan kelamin hanya di input sesuai pilihan
        print('\n\tERROR: KELAMIN HARUS "PRIA" ATAU "WANITA"')
        kelamin = input('\n\tKELAMIN (PRIA/WANITA): ')
    kelamin = kelamin.upper()

    # input diagnosis penyakit pasien
    diagnosis = input('\n\tDIAGNOSIS: ')
    while not (diagnosis.isalpha()): # loop untuk memastikan inputan hanya huruf
        print('\n\tERROR: ANDA MEMASUKKAN BUKAN HURUF')
        diagnosis = input('\n\tDIAGNOSIS: ')
    diagnosis = diagnosis.upper()

    # input tanggal admisi pasien
    admisi_tahun = input('\n\tTAHUN ADMISI 4 DIGIT (CONTOH: 1993): ')
    while not(admisi_tahun.isdigit() 
            and len(admisi_tahun) == 4
            and int(admisi_tahun) <= 2024):
        print('\n\tERROR. SILAHKAN MASUKKAN DATA YANG BENAR')
        admisi_tahun = input('\n\tTAHUN ADMISI 4 DIGIT (CONTOH: 1993): ')
    admisi_tahun_int = int(admisi_tahun)

    admisi_bulan = input('\n\tBULAN ADMISI 2 DIGIT (01 SAMPAI 12): ')
    while not(admisi_bulan.isdigit() 
            and len(admisi_bulan) == 2 
            and 1 <= int(admisi_bulan) <= 12):
        print('\n\tERROR. SILAHKAN MASUKKAN DATA YANG BENAR')
        admisi_bulan = input('\n\tBULAN ADMISI 2 DIGIT (01 SAMPAI 12): ')
    admisi_bulan_int = int(admisi_bulan)

    # input untuk bulan februari sesuai kaidah kalender kabisat
    if admisi_bulan_int == 2:
        if ((admisi_tahun_int % 4 == 0) and (admisi_tahun_int % 100 != 0) or (admisi_tahun_int % 400 == 0)):
            admisi_hari = input('\n\tTANGGAL ADMISI 2 DIGIT (01 SAMPAI 29): ')
            while not(admisi_hari.isdigit() 
                    and len(admisi_hari) == 2 
                    and 1 <= int(admisi_hari) <= 29): 
                print('\n\tERROR. SILAHKAN MASUKKAN DATA YANG BENAR')
                admisi_hari = input('\n\tTANGGAL ADMISI 2 DIGIT (01 SAMPAI 29): ')
        else:
            admisi_hari = input('\n\tTANGGAL ADMISI 2 DIGIT (01 SAMPAI 28): ')
            while not(admisi_hari.isdigit() 
                    and len(admisi_hari) == 2 
                    and 1 <= int(admisi_hari) <= 28): 
                print('\n\tERROR. SILAHKAN MASUKKAN DATA YANG BENAR')
                admisi_hari = input('\n\tTANGGAL ADMISI 2 DIGIT (01 SAMPAI 28): ')

    # input untuk bulan 30 hari
    elif admisi_bulan_int in [4,6,9,11]:
        admisi_hari = input('\n\tTANGGAL ADMISI 2 DIGIT (01 SAMPAI 30): ')
        while not(admisi_hari.isdigit()
                and len(admisi_hari) == 2
                and 1 <= int(admisi_hari) <= 30):
            print('\n\tERROR. SILAHKAN MASUKKAN DATA YANG BENAR')
            admisi_hari = input('\n\tTANGGAL ADMISI 2 DIGIT (01 SAMPAI 30): ')

    # input untuk bulan 31 hari
    else:
        admisi_hari = input('\n\tTANGGAL ADMISI 2 DIGIT (01 SAMPAI 31): ')
        while not(admisi_hari.isdigit()
                and len(admisi_hari) == 2
                and 1 <= int(admisi_hari) <= 31):
            print('\n\tERROR. SILAHKAN MASUKKAN DATA YANG BENAR')
            admisi_hari = input('\n\tTANGGAL ADMISI 2 DIGIT (01 SAMPAI 31): ')

    admisi = f'{admisi_hari}-{admisi_bulan}-{admisi_tahun}'
    
    # perhitungan usia pasien
    usia = hitung_usia(tanggal_lahir,admisi)
    while usia == 'ERROR': # loop untuk memasukkan kembali tanggal lahir dan admisi jika conditional usia memberikan 'ERROR' 
        print('\n\tERROR: TANGGAL LAHIR HARUS SEBELUM TANGGAL ADMISI. SILAHKAN MASUKKAN ULANG.')

        # input ulang tanggal lahir
        tahun_lahir = (input('\n\tTAHUN LAHIR 4 DIGIT (CONTOH: 1993): '))
        while not(tahun_lahir.isdigit() 
                and len(tahun_lahir) == 4
                and 1900 <= int(tahun_lahir) <= 2024):        
            print('\n\tERROR. SILAHKAN MASUKKAN DATA YANG BENAR')
            tahun_lahir = input('\n\tTAHUN LAHIR 4 DIGIT (CONTOH: 1993): ')
        tahun_lahir_int = int(tahun_lahir)    

        bulan_lahir = (input('\n\tBULAN LAHIR 2 DIGIT (01 SAMPAI 12): '))
        while not(bulan_lahir.isdigit() 
                and len(bulan_lahir) == 2
                and 1 <= int(bulan_lahir) <= 12):
            print('\n\tERROR. SILAHKAN MASUKKAN DATA YANG BENAR')
            bulan_lahir = input('\n\tBULAN LAHIR 2 DIGIT (01 SAMPAI 12): ')
        bulan_lahir_int = int(bulan_lahir)
        
        # input untuk bulan februari sesuai kaidah kalender kabisat
        if bulan_lahir_int == 2:
            if ((tahun_lahir_int % 4 == 0) and (tahun_lahir_int % 100 != 0) or (tahun_lahir_int % 400 == 0)):          
                hari_lahir = input('\n\tTANGGAL LAHIR 2 DIGIT (01 SAMPAI 29): ')
                while not(hari_lahir.isdigit() 
                        and len(hari_lahir) == 2
                        and 1 <= int(hari_lahir) <= 29):
                    print('\n\tERROR. SILAHKAN MASUKKAN DATA YANG BENAR')
                    hari_lahir = input('\n\tTANGGAL LAHIR 2 DIGIT (01 SAMPAI 29): ')
            else:   
                hari_lahir = input('\n\tTANGGAL LAHIR 2 DIGIT (01 SAMPAI 28): ')
                while not(hari_lahir.isdigit() 
                        and len(hari_lahir) == 2
                        and 1 <= int(hari_lahir) <= 28):
                    print('\n\tERROR. SILAHKAN MASUKKAN DATA YANG BENAR')
                    hari_lahir = input('\n\tTANGGAL LAHIR 2 DIGIT (01 SAMPAI 28): ')

        #input untuk bulan 30 hari
        elif bulan_lahir_int in [4,6,9,11]:
            hari_lahir = input('\n\tTANGGAL LAHIR 2 DIGIT (01 SAMPAI 30): ')
            while not(hari_lahir.isdigit() 
                    and len(hari_lahir) == 2
                    and 1 <= int(hari_lahir) <= 30):
                print('\n\tERROR. SILAHKAN MASUKKAN DATA YANG BENAR')
                hari_lahir = input('\n\tTANGGAL LAHIR 2 DIGIT (01 SAMPAI 30): ')

        # input untuk bulan 31 hari
        else:
            hari_lahir = input('\n\tTANGGAL LAHIR 2 DIGIT (01 SAMPAI 31): ')
            while not(hari_lahir.isdigit() 
                    and len(hari_lahir) == 2
                    and 1 <= int(hari_lahir) <= 31):
                print('\n\tERROR. SILAHKAN MASUKKAN DATA YANG BENAR')
                hari_lahir = input('\n\tTANGGAL LAHIR 2 DIGIT (01 SAMPAI 31): ')

            tanggal_lahir = f'{hari_lahir}-{bulan_lahir}-{tahun_lahir}' # format DD-MM-YYYY

            # input ulang admisi
            admisi_tahun = input('\n\tTAHUN ADMISI 4 DIGIT (CONTOH: 1993): ')
            while not(admisi_tahun.isdigit() 
                    and len(admisi_tahun) == 4
                    and int(admisi_tahun) <= 2024):
                print('\n\tERROR. SILAHKAN MASUKKAN DATA YANG BENAR')
                admisi_tahun = input('\n\tTAHUN ADMISI 4 DIGIT (CONTOH: 1993): ')
            admisi_tahun_int = int(admisi_tahun)

            admisi_bulan = input('\n\tBULAN ADMISI 2 DIGIT (01-12): ')
            while not(admisi_bulan.isdigit() 
                    and len(admisi_bulan) == 2 
                    and 1 <= int(admisi_bulan) <= 12):
                print('\n\tERROR. SILAHKAN MASUKKAN DATA YANG BENAR')
                admisi_bulan = input('\n\tBULAN ADMISI 2 DIGIT (01-12): ')
            admisi_bulan_int = int(admisi_bulan)

            # input untuk bulan februari sesuai kaidah kalender kabisat
            if admisi_bulan_int == 2:
                if ((admisi_tahun_int % 4 == 0) and (admisi_tahun_int % 100 != 0) or (admisi_tahun_int % 400 == 0)):
                    admisi_hari = input('\n\tTANGGAL ADMISI 2 DIGIT (01 SAMPAI 29): ')
                    while not(admisi_hari.isdigit() 
                            and len(admisi_hari) == 2 
                            and 1 <= int(admisi_hari) <= 29): 
                        print('\n\tERROR. SILAHKAN MASUKKAN DATA YANG BENAR')
                        admisi_hari = input('\n\tTANGGAL ADMISI 2 DIGIT (01 SAMPAI 29): ')
                else:
                    admisi_hari = input('\n\tTANGGAL ADMISI 2 DIGIT (01 SAMPAI 28): ')
                    while not(admisi_hari.isdigit() 
                            and len(admisi_hari) == 2 
                            and 1 <= int(admisi_hari) <= 28): 
                        print('\n\tERROR. SILAHKAN MASUKKAN DATA YANG BENAR')
                        admisi_hari = input('\n\tTANGGAL ADMISI 2 DIGIT (01 SAMPAI 28): ')

            # input untuk bulan 30 hari
            elif admisi_bulan_int in [4,6,9,11]:
                admisi_hari = input('\n\tTANGGAL ADMISI 2 DIGIT (01 SAMPAI 30): ')
                while not(admisi_hari.isdigit()
                        and len(admisi_hari) == 2
                        and 1 <= int(admisi_hari) <= 30):
                    print('\n\tERROR. SILAHKAN MASUKKAN DATA YANG BENAR')
                    admisi_hari = input('\n\tTANGGAL ADMISI 2 DIGIT (01 SAMPAI 30): ')

            # input untuk bulan 31 hari
            else:
                admisi_hari = input('\n\tTANGGAL ADMISI 2 DIGIT (01 SAMPAI 31): ')
                while not(admisi_hari.isdigit()
                        and len(admisi_hari) == 2
                        and 1 <= int(admisi_hari) <= 31):
                    print('\n\tERROR. SILAHKAN MASUKKAN DATA YANG BENAR')
                    admisi_hari = input('\n\tTANGGAL ADMISI 2 DIGIT (01 SAMPAI 31): ')

        admisi = f'{admisi_hari}-{admisi_bulan}-{admisi_tahun}' # format DD-MM-YYYY

        usia = hitung_usia(tanggal_lahir,admisi) # call function perhitungan usia

    # rekam data pasien baru
    pasien_baru = {
        'NRM': nrm,
        'NAMA': nama,
        'TANGGAL_LAHIR': tanggal_lahir,
        'USIA': usia,
        'KELAMIN': kelamin,
        'DIAGNOSIS': diagnosis,
        'ADMISI': admisi
    }

    print('\n\tKONFIRMASI DATA PASIEN BARU') # tampilan tabel data baru untuk mengkonfirmasi input
    print(tabulate([pasien_baru], headers="keys", tablefmt="double_grid"))

    # konfirmasi apabila data baru ingin disimpan
    konfirmasi = input('\n\tAPAKAH DATA INI INGIN DISIMPAN? (YA/TIDAK): ')
    while konfirmasi.lower() not in ['ya', 'tidak']:
        print('\n\tERROR. SILAHKAN MASUKKAN "YA" ATAU "TIDAK"')
        konfirmasi = input('\n\tAPAKAH DATA INI INGIN DISIMPAN? (YA/TIDAK): ')

    if konfirmasi.lower() == 'ya':
        data_pasien.append(pasien_baru)
        print('\n\tDATA PASIEN TELAH DITAMBAHKAN')
    else:
        print('\n\tDATA PASIEN TIDAK DISIMPAN')

#fungsi menampilkan semua data dalam format tabulate
def read_all_data():
    if not data_pasien:  # conditional false untuk memeriksa ada tidaknya data awal
        print('\n\tERROR. DATA PASIEN BELUM TERSEDIA.')
        return
    
    print('\n\tDATA PASIEN OPNAME RUMAH SAKIT DARURAT PALANG MERAH INDONESIA')
    
    tabel_data = []
    for pasien in data_pasien:
        tabel_data.append([
            pasien['NRM'],
            pasien['NAMA'],
            pasien['TANGGAL_LAHIR'],
            pasien['USIA'],
            pasien['KELAMIN'],
            pasien['DIAGNOSIS'],
            pasien['ADMISI']])
    print(tabulate(tabel_data, headers=['NRM', 'NAMA', 'TANGGAL_LAHIR', 'USIA', 'KELAMIN', 'DIAGNOSIS', 'ADMISI'], tablefmt='double_grid', numalign='right', stralign='left'))
    print('\tSEMUA DATA TELAH DITAMPILKAN')


#fungsi menampilkan data tertentu     
def read_x_data():
    if not data_pasien:  # conditional false untuk memeriksa ada tidaknya data awal
        print('\n\tERROR. DATA PASIEN BELUM TERSEDIA.')
        return

    nrm_input = input('\n\tTAMPILKAN DATA TERTENTU. \n\n\tMASUKKAN NOMOR REKAM MEDIS (NRM 4 DIGIT): ')
    rekam_medis = [no_nrm for no_nrm in data_pasien if no_nrm['NRM'] == nrm_input] # list comprehension untuk mengakses nrm yang sesuai dengan input; jadikan kedalam list baru rekam_medis
    if rekam_medis:
        print(tabulate(rekam_medis, headers="keys", tablefmt="double_grid"))
    else:
        print(f'\n\tERROR. DATA PASIEN BELUM TERSEDIA ATAU INPUT SALAH: {nrm_input}')

# fungsi mengganti data
def update_data():
    while True:
        nrm_input = input('\n\tGANTI DATA BARU. \n\n\tMASUKKAN NOMOR REKAM MEDIS (NRM 4 DIGIT): ')
        rekam_medis = [no_nrm for no_nrm in data_pasien if no_nrm['NRM'] == nrm_input] # mengakses nrm yang sesuai dengan input; jadikan list baru rekam_medis
        if rekam_medis:
            print(f'\n\tDATA PASIEN DITEMUKAN. NOMOR REKAM MEDIS: {nrm_input}')
            print(tabulate(rekam_medis, headers="keys", tablefmt="double_grid"))
            break
        else:
            print(f'\n\tERROR. DATA PASIEN BELUM TERSEDIA ATAU INPUT SALAH: {nrm_input}')
            return

    print(f'\n\tKONFIRMASI DATA PASIEN NOMOR REKAM MEDIS: {nrm_input}') # tampilan tabel data baru untuk mengkonfirmasi input
    
    # konfirmasi apabila data pasien ingin diganti
    konfirmasi = input('\n\tAPAKAH DATA INI INGIN DIGANTI? (YA/TIDAK): ')
    while konfirmasi.lower() not in ['ya', 'tidak']:
        print('\n\tERROR. SILAHKAN MASUKKAN "YA" ATAU "TIDAK"')
        konfirmasi = input('\n\tAPAKAH DATA INI INGIN DIGANTI? (YA/TIDAK): ')

    if konfirmasi.lower() == 'ya':
        pasien_update = rekam_medis[0].copy() # duplikasi rekam medis pasien agar dapat mengalterasi data tanpa menimpa data asli
        while True:
            print('\n \tSILAHKAN PILIH DATA YANG INGIN DIGANTI' )
            print('''
                ╔════╦══════════════════╗
                ║ NO ║ UBAH DATA PASIEN ║
                ╠════╬══════════════════╣
                ║ 1  ║ NAMA             ║
                ║ 2  ║ TANGGAL LAHIR    ║
                ║ 3  ║ KELAMIN          ║
                ║ 4  ║ DIAGNOSIS        ║
                ║ 5  ║ ADMISI           ║  
                ║ 6  ║ BATAL GANTI DATA ║
                ╚════╩══════════════════╝
                ''') # tampilan supersubmenu update
            pilihan_update = input ('\tSILAHKAN MASUKKAN NOMOR MENU UNTUK MELANJUTKAN: ')
            while not ( pilihan_update.isdigit() and 1 <= int(pilihan_update) <= 6 ):
                print ('\n\tERROR. SILAHKAN ULANGI PILIHAN')
                pilihan_update = input ('\n\tSILAHKAN MASUKKAN NOMOR MENU UNTUK MELANJUTKAN: ')

            # ganti nama
            if pilihan_update == '1':
                nama_depan = input('\n\tNAMA DEPAN BARU: ')
                while not (nama_depan.isalpha()): # loop untuk memastikan input hanya menggunakan huruf
                    print('\n\tERROR: ANDA MEMASUKKAN BUKAN HURUF' )
                    nama_depan = input('\n\tNAMA DEPAN BARU: ')
                
                nama_belakang = input('\n\tNAMA BELAKANG BARU: ')
                while not (nama_belakang.isalpha()): # loop untuk memastikan input hanya menggunakan huruf
                    print('\n\tERROR: ANDA MEMASUKKAN BUKAN HURUF' )
                    nama_belakang = input('\n\tNAMA BELAKANG BARU: ')

                pasien_update['NAMA'] = f'{nama_depan} {nama_belakang}'.upper() # format untuk menggabungkan nama depan dan belakang
                
            # ganti tanggal lahir
            elif pilihan_update == '2':
                tahun_lahir = (input('\n\tTAHUN LAHIR 4 DIGIT (CONTOH: 1993): '))
                while not(tahun_lahir.isdigit() 
                        and len(tahun_lahir) == 4
                        and 1900 <= int(tahun_lahir) <= 2024):        
                    print('\n\tERROR. SILAHKAN MASUKKAN DATA YANG BENAR')
                    tahun_lahir = input('\n\tTAHUN LAHIR 4 DIGIT (CONTOH: 1993): ')
                tahun_lahir_int = int(tahun_lahir) # casting str menjadi int agar dapat dimasukkan ke perhitungan   

                bulan_lahir = (input('\n\tBULAN LAHIR 2 DIGIT (01 SAMPAI 12): '))
                while not(bulan_lahir.isdigit() 
                        and len(bulan_lahir) == 2
                        and 1 <= int(bulan_lahir) <= 12):
                    print('\n\tERROR. SILAHKAN MASUKKAN DATA YANG BENAR')
                    bulan_lahir = input('\n\tBULAN LAHIR 2 DIGIT (01 SAMPAI 12): ')
                bulan_lahir_int = int(bulan_lahir) # casting str menjadi int agar dapat dimasukkan ke perhitungan               

                # input untuk bulan february    
                if bulan_lahir_int == 2:
                    if ((tahun_lahir_int % 4 == 0) and (tahun_lahir_int % 100 != 0) or (tahun_lahir_int % 400 == 0)):          
                        hari_lahir = input('\n\tTANGGAL LAHIR 2 DIGIT (01 SAMPAI 29): ')
                        while not(hari_lahir.isdigit() 
                                and len(hari_lahir) == 2
                                and 1 <= int(hari_lahir) <= 29):
                            print('\n\tERROR. SILAHKAN MASUKKAN DATA YANG BENAR')
                            hari_lahir = input('\n\tTANGGAL LAHIR 2 DIGIT (01 SAMPAI 29): ')
                    else:   
                        hari_lahir = input('\n\tTANGGAL LAHIR 2 DIGIT (01 SAMPAI 28): ')
                        while not(hari_lahir.isdigit() 
                                and len(hari_lahir) == 2
                                and 1 <= int(hari_lahir) <= 28):
                            print('\n\tERROR. SILAHKAN MASUKKAN DATA YANG BENAR')
                            hari_lahir = input('\n\tTANGGAL LAHIR 2 DIGIT (01 SAMPAI 28): ')

                #input untuk bulan 30 hari
                elif bulan_lahir_int in [4,6,9,11]:
                    hari_lahir = input('\n\tTANGGAL LAHIR 2 DIGIT (01 SAMPAI 30): ')
                    while not(hari_lahir.isdigit() 
                            and len(hari_lahir) == 2
                            and 1 <= int(hari_lahir) <= 30):
                        print('\n\tERROR. SILAHKAN MASUKKAN DATA YANG BENAR')
                        hari_lahir = input('\n\tTANGGAL LAHIR 2 DIGIT (01 SAMPAI 30): ')

                # input untuk bulan 31 hari
                else:
                    hari_lahir = input('\n\tTANGGAL LAHIR 2 DIGIT (01 SAMPAI 31): ')
                    while not(hari_lahir.isdigit() 
                            and len(hari_lahir) == 2
                            and 1 <= int(hari_lahir) <= 31):
                        print('\n\tERROR. SILAHKAN MASUKKAN DATA YANG BENAR')
                        hari_lahir = input('\n\tTANGGAL LAHIR 2 DIGIT (01 SAMPAI 31): ')

                pasien_update['TANGGAL_LAHIR'] = f'{hari_lahir}-{bulan_lahir}-{tahun_lahir}' # DD-MM-YYYY
                tanggal_lahir = pasien_update['TANGGAL_LAHIR']
                admisi = pasien_update['ADMISI']
                pasien_update['USIA'] = hitung_usia(tanggal_lahir,admisi) # perhitungan usia
                    
            elif pilihan_update == '3':   
                kelamin = input('\n\tKELAMIN (PRIA/WANITA): ')
                while kelamin.upper() not in ['PRIA', 'WANITA']: # loop untuk memastikan kelamin hanya di input sesuai pilihan
                    print('\n\tERROR: KELAMIN HARUS "PRIA" ATAU "WANITA"')
                    kelamin = input('\n\tKELAMIN (PRIA/WANITA): ')
                pasien_update['KELAMIN'] = kelamin.upper()

            elif pilihan_update == '4':
                diagnosis = input('\n\tDIAGNOSIS: ')
                while not (diagnosis.isalpha()): # loop untuk memastikan inputan hanya huruf
                    print('\n\tERROR: ANDA MEMASUKKAN BUKAN HURUF')
                    diagnosis = input('\n\tDIAGNOSIS: ')
                pasien_update['DIAGNOSIS'] = diagnosis.upper()
                
            elif pilihan_update == '5':
                admisi_tahun = input('\n\tTAHUN ADMISI 4 DIGIT (CONTOH: 1993): ')
                while not(admisi_tahun.isdigit() 
                        and len(admisi_tahun) == 4
                        and int(admisi_tahun) <= 2024):
                    print('\n\tERROR. SILAHKAN MASUKKAN DATA YANG BENAR')
                    admisi_tahun = input('\n\tTAHUN ADMISI 4 DIGIT (CONTOH: 1993): ')
                admisi_tahun_int = int(admisi_tahun)

                admisi_bulan = input('\n\tBULAN ADMISI 2 DIGIT (01 SAMPAI 12): ')
                while not(admisi_bulan.isdigit() 
                        and len(admisi_bulan) == 2 
                        and 1 <= int(admisi_bulan) <= 12):
                    print('\n\tERROR. SILAHKAN MASUKKAN DATA YANG BENAR')
                    admisi_bulan = input('\n\tBULAN ADMISI 2 DIGIT (01 SAMPAI 12): ')
                admisi_bulan_int = int(admisi_bulan)

                # untuk bulan february
                if admisi_bulan_int == 2:
                    if ((admisi_tahun_int % 4 == 0) and (admisi_tahun_int % 100 != 0) or (admisi_tahun_int % 400 == 0)):
                        admisi_hari = input('\n\tTANGGAL ADMISI 2 DIGIT (01 SAMPAI 29): ')
                        while not(admisi_hari.isdigit() 
                                and len(admisi_hari) == 2 
                                and 1 <= int(admisi_hari) <= 29): 
                            print('\n\tERROR. SILAHKAN MASUKKAN DATA YANG BENAR')
                            admisi_hari = input('\n\tTANGGAL ADMISI 2 DIGIT (01 SAMPAI 29): ')
                    else:
                        admisi_hari = input('\n\tTANGGAL ADMISI 2 DIGIT (01 SAMPAI 28): ')
                        while not(admisi_hari.isdigit() 
                                and len(admisi_hari) == 2 
                                and 1 <= int(admisi_hari) <= 28): 
                            print('\n\tERROR. SILAHKAN MASUKKAN DATA YANG BENAR')
                            admisi_hari = input('\n\tTANGGAL ADMISI 2 DIGIT (01 SAMPAI 28): ')

                # input untuk bulan 30 hari
                elif admisi_bulan_int in [4,6,9,11]:
                    admisi_hari = input('\n\tTANGGAL ADMISI 2 DIGIT (01 SAMPAI 30): ')
                    while not(admisi_hari.isdigit()
                            and len(admisi_hari) == 2
                            and 1 <= int(admisi_hari) <= 30):
                        print('\n\tERROR. SILAHKAN MASUKKAN DATA YANG BENAR')
                        admisi_hari = input('\n\tTANGGAL ADMISI 2 DIGIT (01 SAMPAI 30): ')

                # input untuk bulan 31 hari
                else:
                    admisi_hari = input('\n\tTANGGAL ADMISI 2 DIGIT (01 SAMPAI 31): ')
                    while not(admisi_hari.isdigit()
                            and len(admisi_hari) == 2
                            and 1 <= int(admisi_hari) <= 31):
                        print('\n\tERROR. SILAHKAN MASUKKAN DATA YANG BENAR')
                        admisi_hari = input('\n\tTANGGAL ADMISI 2 DIGIT (01 SAMPAI 31): ')
            
                pasien_update['ADMISI'] = f'{admisi_hari}-{admisi_bulan}-{admisi_tahun}' # DD-MM-YYYY
                tanggal_lahir = pasien_update['TANGGAL_LAHIR']
                admisi = pasien_update['ADMISI']
                pasien_update['USIA'] = hitung_usia(tanggal_lahir,admisi) # perhitungan usia

            elif pilihan_update == '6':
                print('\n\tMENGGANTI DATA PASIEN DIBATALKAN')
                break            

            print('\n\tKONFIRMASI GANTI DATA PASIEN') # tampilan tabel data baru untuk mengkonfirmasi input
            print(tabulate([pasien_update], headers="keys", tablefmt="double_grid"))

            if pasien_update['USIA'] == 'ERROR': # conditional apabila perubahan tanggal membuat perhitungan usia menjadi 'ERROR'
                print('\n\tERROR: TANGGAL LAHIR HARUS SEBELUM TANGGAL ADMISI.')
                
            konfirmasi = input('\n\tAPAKAH DATA INI INGIN DISIMPAN? (YA/TIDAK): ')
            while konfirmasi.lower() not in ['ya', 'tidak']:
                print('\n\tERROR. SILAHKAN MASUKKAN "YA" ATAU "TIDAK"')
                konfirmasi = input('\n\tAPAKAH DATA INI INGIN DISIMPAN? (YA/TIDAK): ')

            if konfirmasi.lower() == 'ya' and pasien_update['USIA'] != 'ERROR':
                index = data_pasien.index(rekam_medis[0])
                data_pasien[index] = pasien_update
                print('\n\tDATA PASIEN TELAH DIGANTIKAN')
                break
            elif konfirmasi.lower() == 'tidak':
                print('\n\tDATA PASIEN TIDAK DISIMPAN')
            else:
                print('\n\tMASIH TERDAPAT ERROR. DATA PASIEN TIDAK DISIMPAN')
                break

# fungsi menghapus data
def delete_data():
    while True:
        nrm_input = input('\n\tHAPUS DATA PASIEN. \n\n\tMASUKKAN NOMOR REKAM MEDIS (NRM 4 DIGIT): ')
        rekam_medis = [no_nrm for no_nrm in data_pasien if no_nrm['NRM'] == nrm_input] # mengakses nrm yang sesuai dengan input; jadikan list baru rekam_medis
        if rekam_medis:
            print('\n\tDATA PASIEN YANG AKAN DIHAPUS')
            print(tabulate(rekam_medis, headers="keys",tablefmt="double_grid"))
            konfirmasi = input('\n\tAPAKAH ANDA YAKIN INGIN MENGHAPUS DATA PASIEN INI? (YA/TIDAK): ')
            while konfirmasi.lower() not in ['ya', 'tidak']:
                print('\n\tERROR. SILAHKAN MASUKKAN "YA" ATAU "TIDAK"')
                konfirmasi = input('\n\tAPAKAH ANDA MASIH YAKIN INGIN MENGHAPUS DATA PASIEN INI? (YA/TIDAK): ')

            if konfirmasi.lower() == 'ya':
                data_pasien.remove(rekam_medis[0])
                print('\n\tDATA PASIEN TELAH DIHAPUS')
            else:
                print('\n\tHAPUS DATA PASIEN DIBATALKAN')
            break
        else:
            print(f'\n\tERROR. DATA PASIEN BELUM TERSEDIA ATAU INPUT SALAH: {nrm_input}')
            return

# tampilan submenu read
def submenu_read():
    while True:
        print('''
                ╔════╦════════════════════════════════╗
                ║ NO ║ MENU MENAMPILKAN DATA PASIEN   ║
                ╠════╬════════════════════════════════╣
                ║ 1  ║ TAMPILKAN SEMUA DATA PASIEN    ║
                ║ 2  ║ TAMPILKAN DATA PASIEN TERTENTU ║
                ║ 3  ║ KELUAR KE MENU UTAMA           ║
                ╚════╩════════════════════════════════╝
            ''')
        pilihan_read = input ('\tSILAHKAN MASUKKAN NOMOR MENU UNTUK MELANJUTKAN: ')
        while not ( pilihan_read.isdigit() and 1 <= int(pilihan_read) <= 3 ):
            print ('\n\tERROR. SILAHKAN ULANGI PILIHAN')
            pilihan_read = input ('\n\tSILAHKAN MASUKKAN NOMOR MENU UNTUK MELANJUTKAN: ')

        if pilihan_read == '1':
            read_all_data()
            

        elif pilihan_read == '2':
            read_x_data()
        
        elif pilihan_read == '3':
            break

# tampilan submenu create
def submenu_create():
    while True:
        print('''
                ╔════╦═══════════════════════════════╗
                ║ NO ║ MENU MENAMBAHKAN DATA PASIEN  ║
                ╠════╬═══════════════════════════════╣
                ║ 1  ║ TAMBAH DATA PASIEN            ║
                ║ 2  ║ KELUAR KE MENU UTAMA          ║
                ╚════╩═══════════════════════════════╝
            ''')
        pilihan_create =input('\tSILAHKAN MASUKKAN NOMOR MENU UNTUK MELANJUTKAN: ')
        while not(pilihan_create.isdigit()and 1<=int(pilihan_create)<=2):
            print('\n\tERROR. SILAHKAN ULANGI PILIHAN')
            pilihan_create=input('\n\tSILAHKAN MASUKKAN NOMOR MENU UNTUK MELANJUTKAN: ')

        if pilihan_create == '1':
            create_data()

        elif pilihan_create == '2':
            break
    
# tampilan submenu update    
def submenu_update():
    while True:
        print('''
                ╔════╦════════════════════════════╗
                ║ NO ║ MENU MENGGANTI DATA PASIEN ║
                ╠════╬════════════════════════════╣
                ║ 1  ║ GANTI DATA PASIEN          ║
                ║ 2  ║ KELUAR KE MENU UTAMA       ║
                ╚════╩════════════════════════════╝
            ''')
        pilihan_update =input('\tSILAHKAN MASUKKAN NOMOR MENU UNTUK MELANJUTKAN: ')
        while not(pilihan_update.isdigit()and 1<=int(pilihan_update)<=2):
            print('\n\tERROR. SILAHKAN ULANGI PILIHAN')
            pilihan_update=input('\n\tSILAHKAN MASUKKAN NOMOR MENU UNTUK MELANJUTKAN: ')

        if pilihan_update == '1':
            update_data()

        elif pilihan_update == '2':
            break

# tampilan submenu delete    
def submenu_delete():
    while True:
        print('''
                ╔════╦════════════════════════════════╗
                ║ NO ║   MENU MENGHAPUS DATA PASIEN   ║
                ╠════╬════════════════════════════════╣
                ║ 1  ║ HAPUS DATA PASIEN              ║
                ║ 2  ║ KELUAR KE MENU UTAMA           ║
                ╚════╩════════════════════════════════╝
            ''')
        pilihan_delete =input('\tSILAHKAN MASUKKAN NOMOR MENU UNTUK MELANJUTKAN: ')
        while not(pilihan_delete.isdigit()and 1<=int(pilihan_delete)<=2):
            print('\n\tERROR. SILAHKAN ULANGI PILIHAN')
            pilihan_delete=input('\n\tSILAHKAN MASUKKAN NOMOR MENU UNTUK MELANJUTKAN: ')

        if pilihan_delete == '1':
            delete_data()

        elif pilihan_delete == '2':
            break

# tampilan menu utama    
def menu_utama():
    while True:
        print('\n \tSELAMAT DATANG DI DATABASE PASIEN OPNAME RUMAH SAKIT DARURAT PMI' )
        print('''
                ╔════╦═════════════════════════╗
                ║ NO ║       MENU UTAMA        ║
                ╠════╬═════════════════════════╣
                ║ 1  ║ MENAMPILKAN DATA PASIEN ║
                ║ 2  ║ MENAMBAH DATA PASIEN    ║
                ║ 3  ║ MENGGANTI DATA PASIEN   ║
                ║ 4  ║ MENGHAPUS DATA PASIEN   ║
                ║ 5  ║ KELUAR PROGRAM          ║
                ╚════╩═════════════════════════╝
            ''')
        pilihan_utama = input ('\tSILAHKAN MASUKKAN NOMOR MENU UNTUK MELANJUTKAN: ')
        while not ( pilihan_utama.isdigit() and 1 <= int(pilihan_utama) <= 5 ):
            print ('\n\tERROR. SILAHKAN ULANGI PILIHAN')
            pilihan_utama = input ('\n\tSILAHKAN MASUKKAN NOMOR MENU UNTUK MELANJUTKAN: ')

        if pilihan_utama == '1':
            submenu_read()

        elif pilihan_utama == '2':
            submenu_create()

        elif pilihan_utama == '3':
            submenu_update()

        elif pilihan_utama == '4':
            submenu_delete()

        elif pilihan_utama == '5':
            print('\n\tTERIMA KASIH. SEMOGA SEHAT SELALU\n')
            break

menu_utama()
        
