from django.shortcuts import render

from katalog.models import CatalogItem

def show_katalog(request):
    katalog = CatalogItem.objects.all()
    context = {
        "nama": "Alvaro Austin",
        "student_id": 2106752180,
        "katalog": katalog
    }
    return render(request, 'katalog.html', context)