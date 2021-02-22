from django.db import models

class Word(models.Model):
    word_text = models.CharField(max_length=50)
    word_chinese = models.CharField(max_length=50)
    def __str__(self):
        return self.word_text

class Sentence(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    sentence_text = models.CharField(max_length=200)
    def __str__(self):
        return self.sentence_text