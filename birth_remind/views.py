from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm


# Create your views here.


def get_birth(request):
    items = Item.objects.all()

    context = {
        'items': items
    }

    return render(request, 'birth_remind/birth.html', context)


def add_birth(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_birth')

        form = ItemForm()
        context = {
            'form': form
        }

    return render(request, 'birth_remind/add_birthdays.html')
