from django import forms
from .models import CharacterSet, Vocabulary, Meaning

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