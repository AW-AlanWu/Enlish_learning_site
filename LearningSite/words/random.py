import random, hashlib
from django.utils import timezone

class Random:
    def __init__(self):
        random.seed(hashlib.md5(timezone.now().ctime().encode('utf-8')).hexdigest())
    def generateRandomList(self, length):
        l1 = []
        for i in range(length):
            l1.append(i)
        l2 = random.sample(l1, len(l1))
        return l2
    def generateRandomNumber(self):
        return random.random()
        
