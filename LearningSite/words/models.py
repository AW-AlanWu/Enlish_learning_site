from django.db import models
from django.contrib.auth.models import User


class CharacterSet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    set_name = models.CharField(max_length = 100)
    def __str__(self):
        return self.set_name
class Vocabulary(models.Model):
    character_set = models.ForeignKey(CharacterSet, on_delete=models.CASCADE)
    english = models.CharField(max_length = 50)
    def __str__(self):
        return self.english
class Meaning(models.Model):
    vocabulary = models.ForeignKey(Vocabulary, on_delete=models.CASCADE)
    noun = 'n'
    pronoun = 'pron'
    verb = 'v'
    adjective = 'adj'
    adverb = 'adv'
    preposition = 'prep'
    conjunction = 'conj'
    interjection = 'int'
    auxiliaryVerb = 'aux'

    SPEECH_CHOICES = [
        (noun, 'n.'),
        (pronoun, 'pron.'),
        (verb, 'v.'),
        (adjective, 'adj.'),
        (adverb, 'adv.'),
        (preposition, 'prep.'),
        (conjunction, 'conj.'),
        (interjection, 'int.'),
        (auxiliaryVerb, 'aux.'),
    ]

    chinese = models.CharField(max_length = 50)
    chinese_sentences = models.CharField(max_length = 250)
    english_sentences = models.CharField(max_length = 250)
    speech = models.CharField(
        max_length = 5,
        choices = SPEECH_CHOICES,
        blank = False
    )
    def __str__(self):
        return self.chinese

class Score(models.Model):
    method1 = '1'
    method2 = '2'
    method3 = '3'

    METHOD_CHOICES = [
        (method1, '中翻英'),
        (method2, '英翻中'),
        (method3, '克漏字'),
    ]

    character_set = models.ForeignKey(CharacterSet, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    correct = models.IntegerField()
    total = models.IntegerField()
    examMethod = models.CharField(
        max_length = 1,
        choices = METHOD_CHOICES,
        blank = False,
        default=None
    )
    def __str__(self):
        return self.character_set.set_name