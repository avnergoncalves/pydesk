# coding: utf-8

from django.db import models


class GridManager(models.Manager):
    map_order = dict()
    queryset = False
    page = 0
    limit = 0
    order = ''

    def __init__(self):
        super(GridManager, self).__init__()

    def _get_order(self, params_grid, default=''):
        order = params_grid.get('order')

        order_s = order.replace('DESC', '-').replace('ASC', '').split(' ')
        order_f = order_s[1]+self.map_order.get(order_s[0], default)

        return order_f

    def set_queryset(self, params_grid, where, params):
        self.order = self._get_order(params_grid)
        self.page = int(params_grid.get('page'))
        self.limit = int(params_grid.get('limit'))

        self.queryset = self.extra(where=where, params=params).order_by(self.order)

    def count_total(self):
        if self.queryset:
            return self.queryset.count()
        else:
            return False

    def get_result(self):
        if self.queryset:
            offset = (self.page-1)*self.limit
            return self.queryset[offset:self.limit]
        else:
            return False