from django.urls import path, include

from myapp.views import top, credit, item

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', top.TopView.as_view(), name='top'),
    path('account/', include('allauth.urls')),

    path('credit/register/', credit.CreditRegisterView.as_view(), name='credit-register'),
    path('credit/update/', credit.CreditUpdateView.as_view(), name='credit-update'),
    path('subscription/cancel/', credit.SubscriptionCancelView.as_view(), name='subscription-cancel'),

    path('item/', item.ItemListView.as_view(), name='item-list'),
    path('item/create/', item.ItemCreateView.as_view(), name='item-create'),
    path('item/update/<int:pk>/', item.ItemUpdateView.as_view(), name='item-update'),
    path('item/delete/<int:pk>/', item.ItemDeleteView.as_view(), name='item-delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
