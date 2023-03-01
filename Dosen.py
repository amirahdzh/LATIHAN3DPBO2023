class Dosen(SivitasAkademik):
    def __init__(self, NIP, nama, jenis_kelamin, fakultas, prodi, pend_terakhir, keahlian):
        super().__init__(NIK=NIP, nama=nama, jenis_kelamin=jenis_kelamin, asal_universitas="", email_edu="")
        self._NIP = NIP
        self._fakultas = fakultas
        self._prodi = prodi
        self._pend_terakhir = pend_terakhir
        self._keahlian = keahlian

    def getNIP(self):
        return self._NIP

    def setNIP(self, NIP):
        self._NIP = NIP

    def getFakultas(self):
        return self._fakultas

    def setFakultas(self, fakultas):
        self._fakultas = fakultas