from django.shortcuts import render

def index(request):
    return render(request, 'personal/home.html')
# render has three parameter request, page and dictionaries

def contact(request):
    return render(request, 'personal/basic.html', {'content': ['If you like to contact me, email me ','usemymail11@gmail.com']})
