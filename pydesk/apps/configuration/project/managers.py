# coding: utf-8

import json

from django.db.models import Q
from django.db import models


class GridProjectManager(models.Manager):

    def __init__(self):
        super(GridProjectManager, self).__init__()
        self.map_order = {'1': 'description'}

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
        status = filters['status']
        find = filters['find'].replace("\\","\\\\")
        #recupera filters

        #cria queryset
        if status != '-1':
            qs = self.filter(Q(is_active=status) & Q(Q(description__icontains=find))).order_by(order)
        else:
            qs = self.filter(Q(description__icontains=find)).order_by(order)
        #cria queryset

        count = qs.count()
        result = qs[offset:limit]

        data = []
        if result:
            for i in result:
                data.append({'1': {'value': i.id, 'events': 'checkbox'},
                             '2': i.description,
                             '5': {'value': i.id, 'events': 'editar'},
                             '6': {'icon': 'ativo'} if i.is_active else {'icon': 'inativo'}})

        return json.dumps({'data': data, 'total': count})
