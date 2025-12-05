from django.shortcuts import render

def login_view(request):
    """View para a página de Login."""
    return render(request, 'users/login.html')

def register_view(request):
    """View para a página de Cadastro."""
    return render(request, 'users/register.html')