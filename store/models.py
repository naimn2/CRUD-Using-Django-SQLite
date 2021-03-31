from django.db import models

class Produk(models.Model):
    nama_produk = models.CharField(max_length=80)
    keterangan = models.CharField(max_length=250)
    harga = models.IntegerField()
    jumlah = models.IntegerField()
    def __str__(self):
        return self.nama_produk