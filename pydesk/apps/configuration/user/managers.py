# coding: utf-8

import json

from django.db.models import Q
from django.db import models


class GridUserManager(models.Manager):

    def __init__(self):
        super(GridUserManager, self).__init__()

        self.map_order = {'1': 'user__first_name',
                          '2': 'user__first_name',
                          '3': 'user__last_name',
                          '4': 'user__email',
                          '5': 'phone',
                          '6': 'cell_phone'}

    def search(self, filters, params_grid):
        #recupera order by
        order_f = params_grid.get('order')
        order_s = order_f.replace('DESC', '-').replace('ASC', '').split(' ')
        order = order_s[1]+self.map_order.get(order_s[0])
        #recupera order by

        #calcula paginação
        page = int(params_grid.get('page'))
        limit = int(params_grid.get('limit'))
        offset = (page-1)*limit
        #calcula paginação

        #recupera filters
        status = filters['is_active']
        find = filters['find_user'].replace("\\","\\\\")
        #recupera filters

        #cria queryset
        if status != '-1':
            qs = self.filter(Q(user__is_active=status) &
                             Q(Q(user__first_name__icontains=find) |
                             Q(user__last_name__icontains=find) |
                             Q(user__email__icontains=find))).order_by(order)
        else:
            qs = self.filter(Q(user__first_name__icontains=find) |
                             Q(user__last_name__icontains=find) |
                             Q(user__email__icontains=find)).order_by(order)
        #cria queryset

        count = qs.count()
        result = qs[offset:limit]

        data = []
        if result:
            for i in result:
                data.append({'1': {'value': i.user_id, 'events': 'checkbox'},
                             '2': i.user.first_name,
                             '3': i.user.last_name,
                             '4': i.user.email,
                             '5': i.phone,
                             '6': i.cell_phone,
                             '7': {'value': i.user_id, 'events': 'editar'},
                             '8': {'icon': 'ativo'} if i.user.is_active else {'icon': 'inativo'}
                             })

        return json.dumps({'data': data, 'total': count})