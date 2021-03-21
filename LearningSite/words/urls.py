from django.urls import path

from . import views

app_name = 'words'
urlpatterns = [
    path('', views.index, name='index'),
    path('WordEditor/', views.WordEditor.as_view(), name='WordEditor')
]