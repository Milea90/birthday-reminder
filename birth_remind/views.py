from django.shortcuts import render

# Create your views here.


def get_birth(request):
    return render(request, 'birth_remind/birth.html')
