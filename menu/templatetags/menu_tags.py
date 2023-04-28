from django import template
from menu.models import MenuItem

register = template.Library()


@register.simple_tag()
def draw_menu(name):
    menu_items = MenuItem.objects.filter(parent__isnull=True, name=name)
    return generate_menu_html(menu_items)


def generate_menu_html(menu_items):
    menu_html = '<ul>'
    for item in menu_items:
        menu_html += f'<li><a href="{item.url}">{item.display_name}</a>'
        if item.children.exists():
            menu_html += generate_menu_html(item.children.all())
        menu_html += '</li>'
    menu_html += '</ul>'
    return menu_html
