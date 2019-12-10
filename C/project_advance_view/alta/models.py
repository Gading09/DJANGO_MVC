from django.db import models

# Create your models here.
class Mentor(models.Model):
    foto_mentor = models.CharField(max_length = 255, default = "")
    jabatan_mentor = models.CharField(max_length = 255, default = "")
    nama_mentor = models.CharField(max_length = 255, default = "")
    pesan_mentor = models.CharField(max_length = 255, default = "")

    def __str__(self):
        return self.nama_mentor

class Mentee(models.Model):
    foto_mentee = models.CharField(max_length = 255, default = "")
    nama_mentee = models.CharField(max_length = 255, default = "")
    pesan_mentee = models.CharField(max_length = 255, default = "")
    def __str__(self):
        return self.nama_mentee

class Blog(models.Model):
    foto_blog = models.CharField(max_length = 255, default = "")
    judul_blog = models.CharField(max_length = 255, default = "")
    berita = models.TextField(default = "")
    tanggal = models.DateField("tanggal",auto_now=True)
    def __str__(self):
        return self.judul_blog