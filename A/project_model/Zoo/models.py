from django.db import models

# Create your models here.
class Hewan(models.Model):
    nama = models.CharField(max_length = 200)
    species = models.CharField(max_length = 200, default="")
    berat = models.IntegerField(default=0)
    umur = models.IntegerField(default=0)
    
    def __str__(self):
        return "%s spesies %s dengan berat %skg dan umurnya %s tahun"%(self.nama, self.species, self.berat, self.umur)

class Kandang(models.Model):
    nama = models.CharField(max_length = 200)
    isi_kandang = models.IntegerField(default=0)
    luas_kandang = models.IntegerField(default=0)

    def __str__(self):
        return "Kandang %s berkapasitas %s ekor, dengan luas kandang %s meter"%(self.nama, self.isi_kandang, self.luas_kandang)

class Penjaga(models.Model):
    nama = models.CharField(max_length = 200)
    nomor_telp = models.CharField(max_length = 13, default="")
    jadwal_jaga = models.DateTimeField("date_published")
    
    def __str__(self):
        return "penjaga bernama %s ,nomor telp %s jadwal nya %s"%(self.nama, self.nomor_telp, self.jadwal_jaga)

class Pengunjung(models.Model):
    nama = models.CharField(max_length = 200)
    nomor_telp = models.CharField(max_length = 13, default="")
    hari_berkunjung = models.DateTimeField("date_published")
    
    def __str__(self):
        return "pengunjung bernama %s, nomor telp %s berkunjung pada tanggal %s"%(self.nama, self.nomor_telp, self.hari_berkunjung)