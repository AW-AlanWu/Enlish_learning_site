from django.urls import path

from . import views

app_name = 'words'
urlpatterns = [
    path('', views.index, name='index'),
    path('WordEditor/', views.CharacterSetEditor, name='CharacterSetEditor'),
    path('WordEditor/voc/<int:set_id>/', views.VocabularyEditor, name='VocabularyEditor'),
    path('WordEditor/voc/meaning/<int:voc_id>', views.MeaningEditor, name='MeaningEditor'),
    path('WordEditor/DelSet', views.DelSet, name='DelSet'),
    path('WordEditor/AddSet', views.AddSet, name='AddSet'),
    path('WordEditor/EditSet', views.EditSet, name='EditSet'),
    path('WordEditor/voc/DelVoc', views.DelVoc, name='DelVoc'),
    path('WordEditor/voc/AddVoc', views.AddVoc, name='AddVoc'),
    path('WordEditor/voc/EditVoc', views.EditVoc, name='EditVoc'),
]