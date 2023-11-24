from django import template

register = template.Library()

@register.filter(is_safe=True)
def display_color(value):
    if value:
        return "#FF0000"