from django.db import models

# Create your models here.

class Dokter(models.Model):
    nama = models.CharField(max_length = 200)
    nomor_telp = models.CharField(max_length = 13, default="")
    bidang = models.CharField(max_length = 200, default="")
    jadwal_praktek = models.DateTimeField("date_published")
    
    def __str__(self):
        return "Dokter bernama %s , nomor telp %s ahli di bidang %s , jadwal praktek %s"%(self.nama, self.nomor_telp, self.bidang, self.jadwal_praktek)

class Pasien(models.Model):
    nama = models.CharField(max_length = 200)
    nomor_telp = models.CharField(max_length = 13, default="")
    alamat = models.CharField(max_length = 255, default="")
    keluhan = models.CharField (max_length = 255, default="")

    def __str__(self):
       return "Pasien bernama %s, nomer telp %s, tingal di %s dengan keluhan %s"%(self.nama, self.nomor_telp, self.alamat, self.keluhan)

class Resep(models.Model):
    nama = models.CharField(max_length = 200)
    total_harga = models.IntegerField(default=0)
    kumpulan_obat = models.CharField(max_length = 255, default="")

    def __str__(self):
       return "Resep %s dengan harga %s obat-obatnya yaitu %s"%(self.nama, self.total_harga, self.kumpulan_obat)

class Obat(models.Model):
    nama = models.CharField(max_length = 200)
    kandungan = models.CharField(max_length = 200, default="")
    khasiat = models.CharField(max_length = 255, default="")

    def __str__(self):
       return "Obat %s dengan kandungan %s khasiat nya %s"%(self.nama, self.kandungan, self.khasiat)