from django.views.generic import View
from django.shortcuts import render


class TopView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'stripe/index.html')