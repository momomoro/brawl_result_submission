from django.urls import path

from . import views


app_name = 'result_submission'
urlpatterns = [
    path('', views.index, name='index'),
    path('ajax/load-decks/', views.load_decks, name='ajax_load_decks')
]