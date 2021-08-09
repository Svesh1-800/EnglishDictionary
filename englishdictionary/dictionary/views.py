from typing import get_args
from django.shortcuts import redirect, render
from django.http import HttpResponse, request
from django.views.generic import View

from PyDictionary import PyDictionary

class IndexView(View):
    def get(self,request):
        return render(request, template_name='dictionary/index.html')

class WordFindView(View):
    def get(self,request,*args, **kwargs):
        
        unknown_word = request.GET.get("unknown-word")
        dictionary = PyDictionary()
        meaning = dictionary.meaning(unknown_word)
        context = {
            "meaning": meaning,
        }
        print(meaning)
        return redirect("dictionary:index")
        
    
        