from django import template


register = template.Library()


@register.simple_tag(takes_context=True)
def get_active_class(context, pattern):
    try:
        from django.core import urlresolvers
        
        path = context.get('request').path
        resolved = urlresolvers.resolve(path)
        
        if path.find(pattern) != -1 or resolved.url_name == pattern:
            return 'ativo'
    except:
        pass

    return ''