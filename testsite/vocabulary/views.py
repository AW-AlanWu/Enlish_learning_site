from django.views import generic
from .models import Word, Sentence

class IndexView(generic.ListView):
    template_name = 'vocabulary/index.html'
    context_object_name = 'vocabulary_list'

    def get_queryset(self):
        return Word.objects.order_by('pk')

class DetailView(generic.DetailView):
    model = Word
    template_name = 'vocabulary/detail.html'