from django.urls import path

from . import views

app_name = 'words'
urlpatterns = [
    path('WordEditor/', views.CharacterSetEditor, name='CharacterSetEditor'),
    path('WordEditor/voc/<int:set_id>/', views.VocabularyEditor, name='VocabularyEditor'),
    path('WordEditor/voc/meaning/<int:voc_id>/', views.MeaningEditor, name='MeaningEditor'),
    path('WordEditor/DelSet/', views.DelSet, name='DelSet'),
    path('WordEditor/AddSet/', views.AddSet, name='AddSet'),
    path('WordEditor/EditSet/', views.EditSet, name='EditSet'),
    path('WordEditor/voc/DelVoc/', views.DelVoc, name='DelVoc'),
    path('WordEditor/voc/AddVoc/', views.AddVoc, name='AddVoc'),
    path('WordEditor/voc/EditVoc/', views.EditVoc, name='EditVoc'),
    path('WordEditor/voc/AddMeaning/', views.AddMeaning, name='AddMeaning'),
    path('WordEditor/voc/DelMeaning/', views.DelMeaning, name='DelMeaning'),
    path('WordEditor/voc/FetchMeaning/', views.FetchMeaning, name='FetchMeaning'),
    path('Exam/', views.Exam, name='Exam'),
    path('Exam/onExam', views.examHandler, name='examHandler'),
]