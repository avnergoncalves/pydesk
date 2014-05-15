# coding: utf-8

from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from pydesk.apps.configuration.enterprise.models import Enterprise
from pydesk.apps.configuration.user.managers import GridUserManager


class Equipe(models.Model):
    description = models.CharField(max_length=200, blank=False)


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='_profile_cache')
    enterprise = models.ForeignKey(Enterprise)
    esquipes = models.ManyToManyField(Equipe)
    receive_email = models.BooleanField(blank=False, default=True)
    color_system = models.CharField(max_length=200, blank=False)
    phone = models.CharField(max_length=200, blank=False)
    cell_phone = models.CharField(max_length=200, blank=False)
    auto_update_dashboard = models.BooleanField(blank=False, default=False)

    objects = models.Manager()
    grid = GridUserManager()

    def consult_grid(self, filters, params_grid):
        map_order = {'1': 'first_name', '2': 'first_name', '3': 'last_name', '4': 'email', '5': '_profile_cache__phone', '6': '_profile_cache__cell_phone', '7':'_profile_cache__enterprise__rasao_social'}

        pagina = int(params_grid.get('pagina'))
        limite = int(params_grid.get('limite'))
        order = params_grid.get('order')

        order_s = order.replace('DESC', '-').replace('ASC', '').split(' ')
        order_f = order_s[1]+map_order.get(order_s[0], 'first_name')

        status = filters['is_active']
        find = '%'+filters['find_user'].replace("\\","\\\\")+'%'

        where = ['first_name LIKE %s OR last_name LIKE %s OR email LIKE %s OR email LIKE %s', 'is_superuser = 0']
        params = [find, find, find, find]

        if status != '-1':
            where.append('is_active = %s')
            params.append(status)

        query = User.objects.select_related('_profile_cache').extra(where=where, params=params).order_by(order_f)
        count = query.count()

        #Calcula paginacao
        offset = (pagina-1)*limite
        fim = (limite*pagina) if pagina > 0 else limite

        if fim > count:
            fim = count

        result = query[offset:fim]
        #Calcula paginacao

        data = []
        for i in result:
            try:
                userprofile = i.get_profile()
            except ObjectDoesNotExist:
                userprofile = None

            data.append( {'1': {'value': i.id, 'events': 'checkbox'},
                          '2': i.first_name,
                          '3': i.last_name,
                          '4': i.email,
                          '5': userprofile.phone if userprofile else '',
                          '6': userprofile.cell_phone if userprofile else '',
                          '7': userprofile.enterprise.rasao_social if userprofile else '',
                          '8': {'value': i.id, 'events': 'editar'},
                          '9': {'icon': 'ativo'} if i.is_active else {'icon': 'inativo'}
                          }
                        )

        grid = {}
        grid['data'] = data
        grid['total'] = count

        return grid