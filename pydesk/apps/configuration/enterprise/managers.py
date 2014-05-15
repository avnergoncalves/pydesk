# coding: utf-8

import json

from django.db.models import Q
from django.db import models


class GridEnterpriseManager(models.Manager):

    def __init__(self):
        super(GridEnterpriseManager, self).__init__()
        self.map_order = {'1': 'rasao_social', '2': 'rasao_social', '3': 'nome_fantasia', '4': 'cnpj'}

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
        status = filters['status_enterprise']
        find = filters['find_enterprise'].replace("\\","\\\\")
        #recupera filters

         #cria queryset
        qs = self.filter(Q(rasao_social__icontains=find) |
                         Q(nome_fantasia__icontains=find) |
                         Q(cnpj__icontains=find) |
                         Q(endereco__icontains=find))

        if status != '-1':
            qs.filter(is_active=status)

        qs.order_by(order)
        #cria queryset

        count = qs.count()
        result = qs[offset:limit]

        data = []
        if result:
            for i in result:
                data.append({'1': {'value': i.id, 'events': 'checkbox'},
                             '2': i.rasao_social,
                             '3': i.nome_fantasia,
                             '4': i.cnpj,
                             '5': {'value': i.id, 'events': 'editar'},
                             '6': {'icon': 'ativo'} if i.is_active else {'icon': 'inativo'}})

        return json.dumps({'data': data, 'total': count})