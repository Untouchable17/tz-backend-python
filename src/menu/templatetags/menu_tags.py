from django import template

from src.menu.models import Category


register = template.Library()

@register.simple_tag(name='draw_menu')
def draw_menu(menu_name):
    categories = Category.objects.prefetch_related('subcategories').all()
    menu_html = '<ul>'
    for category in categories:
        if category.parent is None:
            menu_html += '<li class="parent-category"><a href="{}">{}</a>'.format(
                category.get_absolute_url(), category.name
            )
            subcategories = category.subcategories.all()
            if subcategories.exists():
                menu_html += '<ul>'
                for subcategory in subcategories:
                    menu_html += '<li class="child-category"><a href="{}">{}</a></li>'.format(
                        subcategory.get_absolute_url(), subcategory.name
                    )
                menu_html += '</ul>'
            menu_html += '</li>'
    menu_html += '</ul>'
    return menu_html