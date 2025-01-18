from django import template
from . import views
from .models import Category, TagPost

register = template.Library()

@register.inclusion_tag('main/list_categories.html')
def get_categories():
    cats = Category.objects.all()
    return {'cats': cats, 'cat_selected': cat_selected}
