# coding: utf-8

import json
from django.contrib import messages

from django.utils.translation import ugettext_lazy as _
from django.http.response import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from pydesk.apps.configuration.enterprise.models import Enterprise
from pydesk.apps.configuration.equip.models import Equip
from pydesk.apps.configuration.project.models import Project
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

    context = {'form_user': form, 'id': pk}

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

        u = None
        pk = request.POST.get('id', None)
        if pk:
            u = get_object_or_404(User, pk=pk)

        form1 = CustomUserChangeForm(request.POST, instance=u)

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


@login_required
def user_enterprise_edit(request):
    pk = request.GET.get('id', None)

    selected_enterprises = []
    if pk:
        u = get_object_or_404(User, pk=pk)
        user_profile = u.get_profile()
        obj_selected_enterprises = user_profile.enterprise.all()
        for i in obj_selected_enterprises:
            selected_enterprises.append(i.id)

    all_enterprises = Enterprise.objects.all()

    context = {'all_enterprises': all_enterprises,
               'selected_enterprises': selected_enterprises,
               'id': pk}

    return render(request, 'user/user_enterprise_edit.html', context)


@login_required
def user_enterprise_ajax_edit_save(request):
    if request.method == 'POST' and request.is_ajax():

        enterprises_selected = request.POST.getlist('enterprises[]', None)

        pk = request.POST.get('id', None)
        if pk:
            u = get_object_or_404(User, pk=pk)

        user_profile = u.get_profile()
        user_profile.enterprise.clear()

        if enterprises_selected:
            obj_enterprises_selected = Enterprise.objects.filter(id__in=enterprises_selected)
            user_profile.enterprise = obj_enterprises_selected

        user_profile.save()

        message = unicode(_('Operation successful.'))
        data = {'status': '1', 'message': [message], 'id': pk}

        return HttpResponse(json.dumps(data), content_type='application/json')

    else:
        raise Http404


@login_required
def user_equip_edit(request):
    pk = request.GET.get('id', None)

    selected_equips = []
    if pk:
        u = get_object_or_404(User, pk=pk)
        user_profile = u.get_profile()
        obj_selected_equip = user_profile.equip.all()
        for i in obj_selected_equip:
            selected_equips.append(i.id)

    all_equips = Equip.objects.all()

    context = {'all_equips': all_equips,
               'selected_equips': selected_equips,
               'id': pk}

    return render(request, 'user/user_equip_edit.html', context)


@login_required
def user_equip_ajax_edit_save(request):
    if request.method == 'POST' and request.is_ajax():

        equips_selected = request.POST.getlist('equips[]', None)

        pk = request.POST.get('id', None)
        if pk:
            u = get_object_or_404(User, pk=pk)

        user_profile = u.get_profile()
        user_profile.equip.clear()

        if equips_selected:
            obj_equips_selected = Equip.objects.filter(id__in=equips_selected)
            user_profile.equip = obj_equips_selected

        user_profile.save()

        message = unicode(_('Operation successful.'))
        data = {'status': '1', 'message': [message], 'id': pk}

        return HttpResponse(json.dumps(data), content_type='application/json')

    else:
        raise Http404


@login_required
def user_project_edit(request):
    pk = request.GET.get('id', None)

    selected_projects = []
    if pk:
        u = get_object_or_404(User, pk=pk)
        user_profile = u.get_profile()
        obj_selected_projects = user_profile.project.all()
        for i in obj_selected_projects:
            selected_projects.append(i.id)

    all_projects = Project.objects.all()

    context = {'all_projects': all_projects,
               'selected_projects': selected_projects,
               'id': pk}

    return render(request, 'user/user_project_edit.html', context)


@login_required
def user_project_ajax_edit_save(request):
    if request.method == 'POST' and request.is_ajax():

        projects_selected = request.POST.getlist('projects[]', None)

        pk = request.POST.get('id', None)
        if pk:
            u = get_object_or_404(User, pk=pk)

        user_profile = u.get_profile()
        user_profile.project.clear()

        if projects_selected:
            obj_projects_selected = Project.objects.filter(id__in=projects_selected)
            user_profile.project = obj_projects_selected

        user_profile.save()

        message = unicode(_('Operation successful.'))
        data = {'status': '1', 'message': [message], 'id': pk}

        return HttpResponse(json.dumps(data), content_type='application/json')

    else:
        raise Http404