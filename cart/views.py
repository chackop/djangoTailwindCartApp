from django.http.response import HttpResponseRedirect
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum

from .forms import CartItemForm

from .models import CartItem
# Create your views here.


class CartItemCreateView(LoginRequiredMixin, CreateView):
    model = CartItem
    success_url = "/cart/items"
    form_class = CartItemForm
    template_name = "cart/cart_form.html"
    login_url = "/login"

    # save with that user object
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class CartItemListView(LoginRequiredMixin, ListView):
    model = CartItem
    context_object_name = "cartitems"
    template_name = "cart/cart_list.html"
    login_url = "/login"

    # displays cart items just created by the user
    def get_queryset(self):
        queryset = self.request.user.cart.all()
        queryset = queryset.annotate(price_total=Sum("price"))
        return queryset


class CartItemDetailView(LoginRequiredMixin, DetailView):
    model = CartItem
    context_object_name = "cartitem"
    template_name = "cart/cart_detail.html"
    login_url = "/login"


class CartItemUpdateView(LoginRequiredMixin, UpdateView):
    model = CartItem
    form_class = CartItemForm
    template_name = "cart/cart_form.html"
    login_url = "/login"
    success_url = "/cart/items"


class CartItemDeleteView(LoginRequiredMixin, DeleteView):
    model = CartItem
    success_url = "/cart/items"
    template_name = "cart/cart_delete.html"
    context_object_name = "cartitem"
    login_url = "/login"
