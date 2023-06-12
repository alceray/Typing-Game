from django.urls import include, path
from .views import *

urlpatterns = [
    path('random_sentences/', random_sentences),
    path('book_list/', book_list),
]