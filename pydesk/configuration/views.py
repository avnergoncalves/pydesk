from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def enterprise_list(request):
    return render(request, 'enterprise/enterprise_list.html', {})

@login_required
def enterprise_add(request):
    return render(request, 'enterprise/enterprise_add.html', {})

@login_required
def ajax_enterprise_list(request):
    return render(request, 'enterprise/ajax_enterprise_list.html', {})


@login_required
def ajax_enterprise_save(request):
    return render(request, 'enterprise/ajax_enterprise_save.html', {})


@login_required
def user(request):
    return render(request, 'home/home.html', {})


@login_required
def ajax_user_list(request):
    return render(request, 'home/home.html', {})


@login_required
def ajax_user_salve(request):
    return render(request, 'home/home.html', {})