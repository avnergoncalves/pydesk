'''
Created on Feb 6, 2014

@author: agoncalves
@email: viner_lipe@hotmail.com
'''

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save


class Enterprise(models.Model):
    rasao_social = models.CharField(max_length=200, blank=False)
    nome_fantasia = models.CharField(max_length=200, blank=False)
    cnpj = models.CharField(max_length=100, blank=True)
    inscricao_estadual = models.CharField(max_length=100, blank=True)
    endereco = models.CharField(max_length=100, blank=True)
    observacao = models.CharField(max_length=1024, blank=True)
    is_active = models.BooleanField(default=True)
    
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
            where.append('is_active = %s')
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
                          '6': {'icon': 'ativo'} if i.is_active else {'icon': 'inativo'}
                          }
                        )

        grid = {}
        grid['data'] = data
        grid['total'] = count

        return grid


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


    def consult_grid(self, filters, params_grid):
        map_order = {'2': 'first_name', '3': 'last_name', '4': 'email', '5': 'phone', '6': 'cell_phone'}
        
        pagina = int(params_grid.get('pagina'))
        limite = int(params_grid.get('limite'))
        order = params_grid.get('order')
        
        order_s = order.replace('DESC', '-').replace('ASC', '').split(' ')
        order_f = order_s[1]+map_order.get(order_s[0], 'first_name')
        
        status = filters['is_active']
        find = '%'+filters['find_user'].replace("\\","\\\\")+'%'
        
        where = ['first_name LIKE %s OR last_name LIKE %s OR email LIKE %s OR email LIKE %s', 'is_superuser = 0']
        params = [find,find,find,find]
        
        if status != '-1':
            where.append('is_active = %s')
            params.append(status)
        
        query = User.objects.select_related('_profile_cache').extra(where=where, params=params).order_by(order_f)

        offset = (pagina-1)*limite
        result = query[offset:limite]
        count = query.count()
        
        
        data = []
        for i in result:
            data.append( {'1': {'value': i.id, 'events': 'checkbox'},
                          '2': i.first_name,
                          '3': i.last_name,
                          '4': i.email,
                          '5': i.userprofile.phone if hasattr(i, 'userprofile') else '',
                          '6': i.userprofile.cell_phone if hasattr(i, 'userprofile') else '',
                          '7': i.userprofile.enterprise.rasao_social if hasattr(i, 'userprofile') else '',
                          '8': {'value': i.id, 'events': 'editar'},
                          '9': {'icon': 'ativo'} if i.is_active else {'icon': 'inativo'}
                          }
                        )

        grid = {}
        grid['data'] = data
        grid['total'] = count

        return grid