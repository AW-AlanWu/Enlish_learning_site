import random, hashlib
from django.utils import timezone

class Random:
    def __init__(self):
        random.seed(hashlib.md5(timezone.now().ctime().encode('utf-8')).hexdigest())
    def generateRandom(self):
        return random.random()
        
