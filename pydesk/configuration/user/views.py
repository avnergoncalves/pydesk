'''
Created on Feb 6, 2014

@author: agoncalves
@email: viner_lipe@hotmail.com
'''

import json

from django.utils.translation import ugettext_lazy as _
from django.http.response import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from pydesk.configuration.user.forms import UserForm
from pydesk.configuration.user.models import UserProfile
from django.contrib.auth.models import User


@login_required
def user_list(request):
    return render(request, 'user/user_list.html', {})


@login_required
def user_add(request):
    return render(request, 'user/user_add.html', {'form_user': UserForm(), 
                                                  'form_relationships': ''})


@login_required
def user_ajax_list(request):
    if request.is_ajax():
        params_grid = dict()
        params_grid['limite'] = request.GET.get('limite', 50)
        params_grid['pagina'] = request.GET.get('pagina', 1)
        params_grid['order'] = request.GET.get('order', '1 ASC')

        filters = dict()
        filters['find_user'] = request.GET.get('find_user', '')
        filters['is_active'] = request.GET.get('is_active', '')

        model = UserProfile()
        grid = model.consult_grid(filters, params_grid)

        return HttpResponse(json.dumps(grid), mimetype='application/json')

    else:
        raise Http404


@login_required
def user_ajax_save(request):
    if request.method == 'POST' and request.is_ajax():
        e = None
        pk = request.POST.get('id', None)
        if pk:
            e = get_object_or_404(User, pk=pk)

        form1 = UserForm(request.POST, instance=e)
        form2 = UserForm(request.POST, instance=e)
        
        is_valid_form1 = form1.is_valid()
        is_valid_form2 = form2.is_valid()
        
        if is_valid_form1 and is_valid_form2:
            form1.save()

            message = unicode(_('Operation successful.'))
            data = {'status': '1', 'message': [message]}
        else:
            data = {'status': '0', 'errors': form1.errors+form2.errors}

        return HttpResponse(json.dumps(data), mimetype='application/json')
    else:
        raise Http404