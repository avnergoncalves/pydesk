# coding: utf-8

from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def show_messages(context, messages):
    try:
        html = ''

        if messages:
            html = '<ul>'
            for message in messages:
                html += '<li class="'+message.tags+'">'+message.message+'</li>'
            html += '</ul>'
    except Exception, e:
        pass

    return html