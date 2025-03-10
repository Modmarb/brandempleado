from django.urls import path
from . import views

app_name = 'home_app'

urlpatterns = [
    path('home/', views.indexview.as_view()),
    path('list/', views.pruebalistview.as_view()),
    path('list-prueba/', views.MODEL_pruebaListView.as_view()),
    path('add/', views.pruebaCreateView.as_view(),name='crear'),
    path('resumenfoundation/', views.resumenfoundationview.as_view(),name='resumenfoundation'),
]
