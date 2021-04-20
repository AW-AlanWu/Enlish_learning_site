from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from .models import CharacterSet, Vocabulary
from django.urls import reverse

def index(request):
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_visits': num_visits,
    }

    return render(request, 'words/index.html', context=context)

def CharacterSetEditor(request):
    CharacterSet_list = CharacterSet.objects.order_by('-pk')
    context = {'CharacterSet_list': CharacterSet_list}
    return render(request, 'words/CharacterSetEditor.html', context)

def VocabularyEditor(request, set_id):
    object = get_object_or_404(CharacterSet, pk=set_id)
    Vocabulary_list = object.vocabulary_set.order_by('-pk')
    context = {
        'Vocabulary_list': Vocabulary_list,
        'title': object.set_name
    }
    return render(request, 'words/VocabularyEditor.html', context)

def MeaningEditor(request, voc_id):
    object = get_object_or_404(Vocabulary, pk=voc_id)
    Meaning_list = object.meaning_set.order_by('-pk')
    context = {
        'Meaning_list': Meaning_list,
        'title': object.english,
        'back': object.character_set.pk
    }
    return render(request, 'words/MeaningEditor.html', context)

def DelSet(request):
    Set = get_object_or_404(CharacterSet, pk=request.POST['id'])
    Set.delete()
    return HttpResponseRedirect(reverse('words:CharacterSetEditor'))

def EditSet(request):
    return HttpResponse("HI")

def AddSet(request):
    return HttpResponse("HI")

def DelVoc(request):
    Voc = get_object_or_404(Vocabulary, pk=request.POST['id'])
    args = Voc.character_set_id
    Voc.delete()
    return HttpResponseRedirect(reverse('words:VocabularyEditor', args=(args,)))
    
def EditSet(request):
    return HttpResponse("HI")

def AddSet(request):
    return HttpResponse("HI")