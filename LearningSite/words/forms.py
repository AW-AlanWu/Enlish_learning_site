from django import forms
from .models import CharacterSet, Vocabulary, Meaning
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CharacterSetModelForm(forms.ModelForm):
    class Meta:
        model = CharacterSet
        fields = '__all__'

        widgets = {
            'set_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '請輸入字集'})
        }

        labels = {
            'set_name': '新增字集'
        }

class VocabularySetModelForm(forms.ModelForm):
    class Meta:
        model = Vocabulary
        exclude = ['character_set']

        widgets = {
            'english': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '請輸入單字'})
        }

        labels = {
            'english': '新增單字'
        }

class MeaningSetModelForm(forms.ModelForm):
    class Meta:
        model = Meaning
        exclude = ['vocabulary']

        widgets = {
            'chinese': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '請輸入中文解釋'}),
            'chinese_sentences': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '請輸入例句(中)'}),
            'english_sentences': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '請輸入例句(英)'}),
            'speech': forms.Select(attrs={'class': 'form-control', 'placeholder': '請輸入例句(英)'})
        }

        labels = {
            'chinese': '中文解釋',
            'chinese_sentences': '例句(中)',
            'english_sentences': '例句(英)',
            'speech': '詞性'
        }

class RegisterForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text', 'name': 'name', 'id': 'name', 'placeholder': 'Your Name', 'pattern': "\w{6,24}", 'title': '帳號名稱內不可含有特殊字元'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'type': 'email', 'name': 'email', 'id': 'email', 'placeholder': 'Your Email'})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'type': 'password', 'name': 'pass', 'id': 'pass', 'placeholder': 'Password', 'pattern': "^((?=.{8,}$)(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).*|(?=.{8,}$)(?=.*\d)(?=.*[a-zA-Z])(?=.*[!\u0022#$%&'()*+,./:;<=>?@[\]\^_`{|}~-]).*)", 'minlength': '8', 'title': '請最少輸入8位以上的大小寫英文與數字以及特殊符號'})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'type': 'password', 'name': 're_pass', 'id': 're_pass', 'placeholder': 'Repeat your password', 'pattern': "^((?=.{8,}$)(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).*|(?=.{8,}$)(?=.*\d)(?=.*[a-zA-Z])(?=.*[!\u0022#$%&'()*+,./:;<=>?@[\]\^_`{|}~-]).*)", 'minlength': '8', 'title': '請最少輸入8位以上的大小寫英文與數字以及特殊符號'})
    )
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')