from django.http.response import HttpResponseServerError
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views import generic
from .models import CharacterSet, Vocabulary, Meaning
from .forms import CharacterSetModelForm, VocabularySetModelForm, MeaningSetModelForm, RegisterForm, LoginForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.models import User
from .spider import fetchMeaning

def index(request):
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    
    context = {
        'num_visits': num_visits,
    }
    if request.user.is_authenticated:
        context['is_authenticated'] = request.user.is_authenticated

    return render(request, 'words/index.html', context=context)

@login_required(login_url="Login")
def CharacterSetEditor(request):
    object = request.user
    CharacterSet_list = object.characterset_set.order_by('-pk')
    form =  CharacterSetModelForm()
    context = {
        'CharacterSet_list': CharacterSet_list,
        'form': form
    }
    if request.user.is_authenticated:
        context['is_authenticated'] = request.user.is_authenticated
    return render(request, 'words/CharacterSetEditor.html', context)

@login_required(login_url="Login")
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
    if request.user.is_authenticated:
        context['is_authenticated'] = request.user.is_authenticated
    return render(request, 'words/VocabularyEditor.html', context)

@login_required(login_url="Login")
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
    if request.user.is_authenticated:
        context['is_authenticated'] = request.user.is_authenticated
    return render(request, 'words/MeaningEditor.html', context)

@login_required(login_url="Login")
def DelSet(request):
    Set = get_object_or_404(CharacterSet, pk=request.POST['id'])
    Set.delete()
    return HttpResponseRedirect(reverse('words:CharacterSetEditor'))

@login_required(login_url="Login")
def EditSet(request):
    Set = get_object_or_404(CharacterSet, pk=request.POST['id'])
    Set.set_name = request.POST['set_change']
    Set.save()
    return HttpResponseRedirect(reverse('words:CharacterSetEditor'))

@login_required(login_url="Login")
def AddSet(request):
    Set = CharacterSet(set_name = request.POST['set_name'], user = request.user)
    Set.save()
    return HttpResponseRedirect(reverse('words:CharacterSetEditor'))

@login_required(login_url="Login")
def DelVoc(request):
    Voc = get_object_or_404(Vocabulary, pk=request.POST['id'])
    args = Voc.character_set_id
    Voc.delete()
    return HttpResponseRedirect(reverse('words:VocabularyEditor', args=(args,)))
    
@login_required(login_url="Login")
def EditVoc(request):
    Voc = get_object_or_404(Vocabulary, pk=request.POST['id'])
    Voc.english = request.POST['voc_change']
    Voc.save()
    args = Voc.character_set_id
    return HttpResponseRedirect(reverse('words:VocabularyEditor', args=(args,)))

@login_required(login_url="Login")
def AddVoc(request):
    args = request.POST['id']
    Set = get_object_or_404(CharacterSet, pk=args)
    Voc = Vocabulary(english = request.POST['english'], character_set = Set)
    Voc.save()
    return HttpResponseRedirect(reverse('words:VocabularyEditor', args=(args,)))

@login_required(login_url="Login")
def AddMeaning(request):
    args = request.POST['id']
    Voc = get_object_or_404(Vocabulary, pk=args)
    Mean = Meaning(chinese = request.POST['chinese'], chinese_sentences = request.POST['chinese_sentences'], english_sentences = request.POST['english_sentences'], speech = request.POST['speech'], vocabulary = Voc)
    Mean.save()
    return HttpResponseRedirect(reverse('words:MeaningEditor', args=(args,)))

@login_required(login_url="Login")
def DelMeaning(request):
    Mean = get_object_or_404(Meaning, pk=request.POST['id'])
    args = Mean.vocabulary_id
    Mean.delete()
    return HttpResponseRedirect(reverse('words:MeaningEditor', args=(args,)))

def Login(request):
    form = LoginForm()
    context = {
        'form': form
    }
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('index'))
    return render(request, 'words/Login.html', context)

def Sign_up(request):
    form = RegisterForm()

    context = {
        'form': form
    }
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('index'))
    return render(request, 'words/register.html', context)

def saveAccount(request):
    if User.objects.filter(username = request.POST['username']) and User.objects.filter(email = request.POST['email']):
        raise Http404("username or email already exists")
    else:
        user = User.objects.create_user(
            request.POST['username'],
            request.POST['email'],
            request.POST['password1'],
        )
        user.save()
        return HttpResponseRedirect(reverse('Login'))

def authenticateAccount(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('index'))
    else:
        raise Http404("The account does not exist")

def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('Login'))

@login_required(login_url="Login")
def FetchMeaning(request):
    args = request.POST['id']
    Voc = get_object_or_404(Vocabulary, pk=args)
    msg = fetchMeaning(request.POST['voc'], Voc)
    if msg != "success":
        raise Http404(msg)
    return HttpResponseRedirect(reverse('words:MeaningEditor', args=(args,)))

@login_required(login_url="Login")
def UserProfile(request, info):
    context = {}
    if request.user.is_authenticated:
        context['is_authenticated'] = request.user.is_authenticated

    object = request.user
    context['username'] = object.username
    context['email'] = object.email
    context['last_login'] = str(object.last_login.ctime())
    context['date_joined'] = str(object.date_joined.ctime())

    if info == "CharacterSet":
        CharacterSet_list = object.characterset_set.order_by('-pk')
        context['CharacterSet_list'] = CharacterSet_list
        return render(request, 'words/UserProfile.html', context)
    elif info == "score":
        context['Score_list'] = "None"
        return render(request, 'words/UserProfile.html', context)
    else:
       raise Http404("This site does not exist")
