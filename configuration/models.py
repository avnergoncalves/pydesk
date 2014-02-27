'''
Created on Feb 6, 2014

@author: agoncalves
@email: viner_lipe@hotmail.com
'''

from django.db import models

# Create your models here.
class Enterprise(models.Model):
    rasao_social = models.CharField(max_length=200, blank=False)
    nome_fantasia = models.CharField(max_length=200, blank=False)
    cnpj = models.CharField(max_length=100, blank=True)
    inscricao_estadual = models.CharField(max_length=100, blank=True)
    endereco = models.CharField(max_length=100, blank=True)
    observacao = models.CharField(max_length=1024, blank=True)
    status = models.BooleanField(blank=False, default=True)
    
    def consult_grid(self, filters, params_grid):
        map_order = {'2': 'rasao_social', '3': 'nome_fantasia', '4': 'cnpj'}
        
        pagina = int(params_grid.get('pagina'))
        limite = int(params_grid.get('limite'))
        order = params_grid.get('order')
        
        order_s = order.replace('DESC', '-').replace('ASC', '').split(' ')
        order_f = order_s[1]+map_order.get(order_s[0], 'rasao_social')
        
        status = filters['status_enterprise']
        find = '%'+filters['find_enterprise'].replace("\\","\\\\")+'%'
        
        where = ['rasao_social LIKE %s OR nome_fantasia LIKE %s OR cnpj LIKE %s OR endereco LIKE %s']
        params = [find,find,find,find]
        
        if status != '-1':
            where.append('status = %s')
            params.append(status)
        
        query = Enterprise.objects.extra(where=where, params=params).order_by(order_f)

        offset = (pagina-1)*limite
        result = query[offset:limite]
        count = query.count()

        data = []
        for i in result:
            data.append( {'1': {'value': i.id, 'events': 'checkbox'},
                          '2': i.rasao_social,
                          '3': i.nome_fantasia,
                          '4': i.cnpj,
                          '5': {'value': i.id, 'events': 'editar'},
                          '6': {'icon': 'ativo'} if i.status else {'icon': 'inativo'}
                          }
                        )

        grid = {}
        grid['data'] = data
        grid['total'] = count

        return grid