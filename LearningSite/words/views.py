from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.views import generic
from .models import CharacterSet, Vocabulary

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
    return render(request, 'words/VocabularyEditor.html', {'Vocabulary_list': Vocabulary_list})