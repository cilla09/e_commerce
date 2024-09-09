from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306152153',
        'nama': 'Priscilla Natanael Surjanto',
        'product1': 'Air Mineral',
        'harga1': 'Rp. 5000',
        'desc1': 'Air mineral yang sangat sehat dan menyegarkan',
        'product2': 'Teh Botol',
        'harga2': 'Rp. 8000',
        'desc2': 'Teh dari daun teh pilihan',
        'product3': 'Kopi Bubuk',
        'harga3': 'Rp. 10000',
        'desc3': 'Kopi bubuk dari biji kopi pilihan',
    }

    return render(request, "main.html", context)

