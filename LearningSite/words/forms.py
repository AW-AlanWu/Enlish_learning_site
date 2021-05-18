from django import forms
from .models import CharacterSet, Vocabulary, Meaning
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CharacterSetModelForm(forms.ModelForm):
    class Meta:
        model = CharacterSet
        fields = '__all__'

        widgets = {
            'set_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '請輸入字集', 'pattern': "[\u4e00-\u9fa5_a-zA-Z0-9]+$", 'title': '字集名稱內不可包含特殊字元'})
        }

        labels = {
            'set_name': '新增字集'
        }

class VocabularySetModelForm(forms.ModelForm):
    class Meta:
        model = Vocabulary
        exclude = ['character_set']

        widgets = {
            'english': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '請輸入單字', 'pattern': "[a-zA-Z]+$", 'title': '單字只可由英文大小寫組成'})
        }

        labels = {
            'english': '新增單字'
        }

class MeaningSetModelForm(forms.ModelForm):
    class Meta:
        model = Meaning
        exclude = ['vocabulary']

        widgets = {
            'chinese': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '請輸入中文解釋', 'pattern': "[a-zA-Z\u4e00-\u9fa5;]+$", 'title': '解釋只可由大小寫英文和中文以及分號組成'}),
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
        widget=forms.TextInput(attrs={'type': 'text', 'name': 'name', 'id': 'name', 'placeholder': 'Your Name', 'pattern': "^[a-zA-Z][0-9a-zA-Z_]*", 'title': '帳號名稱開頭不可為數字且內容不可含有特殊字元'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'type': 'email', 'name': 'email', 'id': 'email', 'placeholder': 'Your Email', 'pattern': "^\w+((-\w+)|(\.\w+))*[@][A-Za-z0-9]+((\.|-)[A-Za-z0-9]+)*\.[A-Za-z]{2,4}$", 'title': '此電子郵件地址無效。請務必確認其格式為 example@email.com'})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'type': 'password', 'name': 'pass', 'id': 'pass', 'placeholder': 'Password', 'pattern': "^((?=.{8,}$)(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).*|(?=.{8,}$)(?=.*\d)(?=.*[a-zA-Z])(?=.*[!\u0022#$%&'()*+,./:;<=>?@[\]\^_`{|}~-]).*)", 'minlength': '8', 'title': '請最少輸入8位以上的大小寫英文與數字以及特殊符號'})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'type': 'password', 'name': 're_pass', 'id': 're_pass', 'placeholder': 'Repeat your password', 'pattern': "^((?=.{8,}$)(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).*|(?=.{8,}$)(?=.*\d)(?=.*[a-zA-Z])(?=.*[!\u0022#$%&'()*+,./:;<=>?@[\]\^_`{|}~-]).*)", 'minlength': '8', 'title': '請最少輸入8位以上的大小寫英文與數字以及特殊符號'})
    )

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text', 'name': 'your_name', 'id': 'your_name', 'placeholder': 'Your Name'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'type': 'password', 'name': 'your_pass', 'id': 'your_pass', 'placeholder': 'Password'})
    )