from django.urls import path, include

from myapp.views import top, credit

urlpatterns = [
    path('', top.TopView.as_view(), name='top'),
    path('account/', include('allauth.urls')),

    path('credit/register', credit.CreditRegisterView.as_view(), name='credit-register'),
    path('credit/update', credit.CreditUpdateView.as_view(), name='credit-update'),
    path('subscription/cancel', credit.SubscriptionCancelView.as_view(), name='subscription-cancel'),
]