from django.shortcuts import render, redirect
from .models import Produk

# Create your views here.
def index(request):
    products = Produk.objects.all()
    context = {
        'products': products
    }
    return render(request, 'store/index.html', context)

def ubah(request):
    did = request.POST.get('id', None)
    if (did != None):
        product = Produk.objects.get(id=did)
        context = {
            'produk': product
        }
        return render(request, 'store/ubah.html', context)
    return redirect('/store')

def simpan(request):
    bId = request.POST.get('id', None)
    bNama = request.POST.get('nama', None)
    bKet = request.POST.get('keterangan', None)
    bHarga = request.POST.get('harga', None)
    bJumlah = request.POST.get('jumlah', None)
    if (bId != None):
        produk = Produk.objects.get(id=bId)
        if (produk != None):
            produk.nama_produk = bNama
            produk.keterangan = bKet
            produk.harga = bHarga
            produk.jumlah = bJumlah
            produk.save()
    return redirect('/store')

def hapus(request):
    did = request.POST.get('id', None)
    if (id != None):
        produk = Produk.objects.get(id=did)
        produk.delete()
    return redirect('/store')

def tambah(request):
    produkBaru = Produk(
        nama_produk=request.POST.get('nama', None),
        keterangan=request.POST.get('keterangan', None),
        harga=request.POST.get('harga', None),
        jumlah=request.POST.get('jumlah', None)
    )
    produkBaru.save()
    return redirect('/store')