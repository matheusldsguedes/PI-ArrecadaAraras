from django.shortcuts import render

def cadastro(request):
    if request.method == 'post':
        return render(request, 'home.html')
