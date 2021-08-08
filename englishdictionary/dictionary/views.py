from django.shortcuts import render
from django.http import HttpResponse, request
from django.views.generic import View

import PyDictionary

class IndexView(View):
    def get(self,request):
        return render(request, template_name='dictionary/index.html')

