from typing import get_args
from django.shortcuts import render
from django.views.generic import View

from PyDictionary import PyDictionary

class IndexView(View):
    def get(self,request):
        return render(request, template_name='dictionary/index.html')

class WordFindView(View):
    def get(self,request,*args, **kwargs):
        
        unknown_word = request.GET.get("unknown-word")
        dictionary = PyDictionary()
        meanings = dictionary.meaning(unknown_word)
        synonums = dictionary.synonym(unknown_word)
        context = {
            "meanings" : meanings,
            "synonums": synonums,
            "word": unknown_word.title()
        }
        if context["meanings"] is None:
            context["empty_response"] = True
        else:
            context["empty_response"] = False
        
        return render(request,template_name='dictionary/index.html', context= context)
        
    
        