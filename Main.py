from SivitasAkademik import SivitasAkademik

class main(SivitasAkademik):
    
    data = SivitasAkademik()
    
   # membuat objek Mahasiswa
    mahasiswa1 = Mahasiswa(NIM="001", nama="John Doe", jenis_kelamin="Laki-laki", fakultas="Fakultas Teknik", prodi="Teknik Informatika")
    print("Mahasiswa 1")
    print("NIM        : ", mahasiswa1.getNIM())
    print("Nama       : ", mahasiswa1.getNama())
    print("Jenis Kelamin : ", mahasiswa1.getJenisKelamin())
    print("Fakultas   : ", mahasiswa1.getFakultas())
    print("Program Studi : ", mahasiswa1.getProdi())
    print()

    # mengubah nama mahasiswa1
    mahasiswa1.setNama("Jane Doe")
    print("Mahasiswa 1 (setelah diubah)")
    print("NIM        : ", mahasiswa1.getNIM())
    print("Nama       : ", mahasiswa1.getNama())
    print("Jenis Kelamin : ", mahasiswa1.getJenisKelamin())
    print("Fakultas   : ", mahasiswa1.getFakultas())
    print("Program Studi : ", mahasiswa1.getProdi())
    print()

    # membuat objek Dosen
    dosen1 = Dosen(NIP="101", nama="Dr. Jekyll", jenis_kelamin="Laki-laki", fakultas="Fakultas Kedokteran", prodi="Kedokteran Umum", pend_terakhir="S3", keahlian="Psikologi")
    print("Dosen 1")
    print("NIP        : ", dosen1.getNIP())
    print("Nama       : ", dosen1.getNama())
    print("Jenis Kelamin : ", dosen1.getJenisKelamin())
    print("Fakultas   : ", dosen1.getFakultas())
    print("Program Studi : ", dosen1.getProdi())
    print("Pendidikan Terakhir : ", dosen1._pend_terakhir) # menggunakan akses langsung karena tidak ada getter nya
    print("Keahlian   : ", dosen1._keahlian) # menggunakan akses langsung karena tidak ada getter nya
    print()

    # mengubah fakultas dan prodi dosen1
    dosen1.setFakultas("Fakultas Psikologi")
    dosen1.setProdi("Psikologi")
    print("Dosen 1 (setelah diubah)")
    print("NIP        : ", dosen1.getNIP())
    print("Nama       : ", dosen1.getNama())
    print("Jenis Kelamin : ", dosen1.getJenisKelamin())
    print("Fakultas   : ", dosen1.getFakultas())
    print("Program Studi : ", dosen1.getProdi())
    print("Pendidikan Terakhir : ", dosen1._pend_terakhir) # menggunakan akses langsung karena tidak ada getter nya
    print("Keahlian   : ", dosen1._keahlian) # menggunakan akses langsung karena tidak ada getter nya
    print()
