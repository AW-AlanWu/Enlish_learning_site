from django.db import models


class CharacterSet(models.Model):
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

    SPEECH_CHOICES = [
        (noun, 'n.'),
        (pronoun, 'pron.'),
        (verb, 'v.'),
        (adjective, 'adj.'),
        (adverb, 'adv.'),
        (preposition, 'prep.'),
        (conjunction, 'conj.'),
        (interjection, 'int.'),
    ]

    chinese = models.CharField(max_length = 50)
    chinese_sentences = models.CharField(max_length = 250)
    enlish_sentences = models.CharField(max_length = 250)
    speech = models.CharField(
        max_length = 4,
        choices = SPEECH_CHOICES,
        blank = False
    )
    def __str__(self):
        return self.chinese
