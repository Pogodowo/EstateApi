from django.shortcuts import render

def home(request):
    ogl=['o','p']



    return render(request, 'home.html', {'ret': ogl,'text':'test'})
#
