# Membuat dictionary dan list
dic_email = dict()
lst = list()

# Meminta pengguna untuk memasukkan nama file
fname = input('Nama File: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File tidak bisa dibuka:', fname)
    quit()

# Memproses setiap baris dalam file
for baris in fhand:
    kata = baris.split()
    if len(kata) < 2 or kata[0] != 'From':
        continue
    else:
        if kata[1] not in dic_email:
            dic_email[kata[1]] = 1  # entri pertama
        else:
            dic_email[kata[1]] += 1  # menambah hitungan

# Mengubah dictionary menjadi list tuple dan mengurutkannya
for key, val in dic_email.items():
    lst.append((val, key))  # isi daftar dengan nilai kunci dict

lst.sort(reverse=True)  # urutkan berdasarkan nilai tertinggi

# Menampilkan nilai pertama (terbesar)
for key, val in lst[:1]:
    print(val, key)