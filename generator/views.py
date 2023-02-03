from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html', {'password':'sddsdsdsds'})

def test(request):
    if request.method == 'POST':
        characters = list()

        if request.POST.get('lowercase') == 'true':
            characters = list('abcdefghijklmnopqestuvwxyz')

        if request.POST.get('uppercase') == 'true':
            characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

        if request.POST.get('special') == 'true':
            characters.extend(list('!@#$~^&*()_%?'))

        if request.POST.get('number') == 'true':
            characters.extend(list('1234567890'))

        length = int(request.POST.get('length'))
        thepassword = ''

        for x in range(length):
            thepassword += random.choice(characters)

        return JsonResponse({'password': thepassword})


    else:
        return render(request, 'generator/generate-password.html')



def password(request):

    characters = list('abcdefghijklmnopqestuvwxyz')

    if request.POST.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.POST.get('special'):
        characters.extend(list('!@#$~^&*()_%?'))

    if request.POST.get('numbers'):
        characters.extend(list('1234567890'))

    length = int(request.POST.get('length'))
    thepassword = ''

    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/test.html', {'password': thepassword})
