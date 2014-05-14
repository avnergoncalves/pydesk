# coding: utf-8

import json

from django.db import models


class GridEnterpriseManager(models.Manager):

    def search(self, filters, params_grid):
        map_order = {'2': 'rasao_social', '3': 'nome_fantasia', '4': 'cnpj'}

        page = int(params_grid.get('pagina'))
        limit = int(params_grid.get('limite'))
        order = params_grid.get('order')

        order_s = order.replace('DESC', '-').replace('ASC', '').split(' ')
        order_f = order_s[1]+map_order.get(order_s[0], 'rasao_social')

        status = filters['status_enterprise']
        find = '%'+filters['find_enterprise'].replace("\\","\\\\")+'%'

        where = ['rasao_social LIKE %s OR nome_fantasia LIKE %s OR cnpj LIKE %s OR endereco LIKE %s']
        params = [find, find, find, find]

        if status != '-1':
            where.append('is_active = %s')
            params.append(status)

        qs = self.extra(where=where, params=params).order_by(order_f)

        count = qs.count()

        offset = (page-1)*limit
        result = qs[offset:limit]

        data = []
        for i in result:
            data.append({'1': {'value': i.id, 'events': 'checkbox'},
                         '2': i.rasao_social,
                         '3': i.nome_fantasia,
                         '4': i.cnpj,
                         '5': {'value': i.id, 'events': 'editar'},
                         '6': {'icon': 'ativo'} if i.is_active else {'icon': 'inativo'}})

        return json.dumps({'data': data, 'total': count})