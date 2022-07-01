from django.views import View
from django.shortcuts import render

# Create your views here.
class HomeView(View):
    def get(self, request, *args, **kwarg):

        return render(request, 'home.html')

home = HomeView.as_view()
