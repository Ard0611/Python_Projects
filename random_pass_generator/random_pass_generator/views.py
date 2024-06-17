from django.http import HttpResponse
from django.shortcuts import render
import random

def home(request):
    return render(request, 'index.html')

def password(request):
    length = int(request.GET.get('length'))
    isUpper = request.GET.get('uppercase')
    isNumber = request.GET.get('number')
    isSymbol = request.GET.get('symbol')
    # print (length,isUpper, isNumber, isSymbol)
    choices_I_have = list("abcdefghijklmnopqrstuvwxyz")
    if isUpper == 'on':
        choices_I_have.extend(list("ABCDEFGHJKLMNOPQRSTUVWXYZ"))
    if isNumber == 'on':
        choices_I_have.extend(list("0123456789"))
    if isSymbol == 'on':
        choices_I_have.extend(list("!@#$%^&*()[]{}+-=_<>?'"))

    myPassword = ""
    for i in range(length):
        choosen = random.choice(choices_I_have)
        myPassword += choosen

    data = {
        'password': myPassword
    }


    return render(request, 'password.html', data)

def contact(request):
    return render(request, 'contact.html')