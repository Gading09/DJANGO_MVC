from django.contrib import admin
from .models import Dokter,Pasien,Resep,Obat
# Register your models here.
admin.site.register(Dokter)
admin.site.register(Pasien)
admin.site.register(Resep)
admin.site.register(Obat)