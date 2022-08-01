from difflib import context_diff
from django.shortcuts import render
from django.views import generic




def indexView(request):
   
    return render(request, template_name='index.html')

class DetailProfile(generic.DetailView):
    pass


# Create your views here.
