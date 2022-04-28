# Custom filters for template tags

from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value, arg):
    """  Cuts out the values of arg from the string """

    return value.replace(arg, '')

# Pass this function to the template tags register
#register.filter('cut', cut)
