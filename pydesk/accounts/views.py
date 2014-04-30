'''
Created on Feb 6, 2014

@author: agoncalves
@email: viner_lipe@hotmail.com
'''

from django.shortcuts import render, redirect
from django.contrib import auth
from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm


def login(request):
    v_next = request.GET.get('next', settings.MAP_URLS['HOME'])

    if request.user.is_authenticated():
        return redirect(v_next)

    form = AuthenticationForm(data=request.POST or None)
    if form.is_valid():
        auth.login(request, form.get_user())
        return redirect(v_next)

    return render(request, 'accounts/login.html', {'form': form})


def logout(request):
    auth.logout(request)
    return redirect(settings.MAP_URLS['LOGIN'])
