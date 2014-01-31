from django.shortcuts import render_to_response, redirect
from django.contrib.auth import authenticate, login, logout
from django.template.context import RequestContext
from autentication.forms.login import LoginForm


def login(request, user_id=None):

    form = LoginForm()

    if request.method == 'POST':
        
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    redirect('/dashboard/home')
                else:
                    # Retorna uma mensagem de erro de 'conta desabilitada' .
                    pass
            else:
                # Retorna uma mensagem de erro 'login invalido'.
                pass

    return render_to_response('login/login.html', {'form': form}, context_instance=RequestContext(request))


def logout(request, user_id=None):
    logout(request)
    
    redirect('/auth/login')
