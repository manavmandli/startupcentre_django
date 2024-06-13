from django import template
from django.urls import resolve

register = template.Library()

@register.simple_tag
def active_url(request, url_name):
    try:
        return 'active' if resolve(request.path_info).url_name == url_name else ''
    except:
        return ''