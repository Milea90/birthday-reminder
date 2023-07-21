from django.shortcuts import render
from .models import Item


# Create your views here.


def get_birth(request):
    items = Item.objects.all()

    context = {
        'items': items
    }

    return render(request, 'birth_remind/birth.html', context)


def add_birth(request):

    return render(request, 'birth_remind/add_birthdays.html')
