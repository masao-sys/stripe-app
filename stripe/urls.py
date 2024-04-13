from django.urls import path
from stripe.views import top

urlpatterns = [
    path('', top.TopView.as_view(), name='top'),
]