from django.urls import path
from dictionary.views import IndexView, WordFindView
app_name = "dictionary"

urlpatterns = [
    path('',IndexView.as_view(),name="index"),
    path('word', WordFindView.as_view(),name="word")
]
