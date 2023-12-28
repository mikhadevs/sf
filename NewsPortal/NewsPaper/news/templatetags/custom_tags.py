from datetime import datetime
from django import template
#from django.template.loader_tags import register

register = template.Library()


# @register.simple_tag()
# def current_time(format_string='%b %d %Y'):
#    return datetime.utcnow().strftime(format_string)

@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
   d = context['request'].GET.copy() # позволяет скопировать все параметры текущего запроса.
   for k, v in kwargs.items():
       d[k] = v
# кодируем параметры в формат, который может быть указан в строке браузера.
   return d.urlencode()
