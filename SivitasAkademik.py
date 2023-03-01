from Mahasiswa import Mahasiswa

class SivitasAkademik(Mahasiswa):
    def __init__(self, NIK, nama, jenis_kelamin, asal_universitas, email_edu):
        super().__init__(NIK=NIK, nama=nama, jenis_kelamin=jenis_kelamin)
        self._asal_universitas = asal_universitas
        self._email_edu = email_edu

    def getAsalUniversitas(self):
        return self._asal_universitas

    def setAsalUniversitas(self, asal_universitas):
        self._asal_universitas = asal_universitas

    def getEmailEdu(self):
        return self._email_edu

    def setEmailEdu(self, email_edu):
        self._email_edu = email_edu