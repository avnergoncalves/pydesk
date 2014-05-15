# coding: utf-8

import json

from pydesk.apps.core import managers


class GridEnterpriseManager(managers.GridManager):

    def __init__(self):
        super(GridEnterpriseManager, self).__init__()
        self.map_order = {'1': 'rasao_social', '2': 'rasao_social', '3': 'nome_fantasia', '4': 'cnpj'}

    def search(self, filters, params_grid):

        status = filters['status_enterprise']
        find = '%'+filters['find_enterprise'].replace("\\","\\\\")+'%'

        where = ['rasao_social LIKE %s OR nome_fantasia LIKE %s OR cnpj LIKE %s OR endereco LIKE %s']
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
                data.append({'1': {'value': i.id, 'events': 'checkbox'},
                             '2': i.rasao_social,
                             '3': i.nome_fantasia,
                             '4': i.cnpj,
                             '5': {'value': i.id, 'events': 'editar'},
                             '6': {'icon': 'ativo'} if i.is_active else {'icon': 'inativo'}})

        return json.dumps({'data': data, 'total': count})