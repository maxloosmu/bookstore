from django import template

register = template.Library()

@register.filter(name='get_quantity')
def get_cart_quantity(cart, book_id):
  return cart[str(book_id)]
  # return cart.get(str(book_id), 0)
