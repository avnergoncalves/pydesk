# coding: utf-8

import json
from django.contrib import messages

from django.utils.translation import ugettext_lazy as _
from django.http.response import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from pydesk.apps.configuration.user.forms import CustomUserCreationForm, CustomUserChangeForm
from pydesk.apps.configuration.user.models import UserProfile

@login_required
def user_list(request):
    return render(request, 'user/user_list.html', {})


@login_required
def user_add(request):
    return render(request, 'user/user_add.html', {'form_user': CustomUserCreationForm()})

@login_required
def user_edit(request):
    pk = request.GET.get('id') or None

    data = get_object_or_404(User, pk=pk)
    form = CustomUserChangeForm(instance=data)

    context = {'form_user': form}

    return render(request, 'user/user_edit.html', context)

@login_required
def user_ajax_list(request):
    if request.is_ajax():
        params_grid = dict()
        params_grid['limit'] = request.GET.get('limite', 50)
        params_grid['page'] = request.GET.get('pagina', 1)
        params_grid['order'] = request.GET.get('order', '1 ASC')

        filters = dict()
        filters['find_user'] = request.GET.get('find_user', '')
        filters['is_active'] = request.GET.get('is_active', '')

        try:
            grid = UserProfile.grid.search(filters, params_grid)
        except Exception as e:
            return e

        return HttpResponse(grid, content_type='application/json')

    else:
        raise Http404


@login_required
def user_ajax_add_save(request):
    if request.method == 'POST' and request.is_ajax():

        form1 = CustomUserCreationForm(request.POST)
        
        is_valid_form1 = form1.is_valid()
        
        if is_valid_form1:
            user = form1.save()

            message = unicode(_('Operation successful.'))
            messages.add_message(request, messages.SUCCESS, message)

            data = {'status': '1', 'id': user.id}
        else:
            data = {'status': '0', 'errors': form1.errors}

        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        raise Http404


@login_required
def user_ajax_edit_save(request):
    if request.method == 'POST' and request.is_ajax():

        form1 = CustomUserChangeForm(request.POST)

        is_valid_form1 = form1.is_valid()

        if is_valid_form1:
            user = form1.save()

            message = unicode(_('Operation successful.'))

            data = {'status': '1', 'message': [message], 'id': user.id}
        else:
            data = {'status': '0', 'errors': form1.errors}

        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        raise Http404