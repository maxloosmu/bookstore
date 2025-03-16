from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from books.models import Book
from .utils import calculate_cart_total
from .models import Order, Item
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    cart_total = 0
    books_in_cart = []
    cart = request.session.get('cart', {})
    book_ids = list(cart.keys())
    if (book_ids != []):
        books_in_cart = Book.objects.filter(id__in=book_ids)
        cart_total = calculate_cart_total(cart, books_in_cart)

    template_data = {}
    template_data['title'] = 'Cart'
    template_data['books_in_cart'] = books_in_cart
    template_data['cart_total'] = cart_total
    return render(request, 'cart/index.html', {'template_data': template_data})

def add(request, id):
    get_object_or_404(Book, id=id)
    cart = request.session.get('cart', {})
    cart[id] = request.POST['quantity']
    request.session['cart'] = cart
    return redirect('cart.index')
    # return redirect('home.index')

def clear(request):
    request.session['cart'] = {}
    return redirect('cart.index')

@login_required
def purchase(request):
    cart = request.session.get('cart', {})
    book_ids = list(cart.keys())

    if (book_ids == []):
        return redirect('cart.index')
    
    books_in_cart = Book.objects.filter(id__in=book_ids)
    cart_total = calculate_cart_total(cart, books_in_cart)

    order = Order()
    order.user = request.user
    order.total = cart_total
    order.save()

    for book in books_in_cart:
        item = Item()
        item.book = book
        item.price = book.price
        item.order = order
        item.quantity = cart[str(book.id)]
        item.save()

    request.session['cart'] = {}
    template_data = {}
    template_data['title'] = 'Purchase Confirmation'
    template_data['order_id'] = order.id
    return render(request, 'cart/purchase.html', {'template_data': template_data})