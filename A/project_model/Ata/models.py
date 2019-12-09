from django.db import models

# Create your models here.

class MataPelajarn(models.Model):
    nama_pelajaran = models.CharField(max_length = 200)
    jadwal_dimulai = models.TimeField("jadwal mulai")
    jadwal_berakhir = models.TimeField("jadwal berakhir")

    def __str__(self):
       return "Mata Pelajaran %s di mulai pukul %s dan berakhir pukul %s"%(self.nama_pelajaran, self.jadwal_dimulai, self.jadwal_berakhir)

class Direksi(models.Model):
    nama_lengkap = models.CharField(max_length = 200)
    nomor_telp = models.CharField(max_length = 13, default="")
    jabatan = models.CharField(max_length = 255, default="")

    def __str__(self):
       return "Direksi bernama %s , nomor telp %s dengan jabatan %s"%(self.nama_lengkap, self.nomor_telp, self.jabatan)

class Mentee(models.Model):
    nama_lengkap = models.CharField(max_length = 200)
    nomor_telp = models.CharField(max_length = 13, default="")
    nomor_absen = models.CharField(max_length = 50, default="")
    nilai_rata = models.IntegerField(default=0)

    def __str__(self):
       return "Peserta bernama %s, nomor telp %s , nomor absen %s, nilai rata-rata %s" %(self.nama_lengkap, self.nomor_telp, self.nomor_absen, self.nilai_rata)
    
class Mentor(models.Model):
    nama_lengkap = models.CharField(max_length = 200)
    nomor_telp = models.CharField(max_length = 13, default="")
    mata_pelajaran = models.ForeignKey(MataPelajarn, on_delete = models.CASCADE)

    def __str__(self):
       return "Mentor bernama %s, nomor telp %s , mengajar mata kuliah %s"%(self.nama_lengkap, self.nomor_telp, self.mata_pelajaran)

class Challenge(models.Model):
    nama_challenge = models.CharField(max_length = 200)
    banyak_soal = models.IntegerField(default=0)
    bobot_nilai = models.CharField(max_length = 10, default="")
    mata_pelajaran = models.ForeignKey(MataPelajarn, on_delete = models.CASCADE)

    def __str__(self):
       return "%s banyak soal %s dengan bobot nya %s dan kisi-kisi nya %s"%(self.nama_challenge, self.banyak_soal, self.bobot_nilai, self.mata_pelajaran)

class LiveCode(models.Model):
    nama_live_code = models.CharField(max_length = 200)
    banyak_soal = models.IntegerField(default=0)
    bobot_nilai = models.CharField(max_length = 100, default="")
    tanggal_pelaksanaan = models.DateTimeField("date_published")
    mata_pelajaran = models.ForeignKey(MataPelajarn, on_delete = models.CASCADE)

    def __str__(self):
       return "%s banyak soal %s dengnan bobot nya %s di laksanakan tanggal %s dan kisi-kisinya %s"%(self.nama_live_code, self.banyak_soal, self.bobot_nilai, self.tanggal_pelaksanaan, self.mata_pelajaran)