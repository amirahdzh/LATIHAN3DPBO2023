from Human import Human

class Mahasiswa(Human):
    def __init__(self, NIM, nama, jenis_kelamin, fakultas, prodi):
        super().__init__(NIK=NIM, nama=nama, jenis_kelamin=jenis_kelamin)
        self._NIM = NIM
        self._fakultas = fakultas
        self._prodi = prodi

    def getNIM(self):
        return self._NIM

    def setNIM(self, NIM):
        self._NIM = NIM

    def getFakultas(self):
        return self._fakultas

    def setFakultas(self, fakultas):
        self._fakultas = fakultas

    def getProdi(self):
        return self._prodi

    def setProdi(self, prodi):
        self._prodi = prodi
