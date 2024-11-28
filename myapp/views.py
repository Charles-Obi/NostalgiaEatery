from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def starter(request):
    return render(request, 'starter-page.html')

def about(request):
    return render(request, 'about.html')

def menu(request):
    return render(request, 'menu.html')

def specials(request):
    return render(request, 'specials.html')

def events(request):
    return render(request, 'events.html')

def chefs(request):
    return render(request, 'chefs.html')

def gallery(request):
    return render(request, 'gallery.html')

def contact(request):
    return render(request, 'contact.html')