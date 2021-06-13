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
