def hitung_distribusi_jam(namafile):
    distribusi_jam = {}
    try:
        with open(namafile, 'r') as file:
            for line in file:
                if line.startswith('From '):
                    kata = line.split()
                    waktu = kata[5].split(':')
                    jam = waktu[0]
                    distribusi_jam[jam] = distribusi_jam.get(jam, 0) + 1
    except FileNotFoundError:
        print("File tidak ditemukan")
        return

    print("Distribusi Jam:")
    for jam in sorted(distribusi_jam):
        print(jam, distribusi_jam[jam])

namafile = 'mbox-short.txt'

hitung_distribusi_jam(namafile)