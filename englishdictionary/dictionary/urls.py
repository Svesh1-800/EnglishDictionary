from django.urls import path
from dictionary.views import index
app_name = "dictionary"

urlpatterns = [
    path('',index,name="index")
]
