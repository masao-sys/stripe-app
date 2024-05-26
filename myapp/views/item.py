from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from myapp.models import Item


class ItemListView(ListView):
    template_name = 'stripe/item/list.html'
    model = Item
    paginate_by = 20


class ItemCreateView(CreateView):
    template_name = 'stripe/item/create.html'
    model = Item
    fields = ('name', 'price', 'image')
    success_url = reverse_lazy('item-list')


class ItemUpdateView(UpdateView):
    template_name = 'stripe/item/update.html'
    model = Item
    fields = ('name', 'price', 'image')
    success_url = reverse_lazy('item-list')


class ItemDeleteView(DeleteView):
    template_name = 'stripe/item/delete.html'
    model = Item
    success_url = reverse_lazy('item-list')
