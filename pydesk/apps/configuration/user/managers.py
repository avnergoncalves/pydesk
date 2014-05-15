# coding: utf-8

import json

from pydesk.apps.core import managers
from django.core.exceptions import ObjectDoesNotExist


class GridUserManager(managers.GridManager):

    def __init__(self):
        super(GridUserManager, self).__init__()
        self.map_order = map_order = {'1': 'first_name', '2': 'first_name', '3': 'last_name', '4': 'email', '5': '_profile_cache__phone', '6': '_profile_cache__cell_phone', '7':'_profile_cache__enterprise__rasao_social'}

    def search(self, filters, params_grid):

        status = filters['is_active']
        find = '%'+filters['find_user'].replace("\\","\\\\")+'%'

        where = ['first_name LIKE %s OR last_name LIKE %s OR email LIKE %s OR email LIKE %s', 'is_superuser = 0']
        params = [find, find, find, find]

        if status != '-1':
            where.append('is_active = %s')
            params.append(status)

        self.set_queryset(params_grid, where, params)

        count = self.count_total()
        result = self.get_result()
        data = []

        if result:
            for i in result:
                try:
                    userprofile = i.get_profile()
                except ObjectDoesNotExist:
                    userprofile = None

                data.append({'1': {'value': i.id, 'events': 'checkbox'},
                             '2': i.first_name,
                             '3': i.last_name,
                             '4': i.email,
                             '5': userprofile.phone if userprofile else '',
                             '6': userprofile.cell_phone if userprofile else '',
                             '7': userprofile.enterprise.rasao_social if userprofile else '',
                             '8': {'value': i.id, 'events': 'editar'},
                             '9': {'icon': 'ativo'} if i.is_active else {'icon': 'inativo'}})

        return json.dumps({'data': data, 'total': count})