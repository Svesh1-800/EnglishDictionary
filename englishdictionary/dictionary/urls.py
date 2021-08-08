from django.urls import path
from dictionary.views import IndexView
app_name = "dictionary"

urlpatterns = [
    path('',IndexView.as_view(),name="index")
]
