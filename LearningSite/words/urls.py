from django.urls import path

from . import views

app_name = 'words'
urlpatterns = [
    path('', views.index, name='index'),
    path('WordEditor/', views.CharacterSetEditor, name='CharacterSetEditor'),
    path('WordEditor/<int:set_id>/', views.VocabularyEditor, name='VocabularyEditor'),
]