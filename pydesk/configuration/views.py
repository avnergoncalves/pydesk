import json

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from configuration.forms import EnterpriseForm
from django.http.response import HttpResponse, Http404
from configuration.models import Enterprise
from django.forms.models import model_to_dict


@login_required
def enterprise_list(request):
    return render(request, 'enterprise/enterprise_list.html', {})


@login_required
def enterprise_add(request):
    form = EnterpriseForm()

    return render(request, 'enterprise/enterprise_add.html', {'form': form})


@login_required
def enterprise_edit(request):
    pk = request.GET.get('id') or None

    data = get_object_or_404(Enterprise, pk=pk)
    form = EnterpriseForm(instance=data)

    return render(request, 'enterprise/enterprise_add.html', {'form': form})


@login_required
def enterprise_ajax_list(request):
    return render(request, 'enterprise/ajax_enterprise_list.html', {})


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
            data = {'status': '1', 'message': 'Enterprise cadastrada com sucesso'}
        else:
            data = {'status': '0', 'errors': form.errors}

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