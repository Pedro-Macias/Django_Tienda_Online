from django import template
from carro.utils import get_or_set_order_session

register = template.Library()

# contar los items que hay en el carro
@register.filter
def carro_item_count(request):
    order = get_or_set_order_session(request)
    count = order.items.count()
    return count