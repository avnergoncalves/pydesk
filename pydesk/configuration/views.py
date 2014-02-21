'''
Created on Feb 6, 2014

@author: agoncalves
@email: viner_lipe@hotmail.com
'''

import json

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from configuration.forms import EnterpriseForm
from django.http.response import HttpResponse, Http404
from configuration.models import Enterprise
from django.utils.translation import ugettext_lazy as _


@login_required
def enterprise_list(request):
    return render(request, 'enterprise/enterprise_list.html', {})


@login_required
def enterprise_add(request):
    return render(request, 'enterprise/enterprise_add.html', {'form': EnterpriseForm()})


@login_required
def enterprise_edit(request):
    pk = request.GET.get('id') or None

    data = get_object_or_404(Enterprise, pk=pk)
    form = EnterpriseForm(instance=data)

    return render(request, 'enterprise/enterprise_add.html', {'form': form})


@login_required
def enterprise_ajax_list(request):
    
    if request.is_ajax():
        params_grid = {}
        params_grid['limite'] = request.GET.get('limite', 50)
        params_grid['pagina'] = request.GET.get('pagina', 1)
        params_grid['order'] = request.GET.get('order', '1 ASC')

        filters = {}
        filters['find_enterprise'] = request.GET.get('find_enterprise', '')
        filters['status_enterprise'] = request.GET.get('status_enterprise', '')

        model = Enterprise()
        grid = model.consult_grid(filters, params_grid)

        return HttpResponse(json.dumps(grid), mimetype='application/json')

    else:
        raise Http404


@login_required
def enterprise_ajax_save(request):
    if request.method == 'POST' and request.is_ajax():
        e = None
        pk = request.POST.get('id', None)
        if pk:
            e = get_object_or_404(Enterprise, pk=pk)

        form = EnterpriseForm(request.POST, instance=e)
        if form.is_valid():
            form.save()

            message = unicode(_('Operation successful.'))
            data = {'status': '1', 'message': [message]}
        else:
            data = {'status': '0', 'errors': form.errors}

        return HttpResponse(json.dumps(data), mimetype='application/json')
    else:
        raise Http404

@login_required
def enterprise_ajax_toogle_status(request):
    if request.method == 'POST' and request.is_ajax():
        
        checkboxs = request.POST.getlist('checkboxs', [])
        status = int(request.POST.get('hdd_status', None))
        
        message = []
        erro = False

        if status == None:
            message.append(unicode(_('Undefined stats')))
            erro = True

        if len(checkboxs) == 0:
            message.append(unicode(_('Nenhum item foi selecionado')))
            erro = True

        if not erro:
            for i in checkboxs:
                e = get_object_or_404(Enterprise, pk=i)
                e.status = status
                e.save()

                message.append(unicode(_('Operation successful.')))
                data = {'status': '1', 'message': message}
        else:
            data = {'status': '0', 'errors': {'__all__':message}}

        return HttpResponse(json.dumps(data), mimetype='application/json')
    else:
        raise Http404


@login_required
def user(request):
    return render(request, 'home/home.html', {})


@login_required
def ajax_user_list(request):
    return render(request, 'home/home.html', {})


@login_required
def ajax_user_salve(request):
    return render(request, 'home/home.html', {})