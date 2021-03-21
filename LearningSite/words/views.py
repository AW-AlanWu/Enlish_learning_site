from django.shortcuts import render
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

class WordEditor(generic.ListView):
    template_name = 'words/WordEditor.html'
    context_object_name = 'CharacterSet_list'

    def get_queryset(self):
        return CharacterSet.objects.order_by('-pk')
