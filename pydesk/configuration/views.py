import json

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from configuration.forms import EnterpriseForm
from django.http.response import HttpResponse, Http404


@login_required
def enterprise_list(request):
    return render(request, 'enterprise/enterprise_list.html', {})


@login_required
def enterprise_add(request):
    form = EnterpriseForm()

    return render(request, 'enterprise/enterprise_add.html', {'form': form})


@login_required
def enterprise_ajax_list(request):
    return render(request, 'enterprise/ajax_enterprise_list.html', {})


@login_required
def enterprise_ajax_save(request):
    
    if request.method == 'POST' and request.is_ajax():
        form = EnterpriseForm(request.POST)
        
        if form.is_valid():
            data = {'status': '1'}
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