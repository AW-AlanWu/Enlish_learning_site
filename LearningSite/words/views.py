from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from .models import CharacterSet, Vocabulary, Meaning
from .forms import CharacterSetModelForm, VocabularySetModelForm, MeaningSetModelForm
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
    form =  CharacterSetModelForm()
    context = {
        'CharacterSet_list': CharacterSet_list,
        'form': form
    }
    return render(request, 'words/CharacterSetEditor.html', context)

def VocabularyEditor(request, set_id):
    object = get_object_or_404(CharacterSet, pk=set_id)
    Vocabulary_list = object.vocabulary_set.order_by('-pk')
    form = VocabularySetModelForm()
    context = {
        'Vocabulary_list': Vocabulary_list,
        'title': object.set_name,
        'Set_id': object.pk,
        'form': form
    }
    return render(request, 'words/VocabularyEditor.html', context)

def MeaningEditor(request, voc_id):
    object = get_object_or_404(Vocabulary, pk=voc_id)
    Meaning_list = object.meaning_set.order_by('-pk')
    form = MeaningSetModelForm()
    context = {
        'Meaning_list': Meaning_list,
        'title': object.english,
        'Voc_id': object.pk,
        'Set_id': object.character_set.pk,
        'form': form
    }
    return render(request, 'words/MeaningEditor.html', context)

def DelSet(request):
    Set = get_object_or_404(CharacterSet, pk=request.POST['id'])
    Set.delete()
    return HttpResponseRedirect(reverse('words:CharacterSetEditor'))

def EditSet(request):
    Set = get_object_or_404(CharacterSet, pk=request.POST['id'])
    Set.set_name = request.POST['set_change']
    Set.save()
    return HttpResponseRedirect(reverse('words:CharacterSetEditor'))

def AddSet(request):
    Set = CharacterSet(set_name = request.POST['set_name'])
    Set.save()
    return HttpResponseRedirect(reverse('words:CharacterSetEditor'))

def DelVoc(request):
    Voc = get_object_or_404(Vocabulary, pk=request.POST['id'])
    args = Voc.character_set_id
    Voc.delete()
    return HttpResponseRedirect(reverse('words:VocabularyEditor', args=(args,)))
    
def EditVoc(request):
    Voc = get_object_or_404(Vocabulary, pk=request.POST['id'])
    Voc.english = request.POST['voc_change']
    Voc.save()
    args = Voc.character_set_id
    return HttpResponseRedirect(reverse('words:VocabularyEditor', args=(args,)))

def AddVoc(request):
    args = request.POST['id']
    Set = get_object_or_404(CharacterSet, pk=args)
    Voc = Vocabulary(english = request.POST['english'], character_set = Set)
    Voc.save()
    return HttpResponseRedirect(reverse('words:VocabularyEditor', args=(args,)))

def AddMeaning(request):
    args = request.POST['id']
    Voc = get_object_or_404(Vocabulary, pk=args)
    Mean = Meaning(chinese = request.POST['chinese'], chinese_sentences = request.POST['chinese_sentences'], english_sentences = request.POST['english_sentences'], speech = request.POST['speech'], vocabulary = Voc)
    Mean.save()
    return HttpResponseRedirect(reverse('words:MeaningEditor', args=(args,)))

def DelMeaning(request):
    Mean = get_object_or_404(Meaning, pk=request.POST['id'])
    args = Mean.vocabulary_id
    Mean.delete()
    return HttpResponseRedirect(reverse('words:MeaningEditor', args=(args,)))
