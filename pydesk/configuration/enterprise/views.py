# coding: utf-8

import json

from django.utils.translation import ugettext_lazy as _
from django.http.response import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from pydesk.configuration.enterprise.forms import EnterpriseForm
from pydesk.configuration.enterprise.models import Enterprise


@login_required
def enterprise_list(request):
    return render(request, 'enterprise/enterprise_list.html', {})


@login_required
def enterprise_add(request):
    context = {'form': EnterpriseForm()}
    return render(request, 'enterprise/enterprise_add.html', context)


@login_required
def enterprise_edit(request):
    pk = request.GET.get('id') or None

    data = get_object_or_404(Enterprise, pk=pk)
    form = EnterpriseForm(instance=data)

    context = {'form': form}

    return render(request, 'enterprise/enterprise_add.html', context)


@login_required
def enterprise_ajax_list(request):
    
    if request.is_ajax():
        params_grid = dict()
        params_grid['limite'] = request.GET.get('limite', 50)
        params_grid['pagina'] = request.GET.get('pagina', 1)
        params_grid['order'] = request.GET.get('order', '1 ASC')

        filters = dict()
        filters['find_enterprise'] = request.GET.get('find_enterprise', '')
        filters['status_enterprise'] = request.GET.get('status_enterprise', '')

        json_grid = Enterprise.grid.search(filters, params_grid)

        return HttpResponse(json_grid, mimetype='application/json')
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
        is_active = int(request.POST.get('hdd_is_active', None))
        
        message = []
        erro = False

        if is_active == None:
            message.append(unicode(_('Undefined stats')))
            erro = True

        if len(checkboxs) == 0:
            message.append(unicode(_('Nenhum item foi selecionado')))
            erro = True

        if not erro:
            for i in checkboxs:
                e = get_object_or_404(Enterprise, pk=i)
                e.is_active = is_active
                e.save()

                message.append(unicode(_('Operation successful.')))
                data = {'status': '1', 'message': message}
        else:
            data = {'status': '0', 'errors': {'__all__': message}}

        return HttpResponse(json.dumps(data), mimetype='application/json')
    else:
        raise Http404