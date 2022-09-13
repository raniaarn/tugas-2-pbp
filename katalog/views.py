from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_katalog(request):
    data_barang_katalog = CatalogItem.objects.all()
    context = {
        'list_of_items': data_barang_katalog,
        'name': 'Rania Maharani Narendra',
        'student_id' : '2106650222'
    }
    return render(request, "katalog.html", context)