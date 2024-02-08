from django import template
from myapp.models import MenuItem

from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def draw_menu(menu_name):
    menu_items = MenuItem.objects.filter(parent__isnull=True, title=menu_name)
    

    def render_menu_item(menu_item):
        result = f'<li><a href="{menu_item.get_absolute_url()}">{menu_item.title}</a>'
        child_items = MenuItem.objects.filter(parent=menu_item)
        if child_items.exists():
            result += '<ul>'
            for child_item in child_items:
                result += render_menu_item(child_item)
            result += '</ul>'
        result += '</li>'
        return result

    menu_html = ''.join(render_menu_item(item) for item in menu_items)
    return mark_safe('<ul>' + menu_html + '</ul>')