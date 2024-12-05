from django.shortcuts import render

# view para página principal
def index(request):
    return render(request, 'index.html')

# view para pagina de perfil
def profile(request):
    return render(request, 'profile.html')

