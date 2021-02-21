from django.db import models

class Words(models.Model):
    words_text = models.CharField(max_length=50)
    words_chinese = models.CharField(max_length=50)
    def __str__(self):
        return self.words_text

class Sentences(models.Model):
    words = models.ForeignKey(Words, on_delete=models.CASCADE)
    sentences_text = models.CharField(max_length=200)
    def __str__(self):
        return self.sentences_text